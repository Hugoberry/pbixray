import xml.etree.ElementTree as ET
from .backup_log import BackupLog
from .backup_log_header import BackupLogHeader
from .virtual_directory import VirtualDirectory

class AbfParser:
    def __init__(self, decompressed_buffer):
        self.__buffer = decompressed_buffer
        self.__backup_log_header = None
        self.__virtual_directory = None
        self.__backup_log = None
        self.file_log = None  # public attribute

        # Trigger the parsing process upon initialization
        self.__parse_all()

    def __parse_all(self):
        self.__parse_backup_log_header()
        self.__parse_virtual_directory()
        self.__parse_backup_log()
        self.__match_logs_and_get_attributes()

    def __parse_backup_log_header(self):
        offset = 72 # STREAM_STORAGE_SIGNATURE_)!@#$%^&*(
        page = 0x1000 # header is always one page (4096 bytes) in size
        self.__backup_log_header = BackupLogHeader(self.__buffer[offset:page])

    def __parse_virtual_directory(self):
        offset = int(self.__backup_log_header.m_cbOffsetHeader)
        size = int(self.__backup_log_header.DataSize)
        self.__virtual_directory = VirtualDirectory(self.__buffer[offset: offset+size])

    def __parse_backup_log(self):
        log = self.__virtual_directory.BackupFiles[-1]
        offset = int(log.m_cbOffsetHeader)
        size = int(log.Size)
        self.__backup_log = BackupLog(self.__buffer[offset:offset+size], self.__backup_log_header.ErrorCode)

    def __match_logs_and_get_attributes(self):
        persist_root = self.__backup_log.FileGroups[1].PersistLocationPath + '\\'
        virtual_directory_files_by_path = {file.Path: file for file in self.__virtual_directory.BackupFiles}
        matched_data = []

        for file_group in self.__backup_log.FileGroups:
            for backup_file in file_group.FileList:
                if backup_file.StoragePath in virtual_directory_files_by_path:
                    matched_file = virtual_directory_files_by_path[backup_file.StoragePath]
                    if backup_file.Path.startswith(persist_root):
                        path_without_persist_root = backup_file.Path.replace(persist_root, '', 1)
                    else:
                        path_without_persist_root = backup_file.Path
                    matched_data.append({
                        'Path': path_without_persist_root,
                        'StoragePath': backup_file.StoragePath,
                        'Size': matched_file.Size,
                        'm_cbOffsetHeader': matched_file.m_cbOffsetHeader
                    })

        self.file_log = matched_data
