meta:
  id: column_data_idf
  file-extension: idf
  endian: le
  license: CC0-1.0
  title: Column Data Storage Format
  ks-version: 0.9
doc: |
  Column data storage file for VertiPaq (xVelocity) in-memory columnar store,
  as used by Power BI, SSAS Tabular, and Excel Power Pivot.

  Decoding an .idf requires the companion XML metadata (PBIX: .idfmeta with the
  SsElement.row_count and CompressionInfo fields; XLSX: the column's
  <XMRawColumn> entry inside <table>.tbl.xml — Records, CompressionInfo<N>.Min,
  Nullable). The IDF alone does not carry a row count.
  See MS-XLDM §2.3.1 (Column Data Storage) and §2.5 (Column Metadata XML).

seq:
  - id: segments
    type: segment
    repeat: eos

types:
  segment:
    doc: |
      One file may contain multiple segments (typical when row_count > 2^20).
      For hybrid RLE (the normal case for column data), each segment carries
      its own primary RLE entries followed by its bit-packed sub-segment.
      See MS-XLDM §2.3.1.1.2 (hybrid-compression layout).
    seq:
      - id: primary_segment_size
        type: u8
        doc: |
          On-disk allocation of the primary segment, in 8-byte units (i.e.
          the number of SegmentEntry slots that physically follow). This is
          the spec's "SegmentSize" (MS-XLDM §2.3.1.1) and reflects file
          layout, not the number of real RLE runs — see primary_segment.
      - id: primary_segment
        type: segment_entry
        repeat: expr
        repeat-expr: primary_segment_size
        doc: |
          The RLE primary segment. Real runs occupy the first K <= N slots
          where N == primary_segment_size; the remaining N - K slots are
          allocation padding. MS-XLDM §2.3.1.1 specifies "Any unused
          trailing bytes within a segment are padded with zeros", in which
          case trailing entries are (data_value=0, repeat_value=0) and a
          consumer can sum repeat_value over all slots without harm. In
          practice some XLSX Power Pivot writers leave stale memory in
          those slots (non-zero data_value and repeat_value). A correct
          decoder must therefore stop accumulating real runs once
          cumulative repeat_value reaches the row count carried in the
          companion XML metadata, not when it reaches primary_segment_size.
      - id: sub_segment_size
        type: u8
        doc: Sub-segment size in 8-byte units (bit-packed payload below).
      - id: sub_segment
        doc: |
          Bit-packed values referenced by primary_segment entries whose
          data_value matches the sliding sentinel
          (0xFFFFFFFF - cumulative_bit_packed_offset). The bit width comes
          from the segment's CompressionInfo class in the companion XML
          (e.g. XMRENoSplitCompressionInfo<12> → 12 bits). Returned as raw
          bytes here; the consumer parses these as u8 little-endian words
          with numpy for performance.
        size: sub_segment_size * 8

  segment_entry:
    doc: |
      One RLE run. If data_value == 0xFFFFFFFF - bit_packed_offset, the run
      is "bit-packed": the next `repeat_value` rows come from the
      sub-segment starting at bit_packed_offset, after which bit_packed_offset
      advances by repeat_value. Otherwise it is a literal run of
      `repeat_value` rows all carrying data_value.
    seq:
      - id: data_value
        type: u4
      - id: repeat_value
        type: u4
