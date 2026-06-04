from dataclasses import dataclass
from enum import Enum
from typing import Union

from .mapped_buffer import MappedBuffer


class Container(Enum):
    PBIX = "pbix"
    XLSX = "xlsx"


@dataclass
class DataModel:
    file_log: list
    # ``bytes``/``bytearray`` when loaded in RAM (default), or a slice-able
    # ``MappedBuffer`` over a temp file when the loader runs with ``on_disk=True``.
    decompressed_data: Union[bytes, bytearray, MappedBuffer]
    container: Container = Container.PBIX
    error_code: bool = False
    apply_compression: bool = False

    def close(self):
        """Release the backing buffer if it owns OS resources (mmap/temp file)."""
        buf = self.decompressed_data
        if isinstance(buf, MappedBuffer):
            buf.close()
