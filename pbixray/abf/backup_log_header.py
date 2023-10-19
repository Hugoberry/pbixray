import xml.etree.ElementTree as ET

class BackupLogHeader:
    def __init__(self, xml_string):
        # header is always one page (4096 bytes) in size and padded with zeros between the last header element and the end of the page
        trimmed_xml_string = xml_string.decode('utf-16').rstrip('\x00')
        root = ET.fromstring(trimmed_xml_string)
        self.BackupRestoreSyncVersion = int(root.findtext("BackupRestoreSyncVersion"))
        self.Fault = root.findtext("Fault") == "true"
        self.faultcode = int(root.findtext("faultcode"))
        self.ErrorCode = root.findtext("ErrorCode") == "true"
        self.EncryptionFlag = root.findtext("EncryptionFlag") == "true"
        self.EncryptionKey = int(root.findtext("EncryptionKey"))
        self.ApplyCompression = root.findtext("ApplyCompression") == "true"
        self.m_cbOffsetHeader = int(root.findtext("m_cbOffsetHeader"))
        self.DataSize = int(root.findtext("DataSize"))
        self.Files = int(root.findtext("Files"))
        self.ObjectID = root.findtext("ObjectID")
        self.m_cbOffsetData = int(root.findtext("m_cbOffsetData"))

    @classmethod
    def from_xml_string(cls, xml_string):
        trimmed_xml_string = xml_string.decode('utf-16').rstrip('\x00')
        return cls(trimmed_xml_string)
