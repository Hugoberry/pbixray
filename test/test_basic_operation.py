import pytest
from pbixray import PBIXRay

PBIX_FILE_PATH = r"C:\git\hub\pbixray\test-data\Sales & Returns Sample v201912.pbix"
# C:\git\hub\pbixray\test-data\Excalidraw.pbix

def test_initialization():
    """Test initialization of the library with the test PBIX file."""
    model = PBIXRay(PBIX_FILE_PATH)
    assert model is not None, "Failed to initialize PBIXRay with the test PBIX file."

def test_metadata_retrieval():
    """Test retrieval of metadata (tables, columns)."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    tables = model.list_tables()
    assert tables, "No tables found in the PBIX file."
    
    assert "Fruit" in tables, "Expected table 'Fruit' not found in the PBIX file."
    
    columns = model.list_columns("Fruit")
    assert columns, "No columns found in the 'Fruit' table."

def test_data_retrieval():
    """Test data retrieval from a specific table."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    table = model.get_table("Fruit")
    assert table, "Failed to retrieve the 'Fruit' table."
    
    arrow_table = table.to_arrow_table()
    assert arrow_table, "Failed to retrieve data from 'Fruit' table as an Arrow table."

    dataframe = table.to_dataframe()
    assert not dataframe.empty, "Failed to retrieve data from 'Fruit' table as a DataFrame."
