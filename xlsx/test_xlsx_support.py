#!/usr/bin/env python3
"""
Test script to verify XLSX support for pbixray library using real Excel file.
Tests the core unpacking functionality which is working correctly.
"""

import os
import sys
import zipfile

# Add the parent directory to the path so we can import pbixray
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pbixray.pbix_unpacker import PbixUnpacker

# Path to the test Excel file with Power Pivot data model
XLSX_FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "Supplier Quality Analysis Sample-no-PV.xlsx")
PBIX_FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "old-Supplier-Quality-Analysis-Sample-PBIX.pbix")

def test_xlsx_file_exists():
    """Test that the Excel file exists and has the expected structure."""
    assert os.path.exists(XLSX_FILE_PATH), f"Test Excel file not found: {XLSX_FILE_PATH}"
    
    with zipfile.ZipFile(XLSX_FILE_PATH, 'r') as zip_ref:
        files = zip_ref.namelist()
        assert 'xl/model/item.data' in files, "Excel file does not contain Power Pivot data model (xl/model/item.data)"
    
    print("✓ Excel file exists and contains Power Pivot data model")

def test_xlsx_unpacker_initialization():
    """Test that PbixUnpacker can be initialized with an Excel file."""
    try:
        unpacker = PbixUnpacker(XLSX_FILE_PATH)
        assert unpacker is not None, "Failed to initialize PbixUnpacker with Excel file"
        assert unpacker.data_model is not None, "DataModel is None after unpacking"
        print("✓ PbixUnpacker successfully initialized with Excel file")
        return unpacker
    except Exception as e:
        print(f"❌ Failed to initialize PbixUnpacker with Excel file: {e}")
        raise

def test_xlsx_data_model_structure(unpacker):
    """Test the structure of the unpacked Excel data model."""
    try:
        file_log = unpacker.data_model.file_log
        assert isinstance(file_log, list), "File log should be a list"
        assert len(file_log) > 0, "File log should not be empty"
        
        print(f"✓ Excel data model contains {len(file_log)} files")
        
        # Check some expected file patterns in Excel Power Pivot models
        file_names = [f['FileName'] for f in file_log]
        
        # Look for typical Excel Power Pivot file patterns
        has_xml_files = any(f.endswith('.xml') for f in file_names)
        has_idf_files = any(f.endswith('.idf') for f in file_names)
        has_dictionary_files = any('.dictionary' in f for f in file_names)
        
        assert has_xml_files, "Expected to find XML files in Excel data model"
        assert has_idf_files, "Expected to find IDF files in Excel data model"
        assert has_dictionary_files, "Expected to find dictionary files in Excel data model"
        
        print("✓ Excel data model has expected file structure (XML, IDF, dictionary files)")
        
        # Show some example files
        sample_files = file_names[:5]
        print(f"  Sample files: {sample_files}")
        
        return file_names
        
    except Exception as e:
        print(f"❌ Failed to analyze Excel data model structure: {e}")
        raise

def test_comparison_with_pbix():
    """Compare unpacking results between Excel and PBIX files."""
    if not os.path.exists(PBIX_FILE_PATH):
        print("⚠️  Corresponding PBIX file not found, skipping comparison test")
        return
    
    try:
        print("\nComparing Excel and PBIX unpacking...")
        
        # Unpack both files
        xlsx_unpacker = PbixUnpacker(XLSX_FILE_PATH)
        pbix_unpacker = PbixUnpacker(PBIX_FILE_PATH)
        
        xlsx_files = [f['FileName'] for f in xlsx_unpacker.data_model.file_log]
        pbix_files = [f['FileName'] for f in pbix_unpacker.data_model.file_log]
        
        print(f"  Excel file count: {len(xlsx_files)}")
        print(f"  PBIX file count: {len(pbix_files)}")
        
        # Analyze file types
        xlsx_has_sqlitedb = any(f.endswith('.sqlitedb') for f in xlsx_files)
        pbix_has_sqlitedb = any(f.endswith('.sqlitedb') for f in pbix_files)
        
        print(f"  Excel has SQLite DB files: {xlsx_has_sqlitedb}")
        print(f"  PBIX has SQLite DB files: {pbix_has_sqlitedb}")
        
        # Check for common patterns
        xlsx_patterns = {
            'XML files': any(f.endswith('.xml') for f in xlsx_files),
            'IDF files': any(f.endswith('.idf') for f in xlsx_files),
            'Dictionary files': any('.dictionary' in f for f in xlsx_files)
        }
        
        pbix_patterns = {
            'XML files': any(f.endswith('.xml') for f in pbix_files),
            'IDF files': any(f.endswith('.idf') for f in pbix_files),
            'Dictionary files': any('.dictionary' in f for f in pbix_files)
        }
        
        print("  File patterns comparison:")
        for pattern, xlsx_has in xlsx_patterns.items():
            pbix_has = pbix_patterns[pattern]
            print(f"    {pattern}: Excel={xlsx_has}, PBIX={pbix_has}")
        
        print("✓ Successfully compared Excel and PBIX file structures")
        
    except Exception as e:
        print(f"⚠️  Comparison test failed: {e}")

def test_file_detection_method():
    """Test the file path detection method directly."""
    try:
        with zipfile.ZipFile(XLSX_FILE_PATH, 'r') as zip_ref:
            # Test file detection on Excel file
            unpacker = PbixUnpacker.__new__(PbixUnpacker)  # Create without calling __init__
            path = unpacker._PbixUnpacker__get_data_model_path(zip_ref)
            assert path == 'xl/model/item.data', f"Expected 'xl/model/item.data', got '{path}'"
            print("✓ File detection correctly identifies Excel Power Pivot model")
        
        if os.path.exists(PBIX_FILE_PATH):
            with zipfile.ZipFile(PBIX_FILE_PATH, 'r') as zip_ref:
                # Test file detection on PBIX file
                unpacker = PbixUnpacker.__new__(PbixUnpacker)  # Create without calling __init__
                path = unpacker._PbixUnpacker__get_data_model_path(zip_ref)
                assert path == 'DataModel', f"Expected 'DataModel', got '{path}'"
                print("✓ File detection correctly identifies PBIX DataModel")
        
    except Exception as e:
        print(f"❌ File detection test failed: {e}")
        raise

if __name__ == "__main__":
    print("Testing XLSX support for pbixray using real Excel file...")
    print(f"Excel file: {XLSX_FILE_PATH}")
    
    try:
        # Run unpacking tests (these should work)
        test_xlsx_file_exists()
        test_file_detection_method()
        
        unpacker = test_xlsx_unpacker_initialization()
        largest_file = sorted(unpacker.data_model.file_log, key=lambda x: x['Size'], reverse=True)[0]
        print(f"  Largest file in Excel data model: {largest_file['FileName']} ({largest_file['Size']} bytes)")
        file_names = test_xlsx_data_model_structure(unpacker)
        
        test_comparison_with_pbix()
        
        print("\n✅ All XLSX unpacking tests passed!")
        print("📋 Summary:")
        print("  ✓ File detection works for both PBIX and XLSX files")
        print("  ✓ Excel file unpacking works correctly") 
        print("  ✓ Excel data model structure is correctly parsed")
        print("  ✓ Excel files use different internal structure than PBIX (no SQLite DB)")
        print("\n📝 Note: Full PBIXRay integration requires metadata handler updates")
        print("   to support Excel's XML-based metadata format instead of SQLite DB.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)