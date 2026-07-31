"""
Tests for xlsx parsing support.

PBIXRay accepts Excel workbooks (.xlsx) in addition to .pbix files — the same
API surface applies. The fixture is provided by conftest.py (xlsx_model).
"""
import os
import pandas as pd
import pytest

CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "xlsx")


def _is_nonempty_df(obj):
    return isinstance(obj, pd.DataFrame) and not obj.empty


def _is_df(obj):
    return isinstance(obj, pd.DataFrame)


def _load_fixture(name):
    df = pd.read_csv(os.path.join(CSV_DIR, f"{name}.csv"))
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    return df


def _row_multiset_equal(got, expected):
    """VertiPaq stores rows in RLE-friendly order, not insertion order.
    Compare as a multiset: sort both by every column and check equality.
    """
    cols = list(expected.columns)
    assert list(got.columns) == cols, (
        f"column mismatch: got {list(got.columns)} expected {cols}"
    )
    # Align dtypes via the expected fixture's dtypes
    got = got.copy()
    for c in cols:
        if got[c].dtype != expected[c].dtype:
            got[c] = got[c].astype(expected[c].dtype)
    a = got.sort_values(cols).reset_index(drop=True)
    b = expected.sort_values(cols).reset_index(drop=True)
    return a.equals(b)


def test_xlsx_tables(xlsx_model):
    assert len(xlsx_model.tables) > 0


def test_xlsx_statistics(xlsx_model):
    assert _is_nonempty_df(xlsx_model.statistics)


def test_xlsx_dax_tables(xlsx_model):
    assert _is_df(xlsx_model.dax_tables)


def test_xlsx_dax_measures(xlsx_model):
    assert _is_df(xlsx_model.dax_measures)


def test_xlsx_size(xlsx_model):
    assert isinstance(xlsx_model.size, int)
    assert xlsx_model.size > 0


def test_xlsx_schema(xlsx_model):
    assert _is_nonempty_df(xlsx_model.schema)


def test_xlsx_relationships(xlsx_model):
    assert _is_df(xlsx_model.relationships)


# -------------------------------------------------------------------------
# Endpoints with no XLSX equivalent must still return an empty DataFrame
# (uniform surface with PBIX), never raise.
# -------------------------------------------------------------------------

@pytest.mark.parametrize(
    "endpoint",
    ["aggregations", "ols", "perspectives", "tmschema_column_permissions"],
)
def test_xlsx_pbix_only_endpoints_empty(xlsx_model, endpoint):
    df = getattr(xlsx_model, endpoint)
    assert _is_df(df) and df.empty


# -------------------------------------------------------------------------
# get_table data fidelity — verified against CSV fixtures captured from
# Excel's Power Pivot view. Compared as row-tuple multisets because
# VertiPaq stores rows in RLE-friendly order, not insertion order.
# -------------------------------------------------------------------------

@pytest.mark.parametrize(
    "table",
    ["Plant", "Category", "Material Type", "Defect Type", "Metrics"],
)
def test_xlsx_get_table_matches_fixture(xlsx_model, table):
    expected = _load_fixture(table)
    got = xlsx_model.get_table(table)
    assert len(got) == len(expected), (
        f"{table}: row count {len(got)} != fixture {len(expected)}"
    )
    assert _row_multiset_equal(got, expected), (
        f"{table}: row multiset does not match fixture"
    )


# -------------------------------------------------------------------------
# Data files are named <n>.<dimension_id>.<column>.<ext> (hierarchy files use
# <n>.H$<dimension_id>$<column>.<ext>), so the dimension id is a delimited
# token. Matching it as a bare substring handed one table's files to another
# whenever a dimension id also appeared inside some other table's column name.
# -------------------------------------------------------------------------

@pytest.mark.parametrize(
    "dimension_id, file_name, owned",
    [
        # Files the dimension really owns.
        ("Product", "0.Product.Product Key.0.idf", True),
        ("Product", "0.Product.Product.dictionary", True),
        ("Product", "3.H$Product$Product Key.hidx", True),
        ("Fact_fb28d60b", "17.Fact_fb28d60b.Product Key.dictionary", True),
        ("Fact_fb28d60b", "6.H$Fact_fb28d60b$Product Key.POS_TO_ID.0.idf", True),
        # The Customer Profitability collision: "Product"/"Scenario" occur
        # inside the fact table's column names, never as its dimension token.
        ("Product", "17.Fact_fb28d60b.Product Key.dictionary", False),
        ("Scenario", "17.Fact_fb28d60b.Scenario Key.dictionary", False),
        # An id that is only a prefix or a suffix of the real one.
        ("Fact", "17.Fact_fb28d60b.Product Key.dictionary", False),
        ("fb28d60b", "17.Fact_fb28d60b.Product Key.dictionary", False),
    ],
)
def test_dimension_file_pattern_matches_only_its_own_token(
    dimension_id, file_name, owned
):
    from pbixray.meta.xml_source import XmlMetadataSource

    pattern = XmlMetadataSource._dimension_file_pattern(dimension_id)
    assert bool(pattern.search(file_name)) is owned


def test_xlsx_get_table_no_rownumber_column(xlsx_model):
    # RowNumber is VertiPaq's internal storage position; we hide it the
    # same way PBIX does, so get_table only exposes user-facing columns.
    for table in ["Plant", "Category", "Metrics"]:
        assert "RowNumber" not in xlsx_model.get_table(table).columns
