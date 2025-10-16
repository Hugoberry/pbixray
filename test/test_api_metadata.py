"""
Test suite for PBIXRay metadata properties API.
Tests: tables, metadata, size, schema properties for both PBIX and XLSX files.
"""
import pytest
import pandas as pd


class TestTablesProperty:
    """Test the tables property."""

    def test_pbix_tables_returns_series(self, pbix_model):
        """Test that tables property returns a pandas Series for PBIX."""
        tables = pbix_model.tables
        assert isinstance(tables, pd.Series)

    def test_xlsx_tables_returns_series(self, xlsx_model):
        """Test that tables property returns a pandas Series for XLSX."""
        tables = xlsx_model.tables
        assert isinstance(tables, pd.Series)

    def test_pbix_tables_not_empty(self, pbix_model):
        """Test that PBIX file contains tables."""
        tables = pbix_model.tables
        assert len(tables) > 0, "PBIX file should contain at least one table"

    def test_xlsx_tables_not_empty(self, xlsx_model):
        """Test that XLSX file contains tables."""
        tables = xlsx_model.tables
        assert len(tables) > 0, "XLSX file should contain at least one table"

    def test_tables_have_names(self, pbix_model):
        """Test that all tables have valid names."""
        tables = pbix_model.tables
        for table_name in tables:
            assert table_name is not None
            assert isinstance(table_name, str)
            assert len(table_name) > 0


class TestMetadataProperty:
    """Test the metadata property."""

    def test_pbix_metadata_returns_dataframe(self, pbix_model):
        """Test that metadata property returns a DataFrame for PBIX."""
        metadata = pbix_model.metadata
        assert isinstance(metadata, pd.DataFrame)

    def test_xlsx_metadata_returns_dataframe(self, xlsx_model):
        """Test that metadata property returns a DataFrame for XLSX."""
        metadata = xlsx_model.metadata
        assert isinstance(metadata, pd.DataFrame)

    def test_pbix_metadata_not_empty(self, pbix_model):
        """Test that PBIX metadata is not empty."""
        metadata = pbix_model.metadata
        assert len(metadata) > 0


class TestSizeProperty:
    """Test the size property."""

    def test_pbix_size_returns_integer(self, pbix_model):
        """Test that size property returns an integer for PBIX."""
        size = pbix_model.size
        assert isinstance(size, int)

    def test_xlsx_size_returns_integer(self, xlsx_model):
        """Test that size property returns an integer for XLSX."""
        size = xlsx_model.size
        assert isinstance(size, int)

    def test_pbix_size_is_positive(self, pbix_model):
        """Test that PBIX size is positive."""
        size = pbix_model.size
        assert size > 0, "Model size should be greater than 0"

    def test_xlsx_size_is_positive(self, xlsx_model):
        """Test that XLSX size is positive."""
        size = xlsx_model.size
        assert size > 0, "Model size should be greater than 0"


class TestSchemaProperty:
    """Test the schema property."""

    def test_pbix_schema_returns_dataframe(self, pbix_model):
        """Test that schema property returns a DataFrame for PBIX."""
        schema = pbix_model.schema
        assert isinstance(schema, pd.DataFrame)

    def test_xlsx_schema_returns_dataframe(self, xlsx_model):
        """Test that schema property returns a DataFrame for XLSX."""
        schema = xlsx_model.schema
        assert isinstance(schema, pd.DataFrame)

    def test_pbix_schema_has_required_columns(self, pbix_model):
        """Test that PBIX schema has required columns."""
        schema = pbix_model.schema
        assert 'TableName' in schema.columns
        assert 'ColumnName' in schema.columns
        assert 'PandasDataType' in schema.columns

    def test_xlsx_schema_has_required_columns(self, xlsx_model):
        """Test that XLSX schema has required columns."""
        schema = xlsx_model.schema
        assert 'TableName' in schema.columns
        assert 'ColumnName' in schema.columns
        assert 'PandasDataType' in schema.columns

    def test_pbix_schema_not_empty(self, pbix_model):
        """Test that PBIX schema is not empty."""
        schema = pbix_model.schema
        assert len(schema) > 0, "Schema should contain at least one row"

    def test_xlsx_schema_not_empty(self, xlsx_model):
        """Test that XLSX schema is not empty."""
        schema = xlsx_model.schema
        assert len(schema) > 0, "Schema should contain at least one row"

    def test_schema_datatypes_are_valid(self, pbix_model):
        """Test that schema contains valid pandas data types."""
        schema = pbix_model.schema
        valid_types = ['object', 'int64', 'float64', 'bool', 'datetime64[ns]', 
                      'Int64', 'Float64', 'string', 'category']
        
        for dtype in schema['PandasDataType']:
            # Check if it's a base type or starts with a valid type
            assert any(dtype == vt or str(dtype).startswith(vt) for vt in valid_types), \
                f"Invalid data type found: {dtype}"


class TestStatisticsProperty:
    """Test the statistics property."""

    def test_pbix_statistics_returns_dataframe(self, pbix_model):
        """Test that statistics property returns a DataFrame for PBIX."""
        stats = pbix_model.statistics
        assert isinstance(stats, pd.DataFrame)

    def test_xlsx_statistics_returns_dataframe(self, xlsx_model):
        """Test that statistics property returns a DataFrame for XLSX."""
        stats = xlsx_model.statistics
        assert isinstance(stats, pd.DataFrame)

    def test_pbix_statistics_has_required_columns(self, pbix_model):
        """Test that PBIX statistics has required columns."""
        stats = pbix_model.statistics
        expected_columns = ['TableName', 'ColumnName', 'Cardinality', 
                          'Dictionary', 'HashIndex', 'DataSize']
        for col in expected_columns:
            assert col in stats.columns, f"Missing column: {col}"

    def test_xlsx_statistics_has_required_columns(self, xlsx_model):
        """Test that XLSX statistics has required columns."""
        stats = xlsx_model.statistics
        expected_columns = ['TableName', 'ColumnName', 'Cardinality', 
                          'Dictionary', 'HashIndex', 'DataSize']
        for col in expected_columns:
            assert col in stats.columns, f"Missing column: {col}"

    def test_statistics_values_are_numeric(self, pbix_model):
        """Test that statistics contains numeric values where expected."""
        stats = pbix_model.statistics
        numeric_columns = ['Cardinality', 'Dictionary', 'HashIndex', 'DataSize']
        
        for col in numeric_columns:
            if col in stats.columns and len(stats) > 0:
                # Check that values are numeric (allowing for NaN)
                assert pd.api.types.is_numeric_dtype(stats[col]), \
                    f"Column {col} should be numeric"
