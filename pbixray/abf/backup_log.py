import xml.etree.ElementTree as ET

class BackupLog:
    def __init__(self, xml_string, error_code):
        #if error_code trim last 4 bytes
        if error_code:
            xml_string = xml_string[:-4]
        trimmed_xml_string = xml_string.decode('utf-16')
        root = ET.fromstring(trimmed_xml_string)
        self.BackupRestoreSyncVersion = root.findtext("BackupRestoreSyncVersion")
        self.ServerRoot = root.findtext("ServerRoot")
        self.SvrEncryptPwdFlag = root.findtext("SvrEncryptPwdFlag") == "true"
        self.ServerEnableBinaryXML = root.findtext("ServerEnableBinaryXML") == "true"
        self.ServerEnableCompression = root.findtext("ServerEnableCompression") == "true"
        self.CompressionFlag = root.findtext("CompressionFlag") == "true"
        self.EncryptionFlag = root.findtext("EncryptionFlag") == "true"
        self.ObjectName = root.findtext("ObjectName")
        self.ObjectId = root.findtext("ObjectId")
        self.Write = root.findtext("Write")
        self.OlapInfo = root.findtext("OlapInfo") == "true"
        self.Collations = [collation.text for collation in root.findall("Collations/Collation")]
        self.Languages = [int(lang.text) for lang in root.findall("Languages/Language")]
        self.FileGroups = [FileGroup.from_xml(filegroup) for filegroup in root.findall("FileGroups/FileGroup")]

class FileGroup:
    @classmethod
    def from_xml(cls, element):
        fileGroup = cls()
        fileGroup.Class = int(element.findtext("Class"))
        fileGroup.ID = element.findtext("ID")
        fileGroup.Name = element.findtext("Name")
        fileGroup.ObjectVersion = int(element.findtext("ObjectVersion"))
        fileGroup.PersistLocation = int(element.findtext("PersistLocation"))
        fileGroup.PersistLocationPath = element.findtext("PersistLocationPath")
        fileGroup.StorageLocationPath = element.findtext("StorageLocationPath")
        fileGroup.ObjectID = element.findtext("ObjectID")
        fileGroup.FileList = [BackupFile.from_xml(backupfile) for backupfile in element.findall("FileList/BackupFile")]
        return fileGroup

class BackupFile:
    @classmethod
    def from_xml(cls, element):
        backupFile = cls()
        backupFile.Path = element.findtext("Path")
        backupFile.StoragePath = element.findtext("StoragePath")
        backupFile.LastWriteTime = int(element.findtext("LastWriteTime"))
        backupFile.Size = int(element.findtext("Size"))
        return backupFile
