"""Regression tests for calculated-table columns (issue #61).

Columns of a calculated table, including the auto date/time LocalDateTable_*
and DateTableTemplate_* ones, have Column.Type = 4 and no ExplicitName. The
schema query selected only types 1 and 2 and read the name from ExplicitName,
so those columns were missing from schema, statistics and get_table.

Fixture: data/rls-sample-report.pbix.
"""
import pandas as pd

LOCAL_DATE_TABLE = "LocalDateTable_8c493ee4-3ad6-4e77-801a-7c5f9c8e129c"
DATE_TABLE_TEMPLATE = "DateTableTemplate_ab5c2ea0-9b35-4f92-b27d-635c56fb6330"

LOCAL_DATE_COLUMNS = ["Date", "Year", "MonthNo", "Month", "QuarterNo", "Quarter", "Day"]


def test_local_date_table_has_date_column_in_schema(rls_model):
    schema = rls_model.schema
    columns = schema[schema["TableName"] == LOCAL_DATE_TABLE]
    assert list(columns["ColumnName"]) == LOCAL_DATE_COLUMNS


def test_no_column_name_is_null(rls_model):
    # Without the COALESCE onto InferredName these come through unnamed.
    assert not rls_model.schema["ColumnName"].isna().any()
    assert not rls_model.statistics["ColumnName"].isna().any()


def test_local_date_table_statistics_include_date(rls_model):
    stats = rls_model.statistics
    date_row = stats[
        (stats["TableName"] == LOCAL_DATE_TABLE) & (stats["ColumnName"] == "Date")
    ]
    assert len(date_row) == 1
    row = date_row.iloc[0]
    # 1461 days, the 2022-2025 range of the source column.
    assert row["Cardinality"] == 1461
    # The largest column of the table by dictionary size.
    assert row["Dictionary"] > 0
    assert row["Dictionary"] == stats[stats["TableName"] == LOCAL_DATE_TABLE]["Dictionary"].max()
    assert row["DataSize"] > 0


def test_date_table_template_included(rls_model):
    stats = rls_model.statistics
    template = stats[stats["TableName"] == DATE_TABLE_TEMPLATE]
    assert list(template["ColumnName"]) == LOCAL_DATE_COLUMNS


def test_local_date_table_decodes(rls_model):
    table = rls_model.get_table(LOCAL_DATE_TABLE)
    assert list(table.columns) == LOCAL_DATE_COLUMNS
    assert len(table) == 1461
    assert pd.api.types.is_datetime64_any_dtype(table["Date"])
    assert table["Date"].nunique() == 1461
    assert table["Date"].min() == pd.Timestamp("2022-01-01")
    assert table["Date"].max() == pd.Timestamp("2025-12-31")


def test_dax_calculated_table_columns_decode(rls_model):
    # Every column but Year Category is type 4, so this used to decode to one column.
    table = rls_model.get_table("DateTable")
    assert len(table.columns) == 16
    assert len(table) == 1461
    # Storage order starts mid-range at 2022-07-01.
    assert table["Date"].min() == pd.Timestamp("2022-01-01")
    assert table["Date"].max() == pd.Timestamp("2025-12-31")
    assert table["Year"].nunique() == 4


def test_row_number_stays_excluded(rls_model):
    assert not rls_model.schema["ColumnName"].str.startswith("RowNumber").any()
