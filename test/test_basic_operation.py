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
    #test number of tables greater than 0
    assert tables.size, "No tables found in the PBIX file."
    
    assert "Age" in tables, "Expected table 'Age' not found in the PBIX file."
    
    columns = model.list_columns("Age")
    assert columns.size, "No columns found in the 'Age' table."

def test_data_retrieval():
    """Test data retrieval from a specific table."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    table = model.get_table("Age")
    assert table.size, "Failed to retrieve the 'Age' table."
    
    # arrow_table = table.to_arrow_table()
    # assert arrow_table, "Failed to retrieve data from 'Age' table as an Arrow table."

    # dataframe = table.to_dataframe()
    # assert not dataframe.empty, "Failed to retrieve data from 'Age' table as a DataFrame."
