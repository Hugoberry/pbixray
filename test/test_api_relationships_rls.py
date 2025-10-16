"""
Test suite for PBIXRay relationships and RLS properties API.
Tests: relationships, rls properties for both PBIX and XLSX files.
"""
import pytest
import pandas as pd


class TestRelationshipsProperty:
    """Test the relationships property."""

    def test_pbix_relationships_returns_dataframe(self, pbix_model):
        """Test that relationships property returns a DataFrame for PBIX."""
        relationships = pbix_model.relationships
        assert isinstance(relationships, pd.DataFrame)

    def test_xlsx_relationships_returns_dataframe(self, xlsx_model):
        """Test that relationships property returns a DataFrame for XLSX."""
        relationships = xlsx_model.relationships
        assert isinstance(relationships, pd.DataFrame)

    def test_pbix_relationships_has_required_columns_when_not_empty(self, pbix_model):
        """Test that PBIX relationships has required columns when not empty."""
        relationships = pbix_model.relationships
        if len(relationships) > 0:
            expected_columns = [
                'FromTableName', 'FromColumnName', 
                'ToTableName', 'ToColumnName',
                'IsActive', 'Cardinality', 'CrossFilteringBehavior',
                'FromKeyCount', 'ToKeyCount', 'RelyOnReferentialIntegrity'
            ]
            for col in expected_columns:
                assert col in relationships.columns, f"Missing column: {col}"

    def test_xlsx_relationships_may_be_empty(self, xlsx_model):
        """Test that XLSX relationships may be empty (expected behavior)."""
        relationships = xlsx_model.relationships
        # XLSX relationship parsing may not be fully implemented
        assert isinstance(relationships, pd.DataFrame)

    def test_relationships_reference_existing_tables(self, pbix_model):
        """Test that relationships reference existing tables."""
        relationships = pbix_model.relationships
        tables = pbix_model.tables
        
        if len(relationships) > 0:
            # Check FromTableName
            for table_name in relationships['FromTableName'].unique():
                assert table_name in tables.values, \
                    f"FromTableName {table_name} not found in tables"
            
            # Check ToTableName
            for table_name in relationships['ToTableName'].unique():
                assert table_name in tables.values, \
                    f"ToTableName {table_name} not found in tables"

    def test_relationships_have_valid_cardinality(self, pbix_model):
        """Test that relationships have valid cardinality values."""
        relationships = pbix_model.relationships
        valid_cardinalities = ['OneToOne', 'OneToMany', 'ManyToOne', 'ManyToMany']
        
        if len(relationships) > 0 and 'Cardinality' in relationships.columns:
            for cardinality in relationships['Cardinality']:
                assert cardinality in valid_cardinalities or pd.isna(cardinality), \
                    f"Invalid cardinality: {cardinality}"

    def test_relationships_isactive_is_boolean(self, pbix_model):
        """Test that IsActive column contains boolean values."""
        relationships = pbix_model.relationships
        
        if len(relationships) > 0 and 'IsActive' in relationships.columns:
            for is_active in relationships['IsActive']:
                assert isinstance(is_active, (bool, type(None))) or pd.isna(is_active), \
                    f"IsActive should be boolean, got: {type(is_active)}"

    def test_relationships_key_counts_are_numeric(self, pbix_model):
        """Test that key counts are numeric."""
        relationships = pbix_model.relationships
        
        if len(relationships) > 0:
            if 'FromKeyCount' in relationships.columns:
                assert pd.api.types.is_numeric_dtype(relationships['FromKeyCount']) or \
                       relationships['FromKeyCount'].isna().all()
            
            if 'ToKeyCount' in relationships.columns:
                assert pd.api.types.is_numeric_dtype(relationships['ToKeyCount']) or \
                       relationships['ToKeyCount'].isna().all()


class TestRLSProperty:
    """Test the rls (Row-Level Security) property."""

    def test_pbix_rls_returns_dataframe(self, pbix_model):
        """Test that rls property returns a DataFrame for PBIX."""
        rls = pbix_model.rls
        assert isinstance(rls, pd.DataFrame)

    def test_xlsx_rls_returns_dataframe(self, xlsx_model):
        """Test that rls property returns a DataFrame for XLSX."""
        rls = xlsx_model.rls
        assert isinstance(rls, pd.DataFrame)

    def test_rls_has_required_columns_when_not_empty(self, pbix_model):
        """Test that rls has required columns when not empty."""
        rls = pbix_model.rls
        if len(rls) > 0:
            expected_columns = [
                'TableName', 'RoleName', 'RoleDescription',
                'FilterExpression', 'State', 'MetadataPermission'
            ]
            for col in expected_columns:
                assert col in rls.columns, f"Missing column: {col}"

    def test_xlsx_rls_may_be_empty(self, xlsx_model):
        """Test that XLSX rls may be empty (expected behavior)."""
        rls = xlsx_model.rls
        # XLSX RLS parsing may not be fully implemented
        assert isinstance(rls, pd.DataFrame)

    def test_rls_references_existing_tables(self, pbix_model):
        """Test that RLS rules reference existing tables."""
        rls = pbix_model.rls
        tables = pbix_model.tables
        
        if len(rls) > 0 and 'TableName' in rls.columns:
            for table_name in rls['TableName'].unique():
                assert table_name in tables.values, \
                    f"RLS table {table_name} not found in tables"

    def test_rls_filter_expressions_are_strings(self, pbix_model):
        """Test that RLS filter expressions are strings."""
        rls = pbix_model.rls
        
        if len(rls) > 0 and 'FilterExpression' in rls.columns:
            for expr in rls['FilterExpression']:
                assert isinstance(expr, str) or pd.isna(expr)


class TestRLSWithSampleFile:
    """Test RLS functionality with a file that has RLS defined."""

    def test_rls_sample_file_has_rls_rules(self, rls_model):
        """Test that RLS sample file contains RLS rules."""
        rls = rls_model.rls
        assert len(rls) > 0, "RLS sample file should contain RLS rules"

    def test_rls_sample_file_has_roles(self, rls_model):
        """Test that RLS sample file has defined roles."""
        rls = rls_model.rls
        if len(rls) > 0 and 'RoleName' in rls.columns:
            roles = rls['RoleName'].unique()
            assert len(roles) > 0, "Should have at least one role defined"

    def test_rls_sample_file_has_filter_expressions(self, rls_model):
        """Test that RLS sample file has filter expressions."""
        rls = rls_model.rls
        if len(rls) > 0 and 'FilterExpression' in rls.columns:
            # At least some rules should have filter expressions
            non_empty_filters = rls['FilterExpression'].notna().sum()
            assert non_empty_filters > 0, "Should have at least one filter expression"


class TestRelationshipsAndRLSConsistency:
    """Test consistency between relationships and RLS."""

    def test_rls_tables_exist_in_model(self, pbix_model):
        """Test that all tables referenced in RLS exist in the model."""
        rls = pbix_model.rls
        tables = pbix_model.tables
        
        if len(rls) > 0 and 'TableName' in rls.columns:
            for table_name in rls['TableName'].unique():
                if pd.notna(table_name):
                    assert table_name in tables.values, \
                        f"RLS references non-existent table: {table_name}"

    def test_relationship_tables_have_columns_in_schema(self, pbix_model):
        """Test that relationship columns exist in schema."""
        relationships = pbix_model.relationships
        schema = pbix_model.schema
        
        if len(relationships) > 0:
            for _, rel in relationships.iterrows():
                # Check FromTable and FromColumn
                from_table = rel.get('FromTableName')
                from_column = rel.get('FromColumnName')
                if pd.notna(from_table) and pd.notna(from_column):
                    mask = (schema['TableName'] == from_table) & \
                           (schema['ColumnName'] == from_column)
                    assert mask.any(), \
                        f"Column {from_table}.{from_column} not found in schema"
                
                # Check ToTable and ToColumn
                to_table = rel.get('ToTableName')
                to_column = rel.get('ToColumnName')
                if pd.notna(to_table) and pd.notna(to_column):
                    mask = (schema['TableName'] == to_table) & \
                           (schema['ColumnName'] == to_column)
                    assert mask.any(), \
                        f"Column {to_table}.{to_column} not found in schema"
