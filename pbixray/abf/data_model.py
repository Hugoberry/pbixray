from dataclasses import dataclass
from enum import Enum


class Container(Enum):
    PBIX = "pbix"
    XLSX = "xlsx"


@dataclass
class DataModel:
    file_log: list
    decompressed_data: bytes
    container: Container = Container.PBIX
    error_code: bool = False
    apply_compression: bool = False
