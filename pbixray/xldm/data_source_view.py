import xml.etree.ElementTree as ET
from typing import List, Optional

class Annotation:
    def __init__(self, element):
        if element is None:
            return
        self.Name = element.findtext("Name")
        self.Value = element.findtext("Value")

class DataSourceView:
    def __init__(self, element, namespaces=None):
        if element is None:
            return
        
        if namespaces is None:
            namespaces = {}
        
        # Common MajorObject elements
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.ID = element.findtext("ID", namespaces=namespaces)
        self.CreatedTimestamp = element.findtext("CreatedTimestamp", namespaces=namespaces)
        self.LastSchemaUpdate = element.findtext("LastSchemaUpdate", namespaces=namespaces)
        self.Description = element.findtext("Description", namespaces=namespaces)
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]
        
        # DataSourceView-specific elements
        self.DataSourceID = element.findtext("DataSourceID", namespaces=namespaces)
        
        # Parse Schema element (contains xsd:schema)
        schema_elem = element.find("Schema", namespaces=namespaces)
        self.Schema = None
        self.SchemaElement = None
        if schema_elem is not None:
            # Get the xsd:schema element
            xsd_schema = schema_elem.find("{http://www.w3.org/2001/XMLSchema}schema")
            if xsd_schema is not None:
                self.SchemaElement = xsd_schema
                # Store as string for easier manipulation
                self.Schema = ET.tostring(xsd_schema, encoding='unicode')

class DataSourceViewDefinition:
    def __init__(self, xml_string):
        self.namespaces = {
            '': 'http://schemas.microsoft.com/analysisservices/2003/engine',
            'xsd': 'http://www.w3.org/2001/XMLSchema',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
        }
        
        root = ET.fromstring(xml_string)
        self.DataSourceView = DataSourceView(root, self.namespaces)
    
    @classmethod
    def from_xml_file(cls, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            xml_string = f.read()
        return cls(xml_string)
    
    @classmethod
    def from_xml_string(cls, xml_string):
        return cls(xml_string)