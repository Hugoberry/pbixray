import xml.etree.ElementTree as ET
from typing import List, Optional

class Annotation:
    def __init__(self, element):
        self.Name = element.findtext("Name")
        self.Value = element.findtext("Value")

class Command:
    def __init__(self, element, namespaces):
        self.Text = element.findtext("Text", namespaces=namespaces)
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]

class CalculationProperty:
    def __init__(self, element, namespaces):
        self.CalculationReference = element.findtext("CalculationReference", namespaces=namespaces)
        self.CalculationType = element.findtext("CalculationType", namespaces=namespaces)
        self.Description = element.findtext("Description", namespaces=namespaces)
        visible_text = element.findtext("Visible", namespaces=namespaces)
        self.Visible = visible_text == "true" if visible_text is not None else None
        self.FormatString = element.findtext("FormatString", namespaces=namespaces)
        self.ForeColor = element.findtext("ForeColor", namespaces=namespaces)
        self.BackColor = element.findtext("BackColor", namespaces=namespaces)
        self.FontName = element.findtext("FontName", namespaces=namespaces)
        self.FontSize = element.findtext("FontSize", namespaces=namespaces)
        self.FontFlags = element.findtext("FontFlags", namespaces=namespaces)
        self.NonEmptyBehavior = element.findtext("NonEmptyBehavior", namespaces=namespaces)
        self.AssociatedMeasureGroupID = element.findtext("AssociatedMeasureGroupID", namespaces=namespaces)
        self.DisplayFolder = element.findtext("DisplayFolder", namespaces=namespaces)
        self.Language = element.findtext("Language", namespaces=namespaces)
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]

class MdxScript:
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
        self.DefaultScript = element.findtext("DefaultScript", namespaces=namespaces) == "true"
        
        # Parse Commands
        commands_elem = element.find("Commands", namespaces=namespaces)
        self.Commands = []
        if commands_elem is not None:
            self.Commands = [Command(cmd, namespaces) for cmd in commands_elem.findall("Command", namespaces=namespaces)]
        
        # Parse CalculationProperties
        calc_props_elem = element.find("CalculationProperties", namespaces=namespaces)
        self.CalculationProperties = []
        if calc_props_elem is not None:
            self.CalculationProperties = [CalculationProperty(cp, namespaces) for cp in calc_props_elem.findall("CalculationProperty", namespaces=namespaces)]

class ParentObject:
    def __init__(self, element, namespaces):
        self.DatabaseID = element.findtext("DatabaseID", namespaces=namespaces)
        self.CubeID = element.findtext("CubeID", namespaces=namespaces)

class ObjectDefinition:
    def __init__(self, element, namespaces):
        mdx_script_elem = element.find("MdxScript", namespaces=namespaces)
        self.MdxScript = MdxScript(mdx_script_elem, namespaces) if mdx_script_elem is not None else None

class MdxScriptXmlLoad:
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