#!/usr/bin/env python3
"""
Simple test to check if xlsx branching works
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_file_type_detection():
    """Test that we can detect file types correctly."""
    try:
        from pbixray.pbix_unpacker import PbixUnpacker
        
        xlsx_file = "data/Supplier Quality Analysis Sample-no-PV.xlsx"
        if os.path.exists(xlsx_file):
            print(f"Testing with {xlsx_file}")
            unpacker = PbixUnpacker(xlsx_file)
            print(f"✓ File type detected: {unpacker.data_model.file_type}")
            print(f"✓ Number of files in log: {len(unpacker.data_model.file_log)}")
            
            # Print first few file names to see the pattern
            print("Sample file names:")
            for i, file_entry in enumerate(unpacker.data_model.file_log[:10]):
                print(f"  {file_entry['FileName']}")
        else:
            print(f"XLSX file not found: {xlsx_file}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

def test_metadata_handler():
    """Test the metadata handler with xlsx."""
    try:
        from pbixray.meta.metadata_handler import MetadataHandler
        from pbixray.pbix_unpacker import PbixUnpacker
        
        xlsx_file = "data/Supplier Quality Analysis Sample-no-PV.xlsx"
        if os.path.exists(xlsx_file):
            print(f"\nTesting metadata handler with {xlsx_file}")
            unpacker = PbixUnpacker(xlsx_file)
            handler = MetadataHandler(unpacker.data_model)
            
            print(f"✓ Metadata handler created")
            print(f"✓ Tables: {handler.tables}")
            
        else:
            print(f"XLSX file not found: {xlsx_file}")
            
    except Exception as e:
        print(f"Error in metadata handler: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_file_type_detection()
    test_metadata_handler()