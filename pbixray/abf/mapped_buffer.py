import mmap
import os
import weakref


class MappedBuffer:
    """Read-only, slice-able view over a temp file holding the decompressed ABF.

    Used by :class:`~pbixray.loader.DataModelLoader` when ``on_disk=True`` so the
    fully decompressed data model never has to live in a single in-process
    ``bytearray``. Slicing returns ``bytes`` (a copy of just the requested range),
    so every existing consumer — ``AbfParser`` and ``get_data_slice`` — keeps
    working unchanged while only the touched pages are faulted in by the OS.

    The temp file is unlinked and the mapping closed either explicitly via
    :meth:`close` (e.g. ``PBIXRay.close()`` / context-manager exit) or by the
    ``weakref.finalize`` backstop when the object is garbage collected.
    """

    def __init__(self, path):
        self._path = path
        self._fd = os.open(path, os.O_RDONLY)
        try:
            self._mmap = mmap.mmap(self._fd, 0, access=mmap.ACCESS_READ)
        except ValueError:
            # Empty file: mmap of length 0 is invalid. Fall back to empty bytes
            # while still cleaning up the fd and temp file.
            os.close(self._fd)
            self._fd = None
            self._mmap = b''
        self._finalizer = weakref.finalize(
            self, _cleanup, self._mmap, self._fd, path
        )

    def __getitem__(self, item):
        return self._mmap[item]

    def __len__(self):
        return len(self._mmap)

    def close(self):
        """Close the mapping, the file descriptor, and unlink the temp file."""
        self._finalizer()


def _cleanup(mm, fd, path):
    """Idempotent teardown shared by ``close()`` and the weakref finalizer."""
    try:
        if hasattr(mm, 'close'):
            mm.close()
    finally:
        try:
            if fd is not None:
                os.close(fd)
        finally:
            try:
                os.unlink(path)
            except OSError:
                pass
