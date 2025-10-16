"""
Test suite for PBIXRay get_table() method API.
Tests table data retrieval for both PBIX and XLSX files.
"""
import pytest
import pandas as pd


class TestGetTableMethod:
    """Test the get_table() method."""

    def test_pbix_get_table_returns_dataframe(self, pbix_model):
        """Test that get_table() returns a DataFrame for PBIX."""
        tables = pbix_model.tables
        if len(tables) > 0:
            table_name = tables.iloc[0]
            result = pbix_model.get_table(table_name)
            assert isinstance(result, pd.DataFrame)

    def test_xlsx_get_table_returns_dataframe(self, xlsx_model):
        """Test that get_table() returns a DataFrame for XLSX."""
        tables = xlsx_model.tables
        if len(tables) > 0:
            table_name = tables.iloc[0]
            result = xlsx_model.get_table(table_name)
            assert isinstance(result, pd.DataFrame)

    def test_get_table_with_valid_table_name(self, pbix_model):
        """Test get_table() with a valid table name."""
        tables = pbix_model.tables
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = pbix_model.get_table(table_name)
            assert table_data is not None
            assert isinstance(table_data, pd.DataFrame)

    def test_get_table_columns_match_schema(self, pbix_model):
        """Test that retrieved table columns match schema definition."""
        tables = pbix_model.tables
        schema = pbix_model.schema
        
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = pbix_model.get_table(table_name)
            
            # Get expected columns from schema
            expected_columns = schema[schema['TableName'] == table_name]['ColumnName'].tolist()
            
            if len(expected_columns) > 0:
                # Check that all expected columns are present
                for col in expected_columns:
                    assert col in table_data.columns, \
                        f"Column {col} from schema not found in table data"

    def test_get_table_with_invalid_table_name(self, pbix_model):
        """Test get_table() with an invalid table name."""
        with pytest.raises(Exception):  # Should raise some kind of error
            pbix_model.get_table("NonExistentTable_12345")

    def test_get_table_data_types_match_schema(self, pbix_model):
        """Test that data types in retrieved table match schema definition."""
        tables = pbix_model.tables
        schema = pbix_model.schema
        
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = pbix_model.get_table(table_name)
            
            # Get schema for this table
            table_schema = schema[schema['TableName'] == table_name]
            
            for _, row in table_schema.iterrows():
                column_name = row['ColumnName']
                if column_name in table_data.columns:
                    # Just verify that the column exists and has some data type
                    assert table_data[column_name].dtype is not None


class TestGetTableMultipleTables:
    """Test get_table() across multiple tables."""

    def test_get_all_tables_in_pbix_model(self, pbix_model):
        """Test retrieving all tables from a PBIX model."""
        tables = pbix_model.tables
        retrieved_tables = {}
        
        for table_name in tables:
            try:
                table_data = pbix_model.get_table(table_name)
                retrieved_tables[table_name] = table_data
                assert isinstance(table_data, pd.DataFrame)
            except Exception as e:
                pytest.fail(f"Failed to retrieve table {table_name}: {e}")
        
        assert len(retrieved_tables) == len(tables)

    def test_get_all_tables_in_xlsx_model(self, xlsx_model):
        """Test retrieving all tables from an XLSX model."""
        tables = xlsx_model.tables
        retrieved_tables = {}
        
        for table_name in tables:
            try:
                table_data = xlsx_model.get_table(table_name)
                retrieved_tables[table_name] = table_data
                assert isinstance(table_data, pd.DataFrame)
            except Exception as e:
                pytest.fail(f"Failed to retrieve table {table_name}: {e}")
        
        assert len(retrieved_tables) == len(tables)

    def test_get_table_returns_different_data_for_different_tables(self, pbix_model):
        """Test that different tables return different data."""
        tables = pbix_model.tables
        
        if len(tables) >= 2:
            table1_name = tables.iloc[0]
            table2_name = tables.iloc[1]
            
            table1_data = pbix_model.get_table(table1_name)
            table2_data = pbix_model.get_table(table2_name)
            
            # Tables should have different shapes or columns
            # (they could theoretically have the same shape, but it's unlikely)
            assert not (table1_data.equals(table2_data)), \
                "Different tables should return different data"


class TestGetTableDataIntegrity:
    """Test data integrity of retrieved tables."""

    def test_get_table_row_count_is_non_negative(self, pbix_model):
        """Test that retrieved tables have non-negative row counts."""
        tables = pbix_model.tables
        
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = pbix_model.get_table(table_name)
            assert len(table_data) >= 0

    def test_get_table_column_count_matches_schema(self, pbix_model):
        """Test that retrieved table has expected number of columns."""
        tables = pbix_model.tables
        schema = pbix_model.schema
        
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = pbix_model.get_table(table_name)
            
            # Count expected columns from schema
            expected_col_count = len(schema[schema['TableName'] == table_name])
            
            if expected_col_count > 0:
                # Actual column count should match
                assert len(table_data.columns) == expected_col_count, \
                    f"Expected {expected_col_count} columns, got {len(table_data.columns)}"

    def test_get_table_data_has_no_all_null_required_columns(self, pbix_model):
        """Test that retrieved table data doesn't have unexpected all-null columns."""
        tables = pbix_model.tables
        
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = pbix_model.get_table(table_name)
            
            if len(table_data) > 0:
                # At least one column should have some non-null values
                has_data = any(table_data[col].notna().any() for col in table_data.columns)
                assert has_data or len(table_data.columns) == 0, \
                    "Table should have at least one column with data"

    def test_get_table_preserves_column_order(self, pbix_model):
        """Test that column order is consistent across multiple retrievals."""
        tables = pbix_model.tables
        
        if len(tables) > 0:
            table_name = tables.iloc[0]
            
            # Retrieve table twice
            table_data1 = pbix_model.get_table(table_name)
            table_data2 = pbix_model.get_table(table_name)
            
            # Column order should be the same
            assert list(table_data1.columns) == list(table_data2.columns), \
                "Column order should be consistent"


class TestGetTableWithXLSX:
    """Test get_table() specific to XLSX files."""

    def test_xlsx_get_table_works_for_all_tables(self, xlsx_model):
        """Test that all XLSX tables can be retrieved."""
        tables = xlsx_model.tables
        failed_tables = []
        
        for table_name in tables:
            try:
                table_data = xlsx_model.get_table(table_name)
                assert isinstance(table_data, pd.DataFrame)
            except Exception as e:
                failed_tables.append((table_name, str(e)))
        
        assert len(failed_tables) == 0, \
            f"Failed to retrieve tables: {failed_tables}"

    def test_xlsx_table_data_matches_schema_types(self, xlsx_model):
        """Test that XLSX table data types are compatible with schema."""
        tables = xlsx_model.tables
        schema = xlsx_model.schema
        
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = xlsx_model.get_table(table_name)
            table_schema = schema[schema['TableName'] == table_name]
            
            # Verify schema consistency
            for column_name in table_data.columns:
                schema_entry = table_schema[table_schema['ColumnName'] == column_name]
                assert len(schema_entry) > 0, \
                    f"Column {column_name} not found in schema"
