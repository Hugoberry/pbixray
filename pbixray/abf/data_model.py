from dataclasses import dataclass

@dataclass
class DataModel:
    file_log: list
    decompressed_data: bytes
    error_code: bool = False
