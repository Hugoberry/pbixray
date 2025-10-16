"""
Integration tests for PBIXRay API.
Tests end-to-end workflows and cross-property consistency.
"""
import pytest
import pandas as pd


class TestAPIConsistency:
    """Test consistency across different API properties."""

    def test_table_names_consistent_across_properties(self, pbix_model):
        """Test that table names are consistent across tables, schema, and statistics."""
        tables = pbix_model.tables
        schema = pbix_model.schema
        stats = pbix_model.statistics
        
        # Tables from tables property
        tables_set = set(tables)
        
        # Tables from schema
        schema_tables = set(schema['TableName'].unique())
        
        # Tables from statistics
        stats_tables = set(stats['TableName'].unique())
        
        # All should contain the same tables
        assert tables_set == schema_tables, \
            "Tables from 'tables' and 'schema' don't match"
        assert tables_set == stats_tables, \
            "Tables from 'tables' and 'statistics' don't match"

    def test_column_names_consistent_between_schema_and_stats(self, pbix_model):
        """Test that column names are consistent between schema and statistics."""
        schema = pbix_model.schema
        stats = pbix_model.statistics
        
        # Create a set of (table, column) tuples from schema
        schema_cols = set(zip(schema['TableName'], schema['ColumnName']))
        
        # Create a set of (table, column) tuples from statistics
        stats_cols = set(zip(stats['TableName'], stats['ColumnName']))
        
        # They should match
        assert schema_cols == stats_cols, \
            "Columns in schema and statistics don't match"

    def test_retrieved_table_columns_match_schema(self, pbix_model):
        """Test that retrieved table columns match what schema says."""
        tables = pbix_model.tables
        schema = pbix_model.schema
        
        if len(tables) > 0:
            # Test first 3 tables
            for table_name in list(tables)[:3]:
                table_data = pbix_model.get_table(table_name)
                expected_columns = set(
                    schema[schema['TableName'] == table_name]['ColumnName']
                )
                actual_columns = set(table_data.columns)
                
                assert expected_columns == actual_columns, \
                    f"Table {table_name}: columns don't match schema"


class TestEndToEndWorkflows:
    """Test complete workflows using multiple API methods."""

    def test_full_model_inspection_workflow(self, pbix_model):
        """Test a typical workflow of inspecting a model."""
        # Step 1: Get basic info
        size = pbix_model.size
        assert size > 0
        
        # Step 2: List all tables
        tables = pbix_model.tables
        assert len(tables) > 0
        
        # Step 3: Get schema
        schema = pbix_model.schema
        assert len(schema) > 0
        
        # Step 4: Get statistics
        stats = pbix_model.statistics
        assert len(stats) > 0
        
        # Step 5: Retrieve a table
        table_name = tables.iloc[0]
        table_data = pbix_model.get_table(table_name)
        assert isinstance(table_data, pd.DataFrame)

    def test_dax_inspection_workflow(self, pbix_model):
        """Test a workflow focused on DAX analysis."""
        # Get all DAX-related info
        dax_tables = pbix_model.dax_tables
        dax_measures = pbix_model.dax_measures
        dax_columns = pbix_model.dax_columns
        
        # All should be DataFrames
        assert isinstance(dax_tables, pd.DataFrame)
        assert isinstance(dax_measures, pd.DataFrame)
        assert isinstance(dax_columns, pd.DataFrame)
        
        # If there are measures, they should reference existing tables
        if len(dax_measures) > 0:
            tables = pbix_model.tables
            for table_name in dax_measures['TableName'].unique():
                assert table_name in tables.values

    def test_relationship_analysis_workflow(self, pbix_model):
        """Test a workflow focused on relationship analysis."""
        # Get relationships
        relationships = pbix_model.relationships
        assert isinstance(relationships, pd.DataFrame)
        
        if len(relationships) > 0:
            # Get schema to verify columns exist
            schema = pbix_model.schema
            
            # Check first relationship
            rel = relationships.iloc[0]
            from_table = rel['FromTableName']
            from_column = rel['FromColumnName']
            
            # Verify the column exists in schema
            mask = (schema['TableName'] == from_table) & \
                   (schema['ColumnName'] == from_column)
            assert mask.any(), "Relationship references non-existent column"

    def test_statistics_analysis_workflow(self, pbix_model):
        """Test a workflow focused on statistics and optimization."""
        # Get statistics
        stats = pbix_model.statistics
        assert len(stats) > 0
        
        # Calculate total size
        total_dict_size = stats['Dictionary'].sum()
        total_hash_size = stats['HashIndex'].sum()
        total_data_size = stats['DataSize'].sum()
        
        assert total_dict_size >= 0
        assert total_hash_size >= 0
        assert total_data_size >= 0
        
        # Model size should be related to component sizes
        model_size = pbix_model.size
        assert model_size > 0


class TestXLSXIntegration:
    """Integration tests specific to XLSX files."""

    def test_xlsx_full_workflow(self, xlsx_model):
        """Test complete workflow with XLSX file."""
        # Basic properties
        size = xlsx_model.size
        tables = xlsx_model.tables
        schema = xlsx_model.schema
        stats = xlsx_model.statistics
        
        assert size > 0
        assert len(tables) > 0
        assert len(schema) > 0
        assert len(stats) > 0
        
        # Retrieve a table
        if len(tables) > 0:
            table_name = tables.iloc[0]
            table_data = xlsx_model.get_table(table_name)
            assert isinstance(table_data, pd.DataFrame)

    def test_xlsx_dax_properties_are_dataframes(self, xlsx_model):
        """Test that XLSX DAX properties return DataFrames (may be empty)."""
        # These may be empty for XLSX, but should still be DataFrames
        assert isinstance(xlsx_model.power_query, pd.DataFrame)
        assert isinstance(xlsx_model.m_parameters, pd.DataFrame)
        assert isinstance(xlsx_model.dax_tables, pd.DataFrame)
        assert isinstance(xlsx_model.dax_measures, pd.DataFrame)
        assert isinstance(xlsx_model.dax_columns, pd.DataFrame)
        assert isinstance(xlsx_model.relationships, pd.DataFrame)
        assert isinstance(xlsx_model.rls, pd.DataFrame)


class TestCrossFileComparison:
    """Test comparing data across different file types."""

    def test_pbix_and_xlsx_have_same_api_surface(self, pbix_model, xlsx_model):
        """Test that PBIX and XLSX models expose the same API."""
        # Both should have the same properties
        pbix_props = dir(pbix_model)
        xlsx_props = dir(xlsx_model)
        
        # Key API properties
        key_props = [
            'tables', 'metadata', 'size', 'schema', 'statistics',
            'power_query', 'm_parameters', 'dax_tables', 'dax_measures',
            'dax_columns', 'relationships', 'rls', 'get_table'
        ]
        
        for prop in key_props:
            assert prop in pbix_props, f"PBIX model missing property: {prop}"
            assert prop in xlsx_props, f"XLSX model missing property: {prop}"

    def test_pbix_and_xlsx_return_same_types(self, pbix_model, xlsx_model):
        """Test that PBIX and XLSX return the same types for properties."""
        # DataFrame properties
        df_props = [
            'metadata', 'schema', 'statistics', 'power_query',
            'm_parameters', 'dax_tables', 'dax_measures', 'dax_columns',
            'relationships', 'rls'
        ]
        
        for prop in df_props:
            pbix_val = getattr(pbix_model, prop)
            xlsx_val = getattr(xlsx_model, prop)
            assert type(pbix_val) == type(xlsx_val), \
                f"Type mismatch for {prop}: PBIX={type(pbix_val)}, XLSX={type(xlsx_val)}"

    def test_both_file_types_have_tables_and_data(self, pbix_model, xlsx_model):
        """Test that both file types have tables and retrievable data."""
        # PBIX should have tables
        pbix_tables = pbix_model.tables
        assert len(pbix_tables) > 0
        
        # XLSX should have tables
        xlsx_tables = xlsx_model.tables
        assert len(xlsx_tables) > 0
        
        # Both should be able to retrieve table data
        pbix_data = pbix_model.get_table(pbix_tables.iloc[0])
        xlsx_data = xlsx_model.get_table(xlsx_tables.iloc[0])
        
        assert isinstance(pbix_data, pd.DataFrame)
        assert isinstance(xlsx_data, pd.DataFrame)


class TestErrorHandling:
    """Test error handling across the API."""

    def test_get_table_with_none(self, pbix_model):
        """Test that get_table handles None gracefully."""
        with pytest.raises((TypeError, AttributeError, Exception)):
            pbix_model.get_table(None)

    def test_get_table_with_empty_string(self, pbix_model):
        """Test that get_table handles empty string gracefully."""
        with pytest.raises(Exception):
            pbix_model.get_table("")

    def test_properties_dont_raise_exceptions(self, pbix_model):
        """Test that accessing properties doesn't raise exceptions."""
        try:
            _ = pbix_model.tables
            _ = pbix_model.metadata
            _ = pbix_model.size
            _ = pbix_model.schema
            _ = pbix_model.statistics
            _ = pbix_model.power_query
            _ = pbix_model.m_parameters
            _ = pbix_model.dax_tables
            _ = pbix_model.dax_measures
            _ = pbix_model.dax_columns
            _ = pbix_model.relationships
            _ = pbix_model.rls
        except Exception as e:
            pytest.fail(f"Property access raised exception: {e}")
