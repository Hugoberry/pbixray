meta:
  id: idfmeta_parser
  file-extension: idfmeta
  endian: le
  license: CC0-1.0
  title: IDF Column Partition Metadata - XM Serialization Format
  # Reverse engineered from Power BI Desktop .pbix files (Microsoft VertiPaq engine)
  #
  # Binary tag encoding: "<ver:TAG\0" opens, "TAG:ver>\0" closes (ver = "1").
  #
  # Compression class IDs (PF_OBJECT_CLASS), from XMICompressionInfo::CreateCompressionInfo:
  #   0x000aba37 = XMRENoSplitCompressionInfo<1>   (1-bit)
  #   0x000aba38 = XMRENoSplitCompressionInfo<2>   (2-bit)
  #   0x000aba39 = XMRENoSplitCompressionInfo<3>   (3-bit)
  #   0x000aba3a = XMRENoSplitCompressionInfo<4>   (4-bit)
  #   0x000aba3b = XMRENoSplitCompressionInfo<5>   (5-bit)
  #   0x000aba3c = XMRENoSplitCompressionInfo<6>   (6-bit)
  #   0x000aba3d = XMRENoSplitCompressionInfo<7>   (7-bit)
  #   0x000aba3e = XMRENoSplitCompressionInfo<8>   (8-bit)
  #   0x000aba3f = XMRENoSplitCompressionInfo<9>   (9-bit)
  #   0x000aba40 = XMRENoSplitCompressionInfo<10>  (10-bit)
  #   0x000aba42 = XMRENoSplitCompressionInfo<12>  (12-bit)
  #   0x000aba46 = XMRENoSplitCompressionInfo<16>  (16-bit)
  #   0x000aba4b = XMRENoSplitCompressionInfo<21>  (21-bit)
  #   0x000aba56 = XMRENoSplitCompressionInfo<32>  (32-bit)
  #   0x000aba57 = XMREGeneralCompressionInfo
  #   0x000aba5a = XMHybridRLECompressionInfo      (sub_compression_class selects inner)
  #   0x000aba5b = XM123CompressionInfo

doc: |
  Metadata stream for a single column partition in the VertiPaq (xVelocity)
  in-memory columnar store, as used by Power BI, SSAS Tabular, and Excel
  Power Pivot.  Each .idfmeta file describes how its companion .idf segment
  data is compressed and laid out.

seq:
  - id: column_partition
    type: cp_element

types:
  # ===================================================================
  #  CP – Column Partition (top-level container)
  # ===================================================================
  cp_element:
    doc: |
      Column Partition – top-level envelope.
    seq:
      - id: open_tag
        contents: ['<1:CP', 0x00]

      - id: num_segments
        type: u8
        doc: |
          Number of column segments in this partition.
          Verified against the in-memory partition segment count on load.

      - id: segments
        type: cs_element(false)
        repeat: expr
        repeat-expr: num_segments

      - id: close_tag
        contents: ['CP:1>', 0x00]

      - id: sdos
        type: sdos_element
        if: _io.size > _io.pos
        doc: |
          Optional Segment Data Objects block.  Present only when on-demand
          (lazy) segment loading is enabled.  The deserializer peeks 8 bytes
          after CP:1> and checks for the "<1:SDOs\0" signature.

  # ===================================================================
  #  CS – Column Segment (recursive; subsegments omit compression / SS)
  # ===================================================================
  cs_element:
    doc: |
      Column Segment metadata.

      Primary segments carry compression info and sub-segment statistics.
      A subsegment (is_subsegment = true) stores only records, base_id,
      has_subsegment, and cannot itself nest further ("!fHasSubsegment ||
      !in_fIsSubsegment").
    params:
      - id: is_subsegment
        type: bool
    seq:
      - id: open_tag
        contents: ['<1:CS', 0x00]

      - id: records
        type: u8

      - id: base_id
        type: u8

      # ----- primary-only fields -----
      - id: compression_class
        type: u4
        if: not is_subsegment
        doc: |
          PF_OBJECT_CLASS of the compression encoding used for this segment.
          Retrieved via CompressionInfo->GetClass().
          See class-ID table in the file header for the full mapping.

      - id: sub_compression_class
        type: u4
        if: not is_subsegment
        doc: |
          PF_OBJECT_CLASS of the sub-compression (inner encoder).
          Meaningful only for HybridRLE (0xaba5a); for other types this
          is typically 0 or a copy of compression_class.
          Retrieved via CompressionInfo->GetSubcompressionClass().

      - id: rle_facet_data
        type: rle_facet_data
        if: not is_subsegment and compression_class == 0x000aba5a
        doc: |
          RLE-specific metadata.  Present only for HybridRLE compression (class 0xaba5a).

      - id: first_run_value
        type: u4
        if: not is_subsegment
        doc: |
          First run value written by the inner (sub-)compression's Serialize.
          Present for every primary segment regardless of compression class,
          because HybridRLE delegates to its sub-compression which also
          writes this field, and non-hybrid types write it directly.

      - id: ss
        type: ss_element
        if: not is_subsegment
        doc: SubSegment statistics for this segment.

      # ----- common tail -----
      - id: has_subsegment
        type: u1
        doc: |
          1 if this segment contains a bit-packed subsegment, 0 otherwise.

      - id: subsegment
        type: cs_element(true)
        if: has_subsegment != 0

      - id: close_tag
        contents: ['CS:1>', 0x00]

  # ===================================================================
  #  RLE facet data (XMRLECompressionInfo::RleFacet fields)
  # ===================================================================
  rle_facet_data:
    doc: |
      Fields written by the RLE facet's Serialize.
      Member names from DBCC string and property-name strings in the binary.
    seq:
      - id: bookmark_bits
        type: u8
        doc: |
          Number of bits for RLE bookmark indexing (log2 of bookmark distance).
          Property: "BookmarkBits".

      - id: storage_alloc_size
        type: u8
        doc: |
          Allocated storage size for segment data in units.
          Member: m_cStorageAllocSize.

      - id: storage_used_size
        type: u8
        doc: |
          Used storage size for segment data in units.
          Member: m_cStorageUsedSize.

      - id: segment_needs_resizing
        type: u1
        doc: |
          Boolean – segment storage needs resizing on next encode.
          Member: m_fSegmentNeedsResizing.

  # ===================================================================
  #  SS – SubSegment Statistics
  # ===================================================================
  ss_element:
    doc: |
      SubSegment statistics.
      Field order and sizes verified from serialization and deserialization.
    seq:
      - id: open_tag
        contents: ['<1:SS', 0x00]

      - id: distinct_states
        type: u8
        doc: Cardinality – number of distinct data IDs.

      - id: min_data_id
        type: u4
        doc: Minimum data ID.

      - id: max_data_id
        type: u4
        doc: Maximum data ID.

      - id: original_min_segment_data_id
        type: u4
        doc: Original minimum data ID before any remapping.

      - id: rle_sort_order
        type: s8
        doc: RLE sort-order indicator.

      - id: row_count
        type: u8
        doc: Total rows in this segment.

      - id: has_nulls
        type: u1
        doc: Whether this segment contains NULLs.

      - id: rle_runs
        type: u8
        doc: Number of RLE runs.

      - id: others_rle_runs
        type: u8
        doc: Number of RLE runs in related segments.

      - id: close_tag
        contents: ['SS:1>', 0x00]

  # ===================================================================
  #  SDOs – Segment Data Objects (on-demand loading offsets)
  # ===================================================================
  sdos_element:
    doc: |
      Segment Data Objects – file-offset information for on-demand loading.
    seq:
      - id: open_tag
        contents: ['<1:SDOs', 0x00]

      - id: entries
        type: 'csdos_element(_parent.num_segments > 0 ? _parent.segments[_index].has_subsegment != 0 : false)'
        repeat: expr
        repeat-expr: _parent.num_segments

      - id: close_tag
        contents: ['SDOs:1>', 0x00]

  # ===================================================================
  #  CSDOs – Column Segment Data Object (offset + size, recursive)
  # ===================================================================
  csdos_element:
    doc: |
      Offset/size pair pointing into the companion .idf file.

      Recursion: if the parent CS has a subsegment, a nested CSDOs follows
    params:
      - id: parent_has_subsegment
        type: bool
    seq:
      - id: open_tag
        contents: ['<1:CSDOs', 0x00]

      - id: segment_data_size
        type: s8
        doc: |
          Size in bytes of this segment's data in the .idf file.
          Must not be -1 (validated on load).

      - id: segment_data_offset
        type: s8
        doc: |
          Byte offset into the .idf file.  Must be >= 0.

      - id: sub_csdos
        type: csdos_element(false)
        if: parent_has_subsegment
        doc: Nested offset/size for the subsegment's data.

      - id: close_tag
        contents: ['CSDOs:1>', 0x00]

instances:
  bit_width:
    value: >-
      column_partition.segments[0].compression_class >= 0xaba37
      and column_partition.segments[0].compression_class <= 0xaba40
      ? column_partition.segments[0].compression_class - 0xaba36
      : (column_partition.segments[0].compression_class == 0xaba42 ? 12
      : (column_partition.segments[0].compression_class == 0xaba46 ? 16
      : (column_partition.segments[0].compression_class == 0xaba4b ? 21
      : (column_partition.segments[0].compression_class == 0xaba56 ? 32
      : (column_partition.segments[0].compression_class == 0xaba5a
         ? (column_partition.segments[0].sub_compression_class >= 0xaba37
            and column_partition.segments[0].sub_compression_class <= 0xaba40
            ? column_partition.segments[0].sub_compression_class - 0xaba36
            : (column_partition.segments[0].sub_compression_class == 0xaba42 ? 12
            : (column_partition.segments[0].sub_compression_class == 0xaba46 ? 16
            : (column_partition.segments[0].sub_compression_class == 0xaba4b ? 21
            : (column_partition.segments[0].sub_compression_class == 0xaba56 ? 32
            : 0)))))
         : 0)))))
    doc: |
      Convenience: bit width of the first segment's encoding.
      For HybridRLE (0xaba5a) this is derived from sub_compression_class
      using the same NoSplit mapping.
      Returns 0 for non-bit-packed types (General/0xaba57, 123/0xaba5b).