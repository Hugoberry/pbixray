"""
Tests for the TMSCHEMA_* DMV-equivalent endpoints added in v0.6.0.

All 39 properties are exercised against the rls-sample-report.pbix fixture
(defined in conftest.py).  Each test asserts:
  - the property returns a DataFrame
  - any *ModifiedTime / *RefreshedTime / *CreatedTime column contains
    datetime objects rather than raw integers
"""
import datetime
import pandas as pd
import pytest


# ---------------------------------------------------------------------------
# Helpers (same conventions as test_metadata.py)
# ---------------------------------------------------------------------------

def _is_df(obj):
    return isinstance(obj, pd.DataFrame)


def _is_nonempty_df(obj):
    return _is_df(obj) and not obj.empty


def _time_cols_are_datetimes(df):
    """Assert every populated time column holds datetime values, not ints."""
    time_suffixes = ("ModifiedTime", "RefreshedTime", "CreatedTime")
    for col in df.columns:
        if col.endswith(time_suffixes):
            for val in df[col].dropna():
                assert isinstance(val, datetime.datetime), (
                    f"Column '{col}' contains {type(val).__name__} instead of datetime: {val!r}"
                )


def _check(df, *, nonempty=False):
    assert _is_df(df)
    if nonempty:
        assert not df.empty
    if not df.empty:
        _time_cols_are_datetimes(df)


# ---------------------------------------------------------------------------
# Model & sources
# ---------------------------------------------------------------------------

def test_model(rls_model):
    _check(rls_model.model, nonempty=True)


def test_tmschema_tables(rls_model):
    df = rls_model.tmschema_tables
    _check(df, nonempty=True)
    assert "Name" in df.columns


def test_columns(rls_model):
    df = rls_model.columns
    _check(df, nonempty=True)
    assert "TableName" in df.columns
    assert "Name" in df.columns


def test_partitions(rls_model):
    df = rls_model.partitions
    _check(df, nonempty=True)
    assert "TableName" in df.columns
    assert "QueryDefinition" in df.columns


def test_datasources(rls_model):
    _check(rls_model.datasources)


# ---------------------------------------------------------------------------
# Hierarchies & levels
# ---------------------------------------------------------------------------

def test_hierarchies(rls_model):
    df = rls_model.hierarchies
    _check(df, nonempty=True)
    assert "TableName" in df.columns


def test_levels(rls_model):
    df = rls_model.levels
    _check(df, nonempty=True)
    assert "HierarchyName" in df.columns
    assert "ColumnName" in df.columns


def test_attribute_hierarchies(rls_model):
    df = rls_model.attribute_hierarchies
    _check(df, nonempty=True)
    assert "ColumnName" in df.columns


def test_variations(rls_model):
    _check(rls_model.variations)


# ---------------------------------------------------------------------------
# Measures, calculations, KPIs
# ---------------------------------------------------------------------------

def test_kpis(rls_model):
    _check(rls_model.kpis)


def test_calculation_groups(rls_model):
    _check(rls_model.calculation_groups)


def test_calculation_items(rls_model):
    _check(rls_model.calculation_items)


def test_calculation_expressions(rls_model):
    _check(rls_model.calculation_expressions)


def test_sets(rls_model):
    _check(rls_model.sets)


def test_functions(rls_model):
    _check(rls_model.functions)


# ---------------------------------------------------------------------------
# Partitions & refresh
# ---------------------------------------------------------------------------

def test_refresh_policies(rls_model):
    _check(rls_model.refresh_policies)


def test_data_coverage_definitions(rls_model):
    _check(rls_model.data_coverage_definitions)


# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------

def test_role_memberships(rls_model):
    _check(rls_model.role_memberships)


# ---------------------------------------------------------------------------
# Perspectives
# ---------------------------------------------------------------------------

def test_perspectives(rls_model):
    _check(rls_model.perspectives)


def test_perspective_tables(rls_model):
    _check(rls_model.perspective_tables)


def test_perspective_columns(rls_model):
    _check(rls_model.perspective_columns)


def test_perspective_hierarchies(rls_model):
    _check(rls_model.perspective_hierarchies)


def test_perspective_measures(rls_model):
    _check(rls_model.perspective_measures)


# ---------------------------------------------------------------------------
# Annotations & metadata properties
# ---------------------------------------------------------------------------

def test_annotations(rls_model):
    df = rls_model.annotations
    _check(df, nonempty=True)
    assert "ObjectType" in df.columns
    assert "Name" in df.columns


def test_extended_properties(rls_model):
    _check(rls_model.extended_properties)


def test_detail_rows_definitions(rls_model):
    _check(rls_model.detail_rows_definitions)


def test_format_string_definitions(rls_model):
    _check(rls_model.format_string_definitions)


# ---------------------------------------------------------------------------
# Internationalisation
# ---------------------------------------------------------------------------

def test_cultures(rls_model):
    df = rls_model.cultures
    _check(df, nonempty=True)
    assert "Name" in df.columns


def test_translations(rls_model):
    _check(rls_model.translations)


def test_linguistic_metadata(rls_model):
    _check(rls_model.linguistic_metadata)


# ---------------------------------------------------------------------------
# Calendars & AI
# ---------------------------------------------------------------------------

def test_calendars(rls_model):
    _check(rls_model.calendars)


def test_calendar_column_groups(rls_model):
    _check(rls_model.calendar_column_groups)


def test_calendar_column_refs(rls_model):
    _check(rls_model.calendar_column_refs)


def test_analytics_ai_metadata(rls_model):
    _check(rls_model.analytics_ai_metadata)


# ---------------------------------------------------------------------------
# Aggregations
# ---------------------------------------------------------------------------

def test_alternate_of(rls_model):
    _check(rls_model.alternate_of)


def test_related_column_details(rls_model):
    df = rls_model.related_column_details
    _check(df, nonempty=True)
    assert "ColumnName" in df.columns


def test_group_by_columns(rls_model):
    _check(rls_model.group_by_columns)


# ---------------------------------------------------------------------------
# Binding
# ---------------------------------------------------------------------------

def test_query_groups(rls_model):
    _check(rls_model.query_groups)


def test_binding_info(rls_model):
    _check(rls_model.binding_info)
