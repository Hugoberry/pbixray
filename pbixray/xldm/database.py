import xml.etree.ElementTree as ET
from typing import List, Optional

class Annotation:
    def __init__(self, element):
        self.Name = element.findtext("Name")
        self.Value = element.findtext("Value")

class DataSourceImpersonationInfo:
    def __init__(self, element, namespaces):
        self.ImpersonationMode = element.findtext("ImpersonationMode", namespaces=namespaces)
        self.Account = element.findtext("Account", namespaces=namespaces)
        self.Password = element.findtext("Password", namespaces=namespaces)

class Database:
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
        self.DataFileList = element.findtext("DataFileList", namespaces=namespaces)
        self.Description = element.findtext("Description", namespaces=namespaces)
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]
        
        self.LastProcessed = element.findtext("LastProcessed", namespaces=namespaces)
        self.AggregationPrefix = element.findtext("AggregationPrefix", namespaces=namespaces)
        self.Language = int(element.findtext("Language", namespaces=namespaces) or 0)
        self.Collation = element.findtext("Collation", namespaces=namespaces)
        
        # Namespace-specific elements
        self.DefaultCollationVersion = element.findtext("{http://schemas.microsoft.com/analysisservices/2012/engine/400}DefaultCollationVersion")
        if self.DefaultCollationVersion:
            self.DefaultCollationVersion = int(self.DefaultCollationVersion)
        
        self.Visible = element.findtext("Visible", namespaces=namespaces) == "true"
        self.MasterDataSourceID = element.findtext("MasterDataSourceID", namespaces=namespaces)
        self.ProcessingPriority = int(element.findtext("ProcessingPriority", namespaces=namespaces) or 0)
        
        self.StorageEngineUsed = element.findtext("{http://schemas.microsoft.com/analysisservices/2010/engine/200/200}StorageEngineUsed")
        self.CompatibilityLevel = element.findtext("{http://schemas.microsoft.com/analysisservices/2010/engine/200}CompatibilityLevel")
        if self.CompatibilityLevel:
            self.CompatibilityLevel = int(self.CompatibilityLevel)
        
        # Parse DataSourceImpersonationInfo
        impersonation_elem = element.find("DataSourceImpersonationInfo", namespaces=namespaces)
        self.DataSourceImpersonationInfo = DataSourceImpersonationInfo(impersonation_elem, namespaces) if impersonation_elem is not None else None
        
        self.DataVersion = int(element.findtext("DataVersion", namespaces=namespaces) or 0)

class ObjectDefinition:
    def __init__(self, element, namespaces):
        database_elem = element.find("Database", namespaces=namespaces)
        self.Database = Database(database_elem, namespaces) if database_elem is not None else None

class DatabaseXmlLoad:
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