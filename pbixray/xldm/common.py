"""
Common base classes and shared utilities for XLDM (XML for Data Mining) objects.
This module contains classes that are used across multiple XLDM modules to avoid duplication.
"""

import xml.etree.ElementTree as ET
from typing import List, Optional, Dict, Any
from datetime import datetime


class Annotation:
    """Common annotation class used across all XLDM objects."""
    
    def __init__(self, element, namespaces=None):
        if element is None:
            self.Name = None
            self.Value = None
            return
        
        if namespaces is None:
            namespaces = {}
            
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.Value = element.findtext("Value", namespaces=namespaces)

    def __repr__(self):
        return f"Annotation(Name='{self.Name}', Value='{self.Value}')"


class Source:
    """Common source class used for various binding types in XLDM objects."""
    
    def __init__(self, element, namespaces=None):
        if element is None:
            self.type = None
            return
        
        if namespaces is None:
            namespaces = {}
            
        # Get the xsi:type attribute to determine binding type
        self.type = element.get("{http://www.w3.org/2001/XMLSchema-instance}type")
        
        # Initialize common attributes
        self.TableID = None
        self.ColumnID = None
        self.DataSourceViewID = None
        self.DataSourceID = None
        self.DbTableName = None
        self.DbSchemaName = None
        self.QueryDefinition = None
        self.NotificationTechnique = None
        self.Expression = None
        self.MeasureName = None
        self.MeasureID = None
        
        # Parse based on binding type
        if not self.type:
            # Generic handling if no type specified
            self.DataSourceViewID = element.findtext("DataSourceViewID", namespaces=namespaces)
            return
        
        # Handle each binding type (remove namespace prefix if present)
        binding_type = self.type.split(':')[-1]
        
        if binding_type == "ColumnBinding":
            self.TableID = element.findtext("TableID", namespaces=namespaces)
            self.ColumnID = element.findtext("ColumnID", namespaces=namespaces)
            
        elif binding_type == "RowBinding":
            self.TableID = element.findtext("TableID", namespaces=namespaces)
            
        elif binding_type == "DataSourceViewBinding":
            self.DataSourceViewID = element.findtext("DataSourceViewID", namespaces=namespaces)
            
        elif binding_type == "MeasureBinding":
            self.MeasureID = element.findtext("MeasureID", namespaces=namespaces)
            
        elif binding_type == "TableBinding":
            self.DataSourceID = element.findtext("DataSourceID", namespaces=namespaces)
            self.DbTableName = element.findtext("DbTableName", namespaces=namespaces)
            self.DbSchemaName = element.findtext("DbSchemaName", namespaces=namespaces)
            
        elif binding_type == "QueryBinding":
            self.DataSourceID = element.findtext("DataSourceID", namespaces=namespaces)
            self.QueryDefinition = element.findtext("QueryDefinition", namespaces=namespaces)
            
        elif binding_type == "ProactiveCachingInheritedBinding":
            self.NotificationTechnique = element.findtext("NotificationTechnique", namespaces=namespaces)
            
        elif binding_type == "RowNumberBinding":
            pass  # No additional properties for RowNumberBinding
            
        elif binding_type == "CalculatedMeasureBinding":
            self.MeasureName = element.findtext("MeasureName", namespaces=namespaces)
            
        elif binding_type == "ExpressionBinding":
            self.Expression = element.findtext("Expression", namespaces=namespaces)
            
        else:
            # Generic fallback
            self.DataSourceViewID = element.findtext("DataSourceViewID", namespaces=namespaces)

    def __repr__(self):
        binding_type = self.type.split(':')[-1] if self.type else "Unknown"
        
        # Show relevant attributes based on what's populated
        attrs = []
        if self.TableID:
            attrs.append(f"TableID='{self.TableID}'")
        if self.ColumnID:
            attrs.append(f"ColumnID='{self.ColumnID}'")
        if self.DataSourceViewID:
            attrs.append(f"DataSourceViewID='{self.DataSourceViewID}'")
        if self.Expression:
            expr_preview = self.Expression[:50] + "..." if len(self.Expression) > 50 else self.Expression
            attrs.append(f"Expression='{expr_preview}'")
        if self.MeasureID:
            attrs.append(f"MeasureID='{self.MeasureID}'")
        if self.MeasureName:
            attrs.append(f"MeasureName='{self.MeasureName}'")
        if self.QueryDefinition:
            attrs.append(f"QueryDefinition='...'")
        if self.NotificationTechnique:
            attrs.append(f"NotificationTechnique='{self.NotificationTechnique}'")
        
        attrs_str = ", ".join(attrs) if attrs else ""
        return f"Source(type='{binding_type}'{', ' + attrs_str if attrs_str else ''})"


class MajorObject:
    """Base class for all major XLDM objects that share common properties."""
    
    def __init__(self, element, namespaces=None):
        if element is None:
            self._init_empty()
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
        self.Annotations = self._parse_annotations(element, namespaces)
    
    def _init_empty(self):
        """Initialize empty object."""
        self.Name = None
        self.ID = None
        self.CreatedTimestamp = None
        self.LastSchemaUpdate = None
        self.Description = None
        self.Annotations = []
    
    def _parse_annotations(self, element, namespaces):
        """Parse annotations from an XML element."""
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        if annotations_elem is not None:
            return [Annotation(ann, namespaces) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]
        return []

    def __repr__(self):
        return f"{self.__class__.__name__}(Name='{self.Name}', ID='{self.ID}')"


class ProcessableObject(MajorObject):
    """Base class for objects that can be processed and have additional metadata."""
    
    def __init__(self, element, namespaces=None):
        super().__init__(element, namespaces)
        
        if element is None:
            self._init_processable_empty()
            return
        
        if namespaces is None:
            namespaces = {}
        
        # Common processable object elements
        self.LastProcessed = element.findtext("LastProcessed", namespaces=namespaces)
        
        # Parse ObjectVersion as integer
        obj_version = element.findtext("ObjectVersion", namespaces=namespaces)
        self.ObjectVersion = int(obj_version) if obj_version else 0
        
        self.ObjectID = element.findtext("ObjectID", namespaces=namespaces)
        
        # Parse Ordinal as integer
        ordinal = element.findtext("Ordinal", namespaces=namespaces)
        self.Ordinal = int(ordinal) if ordinal else 0
        
        # Parse PersistLocation as integer
        persist_loc = element.findtext("PersistLocation", namespaces=namespaces)
        self.PersistLocation = int(persist_loc) if persist_loc else 0
        
        # Parse boolean fields
        self.System = element.findtext("System", namespaces=namespaces) == "true"
        self.Visible = element.findtext("Visible", namespaces=namespaces) == "true"
        
        # Parse Language as integer
        language = element.findtext("Language", namespaces=namespaces)
        self.Language = int(language) if language else 0
        
        self.Collation = element.findtext("Collation", namespaces=namespaces)
        
        # Parse ProcessingPriority as integer
        proc_priority = element.findtext("ProcessingPriority", namespaces=namespaces)
        self.ProcessingPriority = int(proc_priority) if proc_priority else 0
    
    def _init_processable_empty(self):
        """Initialize empty processable object fields."""
        self.LastProcessed = None
        self.ObjectVersion = 0
        self.ObjectID = None
        self.Ordinal = 0
        self.PersistLocation = 0
        self.System = False
        self.Visible = True
        self.Language = 0
        self.Collation = None
        self.ProcessingPriority = 0


class XmlLoadMixin:
    """Mixin class providing common XML loading functionality."""
    
    @classmethod
    def from_xml_file(cls, filepath):
        """Create instance from XML file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            xml_string = f.read()
        return cls.from_xml_string(xml_string)
    
    @classmethod
    def from_xml_string(cls, xml_string):
        """Create instance from XML string."""
        return cls(xml_string)


def parse_int_or_default(value, default=0):
    """Safely parse integer from string with default value."""
    try:
        return int(value) if value else default
    except (ValueError, TypeError):
        return default


def parse_bool_from_text(value):
    """Parse boolean from text value (handles 'true'/'false' strings)."""
    if isinstance(value, str):
        return value.lower() == "true"
    return bool(value) if value is not None else False


def find_text_with_namespace(element, tag, namespaces=None, namespace_tags=None):
    """
    Find text content with optional namespace fallback.
    
    Args:
        element: XML element to search in
        tag: Tag name to search for
        namespaces: Standard namespaces dict
        namespace_tags: List of namespace-prefixed tag names to try
    
    Returns:
        Text content or None
    """
    # Try standard search first
    text = element.findtext(tag, namespaces=namespaces)
    if text is not None:
        return text
    
    # Try namespace-specific tags if provided
    if namespace_tags:
        for ns_tag in namespace_tags:
            text = element.findtext(ns_tag)
            if text is not None:
                return text
    
    return None