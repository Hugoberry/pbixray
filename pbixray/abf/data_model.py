from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union


class Container(Enum):
    PBIX = "pbix"
    XLSX = "xlsx"


@dataclass
class DataModel:
    file_log: list
    # bytes/bytearray for eagerly-loaded models, or a memoryview over an mmap for the
    # lazily-loaded STORED case (see DataModelLoader.__mmap_stored_entry).
    decompressed_data: Union[bytes, bytearray, memoryview]
    container: Container = Container.PBIX
    error_code: bool = False
    apply_compression: bool = False
    # Backing handles for the mmap-backed (lazy) path; None for eagerly-loaded models.
    mmap_obj: Optional[object] = field(default=None, repr=False)
    file_handle: Optional[object] = field(default=None, repr=False)

    def close(self):
        """Release the memory-map and file handle, if any.

        The memoryview must be released before the mmap is closed, otherwise CPython raises
        "cannot close exported pointers exist". Safe to call multiple times and on eagerly
        loaded models (where it is a no-op)."""
        if self.mmap_obj is None and self.file_handle is None:
            return
        if isinstance(self.decompressed_data, memoryview):
            self.decompressed_data.release()
        self.decompressed_data = b''
        if self.mmap_obj is not None:
            self.mmap_obj.close()
            self.mmap_obj = None
        if self.file_handle is not None:
            self.file_handle.close()
            self.file_handle = None
