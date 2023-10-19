# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ColumnDataHidx(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.hash_algorithm = self._io.read_s4le()
        self.hash_entry_size = self._io.read_u4le()
        self.hash_bin_size = self._io.read_u4le()
        self.local_entry_count = self._io.read_u4le()
        self.c_bins = self._io.read_u8le()
        self.number_of_records = self._io.read_s8le()
        self.current_mask = self._io.read_s8le()
        self.hash_stats = self._io.read_u1()
        if self.hash_stats != 0:
            self.hash_statistics = ColumnDataHidx.HashStatisticsType(self._io, self, self._root)

        self._raw_hash_bin_entries = []
        self.hash_bin_entries = []
        for i in range(self.c_bins):
            self._raw_hash_bin_entries.append(self._io.read_bytes(self.hash_bin_size))
            _io__raw_hash_bin_entries = KaitaiStream(BytesIO(self._raw_hash_bin_entries[i]))
            self.hash_bin_entries.append(ColumnDataHidx.HashBin(_io__raw_hash_bin_entries, self, self._root))

        self.overflow_hash_entries_count = self._io.read_u8le()
        self.overflow_hash_entries = []
        for i in range(self.overflow_hash_entries_count):
            self.overflow_hash_entries.append(ColumnDataHidx.HashEntry(self._io, self, self._root))


    class HashStatisticsType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.number_of_elements = self._io.read_u8le()
            self.number_of_bins = self._io.read_u8le()
            self.number_of_used_bins = self._io.read_u8le()
            self.fast_access_elements = self._io.read_u8le()
            self.locals_size_per_bin = self._io.read_u8le()
            self.maximum_chain = self._io.read_u8le()
            self.element_count = self._io.read_u8le()
            self.element_size = self._io.read_u4le()
            self.histogram_vector = []
            for i in range(self.element_count):
                _on = self.element_size
                if _on == 4:
                    self.histogram_vector.append(self._io.read_u4le())
                elif _on == 8:
                    self.histogram_vector.append(self._io.read_u8le())



    class HashBin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.m_rg_chain = self._io.read_u8le()
            self.m_count = self._io.read_u4le()
            self.m_rg_local_entries = []
            for i in range(self._root.local_entry_count):
                self.m_rg_local_entries.append(ColumnDataHidx.HashEntry(self._io, self, self._root))

            self.padding = self._io.read_u4le()


    class HashEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.m_hash = self._io.read_u4le()
            self.m_key = self._io.read_u4le()



