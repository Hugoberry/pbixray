import xml.etree.ElementTree as ET
from typing import List, Optional
from datetime import datetime

class Annotation:
    def __init__(self, element):
        self.Name = element.findtext("Name")
        self.Value = element.findtext("Value")

class Attribute:
    def __init__(self, element):
        self.AttributeID = element.findtext("AttributeID")
        self.AggregationUsage = element.findtext("AggregationUsage")
        self.AttributeHierarchyEnabled = element.findtext("AttributeHierarchyEnabled") == "true"
        self.AttributeHierarchyVisible = element.findtext("AttributeHierarchyVisible") == "true"
        self.AttributeHierarchyOptimizedState = element.findtext("AttributeHierarchyOptimizedState")

class Dimension:
    def __init__(self, element):
        self.ID = element.findtext("ID")
        self.Name = element.findtext("Name")
        self.DimensionID = element.findtext("DimensionID")
        self.Visible = element.findtext("Visible") == "true"
        self.HierarchyUniqueNameStyle = element.findtext("HierarchyUniqueNameStyle")
        self.MemberUniqueNameStyle = element.findtext("MemberUniqueNameStyle")
        self.AllMemberAggregationUsage = element.findtext("AllMemberAggregationUsage")
        
        # Parse Attributes
        attributes_elem = element.find("Attributes")
        self.Attributes = []
        if attributes_elem is not None:
            self.Attributes = [Attribute(attr) for attr in attributes_elem.findall("Attribute")]

class Source:
    def __init__(self, element):
        self.type = element.get("{http://www.w3.org/2001/XMLSchema-instance}type")
        self.DataSourceViewID = element.findtext("DataSourceViewID")

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

class Cube:
    def __init__(self, element, namespaces):
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.ID = element.findtext("ID", namespaces=namespaces)
        self.CreatedTimestamp = element.findtext("CreatedTimestamp", namespaces=namespaces)
        self.LastSchemaUpdate = element.findtext("LastSchemaUpdate", namespaces=namespaces)
        self.ObjectVersion = int(element.findtext("ObjectVersion", namespaces=namespaces) or 0)
        self.ObjectID = element.findtext("ObjectID", namespaces=namespaces)
        self.Ordinal = int(element.findtext("Ordinal", namespaces=namespaces) or 0)
        self.PersistLocation = int(element.findtext("PersistLocation", namespaces=namespaces) or 0)
        self.System = element.findtext("System", namespaces=namespaces) == "true"
        self.Description = element.findtext("Description", namespaces=namespaces)
        self.LastProcessed = element.findtext("LastProcessed", namespaces=namespaces)
        self.Language = int(element.findtext("Language", namespaces=namespaces) or 0)
        self.Collation = element.findtext("Collation", namespaces=namespaces)
        self.DefaultMeasure = element.findtext("DefaultMeasure", namespaces=namespaces)
        self.Visible = element.findtext("Visible", namespaces=namespaces) == "true"
        self.AggregationPrefix = element.findtext("AggregationPrefix", namespaces=namespaces)
        
        # StorageMode with namespace attribute
        storage_mode = element.find("StorageMode", namespaces=namespaces)
        self.StorageMode = storage_mode.text if storage_mode is not None else None
        self.StorageMode_valuens = storage_mode.get("valuens") if storage_mode is not None else None
        
        self.ProcessingMode = element.findtext("ProcessingMode", namespaces=namespaces)
        self.ProcessingPriority = int(element.findtext("ProcessingPriority", namespaces=namespaces) or 0)
        self.ScriptCacheProcessingMode = element.findtext("ScriptCacheProcessingMode", namespaces=namespaces)
        self.ScriptErrorHandlingMode = element.findtext("ScriptErrorHandlingMode", namespaces=namespaces)
        self.StorageLocation = element.findtext("StorageLocation", namespaces=namespaces)
        self.EstimatedRows = int(element.findtext("EstimatedRows", namespaces=namespaces) or 0)
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]
        
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
            self.Dimensions = [Dimension(dim) for dim in dimensions_elem.findall("Dimension", namespaces=namespaces)]
        
        # Additional fields
        self.StructureVersion = int(element.findtext("StructureVersion", namespaces=namespaces) or 0)
        self.DataVersion = int(element.findtext("DataVersion", namespaces=namespaces) or 0)
        self.CalcVersion = int(element.findtext("CalcVersion", namespaces=namespaces) or 0)
        self.LastBindingChange = element.findtext("LastBindingChange", namespaces=namespaces)
        self.LastUpdate = element.findtext("LastUpdate", namespaces=namespaces)
        self.MeasureGroupFileList = element.findtext("MeasureGroupFileList", namespaces=namespaces)
        self.PerspectiveFileList = element.findtext("PerspectiveFileList", namespaces=namespaces)
        self.AssemblyFileList = element.findtext("AssemblyFileList", namespaces=namespaces)
        self.PermissionFileList = element.findtext("PermissionFileList", namespaces=namespaces)

class ParentObject:
    def __init__(self, element, namespaces):
        self.DatabaseID = element.findtext("DatabaseID", namespaces=namespaces)

class ObjectDefinition:
    def __init__(self, element, namespaces):
        cube_elem = element.find("Cube", namespaces=namespaces)
        self.Cube = Cube(cube_elem, namespaces) if cube_elem is not None else None

class CubXmlLoad:
    def __init__(self, xml_string):
        # Define namespaces
        self.namespaces = {
            '': 'http://schemas.microsoft.com/analysisservices/2003/engine',
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
            'xsd': 'http://www.w3.org/2001/XMLSchema',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
        }
        
        root = ET.fromstring(xml_string)
        
        # Parse ParentObject
        parent_obj_elem = root.find("ParentObject", namespaces=self.namespaces)
        self.ParentObject = ParentObject(parent_obj_elem, self.namespaces) if parent_obj_elem is not None else None
        
        # Parse ObjectDefinition
        obj_def_elem = root.find("ObjectDefinition", namespaces=self.namespaces)
        self.ObjectDefinition = ObjectDefinition(obj_def_elem, self.namespaces) if obj_def_elem is not None else None

    @classmethod
    def from_xml_file(cls, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            xml_string = f.read()
        return cls(xml_string)
    
    @classmethod
    def from_xml_string(cls, xml_string):
        return cls(xml_string)