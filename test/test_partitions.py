"""Partition-aware decode + native .abf loading.

Canonical fixture: the AdventureWorks Internet Sales tabular backup
(`Adventure Works Internet Sales Database.abf`), loaded natively as a raw .abf.
Its `Internet Sales` table has 5 partitions (2010..2014); before the
partition-aware fix `get_table` returned only the last partition (1,970 rows)
instead of the full 60,398.

See docs/specs/partition-aware-decode-spec.md.
"""
import os
from decimal import Decimal

import numpy as np
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
# Ground-truth extract of the abf's Internet Sales table (model column names,
# actual stored dates). Used for an exact value comparison against the decode.
INTERNET_SALES_CSV = os.path.join(DATA_DIR, "Internet Sales.csv")

# Per-partition record counts (SegmentMapStorage.RecordCount), keyed by the
# partition's Order Date year. Sum = 60,398.
EXPECTED_PARTITION_COUNTS = {2010: 14, 2011: 2216, 2012: 3397, 2013: 52801, 2014: 1970}
EXPECTED_TOTAL = sum(EXPECTED_PARTITION_COUNTS.values())  # 60398


# fixtures provided by conftest.py: internet_sales_abf_model, adventure_works_model


def test_native_abf_load(internet_sales_abf_model):
    """A raw .abf opens directly (no zip wrapper) and reports its tables."""
    tables = internet_sales_abf_model.tables
    assert tables is not None and len(tables) > 0
    assert "Internet Sales" in tables


def test_multi_partition_row_count(internet_sales_abf_model):
    """All 5 partitions are concatenated, not just the last one."""
    df = internet_sales_abf_model.get_table("Internet Sales")
    assert len(df) == EXPECTED_TOTAL


def test_per_partition_distribution(internet_sales_abf_model):
    """Each partition's rows are present, in storage order, keyed by Order Date year."""
    df = internet_sales_abf_model.get_table("Internet Sales")
    counts = df["Order Date"].dt.year.value_counts().sort_index().to_dict()
    assert counts == EXPECTED_PARTITION_COUNTS


def test_columns_equal_length(internet_sales_abf_model):
    """Every column aligns to the same row count across partitions."""
    df = internet_sales_abf_model.get_table("Internet Sales")
    assert df.shape[1] == 24
    assert {len(df[c]) for c in df.columns} == {EXPECTED_TOTAL}


def test_spot_check_partition_extremes(internet_sales_abf_model):
    """Spot-check the smallest (2010/14) and largest (2013/52801) partitions."""
    df = internet_sales_abf_model.get_table("Internet Sales")
    by_year = df["Order Date"].dt.year
    assert (by_year == 2010).sum() == 14
    assert (by_year == 2013).sum() == 52801


def test_sparse_all_null_column_full_length(internet_sales_abf_model):
    """All-null columns (no dictionary/HIDX) span every partition, not just the
    first — regression guard for the records-vs-count_bit_packed fix."""
    df = internet_sales_abf_model.get_table("Internet Sales")
    for col in ("Carrier Tracking Number", "Customer PO Number"):
        assert df[col].isna().all()
        assert len(df[col]) == EXPECTED_TOTAL


def test_columns_subset_all_partitions(internet_sales_abf_model):
    """columns= still decodes all partitions for the requested columns."""
    sub = internet_sales_abf_model.get_table("Internet Sales", columns=["Order Quantity"])
    assert list(sub.columns) == ["Order Quantity"]
    assert len(sub) == EXPECTED_TOTAL


def test_partition_metadata_unchanged(internet_sales_abf_model):
    """tmschema_partitions still reports all 5 partitions (metadata path intact)."""
    parts = internet_sales_abf_model.tmschema_partitions
    is_parts = parts[parts.TableName == "Internet Sales"]
    assert len(is_parts) == 5


def test_statistics_dedup(internet_sales_abf_model):
    """Each Internet Sales column appears exactly once in statistics (no
    per-partition duplicate-row inflation)."""
    stats = internet_sales_abf_model.statistics
    is_stats = stats[stats.TableName == "Internet Sales"]
    assert len(is_stats) == 24
    assert not is_stats.duplicated(subset=["TableName", "ColumnName"]).any()


def test_values_match_csv_extract(internet_sales_abf_model):
    """Decoded Internet Sales matches a ground-truth CSV extract value-for-value
    across all 24 columns (numeric within tolerance, dates and strings exact).

    Rows are aligned on the unique (Sales Order Number, Sales Order Line Number)
    key because the decode emits partitions in storage order while the extract is
    in the model's row order. Covers the calculated currency column Margin, whose
    /10000 scaling depends on resolving Automatic -> InferredDataType.
    """
    got = internet_sales_abf_model.get_table("Internet Sales")
    exp = pd.read_csv(INTERNET_SALES_CSV)
    assert set(got.columns) == set(exp.columns)
    assert len(got) == len(exp) == EXPECTED_TOTAL

    date_cols = {"Order Date", "Due Date", "Ship Date"}
    str_cols = {"Sales Order Number", "Carrier Tracking Number", "Customer PO Number"}
    key = ["Sales Order Number", "Sales Order Line Number"]
    g = got.sort_values(key).reset_index(drop=True)
    e = exp.sort_values(key).reset_index(drop=True)

    for col in exp.columns:
        gs, es = g[col], e[col]
        if col in date_cols:
            gd, ed = pd.to_datetime(gs), pd.to_datetime(es)
            eq = (gd == ed) | (gd.isna() & ed.isna())
        elif col in str_cols:
            # Treat NaN and "" as the same empty value (all-null string columns).
            g_empty = gs.isna() | (gs.astype(str) == "")
            e_empty = es.isna() | (es.astype(str) == "")
            eq = (g_empty & e_empty) | (gs.astype(str) == es.astype(str))
        else:
            a = pd.to_numeric(
                gs.map(lambda x: float(x) if isinstance(x, Decimal) else x),
                errors="coerce",
            ).to_numpy(dtype=float)
            b = pd.to_numeric(es, errors="coerce").to_numpy(dtype=float)
            eq = np.isclose(a, b, rtol=1e-9, atol=1e-6, equal_nan=True)
        bad = int((~np.asarray(eq)).sum())
        assert bad == 0, f"{bad} value mismatches in column {col!r}"


def test_single_partition_regression(adventure_works_model):
    """A single-partition model still decodes one row per column with stable shape."""
    schema = adventure_works_model._metadata.source.schema_df
    assert not schema.duplicated(subset=["TableName", "ColumnName"]).any()
    df = adventure_works_model.get_table("Product")
    assert not df.empty
