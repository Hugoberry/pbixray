#!/usr/bin/env python3
"""
Final streamlined API test - focusing on the 6 core parsers that were successfully updated.
"""

import os
import sys
from pathlib import Path

# Add the pbixray package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_streamlined_core_api():
    """Test the 6 core XLDM parsers with streamlined API + 1 XMObject parser"""
    print("="*60)
    print("XLDM STREAMLINED API - CORE PARSERS TEST")
    print("="*60)
    
    results = {}
    base_path = Path(__file__).parent.parent / "xlsx" / "extracted_files"
    
    # Test 1: Partition Parser (prt.xml) - Updated API
    print("\n1. Testing Partition Parser (streamlined API)...")
    try:
        from pbixray.xldm.partition import PartitionXmlLoad
        
        test_file = base_path / "Date_29d5fe95-5d05-400e-bc26-d350cd533b88.25.prt.xml"
        with open(test_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        parser = PartitionXmlLoad.from_xml_string(xml_content)
        
        # Direct access to Partition object
        if parser.Partition:
            print(f"   ✓ SUCCESS: Direct access to Partition '{parser.Partition.Name}' (ID: {parser.Partition.ID})")
            results['partition'] = True
        else:
            print("   ✗ FAILED: No Partition object found")
            results['partition'] = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        results['partition'] = False
    
    # Test 2: Dimension Parser (dim.xml) - Updated API
    print("\n2. Testing Dimension Parser (streamlined API)...")
    try:
        from pbixray.xldm.dimension import DimensionXmlLoad
        
        test_file = base_path / "Metrics_29128f4d-37fd-4bf8-a576-cff821896940.38.dim.xml"
        with open(test_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        parser = DimensionXmlLoad.from_xml_string(xml_content)
        
        # Direct access to Dimension object
        if parser.Dimension:
            print(f"   ✓ SUCCESS: Direct access to Dimension '{parser.Dimension.Name}' (ID: {parser.Dimension.ID})")
            results['dimension'] = True
        else:
            print("   ✗ FAILED: No Dimension object found")
            results['dimension'] = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        results['dimension'] = False
    
    # Test 3: MeasureGroup Parser (det.xml) - Updated API
    print("\n3. Testing MeasureGroup Parser (streamlined API)...")
    try:
        from pbixray.xldm.measure_group import MeasureGroupXmlLoad
        
        test_file = base_path / "Date_29d5fe95-5d05-400e-bc26-d350cd533b88.92.det.xml"
        with open(test_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        parser = MeasureGroupXmlLoad.from_xml_string(xml_content)
        
        # Direct access to MeasureGroup object
        if parser.MeasureGroup:
            print(f"   ✓ SUCCESS: Direct access to MeasureGroup '{parser.MeasureGroup.Name}' (ID: {parser.MeasureGroup.ID})")
            results['measure_group'] = True
        else:
            print("   ✗ FAILED: No MeasureGroup object found")
            results['measure_group'] = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        results['measure_group'] = False
    
    # Test 4: Cube Parser (cub.xml) - Updated API
    print("\n4. Testing Cube Parser (streamlined API)...")
    try:
        from pbixray.xldm.cube import CubXmlLoad
        
        test_file = base_path / "Model.191.cub.xml"
        with open(test_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        parser = CubXmlLoad.from_xml_string(xml_content)
        
        # Direct access to Cube object
        if parser.Cube:
            print(f"   ✓ SUCCESS: Direct access to Cube '{parser.Cube.Name}' (ID: {parser.Cube.ID})")
            results['cube'] = True
        else:
            print("   ✗ FAILED: No Cube object found")
            results['cube'] = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        results['cube'] = False
    
    # Test 5: Database Parser (db.xml) - Updated API
    print("\n5. Testing Database Parser (streamlined API)...")
    try:
        from pbixray.xldm.database import DatabaseXmlLoad
        
        test_file = base_path / "32E74685AD35411E98FD.2.db.xml"
        with open(test_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        parser = DatabaseXmlLoad.from_xml_string(xml_content)
        
        # Direct access to Database object
        if parser.Database:
            print(f"   ✓ SUCCESS: Direct access to Database '{parser.Database.Name}' (ID: {parser.Database.ID})")
            results['database'] = True
        else:
            print("   ✗ FAILED: No Database object found")
            results['database'] = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        results['database'] = False
    
    # Test 6: MdxScript Parser (scr.xml) - Updated API
    print("\n6. Testing MdxScript Parser (streamlined API)...")
    try:
        from pbixray.xldm.mdx_script import MdxScriptXmlLoad
        
        test_file = base_path / "MdxScript.88.scr.xml"
        with open(test_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        parser = MdxScriptXmlLoad.from_xml_string(xml_content)
        
        # Direct access to MdxScript object
        if parser.MdxScript:
            print(f"   ✓ SUCCESS: Direct access to MdxScript '{parser.MdxScript.Name}' (ID: {parser.MdxScript.ID})")
            results['mdx_script'] = True
        else:
            print("   ✗ FAILED: No MdxScript object found")
            results['mdx_script'] = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        results['mdx_script'] = False
    
    # Test 7: XMObject Parser (tbl.xml) - Existing API (as reference in test_xldm_basic.py)
    print("\n7. Testing XMObject Parser (existing API)...")
    try:
        from pbixray.xldm.xmobject import XMObjectDocument
        
        test_file = base_path / "Plant_0e1735e0-0b86-4ffe-b864-c4ef70cca25e.8.tbl.xml"
        with open(test_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        parser = XMObjectDocument.from_xml_string(xml_content)
        
        # Use root_object as shown in test_xldm_basic.py
        if parser.root_object and parser.root_object.class_name:
            print(f"   ✓ SUCCESS: XMObject with class '{parser.root_object.class_name}' and name '{parser.root_object.name}'")
            results['xmobject'] = True
        else:
            print("   ✗ FAILED: No root_object found")
            results['xmobject'] = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        results['xmobject'] = False
    
    # Summary
    print("\n" + "="*60)
    print("STREAMLINED API TEST SUMMARY")
    print("="*60)
    
    successful = sum(results.values())
    total = len(results)
    
    print(f"\nResults: {successful}/{total} parsers working")
    
    # Group results
    streamlined_parsers = ['partition', 'dimension', 'measure_group', 'cube', 'database', 'mdx_script']
    existing_parsers = ['xmobject']
    
    print(f"\nStreamlined API Parsers (Load -> Object direct access):")
    for parser_name in streamlined_parsers:
        success = results.get(parser_name, False)
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {parser_name:15} {status}")
    
    print(f"\nExisting API Parsers:")
    for parser_name in existing_parsers:
        success = results.get(parser_name, False)
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {parser_name:15} {status}")
    
    if successful == total:
        print(f"\n🎉 ALL PARSERS WORKING! Streamlined API implementation successful!")
        print(f"✓ 6 parsers now provide direct object access (no more ObjectDefinition navigation)")
        print(f"✓ 1 existing parser maintains its working API")
    else:
        print(f"\n⚠️  {total - successful} parser(s) need attention.")
    
    return successful == total

if __name__ == "__main__":
    success = test_streamlined_core_api()
    sys.exit(0 if success else 1)