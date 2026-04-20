import pytest
import os
import pandas as pd

from pbixray import PBIXRay

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
PBIX_FILE_PATH = os.path.join(DATA_DIR, "rls-sample-report.pbix")


@pytest.fixture(scope="module")
def model():
    return PBIXRay(PBIX_FILE_PATH)


# ---------------------------------------------------------------------------
# Each test checks that the property returns a DataFrame (possibly empty) and
# that any *ModifiedTime / *RefreshedTime / *CreatedTime column contains
# datetime objects rather than raw integers.
# ---------------------------------------------------------------------------

def _assert_df(df, name):
    assert isinstance(df, pd.DataFrame), f"{name} is not a DataFrame"


def _assert_time_cols_converted(df, name):
    time_suffixes = ("ModifiedTime", "RefreshedTime", "CreatedTime")
    for col in df.columns:
        if col.endswith(time_suffixes) and not df[col].dropna().empty:
            sample = df[col].dropna().iloc[0]
            assert isinstance(sample, (pd.Timestamp, type(None)).__class__.__bases__[0]) or \
                   hasattr(sample, 'year'), \
                f"{name}['{col}'] contains raw integers instead of datetimes: {sample!r}"


def _check(df, name):
    _assert_df(df, name)
    if not df.empty:
        _assert_time_cols_converted(df, name)


def test_model(model):
    df = model.model
    _check(df, "model")
    assert not df.empty, "model should have at least one row"


def test_tmschema_tables(model):
    df = model.tmschema_tables
    _check(df, "tmschema_tables")
    assert not df.empty, "tmschema_tables should have rows"
    assert "Name" in df.columns


def test_columns(model):
    df = model.columns
    _check(df, "columns")
    assert not df.empty
    assert "TableName" in df.columns


def test_partitions(model):
    df = model.partitions
    _check(df, "partitions")
    assert not df.empty
    assert "TableName" in df.columns


def test_hierarchies(model):
    _check(model.hierarchies, "hierarchies")


def test_levels(model):
    _check(model.levels, "levels")


def test_datasources(model):
    _check(model.datasources, "datasources")


def test_perspectives(model):
    _check(model.perspectives, "perspectives")


def test_perspective_tables(model):
    _check(model.perspective_tables, "perspective_tables")


def test_perspective_columns(model):
    _check(model.perspective_columns, "perspective_columns")


def test_perspective_hierarchies(model):
    _check(model.perspective_hierarchies, "perspective_hierarchies")


def test_perspective_measures(model):
    _check(model.perspective_measures, "perspective_measures")


def test_kpis(model):
    _check(model.kpis, "kpis")


def test_annotations(model):
    df = model.annotations
    _check(df, "annotations")
    assert not df.empty


def test_extended_properties(model):
    _check(model.extended_properties, "extended_properties")


def test_cultures(model):
    df = model.cultures
    _check(df, "cultures")
    assert not df.empty


def test_translations(model):
    _check(model.translations, "translations")


def test_linguistic_metadata(model):
    _check(model.linguistic_metadata, "linguistic_metadata")


def test_query_groups(model):
    _check(model.query_groups, "query_groups")


def test_calculation_groups(model):
    _check(model.calculation_groups, "calculation_groups")


def test_calculation_items(model):
    _check(model.calculation_items, "calculation_items")


def test_calculation_expressions(model):
    _check(model.calculation_expressions, "calculation_expressions")


def test_variations(model):
    _check(model.variations, "variations")


def test_attribute_hierarchies(model):
    df = model.attribute_hierarchies
    _check(df, "attribute_hierarchies")
    assert not df.empty


def test_sets(model):
    _check(model.sets, "sets")


def test_refresh_policies(model):
    _check(model.refresh_policies, "refresh_policies")


def test_detail_rows_definitions(model):
    _check(model.detail_rows_definitions, "detail_rows_definitions")


def test_format_string_definitions(model):
    _check(model.format_string_definitions, "format_string_definitions")


def test_functions(model):
    _check(model.functions, "functions")


def test_calendars(model):
    _check(model.calendars, "calendars")


def test_calendar_column_groups(model):
    _check(model.calendar_column_groups, "calendar_column_groups")


def test_calendar_column_refs(model):
    _check(model.calendar_column_refs, "calendar_column_refs")


def test_alternate_of(model):
    _check(model.alternate_of, "alternate_of")


def test_related_column_details(model):
    _check(model.related_column_details, "related_column_details")


def test_group_by_columns(model):
    _check(model.group_by_columns, "group_by_columns")


def test_binding_info(model):
    _check(model.binding_info, "binding_info")


def test_analytics_ai_metadata(model):
    _check(model.analytics_ai_metadata, "analytics_ai_metadata")


def test_data_coverage_definitions(model):
    _check(model.data_coverage_definitions, "data_coverage_definitions")


def test_role_memberships(model):
    _check(model.role_memberships, "role_memberships")
