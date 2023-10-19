# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ColumnDataDictionary(KaitaiStruct):

    class DictionaryTypes(Enum):
        xm_type_invalid = -1
        xm_type_long = 0
        xm_type_real = 1
        xm_type_string = 2
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.dictionary_type = KaitaiStream.resolve_enum(ColumnDataDictionary.DictionaryTypes, self._io.read_s4le())
        self.hash_information = ColumnDataDictionary.HashInfo(self._io, self, self._root)
        _on = self.dictionary_type
        if _on == ColumnDataDictionary.DictionaryTypes.xm_type_string:
            self.data = ColumnDataDictionary.StringData(self._io, self, self._root)
        elif _on == ColumnDataDictionary.DictionaryTypes.xm_type_long:
            self.data = ColumnDataDictionary.NumberData(self._io, self, self._root)
        elif _on == ColumnDataDictionary.DictionaryTypes.xm_type_real:
            self.data = ColumnDataDictionary.NumberData(self._io, self, self._root)

    class StringData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.page_layout_information = ColumnDataDictionary.PageLayout(self._io, self, self._root)
            self.dictionary_pages = ColumnDataDictionary.DictionaryPage(self._io, self, self._root)
            self.dictionary_record_handles_vector_info = ColumnDataDictionary.DictionaryRecordHandlesVector(self._io, self, self._root)


    class StringStoreSection(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.remaining_store_available = self._io.read_u8le()
            self.buffer_used_characters = self._io.read_u8le()
            self.allocation_size = self._io.read_u8le()
            self.uncompressed_character_buffer = (self._io.read_bytes(self.allocation_size)).decode(u"UTF-16LE")


    class HashInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash_elements = []
            for i in range(6):
                self.hash_elements.append(self._io.read_s4le())



    class VectorOfVectors(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.element_count = self._io.read_u8le()
            self.element_size = self._io.read_u4le()
            self.values = []
            for i in range(self.element_count):
                _on = self.data_type_id
                if _on == u"int32":
                    self.values.append(self._io.read_s4le())
                elif _on == u"int64":
                    self.values.append(self._io.read_s8le())
                elif _on == u"float64":
                    self.values.append(self._io.read_f8le())


        @property
        def is_int32(self):
            if hasattr(self, '_m_is_int32'):
                return self._m_is_int32

            self._m_is_int32 = self.element_size == 4
            return getattr(self, '_m_is_int32', None)

        @property
        def is_int64(self):
            if hasattr(self, '_m_is_int64'):
                return self._m_is_int64

            self._m_is_int64 =  ((self.element_size == 8) and (self._root.dictionary_type == ColumnDataDictionary.DictionaryTypes.xm_type_long)) 
            return getattr(self, '_m_is_int64', None)

        @property
        def is_float64(self):
            if hasattr(self, '_m_is_float64'):
                return self._m_is_float64

            self._m_is_float64 =  ((self.element_size == 8) and (self._root.dictionary_type == ColumnDataDictionary.DictionaryTypes.xm_type_real)) 
            return getattr(self, '_m_is_float64', None)

        @property
        def data_type_id(self):
            if hasattr(self, '_m_data_type_id'):
                return self._m_data_type_id

            self._m_data_type_id = (u"int32" if self.is_int32 else (u"int64" if self.is_int64 else u"float64"))
            return getattr(self, '_m_data_type_id', None)


    class PageLayout(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.store_string_count = self._io.read_s8le()
            self.f_store_compressed = self._io.read_s1()
            self.store_longest_string = self._io.read_s8le()
            self.store_page_count = self._io.read_s8le()


    class DictionaryPage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.page_mask = self._io.read_u8le()
            self.page_contains_nulls = self._io.read_u1()
            self.page_start_index = self._io.read_u8le()
            self.page_string_count = self._io.read_u8le()
            self.page_compressed = self._io.read_u1()
            self.string_store_begin_mark = self._io.read_u4le()
            self.string_store = ColumnDataDictionary.StringStoreSection(self._io, self, self._root)
            self.string_store_end_mark = self._io.read_u4le()


    class NumberData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vector_of_vectors_info = ColumnDataDictionary.VectorOfVectors(self._io, self, self._root)


    class DictionaryRecordHandlesVector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.element_count = self._io.read_u8le()
            self.element_size = self._io.read_u4le()
            self.vector_of_record_handle_structures = []
            for i in range(self.element_count):
                _on = self.element_size
                if _on == 4:
                    self.vector_of_record_handle_structures.append(self._io.read_u4le())
                elif _on == 8:
                    self.vector_of_record_handle_structures.append(self._io.read_u8le())




