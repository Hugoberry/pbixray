from dataclasses import dataclass
from enum import Enum
from typing import Union

from .mapped_buffer import MappedBuffer, MappedFileWindow


class Container(Enum):
    PBIX = "pbix"
    XLSX = "xlsx"


@dataclass
class DataModel:
    file_log: list
    # ``bytes``/``bytearray`` when loaded in RAM (default). With ``on_disk=True``
    # it is a slice-able ``MappedBuffer`` over a temp file, or a
    # ``MappedFileWindow`` viewing an uncompressed member in place inside the
    # user's own .pbix/.xlsx.
    decompressed_data: Union[bytes, bytearray, MappedBuffer, MappedFileWindow]
    container: Container = Container.PBIX
    error_code: bool = False
    apply_compression: bool = False

    def close(self):
        """Release the backing buffer if it owns OS resources (mmap/temp file)."""
        buf = self.decompressed_data
        if isinstance(buf, (MappedBuffer, MappedFileWindow)):
            buf.close()
