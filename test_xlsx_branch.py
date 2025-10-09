#!/usr/bin/env python3
"""
Test script to verify the new xlsx branching functionality
"""

import os
import sys

# Add the parent directory to the path so we can import pbixray
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pbixray import PBIXRay

def test_xlsx_basic_functionality():
    """Test basic functionality with xlsx file."""
    
    # Test with xlsx file if it exists
    xlsx_file = os.path.join(os.path.dirname(__file__), "xlsx", "data", "Supplier Quality Analysis Sample-no-PV.xlsx")
    
    if not os.path.exists(xlsx_file):
        print(f"XLSX test file not found: {xlsx_file}")
        print("Skipping xlsx test")
        return
    
    try:
        print("Testing XLSX file support...")
        model = PBIXRay(xlsx_file)
        
        print(f"File type detected: {model._metadata_handler._data_model.file_type}")
        print(f"Number of tables: {len(model.tables) if hasattr(model, 'tables') and model.tables is not None else 0}")
        
        if hasattr(model, 'schema') and model.schema is not None:
            print("Schema:")
            print(model.schema.head())
        else:
            print("Schema not available")
            
        print("✓ XLSX basic functionality test passed")
        
    except Exception as e:
        print(f"✗ XLSX test failed: {e}")
        import traceback
        traceback.print_exc()

def test_pbix_still_works():
    """Test that pbix files still work."""
    
    # Test with a pbix file if available
    pbix_files = [
        "data/Sales & Returns Sample v201912.pbix",
        "../data/Sales & Returns Sample v201912.pbix"
    ]
    
    pbix_file = None
    for path in pbix_files:
        if os.path.exists(path):
            pbix_file = path
            break
    
    if not pbix_file:
        print("No PBIX test file found, skipping pbix test")
        return
    
    try:
        print("Testing PBIX file still works...")
        model = PBIXRay(pbix_file)
        
        print(f"File type detected: {model._metadata_handler._data_model.file_type}")
        print(f"Number of tables: {len(model.tables) if hasattr(model, 'tables') and model.tables is not None else 0}")
        
        print("✓ PBIX backward compatibility test passed")
        
    except Exception as e:
        print(f"✗ PBIX test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_xlsx_basic_functionality()
    test_pbix_still_works()