# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class ColumnDataIdf(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        super(ColumnDataIdf, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.segments = []
        i = 0
        while not self._io.is_eof():
            self.segments.append(ColumnDataIdf.Segment(self._io, self, self._root))
            i += 1



    def _fetch_instances(self):
        pass
        for i in range(len(self.segments)):
            pass
            self.segments[i]._fetch_instances()


    class Segment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataIdf.Segment, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.primary_segment_size = self._io.read_u8le()
            self.primary_segment = []
            for i in range(self.primary_segment_size):
                self.primary_segment.append(ColumnDataIdf.SegmentEntry(self._io, self, self._root))

            self.sub_segment_size = self._io.read_u8le()
            self.sub_segment = self._io.read_bytes(self.sub_segment_size * 8)


        def _fetch_instances(self):
            pass
            for i in range(len(self.primary_segment)):
                pass
                self.primary_segment[i]._fetch_instances()



    class SegmentEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(ColumnDataIdf.SegmentEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.data_value = self._io.read_u4le()
            self.repeat_value = self._io.read_u4le()


        def _fetch_instances(self):
            pass



