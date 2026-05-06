# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class IdfmetaParser(KaitaiStruct):
    """Metadata stream for a single column partition in the VertiPaq (xVelocity)
    in-memory columnar store, as used by Power BI, SSAS Tabular, and Excel
    Power Pivot.  Each .idfmeta file describes how its companion .idf segment
    data is compressed and laid out.
    """
    def __init__(self, _io, _parent=None, _root=None):
        super(IdfmetaParser, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.column_partition = IdfmetaParser.CpElement(self._io, self, self._root)


    def _fetch_instances(self):
        pass
        self.column_partition._fetch_instances()

    class CpElement(KaitaiStruct):
        """Column Partition – top-level envelope.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(IdfmetaParser.CpElement, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.open_tag = self._io.read_bytes(6)
            if not self.open_tag == b"\x3C\x31\x3A\x43\x50\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x50\x00", self.open_tag, self._io, u"/types/cp_element/seq/0")
            self.num_segments = self._io.read_u8le()
            self.segments = []
            for i in range(self.num_segments):
                self.segments.append(IdfmetaParser.CsElement(False, self._io, self, self._root))

            self.close_tag = self._io.read_bytes(6)
            if not self.close_tag == b"\x43\x50\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x50\x3A\x31\x3E\x00", self.close_tag, self._io, u"/types/cp_element/seq/3")
            if self._io.size() > self._io.pos():
                pass
                self.sdos = IdfmetaParser.SdosElement(self._io, self, self._root)



        def _fetch_instances(self):
            pass
            for i in range(len(self.segments)):
                pass
                self.segments[i]._fetch_instances()

            if self._io.size() > self._io.pos():
                pass
                self.sdos._fetch_instances()



    class CsElement(KaitaiStruct):
        """Column Segment metadata.
        
        Primary segments carry compression info and sub-segment statistics.
        A subsegment (is_subsegment = true) stores only records, base_id,
        has_subsegment, and cannot itself nest further ("!fHasSubsegment ||
        !in_fIsSubsegment").
        """
        def __init__(self, is_subsegment, _io, _parent=None, _root=None):
            super(IdfmetaParser.CsElement, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_subsegment = is_subsegment
            self._read()

        def _read(self):
            self.open_tag = self._io.read_bytes(6)
            if not self.open_tag == b"\x3C\x31\x3A\x43\x53\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x53\x00", self.open_tag, self._io, u"/types/cs_element/seq/0")
            self.records = self._io.read_u8le()
            self.base_id = self._io.read_u8le()
            if (not (self.is_subsegment)):
                pass
                self.compression_class = self._io.read_u4le()

            if (not (self.is_subsegment)):
                pass
                self.sub_compression_class = self._io.read_u4le()

            if  (((not (self.is_subsegment))) and (self.compression_class == 703066)) :
                pass
                self.rle_facet_data = IdfmetaParser.RleFacetData(self._io, self, self._root)

            if (not (self.is_subsegment)):
                pass
                self.first_run_value = self._io.read_u4le()

            if (not (self.is_subsegment)):
                pass
                self.ss = IdfmetaParser.SsElement(self._io, self, self._root)

            self.has_subsegment = self._io.read_u1()
            if self.has_subsegment != 0:
                pass
                self.subsegment = IdfmetaParser.CsElement(True, self._io, self, self._root)

            self.close_tag = self._io.read_bytes(6)
            if not self.close_tag == b"\x43\x53\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x53\x3A\x31\x3E\x00", self.close_tag, self._io, u"/types/cs_element/seq/10")


        def _fetch_instances(self):
            pass
            if (not (self.is_subsegment)):
                pass

            if (not (self.is_subsegment)):
                pass

            if  (((not (self.is_subsegment))) and (self.compression_class == 703066)) :
                pass
                self.rle_facet_data._fetch_instances()

            if (not (self.is_subsegment)):
                pass

            if (not (self.is_subsegment)):
                pass
                self.ss._fetch_instances()

            if self.has_subsegment != 0:
                pass
                self.subsegment._fetch_instances()



    class CsdosElement(KaitaiStruct):
        """Offset/size pair pointing into the companion .idf file.
        
        Recursion: if the parent CS has a subsegment, a nested CSDOs follows
        """
        def __init__(self, parent_has_subsegment, _io, _parent=None, _root=None):
            super(IdfmetaParser.CsdosElement, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.parent_has_subsegment = parent_has_subsegment
            self._read()

        def _read(self):
            self.open_tag = self._io.read_bytes(9)
            if not self.open_tag == b"\x3C\x31\x3A\x43\x53\x44\x4F\x73\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x43\x53\x44\x4F\x73\x00", self.open_tag, self._io, u"/types/csdos_element/seq/0")
            self.segment_data_size = self._io.read_s8le()
            self.segment_data_offset = self._io.read_s8le()
            if self.parent_has_subsegment:
                pass
                self.sub_csdos = IdfmetaParser.CsdosElement(False, self._io, self, self._root)

            self.close_tag = self._io.read_bytes(9)
            if not self.close_tag == b"\x43\x53\x44\x4F\x73\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x53\x44\x4F\x73\x3A\x31\x3E\x00", self.close_tag, self._io, u"/types/csdos_element/seq/4")


        def _fetch_instances(self):
            pass
            if self.parent_has_subsegment:
                pass
                self.sub_csdos._fetch_instances()



    class RleFacetData(KaitaiStruct):
        """Fields written by the RLE facet's Serialize.
        Member names from DBCC string and property-name strings in the binary.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(IdfmetaParser.RleFacetData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.bookmark_bits = self._io.read_u8le()
            self.storage_alloc_size = self._io.read_u8le()
            self.storage_used_size = self._io.read_u8le()
            self.segment_needs_resizing = self._io.read_u1()


        def _fetch_instances(self):
            pass


    class SdosElement(KaitaiStruct):
        """Segment Data Objects – file-offset information for on-demand loading.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(IdfmetaParser.SdosElement, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.open_tag = self._io.read_bytes(8)
            if not self.open_tag == b"\x3C\x31\x3A\x53\x44\x4F\x73\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x53\x44\x4F\x73\x00", self.open_tag, self._io, u"/types/sdos_element/seq/0")
            self.entries = []
            for i in range(self._parent.num_segments):
                self.entries.append(IdfmetaParser.CsdosElement((self._parent.segments[i].has_subsegment != 0 if self._parent.num_segments > 0 else False), self._io, self, self._root))

            self.close_tag = self._io.read_bytes(8)
            if not self.close_tag == b"\x53\x44\x4F\x73\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x44\x4F\x73\x3A\x31\x3E\x00", self.close_tag, self._io, u"/types/sdos_element/seq/2")


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class SsElement(KaitaiStruct):
        """SubSegment statistics.
        Field order and sizes verified from serialization and deserialization.
        """
        def __init__(self, _io, _parent=None, _root=None):
            super(IdfmetaParser.SsElement, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.open_tag = self._io.read_bytes(6)
            if not self.open_tag == b"\x3C\x31\x3A\x53\x53\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\x31\x3A\x53\x53\x00", self.open_tag, self._io, u"/types/ss_element/seq/0")
            self.distinct_states = self._io.read_u8le()
            self.min_data_id = self._io.read_u4le()
            self.max_data_id = self._io.read_u4le()
            self.original_min_segment_data_id = self._io.read_u4le()
            self.rle_sort_order = self._io.read_s8le()
            self.row_count = self._io.read_u8le()
            self.has_nulls = self._io.read_u1()
            self.rle_runs = self._io.read_u8le()
            self.others_rle_runs = self._io.read_u8le()
            self.close_tag = self._io.read_bytes(6)
            if not self.close_tag == b"\x53\x53\x3A\x31\x3E\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x53\x3A\x31\x3E\x00", self.close_tag, self._io, u"/types/ss_element/seq/10")


        def _fetch_instances(self):
            pass


    @property
    def bit_width(self):
        """Convenience: bit width of the first segment's encoding.
        For HybridRLE (0xaba5a) this is derived from sub_compression_class
        using the same NoSplit mapping.
        Returns 0 for non-bit-packed types (General/0xaba57, 123/0xaba5b)."""
        if hasattr(self, '_m_bit_width'):
            return self._m_bit_width

        self._m_bit_width = (self.column_partition.segments[0].compression_class - 703030 if  ((self.column_partition.segments[0].compression_class >= 703031) and (self.column_partition.segments[0].compression_class <= 703040))  else (12 if self.column_partition.segments[0].compression_class == 703042 else (16 if self.column_partition.segments[0].compression_class == 703046 else (21 if self.column_partition.segments[0].compression_class == 703051 else (32 if self.column_partition.segments[0].compression_class == 703062 else ((self.column_partition.segments[0].sub_compression_class - 703030 if  ((self.column_partition.segments[0].sub_compression_class >= 703031) and (self.column_partition.segments[0].sub_compression_class <= 703040))  else (12 if self.column_partition.segments[0].sub_compression_class == 703042 else (16 if self.column_partition.segments[0].sub_compression_class == 703046 else (21 if self.column_partition.segments[0].sub_compression_class == 703051 else (32 if self.column_partition.segments[0].sub_compression_class == 703062 else 0))))) if self.column_partition.segments[0].compression_class == 703066 else 0))))))
        return getattr(self, '_m_bit_width', None)


