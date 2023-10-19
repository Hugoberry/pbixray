import xml.etree.ElementTree as ET

class VirtualDirectoryBackupFile:
    def __init__(self, element):
        self.Path = element.findtext("Path")
        self.Size = int(element.findtext("Size"))
        self.m_cbOffsetHeader = int(element.findtext("m_cbOffsetHeader"))
        self.Delete = element.findtext("Delete") == "true"
        self.CreatedTimestamp = int(element.findtext("CreatedTimestamp"))
        self.Access = int(element.findtext("Access"))
        self.LastWriteTime = int(element.findtext("LastWriteTime"))

class VirtualDirectory:
    def __init__(self, xml_string):
        root = ET.fromstring(xml_string)
        self.BackupFiles = [VirtualDirectoryBackupFile(e) for e in root.findall("BackupFile")]

    @classmethod
    def from_xml_string(cls, xml_string):
        return cls(xml_string)
