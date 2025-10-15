import xml.etree.ElementTree as ET
from typing import List, Optional, Dict, Any
from enum import Enum

# XMObject Namespaces - used in .tbl.xml files
XMOBJECT_NAMESPACES = {
    '': 'http://schemas.microsoft.com/analysisservices/imbi',  # Default namespace
    'imbi200': 'http://schemas.microsoft.com/analysisservices/2010/imbi/200',
    'imbi200_200': 'http://schemas.microsoft.com/analysisservices/2010/imbi/200/200',
    'xsd': 'http://www.w3.org/2001/XMLSchema',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

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
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Version = int(element.findtext("Version", "0", namespaces=namespaces))
        self.Settings = int(element.findtext("Settings", "0", namespaces=namespaces))
        self.RIViolationCount = int(element.findtext("RIViolationCount", "0", namespaces=namespaces))


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
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.DistinctStates = int(element.findtext("DistinctStates", "0", namespaces=namespaces))
        self.MinDataID = int(element.findtext("MinDataID", "0", namespaces=namespaces))
        self.MaxDataID = int(element.findtext("MaxDataID", "0", namespaces=namespaces))
        self.OriginalMinSegmentDataID = int(element.findtext("OriginalMinSegmentDataID", "0", namespaces=namespaces))
        self.RLESortOrder = int(element.findtext("RLESortOrder", "-1", namespaces=namespaces))
        self.RowCount = int(element.findtext("RowCount", "0", namespaces=namespaces))
        self.HasNulls = element.findtext("HasNulls", "false", namespaces=namespaces) == "true"
        self.RLERuns = int(element.findtext("RLERuns", "0", namespaces=namespaces))
        self.OthersRLERuns = int(element.findtext("OthersRLERuns", "0", namespaces=namespaces))
        self.Usage = int(element.findtext("Usage", "0", namespaces=namespaces))
        self.DBType = int(element.findtext("DBType", "0", namespaces=namespaces))
        self.XMType = int(element.findtext("XMType", "0", namespaces=namespaces))
        self.CompressionType = int(element.findtext("CompressionType", "0", namespaces=namespaces))
        self.CompressionParam = int(element.findtext("CompressionParam", "0", namespaces=namespaces))
        self.EncodingHint = int(element.findtext("EncodingHint", "0", namespaces=namespaces))
        self.AggCounter = int(element.findtext("AggCounter", "0", namespaces=namespaces))
        self.WhereCounter = int(element.findtext("WhereCounter", "0", namespaces=namespaces))
        self.OrderByCounter = int(element.findtext("OrderByCounter", "0", namespaces=namespaces))


class XMColumnSegmentProperties:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Records = int(element.findtext("Records", "0", namespaces=namespaces))
        self.Mask = int(element.findtext("Mask", "0", namespaces=namespaces))


class XMColumnSegmentStatsProperties:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.DistinctStates = int(element.findtext("DistinctStates", "0", namespaces=namespaces))
        self.MinDataID = int(element.findtext("MinDataID", "0", namespaces=namespaces))
        self.MaxDataID = int(element.findtext("MaxDataID", "0", namespaces=namespaces))
        self.OriginalMinSegmentDataID = int(element.findtext("OriginalMinSegmentDataID", "0", namespaces=namespaces))
        self.RLESortOrder = int(element.findtext("RLESortOrder", "-1", namespaces=namespaces))
        self.RowCount = int(element.findtext("RowCount", "0", namespaces=namespaces))
        self.HasNulls = element.findtext("HasNulls", "false", namespaces=namespaces) == "true"
        self.RLERuns = int(element.findtext("RLERuns", "0", namespaces=namespaces))
        self.OthersRLERuns = int(element.findtext("OthersRLERuns", "0", namespaces=namespaces))
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
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Name = element.findtext("Name", "", namespaces=namespaces)
        xm_object_elem = element.find("XMObject", namespaces=namespaces)
        self.XMObject = XMObject(xm_object_elem, namespaces) if xm_object_elem is not None else None


class XMObjectCollection:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Name = element.findtext("Name", "", namespaces=namespaces)
        self.XMObjects = [XMObject(e, namespaces) for e in element.findall("XMObject", namespaces=namespaces)]


class XMObjectDataObject:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        xm_object_elem = element.find("XMObject", namespaces=namespaces)
        self.XMObject = XMObject(xm_object_elem, namespaces) if xm_object_elem is not None else None

class XMMultiPartSegmentMapProperties:
    """Properties for XMMultiPartSegmentMap"""
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.FirstPartitionRecordCount = int(element.findtext("FirstPartitionRecordCount", "0", namespaces=namespaces))
        self.FirstPartitionSegmentCount = int(element.findtext("FirstPartitionSegmentCount", "0", namespaces=namespaces))


class XMRawColumnPartitionDataObjectProperties:
    """Properties for XMRawColumnPartitionDataObject"""
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.DataVersion = int(element.findtext("DataVersion", "0", namespaces=namespaces))
        self.Partition = int(element.findtext("Partition", "0", namespaces=namespaces))
        self.SegmentCount = int(element.findtext("SegmentCount", "0", namespaces=namespaces))


class XMSegment1MapProperties:
    """Properties for XMSegment1Map"""
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Records = int(element.findtext("Records", "0", namespaces=namespaces))


class XMPartitionProperties:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.IsProcessed = element.findtext("IsProcessed", "false", namespaces=namespaces) == "true"
        self.Partition = int(element.findtext("Partition", "0", namespaces=namespaces))


class XMRawColumnProperties:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Settings = int(element.findtext("Settings", "0", namespaces=namespaces))
        self.ColumnFlags = int(element.findtext("ColumnFlags", "0", namespaces=namespaces))
        self.Collation = element.findtext("Collation", "", namespaces=namespaces)
        self.OrderByColumn = element.findtext("OrderByColumn", "", namespaces=namespaces)
        self.Locale = int(element.findtext("Locale", "0", namespaces=namespaces))
        self.BinaryCharacters = int(element.findtext("BinaryCharacters", "0", namespaces=namespaces))


class XMHierarchyProperties:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.SortOrder = int(element.findtext("SortOrder", "0", namespaces=namespaces))
        self.IsProcessed = element.findtext("IsProcessed", "false", namespaces=namespaces) == "true"
        self.TypeMaterialization = int(element.findtext("TypeMaterialization", "-1", namespaces=namespaces))
        self.ColumnPosition2DataID = int(element.findtext("ColumnPosition2DataID", "-1", namespaces=namespaces))
        self.ColumnDataID2Position = int(element.findtext("ColumnDataID2Position", "-1", namespaces=namespaces))
        self.DistinctDataIDs = int(element.findtext("DistinctDataIDs", "0", namespaces=namespaces))
        self.TableStore = element.findtext("TableStore", "", namespaces=namespaces)


class XMValueDictionaryProperties:
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.DataVersion = int(element.findtext("DataVersion", "0", namespaces=namespaces))
        self.BaseId = int(element.findtext("BaseId", "0", namespaces=namespaces))
class XMRelationshipIndexSparseDIDsProperties:
    """Properties for XMRelationshipIndexSparseDIDs"""
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Flags = int(element.findtext("Flags", "0", namespaces=namespaces))


class XMRelationshipIndexDenseDIDsProperties:
    """Properties for XMRelationshipIndexDenseDIDs"""
    def __init__(self, element: ET.Element, namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        self.Records = int(element.findtext("Records", "0", namespaces=namespaces))
        self.TableName = element.findtext("TableName", "", namespaces=namespaces)
        self.Flags = int(element.findtext("Flags", "0", namespaces=namespaces))


# Main XMObject Class
class XMObject:
    def __init__(self, element: Optional[ET.Element], namespaces=None):
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
            
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
        properties_elem = element.find("Properties", namespaces=namespaces)
        self.properties = self._parse_properties(properties_elem, self.class_name, namespaces)
        
        # Parse Members
        members_elem = element.find("Members", namespaces=namespaces)
        self.members = []
        if members_elem is not None:
            self.members = [XMObjectMember(e, namespaces) for e in members_elem.findall("Member", namespaces=namespaces)]
        
        # Parse Collections
        collections_elem = element.find("Collections", namespaces=namespaces)
        self.collections = []
        if collections_elem is not None:
            self.collections = [XMObjectCollection(e, namespaces) for e in collections_elem.findall("Collection", namespaces=namespaces)]
        
        # Parse DataObjects
        data_objects_elem = element.find("DataObjects", namespaces=namespaces)
        self.data_objects = []
        if data_objects_elem is not None:
            self.data_objects = [XMObjectDataObject(e, namespaces) for e in data_objects_elem.findall("DataObject", namespaces=namespaces)]
    
    def _parse_properties(self, properties_elem: Optional[ET.Element], class_name: str, namespaces=None) -> Any:
        if properties_elem is None:
            return None
        
        if namespaces is None:
            namespaces = XMOBJECT_NAMESPACES
        
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
        # For now, don't pass namespaces to these until we update them
        if "XMRENoSplitCompressionInfo" in class_name or "XM123CompressionInfo" in class_name:
            return XMRENoSplitCompressionInfoProperties(properties_elem)
        if "XMRLECompressionInfo" in class_name and "Hybrid" not in class_name:
            return XMRLECompressionInfoProperties(properties_elem)
        if "SegmentEqualMapEx" in class_name:
            return XMSegmentMapProperties(properties_elem)
        
        properties_class = property_map.get(class_name)
        if properties_class:
            # Pass namespaces to classes that have been updated to support them
            updated_classes = {
                "XMSimpleTable", "XMMultiPartSegmentMap", "XMRawColumnPartitionDataObject", 
                "XMSegment1Map", "XMPartition", "XMRawColumn", "XMHierarchy", 
                "XMValueDataDictionary<XM_Long>", "XMValueDataDictionary<XM_Real>",
                "XMRelationshipIndexSparseDIDs", "XMRelationshipIndexDenseDIDs",
                "XMColumnStats", "XMColumnSegment", "XMColumnSegmentStats"
            }
            if class_name in updated_classes:
                return properties_class(properties_elem, namespaces)
            else:
                return properties_class(properties_elem)
        
        return None
    


# Document Root Parser
class XMObjectDocument:
    """Parser for .tbl.xml metadata files"""
    
    def __init__(self, xml_string: str):
        root = ET.fromstring(xml_string)
        self.root_object = XMObject(root, XMOBJECT_NAMESPACES)
    
    @classmethod
    def from_xml_string(cls, xml_string: str):
        return cls(xml_string)
    
    @classmethod
    def from_file(cls, file_path: str):
        tree = ET.parse(file_path)
        root = tree.getroot()
        instance = cls.__new__(cls)
        instance.root_object = XMObject(root, XMOBJECT_NAMESPACES)
        return instance
    
