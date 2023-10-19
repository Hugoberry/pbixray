import xml.etree.ElementTree as ET
from .backup_log import BackupLog
from .backup_log_header import BackupLogHeader
from .virtual_directory import VirtualDirectory

class AbfParser:
    def __init__(self):
        pass

    def parse_backup_log_header(self, buffer):
        offset = 72 # STREAM_STORAGE_SIGNATURE_)!@#$%^&*(
        page = 0x1000 # header is always one page (4096 bytes) in size
        return BackupLogHeader(buffer[offset:page])

    def parse_virtual_directory(self, buffer, header):
        offset = int(header.m_cbOffsetHeader)
        size = int(header.DataSize)
        return VirtualDirectory(buffer[offset: offset+size])

    def parse_backup_log(self, buffer, virtual_directory):
        log = virtual_directory.BackupFiles[-1]
        offset = int(log.m_cbOffsetHeader)
        size = int(log.Size)
        return BackupLog(buffer[offset:offset+size])

    def get_sqlite_buffer(self, buffer, virtual_directory):
        sqlite = virtual_directory.BackupFiles[-2]
        offset = int(sqlite.m_cbOffsetHeader)
        size = int(sqlite.Size)
        return buffer[offset:offset+size]
    
    def match_logs_and_get_attributes(self, backup_log, virtual_directory):
        # Create a dictionary for quick lookup of VirtualDirectoryBackupFiles based on Path
        virtual_directory_files_by_path = {file.Path: file for file in virtual_directory.BackupFiles}

        matched_data = []

        # For each BackupFile in BackupLog, check if it matches with any VirtualDirectoryBackupFile
        for file_group in backup_log.FileGroups:
            for backup_file in file_group.FileList:
                if backup_file.StoragePath in virtual_directory_files_by_path:
                    matched_file = virtual_directory_files_by_path[backup_file.StoragePath]
                    matched_data.append({
                        'Path': backup_file.Path,
                        'StoragePath': backup_file.StoragePath,
                        'Size': matched_file.Size,
                        'm_cbOffsetHeader': matched_file.m_cbOffsetHeader
                    })

        return matched_data


    def process_data(self, decompressed_buffer):
        backup_log_header = self.parse_backup_log_header(decompressed_buffer)
        virtual_directory = self.parse_virtual_directory(decompressed_buffer, backup_log_header)
        backup_log = self.parse_backup_log(decompressed_buffer, virtual_directory)
        sqlite_buffer = self.get_sqlite_buffer(decompressed_buffer, virtual_directory)
        file_log = self.match_logs_and_get_attributes(backup_log, virtual_directory)

        return virtual_directory, backup_log, sqlite_buffer, file_log
