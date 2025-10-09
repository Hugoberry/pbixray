#!/usr/bin/env python3
"""
Comprehensive test for xlsx and pbix support in pbixray
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_xlsx_functionality():
    """Test xlsx file functionality."""
    print("=" * 60)
    print("TESTING XLSX FUNCTIONALITY")
    print("=" * 60)
    
    try:
        from pbixray import PBIXRay
        
        xlsx_file = "data/Supplier Quality Analysis Sample-no-PV.xlsx"
        if not os.path.exists(xlsx_file):
            print(f"XLSX file not found: {xlsx_file}")
            return False
            
        model = PBIXRay(xlsx_file)
        
        # Test file type detection
        assert model._metadata_handler._data_model.file_type == "xlsx", "File type should be xlsx"
        print("✓ File type correctly detected as xlsx")
        
        # Test tables
        tables = model.tables
        assert len(tables) > 0, "Should have at least one table"
        print(f"✓ Found {len(tables)} tables: {list(tables)}")
        
        # Test schema
        schema = model.schema
        assert not schema.empty, "Schema should not be empty"
        print(f"✓ Schema has {len(schema)} columns")
        
        # Test statistics (should work even if limited data)
        stats = model.statistics
        print(f"✓ Statistics available with {len(stats)} entries")
        
        # Test size property
        size = model.size
        assert size > 0, "Model size should be greater than 0"
        print(f"✓ Model size: {size} bytes")
        
        # Test that empty dataframes are returned for unsupported features in xlsx
        assert model.power_query.empty, "Power Query should be empty for xlsx"
        assert model.m_parameters.empty, "M Parameters should be empty for xlsx"
        assert model.dax_tables.empty, "DAX Tables should be empty for xlsx"
        assert model.dax_measures.empty, "DAX Measures should be empty for xlsx"
        assert model.dax_columns.empty, "DAX Columns should be empty for xlsx"
        print("✓ Unsupported features correctly return empty dataframes")
        
        print("✓ XLSX functionality test PASSED")
        return True
        
    except Exception as e:
        print(f"✗ XLSX functionality test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_pbix_functionality():
    """Test pbix file functionality (backward compatibility)."""
    print("\n" + "=" * 60)
    print("TESTING PBIX BACKWARD COMPATIBILITY")
    print("=" * 60)
    
    try:
        from pbixray import PBIXRay
        
        pbix_file = "data/Sales & Returns Sample v201912.pbix"
        if not os.path.exists(pbix_file):
            print(f"PBIX file not found: {pbix_file}")
            return False
            
        model = PBIXRay(pbix_file)
        
        # Test file type detection
        assert model._metadata_handler._data_model.file_type == "pbix", "File type should be pbix"
        print("✓ File type correctly detected as pbix")
        
        # Test tables
        tables = model.tables
        assert len(tables) > 0, "Should have at least one table"
        print(f"✓ Found {len(tables)} tables")
        
        # Test schema
        schema = model.schema
        assert not schema.empty, "Schema should not be empty"
        print(f"✓ Schema has {len(schema)} columns")
        
        # Test features that should work in pbix
        power_query = model.power_query
        print(f"✓ Power Query: {len(power_query)} entries")
        
        dax_measures = model.dax_measures
        print(f"✓ DAX Measures: {len(dax_measures)} entries")
        
        relationships = model.relationships
        print(f"✓ Relationships: {len(relationships)} entries")
        
        print("✓ PBIX backward compatibility test PASSED")
        return True
        
    except Exception as e:
        print(f"✗ PBIX backward compatibility test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_dimension_and_attribute_extraction():
    """Test that we can extract dimension IDs and attribute information correctly."""
    print("\n" + "=" * 60)
    print("TESTING DIMENSION/ATTRIBUTE EXTRACTION")
    print("=" * 60)
    
    try:
        from pbixray import PBIXRay
        
        xlsx_file = "data/Supplier Quality Analysis Sample-no-PV.xlsx"
        if not os.path.exists(xlsx_file):
            print(f"XLSX file not found: {xlsx_file}")
            return False
            
        model = PBIXRay(xlsx_file)
        
        # Check if we have the expected tables (dimensions)
        expected_tables = ['Defect Type', 'Defect', 'Material Type', 'Metrics', 'Plant', 'Category', 'Vendor', 'Date']
        tables = model.tables
        
        for expected_table in expected_tables:
            assert expected_table in tables, f"Expected table {expected_table} not found"
        print(f"✓ All expected tables found: {expected_tables}")
        
        # Check schema structure
        schema = model.schema
        assert 'TableName' in schema.columns, "Schema should have TableName column"
        assert 'ColumnName' in schema.columns, "Schema should have ColumnName column"
        assert 'PandasDataType' in schema.columns, "Schema should have PandasDataType column"
        print("✓ Schema has correct structure")
        
        # Check that we have reasonable column counts for each table
        for table in expected_tables:
            table_columns = schema[schema['TableName'] == table]
            assert len(table_columns) > 0, f"Table {table} should have columns"
            print(f"✓ Table '{table}' has {len(table_columns)} columns")
        
        print("✓ Dimension/Attribute extraction test PASSED")
        return True
        
    except Exception as e:
        print(f"✗ Dimension/Attribute extraction test FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running comprehensive pbixray xlsx/pbix support tests...")
    
    results = []
    results.append(test_xlsx_functionality())
    results.append(test_pbix_functionality())
    results.append(test_dimension_and_attribute_extraction())
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✓ ALL TESTS PASSED ({passed}/{total})")
        print("\n🎉 XLSX support successfully implemented!")
        print("📋 Key features working:")
        print("   • File type detection (xlsx vs pbix)")
        print("   • XML metadata parsing for xlsx files")
        print("   • Table/dimension extraction")
        print("   • Column/attribute extraction")
        print("   • Schema generation")
        print("   • Statistics computation")
        print("   • Backward compatibility with pbix files")
    else:
        print(f"✗ SOME TESTS FAILED ({passed}/{total})")
    
    sys.exit(0 if passed == total else 1)