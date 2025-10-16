# PBIXRay Test Suite

## Overview

This test suite provides comprehensive coverage of the PBIXRay API for parsing and analyzing both PBIX and XLSX files with Power Pivot models.

## Test Organization

### Test Files

- **`conftest.py`** - Pytest configuration and shared fixtures
- **`test_api_initialization.py`** - Tests for library initialization and file type detection
- **`test_api_metadata.py`** - Tests for metadata properties (tables, schema, size, statistics)
- **`test_api_dax.py`** - Tests for DAX-related properties (power_query, m_parameters, dax_tables, dax_measures, dax_columns)
- **`test_api_relationships_rls.py`** - Tests for relationships and RLS (Row-Level Security)
- **`test_api_get_table.py`** - Tests for the get_table() method
- **`test_api_integration.py`** - Integration tests and cross-property consistency checks

## Running Tests

### Prerequisites

Install test dependencies:

```bash
pip install pytest pytest-cov
```

### Run All Tests

```bash
# From the project root directory
pytest test/

# With verbose output
pytest test/ -v

# With coverage report
pytest test/ --cov=pbixray --cov-report=html
```

### Run Specific Test Files

```bash
# Test initialization only
pytest test/test_api_initialization.py -v

# Test metadata properties
pytest test/test_api_metadata.py -v

# Test get_table method
pytest test/test_api_get_table.py -v
```

### Run Specific Test Classes or Methods

```bash
# Run a specific test class
pytest test/test_api_metadata.py::TestTablesProperty -v

# Run a specific test method
pytest test/test_api_initialization.py::TestInitialization::test_pbix_initialization -v
```

## Test Data

Tests use sample files from the `data/` directory:

- **PBIX files**: `*.pbix` files (e.g., "Sales & Returns Sample v201912.pbix")
- **XLSX files**: `*.xlsx` files with Power Pivot models (e.g., "Supplier Quality Analysis Sample-no-PV.xlsx")

The test suite automatically discovers available test files and skips tests if no suitable files are found.

## Test Structure

### Fixtures

Defined in `conftest.py`:

- `sample_pbix_files` - List of all available PBIX test files
- `sample_xlsx_files` - List of all available XLSX test files
- `primary_pbix_file` - Primary PBIX file for detailed testing
- `primary_xlsx_file` - Primary XLSX file for detailed testing
- `pbix_model` - PBIXRay instance for PBIX file (module scope)
- `xlsx_model` - PBIXRay instance for XLSX file (module scope)
- `rls_model` - PBIXRay instance for RLS testing

### Test Categories

#### 1. Initialization Tests
- Verify successful initialization with PBIX and XLSX files
- Test file type detection
- Error handling for invalid files

#### 2. Metadata Tests
- `tables` property - returns Series of table names
- `metadata` property - returns DataFrame with model metadata
- `size` property - returns integer byte size
- `schema` property - returns DataFrame with table/column/type info
- `statistics` property - returns DataFrame with cardinality and size stats

#### 3. DAX Tests
- `power_query` property - returns DataFrame with M expressions
- `m_parameters` property - returns DataFrame with parameter definitions
- `dax_tables` property - returns DataFrame with calculated tables
- `dax_measures` property - returns DataFrame with DAX measures
- `dax_columns` property - returns DataFrame with calculated columns

#### 4. Relationships and RLS Tests
- `relationships` property - returns DataFrame with model relationships
- `rls` property - returns DataFrame with Row-Level Security rules

#### 5. Data Retrieval Tests
- `get_table()` method - retrieves table data as DataFrame
- Column consistency with schema
- Data type validation
- Error handling

#### 6. Integration Tests
- Cross-property consistency (tables match across different properties)
- End-to-end workflows
- PBIX vs XLSX comparison
- Error handling

## Expected Behavior

### PBIX Files
All properties should return data (may be empty DataFrames if feature not used in specific file):
- ✅ tables, metadata, size, schema, statistics
- ✅ power_query, m_parameters, dax_tables, dax_measures, dax_columns
- ✅ relationships, rls
- ✅ get_table()

### XLSX Files
Core properties work, DAX-related may be empty:
- ✅ tables, metadata, size, schema, statistics
- ⚠️ power_query, m_parameters (usually empty - not available in XLSX)
- ⚠️ dax_tables, dax_measures, dax_columns (may be limited)
- ⚠️ relationships, rls (may not be fully implemented)
- ✅ get_table()

## Writing New Tests

### Best Practices

1. **Use fixtures** from `conftest.py` for test data
2. **Test both PBIX and XLSX** where applicable
3. **Use descriptive test names** that explain what is being tested
4. **Include docstrings** explaining the test purpose
5. **Test edge cases** (empty results, missing data, invalid inputs)
6. **Group related tests** in classes
7. **Use parametrize** for testing same logic with different inputs

### Example Test

```python
import pytest
import pandas as pd

class TestNewFeature:
    """Test description."""

    def test_pbix_new_feature(self, pbix_model):
        """Test new feature with PBIX file."""
        result = pbix_model.new_feature
        assert isinstance(result, pd.DataFrame)
        assert len(result) >= 0

    def test_xlsx_new_feature(self, xlsx_model):
        """Test new feature with XLSX file."""
        result = xlsx_model.new_feature
        assert isinstance(result, pd.DataFrame)
```

## CI/CD Integration

To integrate with CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    pip install pytest pytest-cov
    pytest test/ --cov=pbixray --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

## Troubleshooting

### Tests Skip Due to Missing Files
If you see "No PBIX/XLSX files found", ensure sample files exist in `data/` directory.

### Import Errors
Install the package in development mode:
```bash
pip install -e .
```

### Fixture Not Found
Ensure `conftest.py` is in the `test/` directory and pytest can discover it.

## Contributing

When adding new API features:

1. Add tests in appropriate test file
2. Follow existing test patterns
3. Test both PBIX and XLSX support
4. Update this README if needed
5. Ensure all tests pass before submitting
