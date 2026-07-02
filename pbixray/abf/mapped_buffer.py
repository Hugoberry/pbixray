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


class MappedFileWindow:
    """Read-only window ``[offset, offset+size)`` over an existing file.

    Used to view a STORED ``DataModel`` zip member in place inside the user's
    ``.pbix``/``.xlsx`` instead of copying it out, in two roles:

    - The ``read``/``seek``/``tell`` file interface lets the decompression
      paths treat it like the ``ZipExtFile`` they would otherwise stream from,
      but with free seeks (``ZipExtFile`` emulates them by re-reading the
      member). Reads go through positional ``os.pread`` where available, so
      the sequentially consumed bytes cache in the kernel instead of
      accumulating in this process's resident set — macOS in particular keeps
      every touched page of an mmap in RSS and ignores ``MADV_DONTNEED``.
    - Slicing (``[a:b]`` → ``bytes`` of just that range, the same contract as
      :class:`MappedBuffer`) serves an *uncompressed* member adopted as the
      decompressed model itself. The mmap behind it is created lazily on
      first slice, so pure streaming use never maps the file; touched pages
      are clean and evictable under memory pressure.

    Unlike :class:`MappedBuffer` the backing file is the user's own: closing
    releases the mapping and descriptor but never unlinks the file.
    """

    def __init__(self, path, offset, size):
        self._state = {'fd': os.open(path, os.O_RDONLY), 'mmap': None}
        self._offset = offset
        self._size = size
        self._pos = 0
        self._finalizer = weakref.finalize(self, _cleanup_window, self._state)

    def _ensure_mmap(self):
        if self._state['mmap'] is None:
            self._state['mmap'] = mmap.mmap(
                self._state['fd'], 0, access=mmap.ACCESS_READ
            )
        return self._state['mmap']

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        mm = self._ensure_mmap()
        if isinstance(item, slice):
            start, stop, step = item.indices(self._size)
            return mm[self._offset + start:self._offset + stop:step]
        if item < 0:
            item += self._size
        if not 0 <= item < self._size:
            raise IndexError("MappedFileWindow index out of range")
        return mm[self._offset + item]

    # ---- file-like interface (what the decompression paths consume) ----

    def read(self, n=-1):
        remaining = max(self._size - self._pos, 0)
        n = remaining if (n is None or n < 0) else min(n, remaining)
        if n == 0:
            return b''
        abs_pos = self._offset + self._pos
        if hasattr(os, 'pread'):
            data = os.pread(self._state['fd'], n, abs_pos)
        else:  # Windows: no pread; fall back to the mapping
            data = self._ensure_mmap()[abs_pos:abs_pos + n]
        self._pos += len(data)
        return data

    def seek(self, pos, whence=0):
        if whence == 0:
            new_pos = pos
        elif whence == 1:
            new_pos = self._pos + pos
        elif whence == 2:
            new_pos = self._size + pos
        else:
            raise ValueError(f"invalid whence: {whence}")
        if new_pos < 0:
            raise ValueError("negative seek position")
        self._pos = new_pos
        return self._pos

    def tell(self):
        return self._pos

    def close(self):
        """Release the mapping and file descriptor (the file itself is kept)."""
        self._finalizer()


def _cleanup_window(state):
    """Idempotent teardown for ``MappedFileWindow`` — no unlink."""
    try:
        if state['mmap'] is not None:
            state['mmap'].close()
    finally:
        os.close(state['fd'])
