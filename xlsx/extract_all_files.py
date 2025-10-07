#!/usr/bin/env python3
"""
Script to extract ALL files from the Excel data model file_log to a folder for inspection.
This will extract all 206+ files from the "Supplier Quality Analysis Sample-no-PV.xlsx" data model.
"""

import os
import sys
import shutil
from pathlib import Path

# Add the parent directory to the path so we can import pbixray
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pbixray.pbix_unpacker import PbixUnpacker
from pbixray.utils import get_data_slice

# Path to the Excel file
XLSX_FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "Supplier Quality Analysis Sample-no-PV.xlsx")

# Output directory for extracted files
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "extracted_files")

def sanitize_filename(filename):
    """Sanitize filename to be safe for filesystem."""
    # Replace problematic characters
    sanitized = filename.replace('/', '_').replace('\\', '_').replace(':', '_')
    sanitized = sanitized.replace('<', '_').replace('>', '_').replace('|', '_')
    sanitized = sanitized.replace('?', '_').replace('*', '_').replace('"', '_')
    return sanitized

def extract_all_files_from_excel():
    """Extract all files from the Excel data model file_log."""
    
    print(f"Extracting ALL files from Excel data model...")
    print(f"Source: {XLSX_FILE_PATH}")
    print(f"Output directory: {OUTPUT_DIR}")
    
    # Create output directory
    if os.path.exists(OUTPUT_DIR):
        print(f"⚠️  Output directory exists, removing: {OUTPUT_DIR}")
        shutil.rmtree(OUTPUT_DIR)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"✓ Created output directory: {OUTPUT_DIR}")
    
    # Initialize the unpacker
    print("\nInitializing unpacker...")
    unpacker = PbixUnpacker(XLSX_FILE_PATH)
    
    # Get all files from file_log
    file_log = unpacker.data_model.file_log
    total_files = len(file_log)
    
    print(f"✓ Found {total_files} files in data model file_log")
    
    # Track statistics
    extracted_count = 0
    failed_count = 0
    total_size = 0
    file_types = {}
    
    # Extract each file
    print(f"\nExtracting files...")
    print("-" * 60)
    
    for i, file_info in enumerate(file_log, 1):
        filename = file_info['FileName']
        file_size = file_info['Size']
        
        try:
            # Extract file content
            file_content = get_data_slice(unpacker.data_model, filename)
            
            # Sanitize filename for filesystem
            safe_filename = sanitize_filename(filename)
            output_path = os.path.join(OUTPUT_DIR, safe_filename)
            
            # Determine if content is text or binary
            is_text = False
            text_content = None
            
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
            
            # Save file
            if is_text:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text_content)
            else:
                with open(output_path, 'wb') as f:
                    f.write(file_content)
            
            # Track statistics
            extracted_count += 1
            total_size += len(file_content)
            
            # Track file extensions
            if '.' in filename:
                ext = filename.split('.')[-1].lower()
                file_types[ext] = file_types.get(ext, 0) + 1
            else:
                file_types['no_extension'] = file_types.get('no_extension', 0) + 1
            
            # Progress indicator
            if i % 10 == 0 or i == total_files:
                progress = (i / total_files) * 100
                print(f"Progress: {i}/{total_files} ({progress:.1f}%) - Latest: {filename[:50]}")
            
        except Exception as e:
            failed_count += 1
            print(f"❌ Failed to extract '{filename}': {e}")
    
    # Create summary report
    summary_path = os.path.join(OUTPUT_DIR, "_EXTRACTION_SUMMARY.txt")
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("=== EXCEL DATA MODEL FILE EXTRACTION SUMMARY ===\n\n")
        f.write(f"Source File: {XLSX_FILE_PATH}\n")
        f.write(f"Extraction Date: {sys.version}\n")
        f.write(f"Output Directory: {OUTPUT_DIR}\n\n")
        
        f.write("=== EXTRACTION STATISTICS ===\n")
        f.write(f"Total Files in File Log: {total_files}\n")
        f.write(f"Successfully Extracted: {extracted_count}\n")
        f.write(f"Failed Extractions: {failed_count}\n")
        f.write(f"Total Extracted Size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)\n\n")
        
        f.write("=== FILE TYPES EXTRACTED ===\n")
        for ext, count in sorted(file_types.items()):
            f.write(f"{ext}: {count} files\n")
        f.write("\n")
        
        f.write("=== COMPLETE FILE LIST ===\n")
        for i, file_info in enumerate(file_log, 1):
            filename = file_info['FileName']
            file_size = file_info['Size']
            offset = file_info['m_cbOffsetHeader']
            f.write(f"{i:3d}. {filename} ({file_size:,} bytes, offset: {offset})\n")
    
    print("-" * 60)
    print(f"\n✅ Extraction completed!")
    print(f"📊 Statistics:")
    print(f"  • Total files: {total_files}")
    print(f"  • Successfully extracted: {extracted_count}")
    print(f"  • Failed: {failed_count}")
    print(f"  • Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
    print(f"  • Output directory: {OUTPUT_DIR}")
    print(f"  • Summary report: {summary_path}")
    
    print(f"\n📁 File types extracted:")
    for ext, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True):
        print(f"  • .{ext}: {count} files")
    
    # Show some interesting files
    print(f"\n🔍 Notable files extracted:")
    interesting_patterns = ['.xml', '.db.', 'Model', 'Metrics', '.sqlitedb']
    for pattern in interesting_patterns:
        matching_files = [f['FileName'] for f in file_log if pattern.lower() in f['FileName'].lower()]
        if matching_files:
            print(f"  • Files containing '{pattern}': {len(matching_files)}")
            if len(matching_files) <= 3:
                for mf in matching_files:
                    print(f"    - {mf}")
            else:
                print(f"    - {matching_files[0]}")
                print(f"    - ... and {len(matching_files)-1} more")

if __name__ == "__main__":
    try:
        extract_all_files_from_excel()
    except Exception as e:
        print(f"\n❌ Extraction failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)