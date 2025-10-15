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
        self.Source = Source(source_elem) if source_elem is not None else None

class NameColumn:
    def __init__(self, element, namespaces):
        self.DataType = element.findtext("DataType", namespaces=namespaces)
        data_size = element.findtext("DataSize", namespaces=namespaces)
        self.DataSize = int(data_size) if data_size else None
        self.NullProcessing = element.findtext("NullProcessing", namespaces=namespaces)
        self.InvalidXmlCharacters = element.findtext("InvalidXmlCharacters", namespaces=namespaces)
        self.Collation = element.findtext("Collation", namespaces=namespaces)
        self.Format = element.findtext("Format", namespaces=namespaces)
        
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = Source(source_elem) if source_elem is not None else None

class AttributeRelationship:
    def __init__(self, element, namespaces):
        self.AttributeID = element.findtext("AttributeID", namespaces=namespaces)
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.RelationshipType = element.findtext("RelationshipType", namespaces=namespaces)
        self.Cardinality = element.findtext("Cardinality", namespaces=namespaces)
        self.Optionality = element.findtext("Optionality", namespaces=namespaces)
        self.OverrideBehavior = element.findtext("OverrideBehavior", namespaces=namespaces)

class DimensionAttribute:
    def __init__(self, element, namespaces):
        self.Name = element.findtext("Name", namespaces=namespaces)
        self.ID = element.findtext("ID", namespaces=namespaces)
        self.Description = element.findtext("Description", namespaces=namespaces)
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]
        
        # Type with namespace attribute
        type_elem = element.find("Type", namespaces=namespaces)
        self.Type = type_elem.text if type_elem is not None else None
        self.Type_valuens = type_elem.get("valuens") if type_elem is not None else None
        
        self.Usage = element.findtext("Usage", namespaces=namespaces)
        estimated_count = element.findtext("EstimatedCount", namespaces=namespaces)
        self.EstimatedCount = int(estimated_count) if estimated_count else None
        self.DiscretizationMethod = element.findtext("DiscretizationMethod", namespaces=namespaces)
        discretization_bucket = element.findtext("DiscretizationBucketCount", namespaces=namespaces)
        self.DiscretizationBucketCount = int(discretization_bucket) if discretization_bucket else None
        self.OrderBy = element.findtext("OrderBy", namespaces=namespaces)
        self.InstanceSelection = element.findtext("InstanceSelection", namespaces=namespaces)
        self.DefaultMember = element.findtext("DefaultMember", namespaces=namespaces)
        self.OrderByAttributeID = element.findtext("OrderByAttributeID", namespaces=namespaces)
        self.NamingTemplate = element.findtext("NamingTemplate", namespaces=namespaces)
        self.MembersWithData = element.findtext("MembersWithData", namespaces=namespaces)
        self.MembersWithDataCaption = element.findtext("MembersWithDataCaption", namespaces=namespaces)
        self.MemberNamesUnique = element.findtext("MemberNamesUnique", namespaces=namespaces) == "true"
        self.KeyUniquenessGuarantee = element.findtext("KeyUniquenessGuarantee", namespaces=namespaces) == "true"
        self.IsAggregatable = element.findtext("IsAggregatable", namespaces=namespaces) == "true"
        self.AttributeHierarchyEnabled = element.findtext("AttributeHierarchyEnabled", namespaces=namespaces) == "true"
        self.AttributeHierarchyVisible = element.findtext("AttributeHierarchyVisible", namespaces=namespaces) == "true"
        self.AttributeHierarchyOrdered = element.findtext("AttributeHierarchyOrdered", namespaces=namespaces) == "true"
        self.AttributeHierarchyOptimizedState = element.findtext("AttributeHierarchyOptimizedState", namespaces=namespaces)
        self.AttributeHierarchyDisplayFolder = element.findtext("AttributeHierarchyDisplayFolder", namespaces=namespaces)
        
        # Namespace-specific elements
        self.AttributeHierarchyProcessingState = element.findtext("{http://schemas.microsoft.com/analysisservices/2011/engine/300}AttributeHierarchyProcessingState")
        self.ProcessingState = element.findtext("{http://schemas.microsoft.com/analysisservices/2010/engine/200}ProcessingState")
        
        self.GroupingBehavior = element.findtext("GroupingBehavior", namespaces=namespaces)
        
        # Parse KeyColumns
        key_columns_elem = element.find("KeyColumns", namespaces=namespaces)
        self.KeyColumns = []
        if key_columns_elem is not None:
            self.KeyColumns = [KeyColumn(kc, namespaces) for kc in key_columns_elem.findall("KeyColumn", namespaces=namespaces)]
        
        # Parse NameColumn
        name_column_elem = element.find("NameColumn", namespaces=namespaces)
        self.NameColumn = NameColumn(name_column_elem, namespaces) if name_column_elem is not None else None
        
        # Parse AttributeRelationships
        attr_rels_elem = element.find("AttributeRelationships", namespaces=namespaces)
        self.AttributeRelationships = []
        if attr_rels_elem is not None:
            self.AttributeRelationships = [AttributeRelationship(ar, namespaces) for ar in attr_rels_elem.findall("AttributeRelationship", namespaces=namespaces)]

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

class Dimension:
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
        
        self.LastProcessed = element.findtext("LastProcessed", namespaces=namespaces)
        estimated_size = element.findtext("EstimatedSize", namespaces=namespaces)
        self.EstimatedSize = int(estimated_size) if estimated_size else None
        
        # Parse Source
        source_elem = element.find("Source", namespaces=namespaces)
        self.Source = Source(source_elem) if source_elem is not None else None
        
        self.MiningModelID = element.findtext("MiningModelID", namespaces=namespaces)
        self.Type = element.findtext("Type", namespaces=namespaces)
        
        # UnknownMember with namespace attribute
        unknown_member = element.find("UnknownMember", namespaces=namespaces)
        self.UnknownMember = unknown_member.text if unknown_member is not None else None
        self.UnknownMember_valuens = unknown_member.get("valuens") if unknown_member is not None else None
        
        self.MdxMissingMemberMode = element.findtext("MdxMissingMemberMode", namespaces=namespaces)
        
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
        
        self.ProcessingState = element.findtext("{http://schemas.microsoft.com/analysisservices/2011/engine/300}ProcessingState")
        
        # Parse ErrorConfiguration
        error_config_elem = element.find("ErrorConfiguration", namespaces=namespaces)
        self.ErrorConfiguration = ErrorConfiguration(error_config_elem, namespaces) if error_config_elem is not None else None
        
        # StorageMode with namespace attribute
        storage_mode = element.find("StorageMode", namespaces=namespaces)
        self.StorageMode = storage_mode.text if storage_mode is not None else None
        self.StorageMode_valuens = storage_mode.get("valuens") if storage_mode is not None else None
        
        # CurrentStorageMode with namespace attribute
        current_storage_mode = element.find("CurrentStorageMode", namespaces=namespaces)
        self.CurrentStorageMode = current_storage_mode.text if current_storage_mode is not None else None
        self.CurrentStorageMode_valuens = current_storage_mode.get("valuens") if current_storage_mode is not None else None
        
        processing_priority = element.findtext("ProcessingPriority", namespaces=namespaces)
        self.ProcessingPriority = int(processing_priority) if processing_priority else None
        self.WriteEnabled = element.findtext("WriteEnabled", namespaces=namespaces) == "true"
        self.DependsOnDimensionID = element.findtext("DependsOnDimensionID", namespaces=namespaces)
        language = element.findtext("Language", namespaces=namespaces)
        self.Language = int(language) if language else None
        self.Collation = element.findtext("Collation", namespaces=namespaces)
        self.UnknownMemberName = element.findtext("UnknownMemberName", namespaces=namespaces)
        self.ProcessingMode = element.findtext("ProcessingMode", namespaces=namespaces)
        self.OrderByKey = element.findtext("OrderByKey", namespaces=namespaces) == "true"
        self.AttributeAllMemberName = element.findtext("AttributeAllMemberName", namespaces=namespaces)
        
        # Parse ProactiveCaching
        pc_elem = element.find("ProactiveCaching", namespaces=namespaces)
        self.ProactiveCaching = ProactiveCaching(pc_elem, namespaces) if pc_elem is not None else None
        
        # Parse Attributes
        attributes_elem = element.find("Attributes", namespaces=namespaces)
        self.Attributes = []
        if attributes_elem is not None:
            self.Attributes = [DimensionAttribute(attr, namespaces) for attr in attributes_elem.findall("Attribute", namespaces=namespaces)]
        
        # Version fields
        structure_version = element.findtext("StructureVersion", namespaces=namespaces)
        self.StructureVersion = int(structure_version) if structure_version else None
        data_id_version = element.findtext("DataIDVersion", namespaces=namespaces)
        self.DataIDVersion = int(data_id_version) if data_id_version else None
        inc_data_id_version = element.findtext("IncDataIDVersion", namespaces=namespaces)
        self.IncDataIDVersion = int(inc_data_id_version) if inc_data_id_version else None
        cache_version = element.findtext("CacheVersion", namespaces=namespaces)
        self.CacheVersion = int(cache_version) if cache_version else None
        data_version = element.findtext("DataVersion", namespaces=namespaces)
        self.DataVersion = int(data_version) if data_version else None
        self.LastBindingChange = element.findtext("LastBindingChange", namespaces=namespaces)
        self.PermissionFileList = element.findtext("PermissionFileList", namespaces=namespaces)

class DimensionXmlLoad(XmlDefinitionBase):
    def _parse_xml(self):
        # Parse ParentObject
        parent_obj_elem = self.root.find("ParentObject", namespaces=self.namespaces)
        self.ParentObject = ParentObject(parent_obj_elem, self.namespaces) if parent_obj_elem is not None else None
        
        # Parse ObjectDefinition and extract Dimension directly
        obj_def_elem = self.root.find("ObjectDefinition", namespaces=self.namespaces)
        if obj_def_elem is not None:
            dimension_elem = obj_def_elem.find("Dimension", namespaces=self.namespaces)
            self.Dimension = Dimension(dimension_elem, self.namespaces) if dimension_elem is not None else None
        else:
            self.Dimension = None