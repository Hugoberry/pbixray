#!/usr/bin/env python3
"""
Quick test to identify XMObject parsing issues
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from pbixray.xldm.xmobject import XMObjectDocument
    print("✓ Successfully imported XMObjectDocument")
    
    # Test with a simple XML file
    test_file = "/Users/igor/git/hub/pbixray/xlsx/extracted_files/Date_29d5fe95-5d05-400e-bc26-d350cd533b88.31.tbl.xml"
    
    with open(test_file, 'r', encoding='utf-8') as f:
        xml_content = f.read()
    
    print(f"✓ Read XML file ({len(xml_content)} characters)")
    
    # Try direct parse
    xm_doc = XMObjectDocument.from_xml_string(xml_content)
    print(f"✓ Successfully parsed!")
    print(f"Root class: {xm_doc.root_object.class_name}")
    print(f"Root name: {xm_doc.root_object.name}")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()