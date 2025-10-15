import xml.etree.ElementTree as ET
from typing import List, Optional

from .common import Annotation, ProcessableObject, parse_int_or_default, find_text_with_namespace
from .namespaces import XmlDefinitionBase, ObjectDefinitionBase, STANDARD_NAMESPACES

class DataSourceImpersonationInfo:
    def __init__(self, element, namespaces):
        self.ImpersonationMode = element.findtext("ImpersonationMode", namespaces=namespaces)
        self.Account = element.findtext("Account", namespaces=namespaces)
        self.Password = element.findtext("Password", namespaces=namespaces)

class Database(ProcessableObject):
    def __init__(self, element, namespaces):
        super().__init__(element, namespaces)
        
        if element is None:
            self._init_database_empty()
            return
        
        # Database-specific fields
        self.DataFileList = element.findtext("DataFileList", namespaces=namespaces)
        self.AggregationPrefix = element.findtext("AggregationPrefix", namespaces=namespaces)
        
        # Namespace-specific elements
        default_collation = element.findtext("{http://schemas.microsoft.com/analysisservices/2012/engine/400}DefaultCollationVersion")
        self.DefaultCollationVersion = parse_int_or_default(default_collation, None)
        
        self.MasterDataSourceID = element.findtext("MasterDataSourceID", namespaces=namespaces)
        
        self.StorageEngineUsed = element.findtext("{http://schemas.microsoft.com/analysisservices/2010/engine/200/200}StorageEngineUsed")
        compatibility_level = element.findtext("{http://schemas.microsoft.com/analysisservices/2010/engine/200}CompatibilityLevel")
        self.CompatibilityLevel = parse_int_or_default(compatibility_level, None)
        
        # Parse DataSourceImpersonationInfo
        impersonation_elem = element.find("DataSourceImpersonationInfo", namespaces=namespaces)
        self.DataSourceImpersonationInfo = DataSourceImpersonationInfo(impersonation_elem, namespaces) if impersonation_elem is not None else None
        
        data_version = element.findtext("DataVersion", namespaces=namespaces)
        self.DataVersion = parse_int_or_default(data_version, 0)
    
    def _init_database_empty(self):
        """Initialize empty database-specific fields."""
        self.DataFileList = None
        self.AggregationPrefix = None
        self.DefaultCollationVersion = None
        self.MasterDataSourceID = None
        self.StorageEngineUsed = None
        self.CompatibilityLevel = None
        self.DataSourceImpersonationInfo = None
        self.DataVersion = 0

class ObjectDefinition(ObjectDefinitionBase):
    def __init__(self, element, namespaces):
        super().__init__(element, namespaces, "Database", Database)
    
    @property
    def Database(self):
        return self.object

class DatabaseXmlLoad(XmlDefinitionBase):
    def _parse_xml(self):
        # Parse ObjectDefinition and extract Database directly
        obj_def_elem = self.root.find("ObjectDefinition", namespaces=self.namespaces)
        if obj_def_elem is not None:
            database_elem = obj_def_elem.find("Database", namespaces=self.namespaces)
            self.Database = Database(database_elem, self.namespaces) if database_elem is not None else None
        else:
            self.Database = None