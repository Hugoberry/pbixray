# PBIXRay Test Suite - Quick Start Guide

A comprehensive test suite for the PBIXRay library has been created with **100+ tests** covering all API methods for both PBIX and XLSX files.

## 📁 Test Files Created

```
test/
├── conftest.py                      # Pytest configuration & fixtures
├── test_api_initialization.py       # Initialization & file type tests
├── test_api_metadata.py             # Metadata properties tests  
├── test_api_dax.py                  # DAX & Power Query tests
├── test_api_relationships_rls.py    # Relationships & RLS tests
├── test_api_get_table.py            # Data retrieval tests
├── test_api_integration.py          # Integration & consistency tests
├── requirements.txt                 # Test dependencies
├── README.md                        # Detailed documentation
├── TEST_SUITE_SUMMARY.md           # Complete summary
├── validate_setup.py               # Setup validator
└── run_tests.sh                    # Test runner script
```

## 🚀 Quick Start

### 1. Install Test Dependencies

```bash
pip install pytest pytest-cov
# or
pip install -r test/requirements.txt
```

### 2. Run All Tests

```bash
pytest test/ -v
```

### 3. Using the Test Runner Script

```bash
# Run all tests
./test/run_tests.sh all

# Run specific category
./test/run_tests.sh metadata

# Run with coverage
./test/run_tests.sh coverage

# Validate setup
./test/run_tests.sh validate
```

## 📊 API Coverage

### ✅ All Properties Tested

**Metadata Properties:**
- `tables` - List of table names
- `metadata` - Model metadata DataFrame
- `size` - Model size in bytes
- `schema` - Schema with table/column/types
- `statistics` - Cardinality and size stats

**DAX Properties:**
- `power_query` - M/Power Query expressions
- `m_parameters` - M Parameters
- `dax_tables` - DAX calculated tables
- `dax_measures` - DAX measures
- `dax_columns` - DAX calculated columns

**Relationship Properties:**
- `relationships` - Model relationships
- `rls` - Row-Level Security rules

**Methods:**
- `get_table(name)` - Retrieve table data

### 🔍 Test Categories

| Category | File | Tests |
|----------|------|-------|
| Initialization | `test_api_initialization.py` | File loading, type detection |
| Metadata | `test_api_metadata.py` | tables, metadata, size, schema, statistics |
| DAX | `test_api_dax.py` | power_query, m_parameters, dax_* |
| Relationships | `test_api_relationships_rls.py` | relationships, rls |
| Data Retrieval | `test_api_get_table.py` | get_table() method |
| Integration | `test_api_integration.py` | Workflows, consistency |

## 🧪 Sample Test Commands

```bash
# Run all tests with verbose output
pytest test/ -v

# Run specific test file
pytest test/test_api_metadata.py -v

# Run specific test class
pytest test/test_api_metadata.py::TestTablesProperty -v

# Run specific test method
pytest test/test_api_initialization.py::TestInitialization::test_pbix_initialization -v

# Run tests matching pattern
pytest test/ -k "metadata" -v

# Run with coverage report
pytest test/ --cov=pbixray --cov-report=html

# Run tests in parallel (faster)
pip install pytest-xdist
pytest test/ -n auto
```

## 📋 What's Tested

### PBIX Files
✅ All properties return data
✅ All methods work correctly
✅ Edge cases handled
✅ Error conditions tested

### XLSX Files
✅ Core properties work (tables, schema, statistics, size)
✅ DAX properties return DataFrames (may be empty)
✅ get_table() works correctly
✅ API compatibility with PBIX

### Test Quality
✅ Type validation
✅ Data integrity checks
✅ Cross-property consistency
✅ Error handling
✅ Integration workflows
✅ Both positive and negative cases

## 🔧 Validation

Run the setup validator to check everything is working:

```bash
python test/validate_setup.py
```

This will check:
- PBIXRay can be imported
- Pytest is available
- Test data files exist
- File loading works
- Test files are present

## 📈 Expected Output

When tests run successfully, you'll see:

```
test/test_api_initialization.py::TestInitialization::test_pbix_initialization PASSED
test/test_api_initialization.py::TestInitialization::test_xlsx_initialization PASSED
test/test_api_metadata.py::TestTablesProperty::test_pbix_tables_returns_series PASSED
test/test_api_metadata.py::TestTablesProperty::test_pbix_tables_not_empty PASSED
...
========================= X passed in Y.YYs =========================
```

## 📝 Key Features

### Industry Best Practices
- ✅ Pytest framework with fixtures
- ✅ Modular test organization
- ✅ Comprehensive documentation
- ✅ Reusable test fixtures
- ✅ Parametrized tests
- ✅ CI/CD ready

### Test Coverage
- ✅ Unit tests for each method
- ✅ Integration tests for workflows
- ✅ Consistency validation
- ✅ Error handling
- ✅ Edge cases

## 🐛 Troubleshooting

**Tests skip due to missing files:**
- Ensure PBIX/XLSX files exist in `data/` directory

**Import errors:**
```bash
pip install -e .  # Install package in development mode
```

**Pytest not found:**
```bash
pip install pytest pytest-cov
```

**See import warnings in IDE:**
- These are harmless - pytest is only needed at runtime

## 📚 Documentation

- **README.md** - Detailed test documentation
- **TEST_SUITE_SUMMARY.md** - Complete test summary
- **This file** - Quick start guide

## 🎯 Next Steps

1. **Run validation:** `python test/validate_setup.py`
2. **Run tests:** `pytest test/ -v`
3. **Check coverage:** `pytest test/ --cov=pbixray --cov-report=html`
4. **Review results:** Open `htmlcov/index.html` for coverage report

## 💡 Adding New Tests

See `test/README.md` for detailed instructions on:
- Writing new tests
- Using fixtures
- Best practices
- CI/CD integration

---

**Test Suite Statistics:**
- 📁 7 test files
- 🧪 30+ test classes  
- ✅ 100+ individual tests
- 📊 All API methods covered
- 🔄 PBIX and XLSX support
