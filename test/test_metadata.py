"""
Tests for all PBIXRay metadata properties across multiple PBIX files.
Covers the properties exercised by demo.py, translated into assertions.
"""
import datetime
import pandas as pd
import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_nonempty_df(obj):
    return isinstance(obj, pd.DataFrame) and not obj.empty


def _is_df(obj):
    return isinstance(obj, pd.DataFrame)


# ---------------------------------------------------------------------------
# Sales & Returns — general API surface
# ---------------------------------------------------------------------------

def test_sales_returns_tables(sales_returns_model):
    tables = sales_returns_model.tables
    assert tables is not None
    assert len(tables) > 0
    assert "Age" in tables


def test_sales_returns_metadata(sales_returns_model):
    assert _is_nonempty_df(sales_returns_model.metadata)


def test_sales_returns_power_query(sales_returns_model):
    assert _is_nonempty_df(sales_returns_model.power_query)


def test_sales_returns_statistics(sales_returns_model):
    assert _is_nonempty_df(sales_returns_model.statistics)


def test_sales_returns_size(sales_returns_model):
    # size returns the total model size in bytes as an integer
    size = sales_returns_model.size
    assert isinstance(size, int)
    assert size > 0


def test_sales_returns_schema(sales_returns_model):
    assert _is_nonempty_df(sales_returns_model.schema)


def test_sales_returns_relationships(sales_returns_model):
    assert _is_df(sales_returns_model.relationships)


def test_sales_returns_dax_measures(sales_returns_model):
    assert _is_df(sales_returns_model.dax_measures)


def test_sales_returns_rls(sales_returns_model):
    # Sales & Returns has no RLS — should still return a DataFrame, just empty
    assert _is_df(sales_returns_model.rls)


# ---------------------------------------------------------------------------
# Adventure Works — relationships and DAX measures
# ---------------------------------------------------------------------------

def test_adventure_works_relationships_nonempty(adventure_works_model):
    assert _is_nonempty_df(adventure_works_model.relationships)


def test_adventure_works_dax_measures_nonempty(adventure_works_model):
    assert _is_nonempty_df(adventure_works_model.dax_measures)


def test_adventure_works_statistics(adventure_works_model):
    assert _is_nonempty_df(adventure_works_model.statistics)


def test_adventure_works_schema(adventure_works_model):
    assert _is_nonempty_df(adventure_works_model.schema)


# ---------------------------------------------------------------------------
# Supplier Quality — DAX properties (RLS and m_parameters are empty in this file)
# ---------------------------------------------------------------------------

def test_supplier_quality_rls_returns_df(supplier_quality_model):
    assert _is_df(supplier_quality_model.rls)


def test_supplier_quality_dax_measures(supplier_quality_model):
    assert _is_df(supplier_quality_model.dax_measures)


def test_supplier_quality_dax_columns(supplier_quality_model):
    assert _is_df(supplier_quality_model.dax_columns)


# ---------------------------------------------------------------------------
# Adventure Works DW 2020 — full property sweep + get_table
# ---------------------------------------------------------------------------

def test_adventure_works_dw_tables(adventure_works_dw_model):
    tables = adventure_works_dw_model.tables
    assert tables is not None and len(tables) > 0


def test_adventure_works_dw_metadata(adventure_works_dw_model):
    assert _is_nonempty_df(adventure_works_dw_model.metadata)


def test_adventure_works_dw_power_query(adventure_works_dw_model):
    assert _is_nonempty_df(adventure_works_dw_model.power_query)


def test_adventure_works_dw_statistics(adventure_works_dw_model):
    assert _is_nonempty_df(adventure_works_dw_model.statistics)


def test_adventure_works_dw_dax_tables(adventure_works_dw_model):
    assert _is_df(adventure_works_dw_model.dax_tables)


def test_adventure_works_dw_dax_measures(adventure_works_dw_model):
    # Adventure Works DW 2020 has no DAX measures — should still return a DataFrame
    assert _is_df(adventure_works_dw_model.dax_measures)


def test_adventure_works_dw_size(adventure_works_dw_model):
    assert isinstance(adventure_works_dw_model.size, int)
    assert adventure_works_dw_model.size > 0


def test_adventure_works_dw_schema(adventure_works_dw_model):
    assert _is_nonempty_df(adventure_works_dw_model.schema)


def test_adventure_works_dw_relationships(adventure_works_dw_model):
    assert _is_nonempty_df(adventure_works_dw_model.relationships)


def test_adventure_works_dw_get_table_sales_order(adventure_works_dw_model):
    table = adventure_works_dw_model.get_table("Sales Order")
    assert _is_nonempty_df(table)


# ---------------------------------------------------------------------------
# 2020SU11 Blog Demo — m_parameters, get_table, and DAX properties
# (fixture provided by conftest.py)
# ---------------------------------------------------------------------------

def test_blog_demo_m_parameters_nonempty(blog_demo_model):
    assert _is_nonempty_df(blog_demo_model.m_parameters)


def test_blog_demo_m_parameters_modifiedtime_is_datetime(blog_demo_model):
    params = blog_demo_model.m_parameters
    assert "ModifiedTime" in params.columns
    for val in params["ModifiedTime"]:
        assert isinstance(val, datetime.datetime), f"Expected datetime, got {type(val)}: {val}"


def test_blog_demo_tables(blog_demo_model):
    assert len(blog_demo_model.tables) > 0


def test_blog_demo_power_query(blog_demo_model):
    assert _is_nonempty_df(blog_demo_model.power_query)


def test_blog_demo_dax_columns(blog_demo_model):
    assert _is_df(blog_demo_model.dax_columns)


def test_blog_demo_get_table_reseller(blog_demo_model):
    table = blog_demo_model.get_table("Reseller")
    assert _is_nonempty_df(table)


# ---------------------------------------------------------------------------
# Power Query / parameter classification
#
# The Expression table stores M parameters and shared queries together, and
# only `IsParameterQuery=true` in the expression's meta record separates them.
# Adventure Works, Internet Sales holds one of each: two shared queries
# (Product Category / Product Subcategory, staging queries with "Enable load"
# off) and one real parameter.
# ---------------------------------------------------------------------------

def test_parameters_exclude_shared_queries(adventure_works_model):
    params = adventure_works_model.m_parameters
    assert list(params["ParameterName"]) == ["Adventure Works DW Excel Path"]
    assert params["Expression"].str.contains("IsParameterQuery").all()


def test_shared_queries_surface_in_power_query(adventure_works_model):
    """A query with load disabled owns no partition — Expression is its only home."""
    queries = adventure_works_model.power_query
    shared = queries[queries["Kind"] == "Shared"]
    assert set(shared["TableName"]) == {"Product Category", "Product Subcategory"}
    assert shared["Expression"].str.strip().str.startswith("let").all()


def test_loaded_queries_still_come_from_partitions(adventure_works_model):
    queries = adventure_works_model.power_query
    loaded = queries[queries["Kind"] == "Table"]
    assert set(loaded["TableName"]) == set(adventure_works_model.tables)


def test_no_expression_is_both_a_query_and_a_parameter(adventure_works_model):
    """The two endpoints partition the Expression table; they must not overlap."""
    queries = adventure_works_model.power_query
    shared = set(queries[queries["Kind"] == "Shared"]["TableName"])
    parameters = set(adventure_works_model.m_parameters["ParameterName"])
    assert shared.isdisjoint(parameters)
    # A shared query is never also a loaded table, so nothing is double-counted.
    assert shared.isdisjoint(set(queries[queries["Kind"] == "Table"]["TableName"]))


def test_power_query_kind_is_always_populated(adventure_works_model):
    queries = adventure_works_model.power_query
    assert set(queries["Kind"]) <= {"Table", "Shared"}
    assert queries["Kind"].notna().all()


# ---------------------------------------------------------------------------
# Supplier Quality (old PBIX format) — get_table and remaining properties
# ---------------------------------------------------------------------------

def test_supplier_quality_rls_returns_df(supplier_quality_model):
    assert _is_df(supplier_quality_model.rls)


def test_supplier_quality_tables(supplier_quality_model):
    assert len(supplier_quality_model.tables) > 0


def test_supplier_quality_metadata(supplier_quality_model):
    assert _is_nonempty_df(supplier_quality_model.metadata)


def test_supplier_quality_statistics(supplier_quality_model):
    assert _is_nonempty_df(supplier_quality_model.statistics)


def test_supplier_quality_dax_tables(supplier_quality_model):
    assert _is_df(supplier_quality_model.dax_tables)


def test_supplier_quality_dax_measures(supplier_quality_model):
    assert _is_df(supplier_quality_model.dax_measures)


def test_supplier_quality_dax_columns(supplier_quality_model):
    assert _is_df(supplier_quality_model.dax_columns)


def test_supplier_quality_schema(supplier_quality_model):
    assert _is_nonempty_df(supplier_quality_model.schema)


def test_supplier_quality_relationships(supplier_quality_model):
    assert _is_df(supplier_quality_model.relationships)


def test_supplier_quality_get_table_vendor(supplier_quality_model):
    table = supplier_quality_model.get_table("Vendor")
    assert _is_nonempty_df(table)


# ---------------------------------------------------------------------------
# RLS sample report — row-level security rules
# ---------------------------------------------------------------------------

def test_rls_model_rls_nonempty(rls_model):
    assert _is_nonempty_df(rls_model.rls)


def test_rls_model_tables_nonempty(rls_model):
    assert len(rls_model.tables) > 0


# ---------------------------------------------------------------------------
# Excalidraw — dax_columns and get_table (DAX-defined table)
# ---------------------------------------------------------------------------

def test_excalidraw_tables_nonempty(excalidraw_model):
    assert len(excalidraw_model.tables) > 0


def test_excalidraw_dax_columns_nonempty(excalidraw_model):
    assert _is_nonempty_df(excalidraw_model.dax_columns)



