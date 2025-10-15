import xml.etree.ElementTree as ET
from typing import List, Optional

from .common import Annotation, ProcessableObject, parse_int_or_default
from .namespaces import XmlDefinitionBase, ObjectDefinitionBase, STANDARD_NAMESPACES

class Command:
    def __init__(self, element, namespaces):
        self.Text = element.findtext("Text", namespaces=namespaces)
        
        # Parse Annotations
        annotations_elem = element.find("Annotations", namespaces=namespaces)
        self.Annotations = []
        if annotations_elem is not None:
            self.Annotations = [Annotation(ann, namespaces) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]

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
            self.Annotations = [Annotation(ann, namespaces) for ann in annotations_elem.findall("Annotation", namespaces=namespaces)]

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

class MdxScriptXmlLoad(XmlDefinitionBase):
    def _parse_xml(self):
        # Parse ParentObject
        parent_obj_elem = self.root.find("ParentObject", namespaces=self.namespaces)
        self.ParentObject = ParentObject(parent_obj_elem, self.namespaces) if parent_obj_elem is not None else None
        
        # Parse ObjectDefinition and extract MdxScript directly
        obj_def_elem = self.root.find("ObjectDefinition", namespaces=self.namespaces)
        if obj_def_elem is not None:
            mdx_script_elem = obj_def_elem.find("MdxScript", namespaces=self.namespaces)
            self.MdxScript = MdxScript(mdx_script_elem, self.namespaces) if mdx_script_elem is not None else None
        else:
            self.MdxScript = None
