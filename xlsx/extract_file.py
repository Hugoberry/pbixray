#!/usr/bin/env python3
"""
Script to extract a specific file from the Excel data model for inspection.
Extracts: Metrics_29128f4d-37fd-4bf8-a576-cff821896940.33.tbl.xml
"""

import os
import sys

# Add the current directory to the path so we can import pbixray
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pbixray.pbix_unpacker import PbixUnpacker
from pbixray.utils import get_data_slice

# Path to the Excel file
XLSX_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "Supplier Quality Analysis Sample-no-PV.xlsx")

# Target file to extract
TARGET_FILE = "Metrics_29128f4d-37fd-4bf8-a576-cff821896940.33.tbl.xml"

def extract_file_from_excel():
    """Extract the target file from the Excel data model."""
    
    print(f"Extracting '{TARGET_FILE}' from Excel file...")
    print(f"Source: {XLSX_FILE_PATH}")
    
    # Initialize the unpacker
    unpacker = PbixUnpacker(XLSX_FILE_PATH)
    
    # Check if the target file exists in the file log
    file_names = [f['FileName'] for f in unpacker.data_model.file_log]
    
    if TARGET_FILE not in file_names:
        print(f"❌ File '{TARGET_FILE}' not found in the data model!")
        print("Available files containing 'Metrics':")
        metrics_files = [f for f in file_names if 'Metrics' in f]
        for f in sorted(metrics_files):
            print(f"  - {f}")
        return
    
    # Get file information
    target_file_info = next(f for f in unpacker.data_model.file_log if f['FileName'] == TARGET_FILE)
    print(f"✓ Found target file: {TARGET_FILE}")
    print(f"  Size: {target_file_info['Size']} bytes")
    print(f"  Offset: {target_file_info['m_cbOffsetHeader']}")
    
    # Extract the file content using the utility function
    try:
        file_content = get_data_slice(unpacker.data_model, TARGET_FILE)
        print(f"✓ Successfully extracted {len(file_content)} bytes")
        
        # Save to output file
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extracted_" + TARGET_FILE)
        
        # Determine if content is text or binary
        try:
            # Try to decode as UTF-8
            text_content = file_content.decode('utf-8')
            is_text = True
        except UnicodeDecodeError:
            # If UTF-8 fails, try UTF-16
            try:
                text_content = file_content.decode('utf-16')
                is_text = True
            except UnicodeDecodeError:
                is_text = False
        
        if is_text:
            # Save as text file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text_content)
            print(f"✓ Saved as text file: {output_path}")
            
            # Show a preview of the content
            print("\nFile content preview (first 500 characters):")
            print("-" * 50)
            print(text_content[:500])
            if len(text_content) > 500:
                print("...")
            print("-" * 50)
        else:
            # Save as binary file
            with open(output_path, 'wb') as f:
                f.write(file_content)
            print(f"✓ Saved as binary file: {output_path}")
            
            # Show hex preview for binary files
            print("\nBinary content preview (first 100 bytes as hex):")
            print("-" * 50)
            hex_content = file_content[:100].hex()
            for i in range(0, len(hex_content), 32):
                print(hex_content[i:i+32])
            if len(file_content) > 100:
                print("...")
            print("-" * 50)
        
        print(f"\n✅ File successfully extracted to: {output_path}")
        
    except Exception as e:
        print(f"❌ Failed to extract file content: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    extract_file_from_excel()