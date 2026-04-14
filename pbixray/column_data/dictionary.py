# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class ColumnDataDictionary(KaitaiStruct):
    """
    .. seealso::
       Source - https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-xldm/d6de072d-5234-4099-b090-528322f829dc
    """

    class DictionaryTypes(IntEnum):
        xm_type_invalid = -1
        xm_type_long = 0
        xm_type_real = 1
        xm_type_string = 2
    def __init__(self, _io, _parent=None, _root=None):
        super(ColumnDataDictionary, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.dictionary_type = KaitaiStream.resolve_enum(ColumnDataDictionary.DictionaryTypes, self._io.read_s4le())
        self.hash_information = ColumnDataDictionary.HashInfo(self._io, self, self._root)
        _on = self.dictionary_type
        if _on == ColumnDataDictionary.DictionaryTypes.xm_type_long:
            pass
            self.data = ColumnDataDictionary.NumberData(self._io, self, self._root)
        elif _on == ColumnDataDictionary.DictionaryTypes.xm_type_real:
            pass
            self.data = ColumnDataDictionary.NumberData(self._io, self, self._root)
        elif _on == ColumnDataDictionary.DictionaryTypes.xm_type_string:
            pass
            self.data = ColumnDataDictionary.StringData(self._io, self, self._root)


    def _fetch_instances(self):
        pass
        self.hash_information._fetch_instances()
        _on = self.dictionary_type
        if _on == ColumnDataDictionary.DictionaryTypes.xm_type_long:
            pass
            self.data._fetch_instances()
        elif _on == ColumnDataDictionary.DictionaryTypes.xm_type_real:
            pass
            self.data._fetch_instances()
        elif _on == ColumnDataDictionary.DictionaryTypes.xm_type_string:
            pass
            self.data._fetch_instances()

    class CompressedStrings(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.CompressedStrings, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.store_total_bits = self._io.read_u4le()
            self.character_set_type_identifier = self._io.read_u4le()
            self.len_compressed_string_buffer = self._io.read_u8le()
            if self.character_set_type_identifier == 703121:
                pass
                self.character_set_used = self._io.read_u1()

            self.ui_decode_bits = self._io.read_u4le()
            self.encode_array = []
            for i in range(128):
                self.encode_array.append(self._io.read_u1())

            self.ui64_buffer_size = self._io.read_u8le()
            self.compressed_string_buffer = self._io.read_bytes(self.len_compressed_string_buffer)


        def _fetch_instances(self):
            pass
            if self.character_set_type_identifier == 703121:
                pass

            for i in range(len(self.encode_array)):
                pass



    class DictionaryPage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.DictionaryPage, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.page_mask = self._io.read_u8le()
            self.page_contains_nulls = self._io.read_u1()
            self.page_start_index = self._io.read_u8le()
            self.page_string_count = self._io.read_u8le()
            self.page_compressed = self._io.read_u1()
            self.string_store_begin_mark = self._io.read_bytes(4)
            if not self.string_store_begin_mark == b"\xDD\xCC\xBB\xAA":
                raise kaitaistruct.ValidationNotEqualError(b"\xDD\xCC\xBB\xAA", self.string_store_begin_mark, self._io, u"/types/dictionary_page/seq/5")
            _on = self.page_compressed
            if _on == 0:
                pass
                self.string_store = ColumnDataDictionary.UncompressedStrings(self._io, self, self._root)
            elif _on == 1:
                pass
                self.string_store = ColumnDataDictionary.CompressedStrings(self._io, self, self._root)
            self.string_store_end_mark = self._io.read_bytes(4)
            if not self.string_store_end_mark == b"\xCD\xAB\xCD\xAB":
                raise kaitaistruct.ValidationNotEqualError(b"\xCD\xAB\xCD\xAB", self.string_store_end_mark, self._io, u"/types/dictionary_page/seq/7")


        def _fetch_instances(self):
            pass
            _on = self.page_compressed
            if _on == 0:
                pass
                self.string_store._fetch_instances()
            elif _on == 1:
                pass
                self.string_store._fetch_instances()


    class DictionaryRecordHandlesVector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.DictionaryRecordHandlesVector, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.num_vector_of_record_handle_structures = self._io.read_u8le()
            self.element_size = self._io.read_bytes(4)
            if not self.element_size == b"\x08\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x08\x00\x00\x00", self.element_size, self._io, u"/types/dictionary_record_handles_vector/seq/1")
            self.vector_of_record_handle_structures = []
            for i in range(self.num_vector_of_record_handle_structures):
                self.vector_of_record_handle_structures.append(ColumnDataDictionary.StringRecordHandle(self._io, self, self._root))



        def _fetch_instances(self):
            pass
            for i in range(len(self.vector_of_record_handle_structures)):
                pass
                self.vector_of_record_handle_structures[i]._fetch_instances()



    class HashInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.HashInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.hash_elements = []
            for i in range(6):
                self.hash_elements.append(self._io.read_s4le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.hash_elements)):
                pass



    class NumberData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.NumberData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.vector_of_vectors_info = ColumnDataDictionary.VectorOfVectors(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.vector_of_vectors_info._fetch_instances()


    class OtherRecordHandle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.OtherRecordHandle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bit_or_byte_offset = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class PageLayout(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.PageLayout, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.store_string_count = self._io.read_s8le()
            self.f_store_compressed = self._io.read_s1()
            self.store_longest_string = self._io.read_s8le()
            self.store_page_count = self._io.read_s8le()


        def _fetch_instances(self):
            pass


    class StringData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.StringData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.page_layout_information = ColumnDataDictionary.PageLayout(self._io, self, self._root)
            self.dictionary_pages = []
            for i in range(self.page_layout_information.store_page_count):
                self.dictionary_pages.append(ColumnDataDictionary.DictionaryPage(self._io, self, self._root))

            self.dictionary_record_handles_vector_info = ColumnDataDictionary.DictionaryRecordHandlesVector(self._io, self, self._root)


        def _fetch_instances(self):
            pass
            self.page_layout_information._fetch_instances()
            for i in range(len(self.dictionary_pages)):
                pass
                self.dictionary_pages[i]._fetch_instances()

            self.dictionary_record_handles_vector_info._fetch_instances()


    class StringRecordHandle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.StringRecordHandle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bit_or_byte_offset = self._io.read_u4le()
            self.page_id = self._io.read_u4le()


        def _fetch_instances(self):
            pass


    class UncompressedStrings(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.UncompressedStrings, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.remaining_store_available = self._io.read_u8le()
            self.buffer_used_characters = self._io.read_u8le()
            self.allocation_size = self._io.read_u8le()
            self.uncompressed_character_buffer = (self._io.read_bytes(self.allocation_size)).decode(u"UTF-16LE")


        def _fetch_instances(self):
            pass


    class VectorOfVectors(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataDictionary.VectorOfVectors, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.num_values = self._io.read_u8le()
            self.element_size = self._io.read_u4le()
            self.values = []
            for i in range(self.num_values):
                _on = self.data_type_id
                if _on == u"float64":
                    pass
                    self.values.append(self._io.read_f8le())
                elif _on == u"int32":
                    pass
                    self.values.append(self._io.read_s4le())
                elif _on == u"int64":
                    pass
                    self.values.append(self._io.read_s8le())



        def _fetch_instances(self):
            pass
            for i in range(len(self.values)):
                pass
                _on = self.data_type_id
                if _on == u"float64":
                    pass
                elif _on == u"int32":
                    pass
                elif _on == u"int64":
                    pass


        @property
        def data_type_id(self):
            if hasattr(self, '_m_data_type_id'):
                return self._m_data_type_id

            self._m_data_type_id = (u"int32" if self.is_int32 else (u"int64" if self.is_int64 else u"float64"))
            return getattr(self, '_m_data_type_id', None)

        @property
        def is_float64(self):
            if hasattr(self, '_m_is_float64'):
                return self._m_is_float64

            self._m_is_float64 =  ((self.element_size == 8) and (self._root.dictionary_type == ColumnDataDictionary.DictionaryTypes.xm_type_real)) 
            return getattr(self, '_m_is_float64', None)

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



