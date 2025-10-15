import xml.etree.ElementTree as ET
from typing import List, Optional
from datetime import datetime

from .common import Annotation, MajorObject, parse_int_or_default
from .namespaces import XmlDefinitionBase, SIMPLE_NAMESPACES

class ImpersonationInfo:
    def __init__(self, element):
        if element is None:
            return
        self.ImpersonationMode = element.findtext("ImpersonationMode")
        self.Account = element.findtext("Account")
        self.Password = element.findtext("Password")
        self.ImpersonationInfoSecurity = element.findtext("ImpersonationInfoSecurity")

class DataSourcePermission:
    def __init__(self, element):
        if element is None:
            return
        self.Name = element.findtext("Name")
        self.ID = element.findtext("ID")
        self.CreatedTimestamp = element.findtext("CreatedTimestamp")
        self.LastSchemaUpdate = element.findtext("LastSchemaUpdate")
        self.Description = element.findtext("Description")
        self.RoleID = element.findtext("RoleID")
        self.Process = element.findtext("Process") == "true"
        self.Read = element.findtext("Read")
        self.Write = element.findtext("Write")

class DataSource(MajorObject):
    def __init__(self, element, namespaces=None):
        super().__init__(element, namespaces)
        
        if element is None:
            self._init_datasource_empty()
            return
        
        if namespaces is None:
            namespaces = {}
        
        # DataSource-specific elements
        self.ManagedProvider = element.findtext("ManagedProvider", namespaces=namespaces)
        self.ConnectionString = element.findtext("ConnectionString", namespaces=namespaces)
        self.ConnectionStringSecurity = element.findtext("ConnectionStringSecurity", namespaces=namespaces)
        
        # Parse ImpersonationInfo
        impersonation_elem = element.find("ImpersonationInfo", namespaces=namespaces)
        self.ImpersonationInfo = ImpersonationInfo(impersonation_elem) if impersonation_elem is not None else None
        
        self.Isolation = element.findtext("Isolation", namespaces=namespaces)
        
        max_active = element.findtext("MaxActiveConnections", namespaces=namespaces)
        self.MaxActiveConnections = parse_int_or_default(max_active, 10)
        
        self.Timeout = element.findtext("Timeout", namespaces=namespaces)
        
        # Parse DataSourcePermissions
        permissions_elem = element.find("DataSourcePermissions", namespaces=namespaces)
        self.DataSourcePermissions = []
        if permissions_elem is not None:
            self.DataSourcePermissions = [DataSourcePermission(perm) for perm in permissions_elem.findall("DataSourcePermission", namespaces=namespaces)]
        
        # eng300 namespace elements
        self.QueryImpersonationInfo = None
        query_imp_elem = element.find("{http://schemas.microsoft.com/analysisservices/2011/engine/300}QueryImpersonationInfo")
        if query_imp_elem is not None:
            self.QueryImpersonationInfo = ImpersonationInfo(query_imp_elem)
        
        self.QueryHints = element.findtext("{http://schemas.microsoft.com/analysisservices/2011/engine/300}QueryHints")
    
    def _init_datasource_empty(self):
        """Initialize empty datasource-specific fields."""
        self.ManagedProvider = None
        self.ConnectionString = None
        self.ConnectionStringSecurity = None
        self.ImpersonationInfo = None
        self.Isolation = None
        self.MaxActiveConnections = 10
        self.Timeout = None
        self.DataSourcePermissions = []
        self.QueryImpersonationInfo = None
        self.QueryHints = None

class RelationalDataSource(DataSource):
    def __init__(self, element, namespaces=None):
        super().__init__(element, namespaces)

class OlapDataSource(DataSource):
    def __init__(self, element, namespaces=None):
        super().__init__(element, namespaces)
        
        if namespaces is None:
            namespaces = {}
        
        # OlapDataSource-specific elements
        self.Catalog = element.findtext("Catalog", namespaces=namespaces)

class PushedDataSource(DataSource):
    def __init__(self, element, namespaces=None):
        super().__init__(element, namespaces)
        
        if namespaces is None:
            namespaces = {}
        
        # PushedDataSource-specific elements
        self.RootMoniker = element.findtext("RootMoniker", namespaces=namespaces)

class DataSourceDefinition(XmlDefinitionBase):
    def __init__(self, xml_string):
        super().__init__(xml_string, SIMPLE_NAMESPACES)
    
    def _parse_xml(self):
        # Determine DataSource type based on xsi:type attribute
        ds_type = self.root.get("{http://www.w3.org/2001/XMLSchema-instance}type")
        
        if ds_type == "RelationalDataSource":
            self.DataSource = RelationalDataSource(self.root, self.namespaces)
        elif ds_type == "OlapDataSource":
            self.DataSource = OlapDataSource(self.root, self.namespaces)
        elif ds_type == "PushedDataSource":
            self.DataSource = PushedDataSource(self.root, self.namespaces)
        else:
            self.DataSource = DataSource(self.root, self.namespaces)