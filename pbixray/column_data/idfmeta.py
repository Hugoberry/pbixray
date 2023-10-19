# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class IdfmetaParser(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.blocks = IdfmetaParser.Block(self._io, self, self._root)

    class CPElement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cp_tag = self._io.read_bytes(6)
            if not self.cp_tag == b"\x3C\x31\x3A\x43\x50\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x50\x00", self.cp_tag, self._io, u"/types/c_p_element/seq/0")
            self.version_one = self._io.read_u8le()
            self.cs = IdfmetaParser.CS0Element(self._io, self, self._root)
            self.cp_tag_end = self._io.read_bytes(6)
            if not self.cp_tag_end == b"\x43\x50\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x50\x3A\x31\x3E\x00", self.cp_tag_end, self._io, u"/types/c_p_element/seq/3")


    class CS1Element(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cs_tag = self._io.read_bytes(6)
            if not self.cs_tag == b"\x3C\x31\x3A\x43\x53\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x53\x00", self.cs_tag, self._io, u"/types/c_s1_element/seq/0")
            self.count_bit_packed = self._io.read_u8le()
            self.blob_with9_zeros = self._io.read_bytes(9)
            self.cs_tag_end = self._io.read_bytes(6)
            if not self.cs_tag_end == b"\x43\x53\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x53\x3A\x31\x3E\x00", self.cs_tag_end, self._io, u"/types/c_s1_element/seq/3")


    class CS0Element(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cs_tag = self._io.read_bytes(6)
            if not self.cs_tag == b"\x3C\x31\x3A\x43\x53\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x53\x00", self.cs_tag, self._io, u"/types/c_s0_element/seq/0")
            self.records = self._io.read_u8le()
            self.one = self._io.read_u8le()
            self.a_b_a_5_a = self._io.read_u4le()
            self.iterator = self._io.read_u4le()
            self.bookmark_bits_1_2_8 = self._io.read_u8le()
            self.storage_alloc_size = self._io.read_u8le()
            self.storage_used_size = self._io.read_u8le()
            self.segment_needs_resizing = self._io.read_u1()
            self.compression_info = self._io.read_u4le()
            self.ss = IdfmetaParser.SSElement(self._io, self, self._root)
            self.has_bit_packed_sub_seg = self._io.read_u1()
            self.cs = IdfmetaParser.CS1Element(self._io, self, self._root)
            self.cs_tag_end = self._io.read_bytes(6)
            if not self.cs_tag_end == b"\x43\x53\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x53\x3A\x31\x3E\x00", self.cs_tag_end, self._io, u"/types/c_s0_element/seq/13")


    class SDOsElement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sdos_tag = self._io.read_bytes(8)
            if not self.sdos_tag == b"\x3C\x31\x3A\x53\x44\x4F\x73\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x53\x44\x4F\x73\x00", self.sdos_tag, self._io, u"/types/s_d_os_element/seq/0")
            self.csdos = IdfmetaParser.CSDOsElement(self._io, self, self._root)
            self.sdos_tag_end = self._io.read_bytes(8)
            if not self.sdos_tag_end == b"\x53\x44\x4F\x73\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x44\x4F\x73\x3A\x31\x3E\x00", self.sdos_tag_end, self._io, u"/types/s_d_os_element/seq/2")


    class SSElement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ss_tag = self._io.read_bytes(6)
            if not self.ss_tag == b"\x3C\x31\x3A\x53\x53\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x53\x53\x00", self.ss_tag, self._io, u"/types/s_s_element/seq/0")
            self.distinct_states = self._io.read_u8le()
            self.min_data_id = self._io.read_u4le()
            self.max_data_id = self._io.read_u4le()
            self.original_min_segment_data_id = self._io.read_u4le()
            self.r_l_e_sort_order = self._io.read_s8le()
            self.row_count = self._io.read_u8le()
            self.has_nulls = self._io.read_u1()
            self.r_l_e_runs = self._io.read_u8le()
            self.others_r_l_e_runs = self._io.read_u8le()
            self.ss_tag_end = self._io.read_bytes(6)
            if not self.ss_tag_end == b"\x53\x53\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x53\x3A\x31\x3E\x00", self.ss_tag_end, self._io, u"/types/s_s_element/seq/10")


    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cp = IdfmetaParser.CPElement(self._io, self, self._root)
            self.sdos = IdfmetaParser.SDOsElement(self._io, self, self._root)


    class CSDOs1Element(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.csdos_tag = self._io.read_bytes(9)
            if not self.csdos_tag == b"\x3C\x31\x3A\x43\x53\x44\x4F\x73\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x53\x44\x4F\x73\x00", self.csdos_tag, self._io, u"/types/c_s_d_os1_element/seq/0")
            self.sub_segment_offset = self._io.read_u8le()
            self.sub_segment_size = self._io.read_u8le()
            self.csdos_tag_end = self._io.read_bytes(9)
            if not self.csdos_tag_end == b"\x43\x53\x44\x4F\x73\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x53\x44\x4F\x73\x3A\x31\x3E\x00", self.csdos_tag_end, self._io, u"/types/c_s_d_os1_element/seq/3")


    class CSDOsElement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.csdos_tag = self._io.read_bytes(9)
            if not self.csdos_tag == b"\x3C\x31\x3A\x43\x53\x44\x4F\x73\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x53\x44\x4F\x73\x00", self.csdos_tag, self._io, u"/types/c_s_d_os_element/seq/0")
            self.zero_c_s_d_o = self._io.read_u8le()
            self.primary_segment_size = self._io.read_u8le()
            self.csdos = IdfmetaParser.CSDOs1Element(self._io, self, self._root)
            self.csdos_tag_end = self._io.read_bytes(9)
            if not self.csdos_tag_end == b"\x43\x53\x44\x4F\x73\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x53\x44\x4F\x73\x3A\x31\x3E\x00", self.csdos_tag_end, self._io, u"/types/c_s_d_os_element/seq/4")


    @property
    def bit_width(self):
        if hasattr(self, '_m_bit_width'):
            return self._m_bit_width

        self._m_bit_width = ((36 - self.blocks.cp.cs.a_b_a_5_a) + self.blocks.cp.cs.iterator)
        return getattr(self, '_m_bit_width', None)


