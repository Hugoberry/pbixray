import xml.etree.ElementTree as ET
from typing import List, Optional

from .common import Annotation, MajorObject
from .namespaces import XmlDefinitionBase, SIMPLE_NAMESPACES

class DataSourceView(MajorObject):
    def __init__(self, element, namespaces=None):
        super().__init__(element, namespaces)
        
        if element is None:
            self._init_dsv_empty()
            return
        
        if namespaces is None:
            namespaces = {}
        
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
    
    def _init_dsv_empty(self):
        """Initialize empty data source view fields."""
        self.DataSourceID = None
        self.Schema = None
        self.SchemaElement = None

class DataSourceViewDefinition(XmlDefinitionBase):
    def __init__(self, xml_string):
        super().__init__(xml_string, SIMPLE_NAMESPACES)
    
    def _parse_xml(self):
        self.DataSourceView = DataSourceView(self.root, self.namespaces)