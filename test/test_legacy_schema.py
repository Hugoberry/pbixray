"""
Regression tests for legacy (pre-~2016) PowerPivot/Analysis Services metadata
schemas.

In SCHEMAVERSION < ~18 the ``Column`` table has no ``Type`` column; the column
role (1=Data, 2=Calculated, 3=RowNumber, 4=CalculatedTableColumn) is stored in
``Column.BindingType`` instead. Before the fix, ``__populate_schema`` referenced
``c.Type`` unconditionally, which raised ``SQLError: no such column: Type``; that
was swallowed into an empty schema and surfaced downstream as
``KeyError: 'DataType'`` while constructing ``PBIXRay``.

Fixture: ``data/old-schema17-DataTable.pbix`` (SCHEMAVERSION 17).
"""
import pandas as pd


def test_legacy_model_opens(legacy_schema17_model):
    """Construction must not raise on a schema with no Column.Type column."""
    assert legacy_schema17_model is not None


def test_legacy_tables_listed(legacy_schema17_model):
    tables = legacy_schema17_model.tables
    assert tables is not None and len(tables) > 0


def test_legacy_schema_populated(legacy_schema17_model):
    schema = legacy_schema17_model.schema
    assert isinstance(schema, pd.DataFrame)
    assert len(schema) > 0
    for col in ("TableName", "ColumnName", "PandasDataType"):
        assert col in schema.columns


def test_legacy_get_table_decodes(legacy_schema17_model):
    """The data path should still decode columns for a legacy model."""
    model = legacy_schema17_model
    table = next(iter(model.tables))
    df = model.get_table(table)
    assert df is not None
    assert df.shape[1] > 0


def test_legacy_metadata_properties(legacy_schema17_model):
    """Metadata accessors must return DataFrames, not raise."""
    model = legacy_schema17_model
    for prop in ("metadata", "schema", "relationships", "dax_measures"):
        assert isinstance(getattr(model, prop), pd.DataFrame)


def test_legacy_all_dmv_dataframes_realize(legacy_schema17_model):
    """Force-realize every lazy ``*_df`` populator on a legacy model.

    The Python analogue of the Swift ``test_oldABF_endToEnd_allFixtures`` sweep:
    legacy schemas rename/drop columns the modern DMV queries reference, so every
    populator must resolve to a DataFrame (degrading missing columns to NULL)
    rather than crashing. Populators whose whole table is absent in the legacy
    schema legitimately come back empty.
    """
    source = legacy_schema17_model._metadata.source
    for name in source._lazy_populators:
        df = getattr(source, name)
        assert isinstance(df, pd.DataFrame), f"{name} did not realize to a DataFrame"
    # Core high-traffic populators must actually carry data on this fixture.
    assert len(getattr(source, "tables_df")) > 0
    assert len(getattr(source, "columns_df")) > 0
    assert len(getattr(source, "partitions_df")) > 0


# ---------------------------------------------------------------------------
# Empty-schema models (only calculated tables / measures -> zero schema rows).
# The schema query matches no rows and the APSW wrapper returns a column-less
# frame; the model must still open instead of raising KeyError on the missing
# TableName/ColumnName/Cardinality columns.
# ---------------------------------------------------------------------------

def test_empty_schema_model_opens(empty_schema_model):
    assert empty_schema_model is not None


def test_empty_schema_has_stable_shape(empty_schema_model):
    model = empty_schema_model
    assert len(model.tables) == 0
    assert list(model.schema.columns) == ["TableName", "ColumnName", "PandasDataType"]
    assert len(model.schema) == 0
    # statistics is derived from the schema and must not raise either.
    assert isinstance(model.statistics, pd.DataFrame)


def test_empty_schema_measures_still_work(empty_schema_model):
    # Measures live in their own table, so they remain available even with an
    # empty column schema.
    assert isinstance(empty_schema_model.dax_measures, pd.DataFrame)
