"""
Test suite for PBIXRay DAX-related properties API.
Tests: power_query, m_parameters, dax_tables, dax_measures, dax_columns for both PBIX and XLSX files.
"""
import pytest
import pandas as pd


class TestPowerQueryProperty:
    """Test the power_query property."""

    def test_pbix_power_query_returns_dataframe(self, pbix_model):
        """Test that power_query property returns a DataFrame for PBIX."""
        power_query = pbix_model.power_query
        assert isinstance(power_query, pd.DataFrame)

    def test_xlsx_power_query_returns_dataframe(self, xlsx_model):
        """Test that power_query property returns a DataFrame for XLSX."""
        power_query = xlsx_model.power_query
        assert isinstance(power_query, pd.DataFrame)

    def test_pbix_power_query_has_required_columns(self, pbix_model):
        """Test that PBIX power_query has required columns when not empty."""
        power_query = pbix_model.power_query
        if len(power_query) > 0:
            assert 'TableName' in power_query.columns
            assert 'Expression' in power_query.columns

    def test_xlsx_power_query_may_be_empty(self, xlsx_model):
        """Test that XLSX power_query may be empty (expected behavior)."""
        power_query = xlsx_model.power_query
        # XLSX files may not have Power Query - this is acceptable
        assert isinstance(power_query, pd.DataFrame)

    def test_power_query_expressions_are_strings(self, pbix_model):
        """Test that power query expressions are strings."""
        power_query = pbix_model.power_query
        if len(power_query) > 0 and 'Expression' in power_query.columns:
            for expr in power_query['Expression']:
                assert isinstance(expr, str) or pd.isna(expr)


class TestMParametersProperty:
    """Test the m_parameters property."""

    def test_pbix_m_parameters_returns_dataframe(self, pbix_model):
        """Test that m_parameters property returns a DataFrame for PBIX."""
        m_params = pbix_model.m_parameters
        assert isinstance(m_params, pd.DataFrame)

    def test_xlsx_m_parameters_returns_dataframe(self, xlsx_model):
        """Test that m_parameters property returns a DataFrame for XLSX."""
        m_params = xlsx_model.m_parameters
        assert isinstance(m_params, pd.DataFrame)

    def test_m_parameters_has_required_columns_when_not_empty(self, pbix_model):
        """Test that m_parameters has required columns when not empty."""
        m_params = pbix_model.m_parameters
        if len(m_params) > 0:
            expected_columns = ['ParameterName', 'Description', 'Expression', 'ModifiedTime']
            for col in expected_columns:
                assert col in m_params.columns, f"Missing column: {col}"

    def test_m_parameters_modified_time_is_datetime(self, pbix_model):
        """Test that ModifiedTime is datetime when parameters exist."""
        m_params = pbix_model.m_parameters
        if len(m_params) > 0 and 'ModifiedTime' in m_params.columns:
            assert pd.api.types.is_datetime64_any_dtype(m_params['ModifiedTime'])


class TestDaxTablesProperty:
    """Test the dax_tables property."""

    def test_pbix_dax_tables_returns_dataframe(self, pbix_model):
        """Test that dax_tables property returns a DataFrame for PBIX."""
        dax_tables = pbix_model.dax_tables
        assert isinstance(dax_tables, pd.DataFrame)

    def test_xlsx_dax_tables_returns_dataframe(self, xlsx_model):
        """Test that dax_tables property returns a DataFrame for XLSX."""
        dax_tables = xlsx_model.dax_tables
        assert isinstance(dax_tables, pd.DataFrame)

    def test_dax_tables_has_required_columns_when_not_empty(self, pbix_model):
        """Test that dax_tables has required columns when not empty."""
        dax_tables = pbix_model.dax_tables
        if len(dax_tables) > 0:
            assert 'TableName' in dax_tables.columns
            assert 'Expression' in dax_tables.columns

    def test_xlsx_dax_tables_may_be_empty(self, xlsx_model):
        """Test that XLSX dax_tables may be empty (expected behavior)."""
        dax_tables = xlsx_model.dax_tables
        # XLSX files may not have DAX calculated tables
        assert isinstance(dax_tables, pd.DataFrame)


class TestDaxMeasuresProperty:
    """Test the dax_measures property."""

    def test_pbix_dax_measures_returns_dataframe(self, pbix_model):
        """Test that dax_measures property returns a DataFrame for PBIX."""
        dax_measures = pbix_model.dax_measures
        assert isinstance(dax_measures, pd.DataFrame)

    def test_xlsx_dax_measures_returns_dataframe(self, xlsx_model):
        """Test that dax_measures property returns a DataFrame for XLSX."""
        dax_measures = xlsx_model.dax_measures
        assert isinstance(dax_measures, pd.DataFrame)

    def test_pbix_dax_measures_has_required_columns_when_not_empty(self, pbix_model):
        """Test that PBIX dax_measures has required columns when not empty."""
        dax_measures = pbix_model.dax_measures
        if len(dax_measures) > 0:
            expected_columns = ['TableName', 'Name', 'Expression', 
                              'DisplayFolder', 'Description']
            for col in expected_columns:
                assert col in dax_measures.columns, f"Missing column: {col}"

    def test_xlsx_dax_measures_may_be_empty(self, xlsx_model):
        """Test that XLSX dax_measures may be empty (expected behavior)."""
        dax_measures = xlsx_model.dax_measures
        # XLSX files may not have DAX measures
        assert isinstance(dax_measures, pd.DataFrame)

    def test_dax_measures_expressions_are_strings(self, pbix_model):
        """Test that DAX measure expressions are strings."""
        dax_measures = pbix_model.dax_measures
        if len(dax_measures) > 0 and 'Expression' in dax_measures.columns:
            for expr in dax_measures['Expression']:
                assert isinstance(expr, str) or pd.isna(expr)


class TestDaxColumnsProperty:
    """Test the dax_columns property."""

    def test_pbix_dax_columns_returns_dataframe(self, pbix_model):
        """Test that dax_columns property returns a DataFrame for PBIX."""
        dax_columns = pbix_model.dax_columns
        assert isinstance(dax_columns, pd.DataFrame)

    def test_xlsx_dax_columns_returns_dataframe(self, xlsx_model):
        """Test that dax_columns property returns a DataFrame for XLSX."""
        dax_columns = xlsx_model.dax_columns
        assert isinstance(dax_columns, pd.DataFrame)

    def test_dax_columns_has_required_columns_when_not_empty(self, pbix_model):
        """Test that dax_columns has required columns when not empty."""
        dax_columns = pbix_model.dax_columns
        if len(dax_columns) > 0:
            expected_columns = ['TableName', 'ColumnName', 'Expression']
            for col in expected_columns:
                assert col in dax_columns.columns, f"Missing column: {col}"

    def test_xlsx_dax_columns_may_be_empty(self, xlsx_model):
        """Test that XLSX dax_columns may be empty (expected behavior)."""
        dax_columns = xlsx_model.dax_columns
        # XLSX files may not have DAX calculated columns
        assert isinstance(dax_columns, pd.DataFrame)

    def test_dax_columns_expressions_are_strings(self, pbix_model):
        """Test that DAX column expressions are strings."""
        dax_columns = pbix_model.dax_columns
        if len(dax_columns) > 0 and 'Expression' in dax_columns.columns:
            for expr in dax_columns['Expression']:
                assert isinstance(expr, str) or pd.isna(expr)


class TestDaxPropertiesConsistency:
    """Test consistency across DAX-related properties."""

    def test_dax_tables_referenced_in_schema(self, pbix_model):
        """Test that DAX calculated tables appear in schema."""
        dax_tables = pbix_model.dax_tables
        schema = pbix_model.schema
        
        if len(dax_tables) > 0:
            # All DAX calculated tables should appear in the schema
            for table_name in dax_tables['TableName']:
                assert table_name in schema['TableName'].values, \
                    f"DAX table {table_name} not found in schema"

    def test_dax_measures_belong_to_existing_tables(self, pbix_model):
        """Test that DAX measures reference existing tables."""
        dax_measures = pbix_model.dax_measures
        tables = pbix_model.tables
        
        if len(dax_measures) > 0:
            for table_name in dax_measures['TableName'].unique():
                assert table_name in tables.values, \
                    f"Measure table {table_name} not found in tables list"

    def test_dax_columns_belong_to_existing_tables(self, pbix_model):
        """Test that DAX calculated columns reference existing tables."""
        dax_columns = pbix_model.dax_columns
        tables = pbix_model.tables
        
        if len(dax_columns) > 0:
            for table_name in dax_columns['TableName'].unique():
                assert table_name in tables.values, \
                    f"Column table {table_name} not found in tables list"
