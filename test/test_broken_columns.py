"""
Translated from duckdb-pbix-extension/test/sql/broken_columns.test

Verifies that tables with column names that conflict with internal metadata
schema names (ID, FileName, Name, Type) are read correctly.
"""
import pytest


def test_broken_columns_row_count(abc_model):
    table = abc_model.get_table("BrokenColumns")
    assert len(table) == 3


def test_broken_columns_all_columns_present(abc_model):
    table = abc_model.get_table("BrokenColumns")
    for col in ["ID", "FileName", "Name", "Type"]:
        assert col in table.columns, f"Expected column '{col}' not found in BrokenColumns table"


def test_broken_columns_values(abc_model):
    table = abc_model.get_table("BrokenColumns")
    assert set(table["FileName"]) == {"abc.xlsx", "xyz.pbix", "123.exe"}
    assert set(table["Type"]) == {"Red", "Blue", "Black"}
    assert set(table["Name"]) == {"ABC", "XYZ", "123"}


def test_broken_columns_id_values(abc_model):
    table = abc_model.get_table("BrokenColumns")
    assert set(table["ID"].astype(int)) == {100, 102, 103}


