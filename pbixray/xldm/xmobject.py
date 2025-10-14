import xml.etree.ElementTree as ET
from typing import List, Optional, Dict, Any
from enum import Enum

# Enumerations
class XMObjectClassName(Enum):
    XM_SIMPLE_TABLE = "XMSimpleTable"
    XM_RAW_COLUMN = "XMRawColumn"
    XM_RELATIONSHIP = "XMRelationship"
    XM_COLUMN_SEGMENT = "XMColumnSegment"
    XM_PARTITION = "XMPartition"
    XM_TABLE_STATS = "XMTableStats"
    XM_COLUMN_STATS = "XMColumnStats"
    XM_COLUMN_SEGMENT_STATS = "XMColumnSegmentStats"
    XM_HIERARCHY = "XMHierarchy"
    XM_USER_HIERARCHY = "XMUserHierarchy"
    XM_HASH_DICTIONARY_LONG = "XMHashDataDictionary<XM_Long>"
    XM_HASH_DICTIONARY_REAL = "XMHashDataDictionary<XM_Real>"
    XM_HASH_DICTIONARY_STRING = "XMHashDataDictionary<XM_String>"
    XM_VALUE_DICTIONARY_LONG = "XMValueDataDictionary<XM_Long>"
    XM_VALUE_DICTIONARY_REAL = "XMValueDataDictionary<XM_Real>"


# Base Properties Classes
class XMSimpleTableProperties:
    def __init__(self, element: ET.Element):
        self.Version = int(element.findtext("Version", "0"))
        self.Settings = int(element.findtext("Settings", "0"))
        self.RIViolationCount = int(element.findtext("RIViolationCount", "0"))


class XMTableStatsProperties:
    def __init__(self, element: ET.Element):
        self.SegmentSize = int(element.findtext("SegmentSize", "0"))
        self.Usage = int(element.findtext("Usage", "0"))


class XMRawColumnProperties:
    def __init__(self, element: ET.Element):
        self.Settings = int(element.findtext("Settings", "0"))
        self.ColumnFlags = int(element.findtext("ColumnFlags", "0"))
        self.Collation = element.findtext("Collation", "")
        self.OrderByColumn = element.findtext("OrderByColumn", "")
        self.Locale = int(element.findtext("Locale", "0"))
        self.BinaryCharacters = int(element.findtext("BinaryCharacters", "0"))


class XMColumnStatsProperties:
    def __init__(self, element: ET.Element):
        self.DistinctStates = int(element.findtext("DistinctStates", "0"))
        self.MinDataID = int(element.findtext("MinDataID", "0"))
        self.MaxDataID = int(element.findtext("MaxDataID", "0"))
        self.OriginalMinSegmentDataID = int(element.findtext("OriginalMinSegmentDataID", "0"))
        self.RLESortOrder = int(element.findtext("RLESortOrder", "-1"))
        self.RowCount = int(element.findtext("RowCount", "0"))
        self.HasNulls = element.findtext("HasNulls", "false") == "true"
        self.RLERuns = int(element.findtext("RLERuns", "0"))
        self.OthersRLERuns = int(element.findtext("OthersRLERuns", "0"))
        self.Usage = int(element.findtext("Usage", "0"))
        self.DBType = int(element.findtext("DBType", "0"))
        self.XMType = int(element.findtext("XMType", "0"))
        self.CompressionType = int(element.findtext("CompressionType", "0"))
        self.CompressionParam = int(element.findtext("CompressionParam", "0"))
        self.EncodingHint = int(element.findtext("EncodingHint", "0"))
        self.AggCounter = int(element.findtext("AggCounter", "0"))
        self.WhereCounter = int(element.findtext("WhereCounter", "0"))
        self.OrderByCounter = int(element.findtext("OrderByCounter", "0"))


class XMColumnSegmentProperties:
    def __init__(self, element: ET.Element):
        self.Records = int(element.findtext("Records", "0"))
        self.Mask = int(element.findtext("Mask", "0"))


class XMColumnSegmentStatsProperties:
    def __init__(self, element: ET.Element):
        self.DistinctStates = int(element.findtext("DistinctStates", "0"))
        self.MinDataID = int(element.findtext("MinDataID", "0"))
        self.MaxDataID = int(element.findtext("MaxDataID", "0"))
        self.OriginalMinSegmentDataID = int(element.findtext("OriginalMinSegmentDataID", "0"))
        self.RLESortOrder = int(element.findtext("RLESortOrder", "-1"))
        self.RowCount = int(element.findtext("RowCount", "0"))
        self.HasNulls = element.findtext("HasNulls", "false") == "true"
        self.RLERuns = int(element.findtext("RLERuns", "0"))
        self.OthersRLERuns = int(element.findtext("OthersRLERuns", "0"))


class XMRelationshipProperties:
    def __init__(self, element: ET.Element):
        self.PrimaryTable = element.findtext("PrimaryTable", "")
        self.PrimaryColumn = element.findtext("PrimaryColumn", "")
        self.ForeignColumn = element.findtext("ForeignColumn", "")


class XMPartitionProperties:
    def __init__(self, element: ET.Element):
        self.IsProcessed = element.findtext("IsProcessed", "false") == "true"
        self.Partition = int(element.findtext("Partition", "0"))


class XMHierarchyProperties:
    def __init__(self, element: ET.Element):
        self.SortOrder = int(element.findtext("SortOrder", "0"))
        self.IsProcessed = element.findtext("IsProcessed", "false") == "true"
        self.TypeMaterialization = int(element.findtext("TypeMaterialization", "-1"))
        self.ColumnPosition2DataID = int(element.findtext("ColumnPosition2DataID", "-1"))
        self.ColumnDataID2Position = int(element.findtext("ColumnDataID2Position", "-1"))
        self.DistinctDataIDs = int(element.findtext("DistinctDataIDs", "0"))
        self.TableStore = element.findtext("TableStore", "")


class XMUserHierarchyProperties:
    def __init__(self, element: ET.Element):
        self.IsProcessed = element.findtext("IsProcessed", "false") == "true"
        self.TableStore = element.findtext("TableStore", "")
        self.TableName = element.findtext("TableName", "")


class XMHashDictionaryProperties:
    def __init__(self, element: ET.Element):
        self.DataVersion = int(element.findtext("DataVersion", "0"))
        self.LastId = int(element.findtext("LastId", "0"))
        self.Nullable = element.findtext("Nullable", "false") == "true"
        self.Unique = element.findtext("Unique", "false") == "true"


class XMHashDictionaryLongProperties(XMHashDictionaryProperties):
    def __init__(self, element: ET.Element):
        super().__init__(element)
        self.OperatingOn32 = element.findtext("OperatingOn32", "false") == "true"


class XMHashDictionaryStringProperties(XMHashDictionaryProperties):
    def __init__(self, element: ET.Element):
        super().__init__(element)
        self.DictionaryFlags = int(element.findtext("DictionaryFlags", "0"))


class XMValueDictionaryProperties:
    def __init__(self, element: ET.Element):
        self.DataVersion = int(element.findtext("DataVersion", "0"))
        self.BaseId = int(element.findtext("BaseId", "0"))
        self.Magnitude = float(element.findtext("Magnitude", "0.0"))


class XMRENoSplitCompressionInfoProperties:
    def __init__(self, element: ET.Element):
        self.Min = int(element.findtext("Min", "0"))


class XMRLECompressionInfoProperties:
    def __init__(self, element: ET.Element):
        self.BookmarkBits = int(element.findtext("BookmarkBits", "0"))
        self.StorageAllocSize = int(element.findtext("StorageAllocSize", "0"))
        self.StorageUsedSize = int(element.findtext("StorageUsedSize", "0"))
        self.SegmentNeedsResizing = element.findtext("SegmentNeedsResizing", "false") == "true"


class XMSegmentMapProperties:
    def __init__(self, element: ET.Element):
        self.Segments = int(element.findtext("Segments", "0"))
        self.Records = int(element.findtext("Records", "0"))
        self.RecordsPerSegment = int(element.findtext("RecordsPerSegment", "0"))


# Member and Collection Classes
class XMObjectMember:
    def __init__(self, element: ET.Element):
        self.Name = element.findtext("Name", "")
        xm_object_elem = element.find("XMObject")
        self.XMObject = XMObject(xm_object_elem) if xm_object_elem is not None else None


class XMObjectCollection:
    def __init__(self, element: ET.Element):
        self.Name = element.findtext("Name", "")
        self.XMObjects = [XMObject(e) for e in element.findall("XMObject")]


class XMObjectDataObject:
    def __init__(self, element: ET.Element):
        xm_object_elem = element.find("XMObject")
        self.XMObject = XMObject(xm_object_elem) if xm_object_elem is not None else None

class XMMultiPartSegmentMapProperties:
    """Properties for XMMultiPartSegmentMap"""
    def __init__(self, element: ET.Element):
        self.FirstPartitionRecordCount = int(element.findtext("FirstPartitionRecordCount", "0"))
        self.FirstPartitionSegmentCount = int(element.findtext("FirstPartitionSegmentCount", "0"))


class XMRawColumnPartitionDataObjectProperties:
    """Properties for XMRawColumnPartitionDataObject"""
    def __init__(self, element: ET.Element):
        self.DataVersion = int(element.findtext("DataVersion", "0"))
        self.Partition = int(element.findtext("Partition", "0"))
        self.SegmentCount = int(element.findtext("SegmentCount", "0"))


class XMSegment1MapProperties:
    """Properties for XMSegment1Map"""
    def __init__(self, element: ET.Element):
        self.Records = int(element.findtext("Records", "0"))


class XMRelationshipIndexSparseDIDsProperties:
    """Properties for XMRelationshipIndexSparseDIDs"""
    def __init__(self, element: ET.Element):
        self.Flags = int(element.findtext("Flags", "0"))


class XMRelationshipIndexDenseDIDsProperties:
    """Properties for XMRelationshipIndexDenseDIDs"""
    def __init__(self, element: ET.Element):
        self.Records = int(element.findtext("Records", "0"))
        self.TableName = element.findtext("TableName", "")
        self.Flags = int(element.findtext("Flags", "0"))


# Main XMObject Class
class XMObject:
    def __init__(self, element: Optional[ET.Element]):
        if element is None:
            self.class_name = None
            self.name = None
            self.provider_version = None
            self.properties = None
            self.members = []
            self.collections = []
            self.data_objects = []
            return
        
        self.class_name = element.get("class", "")
        self.name = element.get("name", "")
        self.provider_version = int(element.get("ProviderVersion", "0"))
        
        # Parse Properties based on class type
        properties_elem = element.find("Properties")
        self.properties = self._parse_properties(properties_elem, self.class_name)
        
        # Parse Members
        members_elem = element.find("Members")
        self.members = []
        if members_elem is not None:
            self.members = [XMObjectMember(e) for e in members_elem.findall("Member")]
        
        # Parse Collections
        collections_elem = element.find("Collections")
        self.collections = []
        if collections_elem is not None:
            self.collections = [XMObjectCollection(e) for e in collections_elem.findall("Collection")]
        
        # Parse DataObjects
        data_objects_elem = element.find("DataObjects")
        self.data_objects = []
        if data_objects_elem is not None:
            self.data_objects = [XMObjectDataObject(e) for e in data_objects_elem.findall("DataObject")]
    
    def _parse_properties(self, properties_elem: Optional[ET.Element], class_name: str) -> Any:
        if properties_elem is None:
            return None
        
        property_map = {
            "XMSimpleTable": XMSimpleTableProperties,
            "XMTableStats": XMTableStatsProperties,
            "XMRawColumn": XMRawColumnProperties,
            "XMColumnStats": XMColumnStatsProperties,
            "XMColumnSegment": XMColumnSegmentProperties,
            "XMColumnSegmentStats": XMColumnSegmentStatsProperties,
            "XMRelationship": XMRelationshipProperties,
            "XMPartition": XMPartitionProperties,
            "XMHierarchy": XMHierarchyProperties,
            "XMUserHierarchy": XMUserHierarchyProperties,
            "XMHashDataDictionary<XM_Long>": XMHashDictionaryLongProperties,
            "XMHashDataDictionary<XM_Real>": XMHashDictionaryProperties,
            "XMHashDataDictionary<XM_String>": XMHashDictionaryStringProperties,
            "XMValueDataDictionary<XM_Long>": XMValueDictionaryProperties,
            "XMValueDataDictionary<XM_Real>": XMValueDictionaryProperties,
            "XMMultiPartSegmentMap": XMMultiPartSegmentMapProperties,
            "XMRawColumnPartitionDataObject": XMRawColumnPartitionDataObjectProperties,
            "XMSegment1Map": XMSegment1MapProperties,
            "XMRelationshipIndexSparseDIDs": XMRelationshipIndexSparseDIDsProperties,
            "XMRelationshipIndexDenseDIDs": XMRelationshipIndexDenseDIDsProperties,
        }
        
        # Handle compression info classes (they all use the same properties)
        if "XMRENoSplitCompressionInfo" in class_name or "XM123CompressionInfo" in class_name:
            return XMRENoSplitCompressionInfoProperties(properties_elem)
        if "XMRLECompressionInfo" in class_name and "Hybrid" not in class_name:
            return XMRLECompressionInfoProperties(properties_elem)
        if "SegmentEqualMapEx" in class_name:
            return XMSegmentMapProperties(properties_elem)
        
        properties_class = property_map.get(class_name)
        if properties_class:
            return properties_class(properties_elem)
        
        return None
    


# Document Root Parser
class XMObjectDocument:
    """Parser for .tbl.xml metadata files"""
    
    def __init__(self, xml_string: str):
        root = ET.fromstring(xml_string)
        self.root_object = XMObject(root)
    
    @classmethod
    def from_xml_string(cls, xml_string: str):
        return cls(xml_string)
    
    @classmethod
    def from_file(cls, file_path: str):
        tree = ET.parse(file_path)
        root = tree.getroot()
        instance = cls.__new__(cls)
        instance.root_object = XMObject(root)
        return instance
    
