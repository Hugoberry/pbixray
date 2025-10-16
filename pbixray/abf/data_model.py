from dataclasses import dataclass

@dataclass
class DataModel:
    file_log: list
    decompressed_data: bytes
    file_type: str = "pbix"  # Can be "pbix" or "xlsx"
    error_code: bool = False
    apply_compression: bool = False
