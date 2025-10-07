#!/usr/bin/env python3
"""
Utility script to extract all files from Excel Power Pivot data model.
This script extracts all files from the file_log of the data model to a specified folder.
"""

import os
import sys
import shutil
from pathlib import Path
import argparse

# Add the current directory to the path so we can import pbixray
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pbixray.pbix_unpacker import PbixUnpacker
from pbixray.utils import get_data_slice

def sanitize_filename(filename):
    """Sanitize filename for filesystem compatibility."""
    # Replace characters that might cause issues in filenames
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def determine_file_type(content):
    """Determine if content is text or binary and appropriate extension."""
    try:
        # Try to decode as UTF-8
        text_content = content.decode('utf-8')
        return 'text', text_content, ''
    except UnicodeDecodeError:
        try:
            # Try to decode as UTF-16
            text_content = content.decode('utf-16')
            return 'text', text_content, ''
        except UnicodeDecodeError:
            # If both fail, it's binary
            return 'binary', content, '.bin'

def extract_all_files(xlsx_path, output_dir=None, file_filter=None, max_files=None):
    """Extract all files from the Excel data model."""
    
    if output_dir is None:
        base_name = Path(xlsx_path).stem
        output_dir = f"extracted_{base_name}_files"
    
    # Create output directory
    output_path = Path(output_dir)
    if output_path.exists():
        response = input(f"Directory '{output_dir}' already exists. Remove it? (y/N): ")
        if response.lower() == 'y':
            shutil.rmtree(output_path)
        else:
            print("Extraction cancelled.")
            return
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Extracting files from: {xlsx_path}")
    print(f"Output directory: {output_path.absolute()}")
    
    # Initialize the unpacker
    try:
        unpacker = PbixUnpacker(xlsx_path)
        print(f"✓ Successfully unpacked data model")
    except Exception as e:
        print(f"❌ Failed to unpack data model: {e}")
        return
    
    # Get file list
    file_log = unpacker.data_model.file_log
    print(f"✓ Found {len(file_log)} files in data model")
    
    # Apply filtering if specified
    if file_filter:
        original_count = len(file_log)
        file_log = [f for f in file_log if file_filter.lower() in f['FileName'].lower()]
        print(f"✓ Filtered to {len(file_log)} files (from {original_count}) matching '{file_filter}'")
    
    # Apply max files limit if specified
    if max_files and len(file_log) > max_files:
        file_log = file_log[:max_files]
        print(f"✓ Limited to first {max_files} files")
    
    # Statistics
    total_size = 0
    text_files = 0
    binary_files = 0
    errors = 0
    
    # Create summary file
    summary_path = output_path / "extraction_summary.txt"
    
    print(f"\nExtracting {len(file_log)} files...")
    print("-" * 60)
    
    with open(summary_path, 'w', encoding='utf-8') as summary_file:
        summary_file.write(f"EXTRACTION SUMMARY\n")
        summary_file.write(f"Source: {xlsx_path}\n")
        summary_file.write(f"Output: {output_path.absolute()}\n")
        summary_file.write(f"Total files in data model: {len(unpacker.data_model.file_log)}\n")
        summary_file.write(f"Files extracted: {len(file_log)}\n")
        summary_file.write(f"\n{'='*60}\n\n")
        
        for i, file_info in enumerate(file_log, 1):
            filename = file_info['FileName']
            file_size = file_info['Size']
            offset = file_info['m_cbOffsetHeader']
            
            try:
                # Extract file content
                file_content = get_data_slice(unpacker.data_model, filename)
                
                # Determine file type and get appropriate extension
                file_type, processed_content, extra_ext = determine_file_type(file_content)
                
                # Sanitize filename and add extension if needed
                safe_filename = sanitize_filename(filename)
                if extra_ext and not safe_filename.endswith(extra_ext):
                    safe_filename += extra_ext
                
                # Write file
                output_file_path = output_path / safe_filename
                
                if file_type == 'text':
                    with open(output_file_path, 'w', encoding='utf-8') as f:
                        f.write(processed_content)
                    text_files += 1
                else:
                    with open(output_file_path, 'wb') as f:
                        f.write(processed_content)
                    binary_files += 1
                
                total_size += len(file_content)
                
                # Progress output
                print(f"{i:4d}/{len(file_log)} {filename:<60} ({file_size:>8} bytes) -> {file_type}")
                
                # Write to summary
                summary_file.write(f"{i:4d}. {filename}\n")
                summary_file.write(f"     Original Size: {file_size:,} bytes\n")
                summary_file.write(f"     Extracted Size: {len(file_content):,} bytes\n")
                summary_file.write(f"     Offset: {offset:,}\n")
                summary_file.write(f"     Type: {file_type}\n")
                summary_file.write(f"     Output: {safe_filename}\n")
                summary_file.write(f"\n")
                
            except Exception as e:
                errors += 1
                error_msg = f"❌ Error extracting {filename}: {e}"
                print(error_msg)
                summary_file.write(f"{i:4d}. {filename} - ERROR: {e}\n\n")
    
    print("-" * 60)
    print(f"✅ Extraction completed!")
    print(f"   Total files: {len(file_log)}")
    print(f"   Text files: {text_files}")
    print(f"   Binary files: {binary_files}")
    print(f"   Errors: {errors}")
    print(f"   Total extracted size: {total_size:,} bytes")
    print(f"   Output directory: {output_path.absolute()}")
    print(f"   Summary file: {summary_path}")
    
    # Create file type breakdown
    print(f"\n📊 File Type Analysis:")
    file_extensions = {}
    for file_info in file_log:
        filename = file_info['FileName']
        if '.' in filename:
            ext = filename.split('.')[-1].lower()
            file_extensions[ext] = file_extensions.get(ext, 0) + 1
        else:
            file_extensions['(no extension)'] = file_extensions.get('(no extension)', 0) + 1
    
    for ext, count in sorted(file_extensions.items(), key=lambda x: x[1], reverse=True):
        print(f"   .{ext}: {count} files")

def main():
    parser = argparse.ArgumentParser(
        description="Extract all files from Excel Power Pivot data model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s data/excel_file.xlsx
  %(prog)s data/excel_file.xlsx -o extracted_files
  %(prog)s data/excel_file.xlsx --filter xml --max-files 50
  %(prog)s data/excel_file.xlsx --filter Metrics --output metrics_files
        """
    )
    
    parser.add_argument(
        'xlsx_file',
        help='Path to the Excel file with Power Pivot data model'
    )
    
    parser.add_argument(
        '-o', '--output',
        dest='output_dir',
        help='Output directory for extracted files (default: extracted_<filename>_files)'
    )
    
    parser.add_argument(
        '-f', '--filter',
        dest='file_filter',
        help='Filter files by name (case-insensitive substring match)'
    )
    
    parser.add_argument(
        '-m', '--max-files',
        dest='max_files',
        type=int,
        help='Maximum number of files to extract'
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.xlsx_file):
        print(f"❌ Error: File '{args.xlsx_file}' not found.")
        sys.exit(1)
    
    # Check if it's an Excel file
    if not args.xlsx_file.lower().endswith(('.xlsx', '.xlsm')):
        print(f"⚠️  Warning: File '{args.xlsx_file}' doesn't appear to be an Excel file.")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    try:
        extract_all_files(
            args.xlsx_file,
            args.output_dir,
            args.file_filter,
            args.max_files
        )
    except KeyboardInterrupt:
        print("\n⚠️  Extraction cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()