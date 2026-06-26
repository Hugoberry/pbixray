"""
Tests for the TMSCHEMA_* DMV-equivalent endpoints added in v0.6.0.

All 39 properties are exercised against the rls-sample-report.pbix fixture
(defined in conftest.py).  Each test asserts:
  - the property returns a DataFrame
  - any *ModifiedTime / *RefreshedTime / *CreatedTime column contains
    datetime objects rather than raw integers
"""
import datetime
import os

import pandas as pd
import pytest

from pbixray import PBIXRay

# Packt sample (submodule) carrying a single incremental-refresh policy on a
# SCHEMAVERSION 76 model whose `RefreshPolicy` table predates the `Mode` column.
SAMPLES_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'samples'))
_INCREMENTAL_REFRESH_PBIX = os.path.join(
    SAMPLES_ROOT,
    'Expert-Data-Modeling-with-Power-BI', 'Chapter10',
    'Chapter 10, Incremental Refresh.pbix',
)


@pytest.fixture(scope="module")
def incremental_refresh_model():
    if not os.path.exists(_INCREMENTAL_REFRESH_PBIX):
        pytest.skip("Expert-Data-Modeling-with-Power-BI submodule not initialised")
    return PBIXRay(_INCREMENTAL_REFRESH_PBIX)


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

def test_tmschema_model(rls_model):
    _check(rls_model.tmschema_model, nonempty=True)


def test_tmschema_tables(rls_model):
    df = rls_model.tmschema_tables
    _check(df, nonempty=True)
    assert "Name" in df.columns


def test_tmschema_columns(rls_model):
    df = rls_model.tmschema_columns
    _check(df, nonempty=True)
    assert "TableName" in df.columns
    assert "Name" in df.columns


def test_tmschema_partitions(rls_model):
    df = rls_model.tmschema_partitions
    _check(df, nonempty=True)
    assert "TableName" in df.columns
    assert "QueryDefinition" in df.columns


def test_tmschema_datasources(rls_model):
    _check(rls_model.tmschema_datasources)


# ---------------------------------------------------------------------------
# Hierarchies & levels
# ---------------------------------------------------------------------------

def test_tmschema_hierarchies(rls_model):
    df = rls_model.tmschema_hierarchies
    _check(df, nonempty=True)
    assert "TableName" in df.columns


def test_tmschema_levels(rls_model):
    df = rls_model.tmschema_levels
    _check(df, nonempty=True)
    assert "HierarchyName" in df.columns
    assert "ColumnName" in df.columns


def test_tmschema_attribute_hierarchies(rls_model):
    df = rls_model.tmschema_attribute_hierarchies
    _check(df, nonempty=True)
    assert "ColumnName" in df.columns


def test_tmschema_variations(rls_model):
    _check(rls_model.tmschema_variations)


# ---------------------------------------------------------------------------
# Measures, calculations, KPIs
# ---------------------------------------------------------------------------

def test_tmschema_kpis(rls_model):
    _check(rls_model.tmschema_kpis)


def test_tmschema_calculation_groups(rls_model):
    _check(rls_model.tmschema_calculation_groups)


def test_tmschema_calculation_items(rls_model):
    _check(rls_model.tmschema_calculation_items)


def test_tmschema_calculation_expressions(rls_model):
    _check(rls_model.tmschema_calculation_expressions)


def test_tmschema_sets(rls_model):
    _check(rls_model.tmschema_sets)


def test_tmschema_functions(rls_model):
    _check(rls_model.tmschema_functions)


# ---------------------------------------------------------------------------
# Partitions & refresh
# ---------------------------------------------------------------------------

def test_tmschema_refresh_policies(rls_model):
    _check(rls_model.tmschema_refresh_policies)


def test_tmschema_refresh_policies_no_mode_column(incremental_refresh_model):
    """Regression: a model whose `RefreshPolicy` table predates the `Mode`
    column must still surface its incremental-refresh policy. Previously the
    unconditional `rp.Mode` raised SQLError, swallowed into an empty frame."""
    df = incremental_refresh_model.tmschema_refresh_policies
    _check(df, nonempty=True)
    # The policy row is present with the expected incremental-refresh shape,
    # and `Mode` degrades to NULL rather than failing the whole query.
    assert {"TableName", "PolicyType", "SourceExpression", "Mode"} <= set(df.columns)
    assert df["Mode"].isna().all()


def test_tmschema_data_coverage_definitions(rls_model):
    _check(rls_model.tmschema_data_coverage_definitions)


# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------

def test_tmschema_role_memberships(rls_model):
    _check(rls_model.tmschema_role_memberships)


# ---------------------------------------------------------------------------
# Perspectives
# ---------------------------------------------------------------------------

def test_tmschema_perspectives(rls_model):
    _check(rls_model.tmschema_perspectives)


def test_tmschema_perspective_tables(rls_model):
    _check(rls_model.tmschema_perspective_tables)


def test_tmschema_perspective_columns(rls_model):
    _check(rls_model.tmschema_perspective_columns)


def test_tmschema_perspective_hierarchies(rls_model):
    _check(rls_model.tmschema_perspective_hierarchies)


def test_tmschema_perspective_measures(rls_model):
    _check(rls_model.tmschema_perspective_measures)


# ---------------------------------------------------------------------------
# Annotations & metadata properties
# ---------------------------------------------------------------------------

def test_tmschema_annotations(rls_model):
    df = rls_model.tmschema_annotations
    _check(df, nonempty=True)
    assert "ObjectType" in df.columns
    assert "Name" in df.columns


def test_tmschema_extended_properties(rls_model):
    _check(rls_model.tmschema_extended_properties)


def test_tmschema_detail_rows_definitions(rls_model):
    _check(rls_model.tmschema_detail_rows_definitions)


def test_tmschema_format_string_definitions(rls_model):
    _check(rls_model.tmschema_format_string_definitions)


# ---------------------------------------------------------------------------
# Internationalisation
# ---------------------------------------------------------------------------

def test_tmschema_cultures(rls_model):
    df = rls_model.tmschema_cultures
    _check(df, nonempty=True)
    assert "Name" in df.columns


def test_tmschema_translations(rls_model):
    _check(rls_model.tmschema_translations)


def test_tmschema_linguistic_metadata(rls_model):
    _check(rls_model.tmschema_linguistic_metadata)


# ---------------------------------------------------------------------------
# Calendars & AI
# ---------------------------------------------------------------------------

def test_tmschema_calendars(rls_model):
    _check(rls_model.tmschema_calendars)


def test_tmschema_calendar_column_groups(rls_model):
    _check(rls_model.tmschema_calendar_column_groups)


def test_tmschema_calendar_column_refs(rls_model):
    _check(rls_model.tmschema_calendar_column_refs)


def test_tmschema_analytics_ai_metadata(rls_model):
    _check(rls_model.tmschema_analytics_ai_metadata)


# ---------------------------------------------------------------------------
# Aggregations
# ---------------------------------------------------------------------------

def test_tmschema_alternate_of(rls_model):
    _check(rls_model.tmschema_alternate_of)


def test_tmschema_related_column_details(rls_model):
    df = rls_model.tmschema_related_column_details
    _check(df, nonempty=True)
    assert "ColumnName" in df.columns


def test_tmschema_group_by_columns(rls_model):
    _check(rls_model.tmschema_group_by_columns)


# ---------------------------------------------------------------------------
# Binding
# ---------------------------------------------------------------------------

def test_tmschema_query_groups(rls_model):
    _check(rls_model.tmschema_query_groups)


def test_tmschema_binding_info(rls_model):
    _check(rls_model.tmschema_binding_info)
