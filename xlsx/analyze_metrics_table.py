#!/usr/bin/env python3
"""
Summary analysis of the extracted Metrics table XML file from Excel Power Pivot.
"""

import os
import xml.etree.ElementTree as ET

# File paths
extracted_file = "/Users/igor/git/hub/pbixray/extracted_Metrics_29128f4d-37fd-4bf8-a576-cff821896940.33.tbl.xml"
summary_file = "/Users/igor/git/hub/pbixray/metrics_table_analysis.txt"

def analyze_metrics_table():
    """Analyze the extracted Metrics table XML file."""
    
    print("Analyzing the extracted Metrics table XML file...")
    
    # Read the XML file
    with open(extracted_file, 'r', encoding='utf-8') as f:
        xml_content = f.read()
    
    # Parse the XML
    try:
        root = ET.fromstring(xml_content)
        
        # Extract basic information
        analysis = []
        analysis.append("=== METRICS TABLE ANALYSIS ===\n")
        analysis.append(f"Table Name: {root.get('name', 'Unknown')}")
        analysis.append(f"Class: {root.get('class', 'Unknown')}")
        analysis.append(f"Provider Version: {root.get('ProviderVersion', 'Unknown')}")
        analysis.append("")
        
        # Find properties
        properties = root.find('.//{http://schemas.microsoft.com/analysisservices/imbi}Properties')
        if properties is not None:
            analysis.append("=== TABLE PROPERTIES ===")
            for prop in properties:
                prop_name = prop.tag.split('}')[-1] if '}' in prop.tag else prop.tag
                analysis.append(f"{prop_name}: {prop.text}")
            analysis.append("")
        
        # Find columns
        columns_collection = root.find('.//{http://schemas.microsoft.com/analysisservices/imbi}Collection[@name="Columns"]')
        if columns_collection is not None:
            analysis.append("=== TABLE COLUMNS ===")
            column_count = 0
            for column in columns_collection.findall('.//{http://schemas.microsoft.com/analysisservices/imbi}XMObject[@class="XMRawColumn"]'):
                column_count += 1
                column_name = column.get('name', f'Column_{column_count}')
                analysis.append(f"{column_count}. {column_name}")
                
                # Get column statistics
                col_stats = column.find('.//{http://schemas.microsoft.com/analysisservices/imbi}XMObject[@class="XMColumnStats"]')
                if col_stats is not None:
                    stats_props = col_stats.find('.//{http://schemas.microsoft.com/analysisservices/imbi}Properties')
                    if stats_props is not None:
                        row_count = stats_props.find('.//{http://schemas.microsoft.com/analysisservices/imbi}RowCount')
                        distinct_states = stats_props.find('.//{http://schemas.microsoft.com/analysisservices/imbi}DistinctStates')
                        db_type = stats_props.find('.//{http://schemas.microsoft.com/analysisservices/imbi}DBType')
                        
                        if row_count is not None:
                            analysis.append(f"   Rows: {row_count.text}")
                        if distinct_states is not None:
                            analysis.append(f"   Distinct Values: {distinct_states.text}")
                        if db_type is not None:
                            analysis.append(f"   Data Type: {db_type.text}")
            analysis.append("")
        
        # Find relationships
        relationships_collection = root.find('.//{http://schemas.microsoft.com/analysisservices/imbi}Collection[@name="Relationships"]')
        if relationships_collection is not None:
            analysis.append("=== TABLE RELATIONSHIPS ===")
            rel_count = 0
            for relationship in relationships_collection.findall('.//{http://schemas.microsoft.com/analysisservices/imbi}XMObject[@class="XMRelationship"]'):
                rel_count += 1
                rel_name = relationship.get('name', f'Relationship_{rel_count}')
                analysis.append(f"{rel_count}. {rel_name}")
                
                # Get relationship properties
                rel_props = relationship.find('.//{http://schemas.microsoft.com/analysisservices/imbi}Properties')
                if rel_props is not None:
                    primary_table = rel_props.find('.//{http://schemas.microsoft.com/analysisservices/imbi}PrimaryTable')
                    primary_column = rel_props.find('.//{http://schemas.microsoft.com/analysisservices/imbi}PrimaryColumn')
                    foreign_column = rel_props.find('.//{http://schemas.microsoft.com/analysisservices/imbi}ForeignColumn')
                    
                    if primary_table is not None:
                        analysis.append(f"   Primary Table: {primary_table.text}")
                    if primary_column is not None:
                        analysis.append(f"   Primary Column: {primary_column.text}")
                    if foreign_column is not None:
                        analysis.append(f"   Foreign Column: {foreign_column.text}")
            analysis.append("")
        
        # Save analysis
        analysis_text = "\n".join(analysis)
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(analysis_text)
        
        print("✓ Analysis completed!")
        print(f"✓ Analysis saved to: {summary_file}")
        print("\n" + "="*60)
        print(analysis_text)
        
    except ET.ParseError as e:
        print(f"❌ XML parsing error: {e}")
    except Exception as e:
        print(f"❌ Analysis error: {e}")

if __name__ == "__main__":
    analyze_metrics_table()