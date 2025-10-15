import xml.etree.ElementTree as ET
from typing import List, Optional
from datetime import datetime

from .common import Annotation, Source, ProcessableObject, parse_int_or_default, parse_bool_from_text
from .namespaces import XmlDefinitionBase, ParentObject, ObjectDefinitionBase, STANDARD_NAMESPACES, parse_storage_mode_with_namespace

class Attribute:
    def __init__(self, element, namespaces):
        self.AttributeID = element.findtext("AttributeID", namespaces=namespaces)
        self.AggregationUsage = element.findtext("AggregationUsage", namespaces=namespaces)
        self.AttributeHierarchyEnabled = element.findtext("AttributeHierarchyEnabled", namespaces=namespaces) == "true"
        self.AttributeHierarchyVisible = element.findtext("AttributeHierarchyVisible", namespaces=namespaces) == "true"
        self.AttributeHierarchyOptimizedState = element.findtext("AttributeHierarchyOptimizedState", namespaces=namespaces)

class Dimension:
    def __init__(self, element, namespaces):
        self.ID = element.findtext("ID", namespaces=namespaces)
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.DimensionID = element.findtext("DimensionID", namespaces=namespaces)
        self.Visible = element.findtext("Visible", namespaces=namespaces) == "true"
        self.HierarchyUniqueNameStyle = element.findtext("HierarchyUniqueNameStyle", namespaces=namespaces)
        self.MemberUniqueNameStyle = element.findtext("MemberUniqueNameStyle", namespaces=namespaces)
        self.AllMemberAggregationUsage = element.findtext("AllMemberAggregationUsage", namespaces=namespaces)
        
        # Parse Attributes
        attributes_elem = element.find("Attributes", namespaces=namespaces)
        self.Attributes = []
        if attributes_elem is not None:
            self.Attributes = [Attribute(attr, namespaces) for attr in attributes_elem.findall("Attribute", namespaces=namespaces)]

class ProactiveCachingSource:
    def __init__(self, element):
        self.type = element.get("{http://www.w3.org/2001/XMLSchema-instance}type")
        self.NotificationTechnique = element.findtext("NotificationTechnique")

class ProactiveCaching:
    def __init__(self, element):
        self.SilenceInterval = element.findtext("SilenceInterval")
        self.Latency = element.findtext("Latency")
        self.SilenceOverrideInterval = element.findtext("SilenceOverrideInterval")
        self.ForceRebuildInterval = element.findtext("ForceRebuildInterval")
        self.Enabled = element.findtext("Enabled") == "true"
        self.AggregationStorage = element.findtext("AggregationStorage")
        self.OnlineMode = element.findtext("OnlineMode")
        
        source_elem = element.find("Source")
        self.Source = ProactiveCachingSource(source_elem) if source_elem is not None else None

class Cube(ProcessableObject):
    def __init__(self, element, namespaces):
        super().__init__(element, namespaces)
        
        if element is None:
            self._init_cube_empty()
            return
        
        # Cube-specific fields
        self.DefaultMeasure = element.findtext("DefaultMeasure", namespaces=namespaces)
        self.AggregationPrefix = element.findtext("AggregationPrefix", namespaces=namespaces)
        
        # StorageMode with namespace attribute
        self.StorageMode, self.StorageMode_valuens = parse_storage_mode_with_namespace(element, namespaces)
        
        self.ProcessingMode = element.findtext("ProcessingMode", namespaces=namespaces)
        self.ScriptCacheProcessingMode = element.findtext("ScriptCacheProcessingMode", namespaces=namespaces)
        self.ScriptErrorHandlingMode = element.findtext("ScriptErrorHandlingMode", namespaces=namespaces)
        self.StorageLocation = element.findtext("StorageLocation", namespaces=namespaces)
        
        # Parse EstimatedRows as integer
        estimated_rows = element.findtext("EstimatedRows", namespaces=namespaces)
        self.EstimatedRows = parse_int_or_default(estimated_rows, 0)
        
        # Parse Source
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = Source(source_elem) if source_elem is not None else None
        
        # Parse ProactiveCaching
        pc_elem = element.find("ProactiveCaching", namespaces=namespaces)
        self.ProactiveCaching = ProactiveCaching(pc_elem) if pc_elem is not None else None
        
        # Parse Dimensions
        dimensions_elem = element.find("Dimensions", namespaces=namespaces)
        self.Dimensions = []
        if dimensions_elem is not None:
            self.Dimensions = [Dimension(dim, namespaces) for dim in dimensions_elem.findall("Dimension", namespaces=namespaces)]
        
        # Additional fields
        self.StructureVersion = parse_int_or_default(element.findtext("StructureVersion", namespaces=namespaces), 0)
        self.DataVersion = parse_int_or_default(element.findtext("DataVersion", namespaces=namespaces), 0)
        self.CalcVersion = parse_int_or_default(element.findtext("CalcVersion", namespaces=namespaces), 0)
        self.LastBindingChange = element.findtext("LastBindingChange", namespaces=namespaces)
        self.LastUpdate = element.findtext("LastUpdate", namespaces=namespaces)
        self.MeasureGroupFileList = element.findtext("MeasureGroupFileList", namespaces=namespaces)
        self.PerspectiveFileList = element.findtext("PerspectiveFileList", namespaces=namespaces)
        self.AssemblyFileList = element.findtext("AssemblyFileList", namespaces=namespaces)
        self.PermissionFileList = element.findtext("PermissionFileList", namespaces=namespaces)
    
    def _init_cube_empty(self):
        """Initialize empty cube-specific fields."""
        self.DefaultMeasure = None
        self.AggregationPrefix = None
        self.StorageMode = None
        self.StorageMode_valuens = None
        self.ProcessingMode = None
        self.ScriptCacheProcessingMode = None
        self.ScriptErrorHandlingMode = None
        self.StorageLocation = None
        self.EstimatedRows = 0
        self.Source = None
        self.ProactiveCaching = None
        self.Dimensions = []
        self.StructureVersion = 0
        self.DataVersion = 0
        self.CalcVersion = 0
        self.LastBindingChange = None
        self.LastUpdate = None
        self.MeasureGroupFileList = None
        self.PerspectiveFileList = None
        self.AssemblyFileList = None
        self.PermissionFileList = None

class ObjectDefinition(ObjectDefinitionBase):
    def __init__(self, element, namespaces):
        super().__init__(element, namespaces, "Cube", Cube)
    
    @property
    def Cube(self):
        return self.object

class CubXmlLoad(XmlDefinitionBase):
    def _parse_xml(self):
        # Parse ParentObject
        parent_obj_elem = self.root.find("ParentObject", namespaces=self.namespaces)
        self.ParentObject = ParentObject(parent_obj_elem, self.namespaces) if parent_obj_elem is not None else None
        
        # Parse ObjectDefinition and extract Cube directly
        obj_def_elem = self.root.find("ObjectDefinition", namespaces=self.namespaces)
        if obj_def_elem is not None:
            cube_elem = obj_def_elem.find("Cube", namespaces=self.namespaces)
            self.Cube = Cube(cube_elem, self.namespaces) if cube_elem is not None else None
        else:
            self.Cube = None