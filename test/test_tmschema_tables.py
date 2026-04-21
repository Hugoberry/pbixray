"""
Tests for the tmschema_tables endpoint against work.pbix.

Reference data: data/work/tmschema_tables.tsv — produced by querying
$System.TMSCHEMA_TABLES against the same model in DAX Studio.

Covers:
  - Row count and expected table names
  - ModifiedTime / StructureModifiedTime are Python datetime objects
  - Datetime values match the TSV reference to second precision
    (pbixray truncates FILETIME values to whole seconds by design)
  - DataCategory is populated where expected (Date table → "Time")
  - LineageTag is non-empty for every user table
"""
import datetime
import os

import pandas as pd
import pytest

TSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'work', 'tmschema_tables.tsv')

# Expected table names in work.pbix (order-independent)
EXPECTED_TABLES = {
    "Customer", "Date", "Sales Territory", "Product",
    "Sales Order", "Sales", "Reseller", "Currency Rate", "Currency",
}


@pytest.fixture(scope="module")
def tables_df(work_model):
    return work_model.tmschema_tables


@pytest.fixture(scope="module")
def tsv_ref():
    """Load the TSV reference, stripping surrounding quotes from string cells."""
    df = pd.read_csv(TSV_PATH, sep="\t", keep_default_na=False, na_values=[""])
    for col in df.columns[df.dtypes == object]:
        df[col] = df[col].str.strip('"')
    return df


def _parse_tsv_dt(s: str) -> datetime.datetime:
    """Parse a TSV timestamp and truncate to whole seconds (pbixray's precision)."""
    dt = datetime.datetime.strptime(s.strip('"'), "%Y-%m-%d %H:%M:%S.%f")
    return dt.replace(microsecond=0)


# ---------------------------------------------------------------------------
# Shape & content
# ---------------------------------------------------------------------------

def test_row_count(tables_df):
    assert len(tables_df) == len(EXPECTED_TABLES)


def test_expected_table_names_present(tables_df):
    names = set(tables_df["Name"])
    assert EXPECTED_TABLES == names


def test_date_table_data_category(tables_df):
    """The Date table must carry DataCategory='Time' (time intelligence)."""
    row = tables_df[tables_df["Name"] == "Date"]
    assert len(row) == 1
    assert row.iloc[0]["DataCategory"] == "Time"


def test_other_tables_data_category_empty(tables_df):
    """All tables except Date should have no DataCategory."""
    others = tables_df[tables_df["Name"] != "Date"]
    for val in others["DataCategory"]:
        assert val in ("", None) or (isinstance(val, float) and pd.isna(val)), (
            f"Unexpected DataCategory: {val!r}"
        )


def test_lineage_tags_non_empty(tables_df):
    """Every user table should have a non-empty LineageTag GUID."""
    for _, row in tables_df.iterrows():
        assert isinstance(row["LineageTag"], str) and len(row["LineageTag"]) > 0, (
            f"Table '{row['Name']}' has missing LineageTag"
        )


def test_is_hidden_all_false(tables_df):
    """No table in work.pbix is hidden."""
    assert tables_df["IsHidden"].eq(False).all()


# ---------------------------------------------------------------------------
# Datetime typing
# ---------------------------------------------------------------------------

def test_modified_time_is_datetime(tables_df):
    for val in tables_df["ModifiedTime"].dropna():
        assert isinstance(val, datetime.datetime), (
            f"ModifiedTime: expected datetime, got {type(val).__name__}: {val!r}"
        )


def test_structure_modified_time_is_datetime(tables_df):
    for val in tables_df["StructureModifiedTime"].dropna():
        assert isinstance(val, datetime.datetime), (
            f"StructureModifiedTime: expected datetime, got {type(val).__name__}: {val!r}"
        )


def test_no_null_modified_times(tables_df):
    assert tables_df["ModifiedTime"].notna().all(), "Some ModifiedTime values are null"
    assert tables_df["StructureModifiedTime"].notna().all(), "Some StructureModifiedTime values are null"


def test_datetime_has_no_sub_second_component(tables_df):
    """pbixray truncates FILETIME to whole seconds — microsecond must always be 0."""
    for col in ("ModifiedTime", "StructureModifiedTime"):
        for val in tables_df[col].dropna():
            assert val.microsecond == 0, (
                f"{col}: expected whole-second value, got microsecond={val.microsecond} in {val!r}"
            )


# ---------------------------------------------------------------------------
# Full dataframe match against TSV reference
# ---------------------------------------------------------------------------

# SystemFlags is absent from older-format PBIX files; compare columns present in both.
_COMPARE_SCALAR_COLS = ["Name", "DataCategory", "IsHidden"]
_COMPARE_TIME_COLS   = ["ModifiedTime", "StructureModifiedTime"]
_COMPARE_COLS        = _COMPARE_SCALAR_COLS + _COMPARE_TIME_COLS


def test_full_match_against_tsv(tables_df, tsv_ref):
    """
    Join actual vs TSV on Name and assert key columns match.

    Scalar columns (DataCategory, IsHidden) must be exactly equal.
    Datetime columns are compared at second precision: pbixray truncates
    FILETIME values to whole seconds, so TSV ms values are also truncated
    to seconds before comparison.
    """
    tsv_work = tsv_ref[_COMPARE_COLS].copy()
    for col in _COMPARE_TIME_COLS:
        tsv_work[col] = tsv_work[col].apply(_parse_tsv_dt)

    merged = tables_df[_COMPARE_COLS].merge(
        tsv_work, on="Name", suffixes=("_actual", "_ref")
    )
    assert len(merged) == len(EXPECTED_TABLES), "Name join lost rows — table names diverged"

    for col in _COMPARE_SCALAR_COLS[1:]:  # skip Name (join key)
        # Normalise empty/missing to empty string so None vs NaN doesn't differ.
        a = merged[f"{col}_actual"].fillna("").reset_index(drop=True)
        e = merged[f"{col}_ref"].fillna("").reset_index(drop=True)
        pd.testing.assert_series_equal(a, e, check_names=False, check_dtype=False, obj=col)

    for col in _COMPARE_TIME_COLS:
        for _, row in merged.iterrows():
            assert row[f"{col}_actual"] == row[f"{col}_ref"], (
                f"{row['Name']}.{col}: expected {row[f'{col}_ref']}, got {row[f'{col}_actual']}"
            )
