import xml.etree.ElementTree as ET
from typing import List, Optional
from datetime import datetime

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

class Annotation:
    def __init__(self, element):
        if element is None:
            return
        self.Name = element.findtext("Name")
        self.Value = element.findtext("Value")

class DataSource:
    def __init__(self, element, namespaces=None):
        if element is None:
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
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]
        
        # DataSource-specific elements
        self.ManagedProvider = element.findtext("ManagedProvider", namespaces=namespaces)
        self.ConnectionString = element.findtext("ConnectionString", namespaces=namespaces)
        self.ConnectionStringSecurity = element.findtext("ConnectionStringSecurity", namespaces=namespaces)
        
        # Parse ImpersonationInfo
        impersonation_elem = element.find("ImpersonationInfo", namespaces=namespaces)
        self.ImpersonationInfo = ImpersonationInfo(impersonation_elem) if impersonation_elem is not None else None
        
        self.Isolation = element.findtext("Isolation", namespaces=namespaces)
        
        max_active = element.findtext("MaxActiveConnections", namespaces=namespaces)
        self.MaxActiveConnections = int(max_active) if max_active else 10
        
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

class DataSourceDefinition:
    def __init__(self, xml_string):
        self.namespaces = {
            '': 'http://schemas.microsoft.com/analysisservices/2003/engine',
            'eng': 'http://schemas.microsoft.com/analysisservices/2003/engine',
            'eng300': 'http://schemas.microsoft.com/analysisservices/2011/engine/300',
            'xsd': 'http://www.w3.org/2001/XMLSchema',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
        }
        
        root = ET.fromstring(xml_string)
        
        # Determine DataSource type based on xsi:type attribute
        ds_type = root.get("{http://www.w3.org/2001/XMLSchema-instance}type")
        
        if ds_type == "RelationalDataSource":
            self.DataSource = RelationalDataSource(root, self.namespaces)
        elif ds_type == "OlapDataSource":
            self.DataSource = OlapDataSource(root, self.namespaces)
        elif ds_type == "PushedDataSource":
            self.DataSource = PushedDataSource(root, self.namespaces)
        else:
            self.DataSource = DataSource(root, self.namespaces)
    
    @classmethod
    def from_xml_file(cls, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            xml_string = f.read()
        return cls(xml_string)
    
    @classmethod
    def from_xml_string(cls, xml_string):
        return cls(xml_string)