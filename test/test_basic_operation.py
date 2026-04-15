import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pbix')))

from pbixray import PBIXRay

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

PBIX_FILE_PATH = os.path.join(DATA_DIR, "Sales & Returns Sample v201912.pbix")
# C:\git\hub\pbixray\data\Excalidraw.pbix

ADVENTURE_WORKS_PATH = os.path.join(DATA_DIR, "Adventure Works, Internet Sales.pbix")

def test_initialization():
    """Test initialization of the library with the test PBIX file."""
    model = PBIXRay(PBIX_FILE_PATH)
    assert model is not None, "Failed to initialize PBIXRay with the test PBIX file."

def test_metadata_retrieval():
    """Test retrieval of metadata (tables, columns)."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    tables = model.tables
    #test number of tables greater than 0
    assert tables.size, "No tables found in the PBIX file."
    
    assert "Age" in tables, "Expected table 'Age' not found in the PBIX file."
    
def test_data_retrieval():
    """Test data retrieval from a specific table."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    table = model.get_table("Age")
    assert table.size, "Failed to retrieve the 'Age' table."


@pytest.fixture(scope="module")
def adventure_works_model():
    return PBIXRay(ADVENTURE_WORKS_PATH)


def test_adventure_works_product_table_unvertipaq(adventure_works_model):
    """Test that the Product table can be unvertipaqed from Adventure Works, Internet Sales.pbix."""
    table = adventure_works_model.get_table("Product")
    assert table is not None, "get_table('Product') returned None."
    assert not table.empty, "Product table is empty after unvertipaqing."
    assert len(table) > 0, "Product table has no rows."


def test_adventure_works_internet_sales_null_columns(adventure_works_model):
    """Test that CarrierTrackingNumber and CustomerPONumber in Internet Sales are all NULL."""
    table = adventure_works_model.get_table("Internet Sales")
    assert table is not None, "get_table('Internet Sales') returned None."
    assert not table.empty, "Internet Sales table is empty."
    assert "CarrierTrackingNumber" in table.columns, "'CarrierTrackingNumber' column not found."
    assert "CustomerPONumber" in table.columns, "'CustomerPONumber' column not found."
    assert table["CarrierTrackingNumber"].isna().all(), "CarrierTrackingNumber contains non-NULL values."
    assert table["CustomerPONumber"].isna().all(), "CustomerPONumber contains non-NULL values."

