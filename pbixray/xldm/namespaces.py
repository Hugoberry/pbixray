"""
Common namespaces and XML utilities for XLDM (XML for Data Mining) objects.
This module centralizes namespace definitions and provides common XML loading patterns.
"""

import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional


# Standard XLDM/Analysis Services namespaces
STANDARD_NAMESPACES = {
    '': 'http://schemas.microsoft.com/analysisservices/2003/engine',
    'eng': 'http://schemas.microsoft.com/analysisservices/2003/engine',
    'ddl2': 'http://schemas.microsoft.com/analysisservices/2003/engine/2',
    'ddl2_2': 'http://schemas.microsoft.com/analysisservices/2003/engine/2/2',
    'ddl100': 'http://schemas.microsoft.com/analysisservices/2008/engine/100',
    'ddl100_100': 'http://schemas.microsoft.com/analysisservices/2008/engine/100/100',
    'ddl200': 'http://schemas.microsoft.com/analysisservices/2010/engine/200',
    'ddl200_200': 'http://schemas.microsoft.com/analysisservices/2010/engine/200/200',
    'ddl300': 'http://schemas.microsoft.com/analysisservices/2011/engine/300',
    'ddl300_300': 'http://schemas.microsoft.com/analysisservices/2011/engine/300/300',
    'ddl400': 'http://schemas.microsoft.com/analysisservices/2012/engine/400',
    'ddl400_400': 'http://schemas.microsoft.com/analysisservices/2012/engine/400/400',
    'ddl410': 'http://schemas.microsoft.com/analysisservices/2012/engine/410',
    'ddl410_410': 'http://schemas.microsoft.com/analysisservices/2012/engine/410/410',
    'ddl500': 'http://schemas.microsoft.com/analysisservices/2013/engine/500',
    'ddl500_500': 'http://schemas.microsoft.com/analysisservices/2013/engine/500/500',
    'eng300': 'http://schemas.microsoft.com/analysisservices/2011/engine/300',
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

# Simple namespaces for basic operations
SIMPLE_NAMESPACES = {
    '': 'http://schemas.microsoft.com/analysisservices/2003/engine',
    'eng': 'http://schemas.microsoft.com/analysisservices/2003/engine',
    'eng300': 'http://schemas.microsoft.com/analysisservices/2011/engine/300',
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}


class XmlDefinitionBase:
    """Base class for XML definition loaders with common functionality."""
    
    def __init__(self, xml_string: str, namespaces: Optional[Dict[str, str]] = None):
        """
        Initialize XML definition from string.
        
        Args:
            xml_string: XML content as string
            namespaces: Optional custom namespaces dict, defaults to STANDARD_NAMESPACES
        """
        self.namespaces = namespaces or STANDARD_NAMESPACES.copy()
        self.root = ET.fromstring(xml_string)
        self._parse_xml()
    
    def _parse_xml(self):
        """Override this method in subclasses to parse specific XML content."""
        pass
    
    @classmethod
    def from_xml_file(cls, filepath: str, namespaces: Optional[Dict[str, str]] = None):
        """Create instance from XML file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            xml_string = f.read()
        return cls(xml_string, namespaces)
    
    @classmethod
    def from_xml_string(cls, xml_string: str, namespaces: Optional[Dict[str, str]] = None):
        """Create instance from XML string."""
        return cls(xml_string, namespaces)


class ParentObject:
    """Common parent object class used in various XLDM definitions."""
    
    def __init__(self, element, namespaces):
        if element is None:
            self.DatabaseID = None
            return
        self.DatabaseID = element.findtext("DatabaseID", namespaces=namespaces)

    def __repr__(self):
        return f"ParentObject(DatabaseID='{self.DatabaseID}')"


class ObjectDefinitionBase:
    """Base class for object definitions that wrap specific object types."""
    
    def __init__(self, element, namespaces, object_tag: str, object_class):
        """
        Initialize object definition.
        
        Args:
            element: XML element containing the object definition
            namespaces: Namespaces dictionary
            object_tag: Tag name of the object to find
            object_class: Class to instantiate for the object
        """
        if element is None:
            self._object = None
            return
        
        obj_elem = element.find(object_tag, namespaces=namespaces)
        self._object = object_class(obj_elem, namespaces) if obj_elem is not None else None
    
    @property
    def object(self):
        """Get the wrapped object."""
        return self._object


def get_namespaced_element_text(element, tag: str, namespaces: Dict[str, str], 
                               namespace_variants: Optional[list] = None):
    """
    Get text from element with namespace fallback.
    
    Args:
        element: XML element to search in
        tag: Tag name to search for
        namespaces: Namespaces dictionary
        namespace_variants: List of namespace-prefixed tag variants to try
    
    Returns:
        Text content or None
    """
    # Try standard search first
    text = element.findtext(tag, namespaces=namespaces)
    if text is not None:
        return text
    
    # Try namespace variants
    if namespace_variants:
        for variant in namespace_variants:
            text = element.findtext(variant)
            if text is not None:
                return text
    
    return None


def parse_storage_mode_with_namespace(element, namespaces: Dict[str, str]):
    """
    Parse StorageMode element that may have namespace attributes.
    
    Returns:
        Tuple of (storage_mode_text, valuens_attribute)
    """
    storage_mode = element.find("StorageMode", namespaces=namespaces)
    if storage_mode is not None:
        return storage_mode.text, storage_mode.get("valuens")
    return None, None


def create_definition_loader(object_tag: str, object_class, parent_tag: str = "ParentObject"):
    """
    Factory function to create XML definition loader classes.
    
    Args:
        object_tag: Tag name of the main object
        object_class: Class to instantiate for the main object
        parent_tag: Tag name of the parent object (default "ParentObject")
    
    Returns:
        Class that can load XML definitions
    """
    
    class GeneratedDefinitionLoader(XmlDefinitionBase):
        def _parse_xml(self):
            # Parse ParentObject if present
            parent_obj_elem = self.root.find(parent_tag, namespaces=self.namespaces)
            self.ParentObject = ParentObject(parent_obj_elem, self.namespaces) if parent_obj_elem is not None else None
            
            # Parse ObjectDefinition
            obj_def_elem = self.root.find("ObjectDefinition", namespaces=self.namespaces)
            if obj_def_elem is not None:
                obj_elem = obj_def_elem.find(object_tag, namespaces=self.namespaces)
                self.ObjectDefinition = object_class(obj_elem, self.namespaces) if obj_elem is not None else None
            else:
                self.ObjectDefinition = None
    
    return GeneratedDefinitionLoader