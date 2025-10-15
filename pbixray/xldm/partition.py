import xml.etree.ElementTree as ET
from typing import List, Optional

from .common import Annotation, Source, ProcessableObject, parse_int_or_default
from .namespaces import XmlDefinitionBase, ObjectDefinitionBase, STANDARD_NAMESPACES, ParentObject

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
        self.Source = Source(source_elem) if source_elem is not None else None

class Partition:
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
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]
        
        data_version = element.findtext("DataVersion", namespaces=namespaces)
        self.DataVersion = int(data_version) if data_version else None
        self.LastBindingChange = element.findtext("LastBindingChange", namespaces=namespaces)
        self.LastProcessed = element.findtext("LastProcessed", namespaces=namespaces)
        self.Type = element.findtext("Type", namespaces=namespaces)
        self.AggregationPrefix = element.findtext("AggregationPrefix", namespaces=namespaces)
        
        # StorageMode with namespace attribute
        storage_mode = element.find("StorageMode", namespaces=namespaces)
        self.StorageMode = storage_mode.text if storage_mode is not None else None
        self.StorageMode_valuens = storage_mode.get("valuens") if storage_mode is not None else None
        
        # CurrentStorageMode with namespace attribute
        current_storage_mode = element.find("CurrentStorageMode", namespaces=namespaces)
        self.CurrentStorageMode = current_storage_mode.text if current_storage_mode is not None else None
        self.CurrentStorageMode_valuens = current_storage_mode.get("valuens") if current_storage_mode is not None else None
        
        # Namespace-specific elements
        self.StringStoresCompatibilityLevel = element.findtext("{http://schemas.microsoft.com/analysisservices/2011/engine/300}StringStoresCompatibilityLevel")
        if self.StringStoresCompatibilityLevel:
            self.StringStoresCompatibilityLevel = int(self.StringStoresCompatibilityLevel)
        
        self.InternalStringStoresCompatibilityLevel = element.findtext("{http://schemas.microsoft.com/analysisservices/2011/engine/300}InternalStringStoresCompatibilityLevel")
        if self.InternalStringStoresCompatibilityLevel:
            self.InternalStringStoresCompatibilityLevel = int(self.InternalStringStoresCompatibilityLevel)
        
        self.CurrentStringStoresCompatibilityLevel = element.findtext("{http://schemas.microsoft.com/analysisservices/2011/engine/300}CurrentStringStoresCompatibilityLevel")
        if self.CurrentStringStoresCompatibilityLevel:
            self.CurrentStringStoresCompatibilityLevel = int(self.CurrentStringStoresCompatibilityLevel)
        
        self.ProcessingMode = element.findtext("ProcessingMode", namespaces=namespaces)
        processing_priority = element.findtext("ProcessingPriority", namespaces=namespaces)
        self.ProcessingPriority = int(processing_priority) if processing_priority else None
        
        # Parse ErrorConfiguration
        error_config_elem = element.find("ErrorConfiguration", namespaces=namespaces)
        self.ErrorConfiguration = ErrorConfiguration(error_config_elem, namespaces) if error_config_elem is not None else None
        
        self.StorageLocation = element.findtext("StorageLocation", namespaces=namespaces)
        self.RemoteDataSourceID = element.findtext("RemoteDataSourceID", namespaces=namespaces)
        self.Slice = element.findtext("Slice", namespaces=namespaces)
        estimated_rows = element.findtext("EstimatedRows", namespaces=namespaces)
        self.EstimatedRows = int(estimated_rows) if estimated_rows else None
        self.AggregationDesignID = element.findtext("AggregationDesignID", namespaces=namespaces)
        
        # Parse Source
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = Source(source_elem) if source_elem is not None else None
        
        # Parse ProactiveCaching
        pc_elem = element.find("ProactiveCaching", namespaces=namespaces)
        self.ProactiveCaching = ProactiveCaching(pc_elem, namespaces) if pc_elem is not None else None
        
        estimated_size = element.findtext("EstimatedSize", namespaces=namespaces)
        self.EstimatedSize = int(estimated_size) if estimated_size else None
        cache_version = element.findtext("CacheVersion", namespaces=namespaces)
        self.CacheVersion = int(cache_version) if cache_version else None

class PartitionXmlLoad(XmlDefinitionBase):
    def _parse_xml(self):
        # Parse ParentObject
        parent_obj_elem = self.root.find("ParentObject", namespaces=self.namespaces)
        self.ParentObject = ParentObject(parent_obj_elem, self.namespaces) if parent_obj_elem is not None else None
        
        # Parse ObjectDefinition and extract Partition directly
        obj_def_elem = self.root.find("ObjectDefinition", namespaces=self.namespaces)
        if obj_def_elem is not None:
            partition_elem = obj_def_elem.find("Partition", namespaces=self.namespaces)
            self.Partition = Partition(partition_elem, self.namespaces) if partition_elem is not None else None
        else:
            self.Partition = None