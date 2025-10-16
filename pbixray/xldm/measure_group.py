import xml.etree.ElementTree as ET
from typing import List, Optional

from .common import Annotation, Source, ProcessableObject, parse_int_or_default
from .namespaces import XmlDefinitionBase, ObjectDefinitionBase, STANDARD_NAMESPACES, ParentObject

class KeyColumn:
    def __init__(self, element, namespaces):
        self.DataType = element.findtext("DataType", namespaces=namespaces)
        data_size = element.findtext("DataSize", namespaces=namespaces)
        self.DataSize = int(data_size) if data_size else None
        self.NullProcessing = element.findtext("NullProcessing", namespaces=namespaces)
        self.InvalidXmlCharacters = element.findtext("InvalidXmlCharacters", namespaces=namespaces)
        self.Collation = element.findtext("Collation", namespaces=namespaces)
        self.Format = element.findtext("Format", namespaces=namespaces)
        
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = Source(source_elem, namespaces) if source_elem is not None else None

class MeasureSource:
    def __init__(self, element, namespaces):
        self.DataType = element.findtext("DataType", namespaces=namespaces)
        data_size = element.findtext("DataSize", namespaces=namespaces)
        self.DataSize = int(data_size) if data_size else None
        self.NullProcessing = element.findtext("NullProcessing", namespaces=namespaces)
        self.Collation = element.findtext("Collation", namespaces=namespaces)
        self.Format = element.findtext("Format", namespaces=namespaces)
        
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = Source(source_elem, namespaces) if source_elem is not None else None

class Measure:
    def __init__(self, element, namespaces):
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.ID = element.findtext("ID", namespaces=namespaces)
        self.Description = element.findtext("Description", namespaces=namespaces)
        self.AggregateFunction = element.findtext("AggregateFunction", namespaces=namespaces)
        self.DataType = element.findtext("DataType", namespaces=namespaces)
        self.Visible = element.findtext("Visible", namespaces=namespaces) == "true"
        self.MeasureExpression = element.findtext("MeasureExpression", namespaces=namespaces)
        self.DisplayFolder = element.findtext("DisplayFolder", namespaces=namespaces)
        self.FormatString = element.findtext("FormatString", namespaces=namespaces)
        self.BackColor = element.findtext("BackColor", namespaces=namespaces)
        self.ForeColor = element.findtext("ForeColor", namespaces=namespaces)
        self.FontName = element.findtext("FontName", namespaces=namespaces)
        self.FontSize = element.findtext("FontSize", namespaces=namespaces)
        self.FontFlags = element.findtext("FontFlags", namespaces=namespaces)
        
        # Parse Source
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = MeasureSource(source_elem, namespaces) if source_elem is not None else None

class MeasureGroupAttribute:
    def __init__(self, element, namespaces):
        self.AttributeID = element.findtext("AttributeID", namespaces=namespaces)
        self.Type = element.findtext("Type", namespaces=namespaces)
        self.Enabled = element.findtext("Enabled", namespaces=namespaces) == "true"
        
        # Parse KeyColumns
        key_columns_elem = element.find("KeyColumns", namespaces=namespaces)
        self.KeyColumns = []
        if key_columns_elem is not None:
            self.KeyColumns = [KeyColumn(kc, namespaces) for kc in key_columns_elem.findall("KeyColumn", namespaces=namespaces)]

class MeasureGroupDimension:
    def __init__(self, element, namespaces):
        self.type = element.get("{http://www.w3.org/2001/XMLSchema-instance}type")
        
        # Parse Attributes
        attributes_elem = element.find("Attributes", namespaces=namespaces)
        self.Attributes = []
        if attributes_elem is not None:
            self.Attributes = [MeasureGroupAttribute(attr, namespaces) for attr in attributes_elem.findall("Attribute", namespaces=namespaces)]
        
        # Namespace-specific elements
        self.ShareDimensionStorage = element.findtext("{http://schemas.microsoft.com/analysisservices/2010/engine/200/200}ShareDimensionStorage")
        
        self.CubeDimensionID = element.findtext("CubeDimensionID", namespaces=namespaces)

class ErrorConfiguration:
    def __init__(self, element, namespaces):
        key_error_limit = element.findtext("KeyErrorLimit", namespaces=namespaces)
        self.KeyErrorLimit = int(key_error_limit) if key_error_limit else None
        self.KeyErrorLogFile = element.findtext("KeyErrorLogFile", namespaces=namespaces)
        self.KeyErrorAction = element.findtext("KeyErrorAction", namespaces=namespaces)
        self.KeyErrorLimitAction = element.findtext("KeyErrorLimitAction", namespaces=namespaces)
        self.KeyDuplicate = element.findtext("KeyDuplicate", namespaces=namespaces)
        self.KeyNotFound = element.findtext("KeyNotFound", namespaces=namespaces)
        self.NullKeyConvertedToUnknown = element.findtext("NullKeyConvertedToUnknown", namespaces=namespaces)
        self.NullKeyNotAllowed = element.findtext("NullKeyNotAllowed", namespaces=namespaces)

class ProactiveCaching:
    def __init__(self, element, namespaces):
        self.SilenceInterval = element.findtext("SilenceInterval", namespaces=namespaces)
        self.Latency = element.findtext("Latency", namespaces=namespaces)
        self.SilenceOverrideInterval = element.findtext("SilenceOverrideInterval", namespaces=namespaces)
        self.ForceRebuildInterval = element.findtext("ForceRebuildInterval", namespaces=namespaces)
        self.Enabled = element.findtext("Enabled", namespaces=namespaces) == "true"
        self.AggregationStorage = element.findtext("AggregationStorage", namespaces=namespaces)
        self.OnlineMode = element.findtext("OnlineMode", namespaces=namespaces)
        
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = Source(source_elem, namespaces) if source_elem is not None else None

class MeasureGroup:
    def __init__(self, element, namespaces):
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.ID = element.findtext("ID", namespaces=namespaces)
        self.CreatedTimestamp = element.findtext("CreatedTimestamp", namespaces=namespaces)
        self.LastSchemaUpdate = element.findtext("LastSchemaUpdate", namespaces=namespaces)
        object_version = element.findtext("ObjectVersion", namespaces=namespaces)
        self.ObjectVersion = int(object_version) if object_version else None
        self.ObjectID = element.findtext("ObjectID", namespaces=namespaces)
        ordinal = element.findtext("Ordinal", namespaces=namespaces)
        self.Ordinal = int(ordinal) if ordinal else None
        persist_location = element.findtext("PersistLocation", namespaces=namespaces)
        self.PersistLocation = int(persist_location) if persist_location else None
        self.System = element.findtext("System", namespaces=namespaces) == "true"
        self.DataFileList = element.findtext("DataFileList", namespaces=namespaces)
        self.Description = element.findtext("Description", namespaces=namespaces)
        self.LastProcessed = element.findtext("LastProcessed", namespaces=namespaces)
        self.Type = element.findtext("Type", namespaces=namespaces)
        self.DataAggregation = element.findtext("DataAggregation", namespaces=namespaces)
        self.AggregationPrefix = element.findtext("AggregationPrefix", namespaces=namespaces)
        
        # StorageMode with namespace attribute
        storage_mode = element.find("StorageMode", namespaces=namespaces)
        self.StorageMode = storage_mode.text if storage_mode is not None else None
        self.StorageMode_valuens = storage_mode.get("valuens") if storage_mode is not None else None
        
        processing_priority = element.findtext("ProcessingPriority", namespaces=namespaces)
        self.ProcessingPriority = int(processing_priority) if processing_priority else None
        self.StorageLocation = element.findtext("StorageLocation", namespaces=namespaces)
        self.IgnoreUnrelatedDimensions = element.findtext("IgnoreUnrelatedDimensions", namespaces=namespaces) == "true"
        estimated_rows = element.findtext("EstimatedRows", namespaces=namespaces)
        self.EstimatedRows = int(estimated_rows) if estimated_rows else None
        
        # Parse ErrorConfiguration
        error_config_elem = element.find("ErrorConfiguration", namespaces=namespaces)
        self.ErrorConfiguration = ErrorConfiguration(error_config_elem, namespaces) if error_config_elem is not None else None
        
        self.ProcessingMode = element.findtext("ProcessingMode", namespaces=namespaces)
        
        # Parse ProactiveCaching
        pc_elem = element.find("ProactiveCaching", namespaces=namespaces)
        self.ProactiveCaching = ProactiveCaching(pc_elem, namespaces) if pc_elem is not None else None
        
        # Parse Measures
        measures_elem = element.find("Measures", namespaces=namespaces)
        self.Measures = []
        if measures_elem is not None:
            self.Measures = [Measure(m, namespaces) for m in measures_elem.findall("Measure", namespaces=namespaces)]
        
        # Parse Dimensions
        dimensions_elem = element.find("Dimensions", namespaces=namespaces)
        self.Dimensions = []
        if dimensions_elem is not None:
            self.Dimensions = [MeasureGroupDimension(dim, namespaces) for dim in dimensions_elem.findall("Dimension", namespaces=namespaces)]
        
        # Version fields
        structure_version = element.findtext("StructureVersion", namespaces=namespaces)
        self.StructureVersion = int(structure_version) if structure_version else None
        cache_version = element.findtext("CacheVersion", namespaces=namespaces)
        self.CacheVersion = int(cache_version) if cache_version else None
        data_version = element.findtext("DataVersion", namespaces=namespaces)
        self.DataVersion = int(data_version) if data_version else None
        self.LastBindingChange = element.findtext("LastBindingChange", namespaces=namespaces)
        self.AggregationDesignFileList = element.findtext("AggregationDesignFileList", namespaces=namespaces)
        self.PartitionFileList = element.findtext("PartitionFileList", namespaces=namespaces)

class MeasureGroupXmlLoad(XmlDefinitionBase):
    def _parse_xml(self):
        # Parse ParentObject
        parent_obj_elem = self.root.find("ParentObject", namespaces=self.namespaces)
        self.ParentObject = ParentObject(parent_obj_elem, self.namespaces) if parent_obj_elem is not None else None
        
        # Parse ObjectDefinition and extract MeasureGroup directly
        obj_def_elem = self.root.find("ObjectDefinition", namespaces=self.namespaces)
        if obj_def_elem is not None:
            measure_group_elem = obj_def_elem.find("MeasureGroup", namespaces=self.namespaces)
            self.MeasureGroup = MeasureGroup(measure_group_elem, self.namespaces) if measure_group_elem is not None else None
        else:
            self.MeasureGroup = None
