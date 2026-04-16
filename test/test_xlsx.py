"""
Tests for xlsx parsing support.

PBIXRay accepts Excel workbooks (.xlsx) in addition to .pbix files — the same
API surface applies. The fixture is provided by conftest.py (xlsx_model).
"""
import pandas as pd
import pytest


def _is_nonempty_df(obj):
    return isinstance(obj, pd.DataFrame) and not obj.empty


def _is_df(obj):
    return isinstance(obj, pd.DataFrame)


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
