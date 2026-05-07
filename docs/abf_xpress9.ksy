meta:
  id: abf_xpress9
  file-extension: idf
  endian: le
  license: CC0-1.0
  title: ABF XPress9 Compressed Backup
doc: |
    Container format for SQL Server backup files (.idf) compressed with
    XPress9 (LZ77 + Huffman). The file begins with a UTF-16LE signature
    followed by a sequence of independently-sized chunks. Each chunk
    carries an 8-byte outer envelope (uncompressed/compressed sizes)
    and an inner xpress9 block consisting of a 32-byte header, per-block
    Huffman tables, and LZ77-encoded segments.

    XPress9 uses a sliding window (64 KB - 4 MB) that spans across block
    boundaries, so decompression of block N may reference decoded data
    from earlier blocks within the window. Huffman tables and MTF initial
    offsets are self-contained per block, but MTF offsets still reference
    positions in the sliding window history.

    References:
      - src/Xpress9Internal.h  (header struct, constants)
      - src/Xpress9DecLz77.c   (decoder state machine)
      - src/Xpress9Lz77Dec.i   (LZ77 decode loop)

seq:
  - id: signature
    size: 102
    type: str
    encoding: UTF-16LE
    doc: |
      Fixed 51-character UTF-16LE string (102 bytes) identifying the
      compression method, e.g. "This backup was created using Xpress9 compression."

  - id: chunks
    type: chunk
    repeat: eos
    doc: |
      Stream of compressed chunks. Each chunk is independently sized
      (variable compressed length) but shares a session-wide LZ77
      sliding window with preceding chunks.

types:
  chunk:
    doc: |
      Outer envelope for one xpress9-compressed block. The uncompressed
      and compressed sizes are stored as a pair of u4 values preceding
      the raw compressed payload.
    seq:
      - id: uncompressed
        type: u4
        doc: |
          Uncompressed (original) size of this block in bytes.
          Typically 2 MB (2097152) for full blocks; the final block
          may be smaller.

      - id: compressed
        type: u4
        doc: |
          Compressed payload size in bytes. This is the byte-aligned
          size of the xpress9 node (header + segments). Matches
          ceil(header.encoded_size / 8).

      - id: node
        type: node
        size: compressed
        doc: Raw xpress9-compressed block bounded to `compressed` bytes.

  node:
    doc: |
      One xpress9 block: a 32-byte header followed by the compressed
      bitstream (Huffman tables + LZ77-encoded data).
    seq:
      - id: header
        type: header
        doc: 32-byte block header with magic, sizes, flags, and CRC.

      - id: segments
        size: _parent.compressed - 32
        doc: |
          Compressed bitstream for this block. Contains:
            1. MTF initial offsets (if mtf_entry_count > 0)
            2. Short-symbol Huffman table (up to 1024 symbols)
            3. Long-length Huffman table (up to 256 symbols)
            4. LZ77-encoded data (literals + back-reference pointers)
          Total bit length = header.encoded_size.

  header:
    doc: |
      32-byte xpress9 block header (8 x UInt32 LE).

      Layout:
        [0] magic             0x4e86d72a
        [1] orig_size         uncompressed byte count
        [2] encoded_size      compressed bitstream length in BITS
        [3] flags             compression parameters (see huffman_flags)
        [4] reserved          must be 0
        [5] session_signature constant across all blocks in a session
        [6] block_index       sequential block counter (0, 1, 2, ...)
        [7] crc32             CRC32 over fields [0]-[6] with [4]=0

      The CRC32 is computed by Xpress9Crc32() over the first 28 bytes
      of the header, treating the reserved field as 0.

      See: src/Xpress9DecLz77.c lines 607-643
    seq:
      - id: xpress_magic
        contents: [0x2a, 0xd7, 0x86, 0x4e]
        doc: Magic number 0x4e86d72a (little-endian).

      - id: orig_size
        type: u4
        doc: Uncompressed size of this block in bytes.

      - id: encoded_size
        type: u4
        doc: |
          Total size of the compressed bitstream in BITS (not bytes).
          Byte size = ceil(encoded_size / 8). Includes Huffman tables
          and LZ77-encoded data, but not the 32-byte header.

      - id: flags
        type: huffman_flags
        doc: |
          Compression parameters packed into a 32-bit flags field.
          See huffman_flags type for the bitfield layout.

      - id: reserved
        type: u4
        doc: Reserved field, must be 0. Used as 0 in CRC32 computation.

      - id: session_signature
        type: u4
        doc: |
          Session identifier. Must be identical across all blocks in
          the same compression session. The decoder validates this on
          every block after the first.

      - id: block_index
        type: u4
        doc: |
          Sequential block counter starting at 0 for the first block
          in a session. Increments by 1 for each subsequent block.
          The decoder rejects out-of-order blocks.

      - id: crc32
        type: u4
        doc: |
          CRC32 checksum over the first 7 header fields (28 bytes),
          with the reserved field treated as 0. Validates header
          integrity only -- there is no checksum for the compressed
          data payload.

  huffman_flags:
    doc: |
      Compression parameters encoded in a 32-bit LE integer.

      Bit layout (extracted via right-shifts on the assembled UInt32):
        Bits  0-12  (13 bits): Huffman table length in bits
        Bits 13-15  ( 3 bits): log2(window_size) - 16  (range 0-7, so window = 64 KB .. 8 MB)
        Bits 16-17  ( 2 bits): MTF entry count / 2     (0=none, 1=2 entries, 2=4 entries)
        Bit  18     ( 1 bit ): min pointer match length (0 -> 3, 1 -> 4)
        Bit  19     ( 1 bit ): min MTF match length     (0 -> 2, 1 -> 3)
        Bits 20-31  (12 bits): reserved, must be 0

      IMPORTANT: These fields must be extracted with bitmasks on the
      raw u4 value, not with kaitai's bN bit types. Kaitai reads bits
      MSB-first within each byte, but the C decoder reads a LE u4 and
      uses right-shifts from the LSB. Using bN types produces scrambled
      values (e.g. varying log2_window_size across blocks when it must
      be constant, non-zero reserved field).

      See: src/Xpress9DecLz77.c lines 648-696
    seq:
      - id: raw
        type: u4
        doc: Raw 32-bit flags value, little-endian.

    instances:
      huffman_table_length:
        value: raw & 0x1FFF
        doc: |
          Length of the encoded Huffman tables in bits. This many bits
          after the 32-byte header (and optional MTF state) contain the
          short-symbol and long-length Huffman code tables.

      log2_window_size:
        value: (raw >> 13) & 7
        doc: |
          LZ77 sliding window size as log2(window_size) - 16.
          Actual window size = 2^(log2_window_size + 16).
          Valid range: 0-6, giving windows from 64 KB to 4 MB.
          Must be constant across all blocks in a session.

      window_size:
        value: 1 << (log2_window_size + 16)
        doc: |
          Computed LZ77 window size in bytes.
          This is the maximum back-reference distance: a pointer in
          block N can reference decoded data up to window_size bytes
          back, potentially spanning into earlier blocks.
          Range: 65536 (64 KB) to 4194304 (4 MB).

      mtf_entry_count:
        value: ((raw >> 16) & 3) * 2
        doc: |
          Number of Move-To-Front cache entries: 0, 2, or 4.
          MTF caches recently-used back-reference offsets for more
          efficient encoding of repeated patterns. The value 3 (6
          entries) is reserved and invalid.
          When 0, no MTF optimization is used -- only regular LZ77
          pointers and literals appear in the bitstream.

      min_ptr_match_length:
        value: ((raw >> 18) & 1) + 3
        doc: |
          Minimum match length for regular LZ77 pointers: 3 or 4
          bytes. Shorter matches are encoded as literals instead.

      min_mtf_match_length:
        value: ((raw >> 19) & 1) + 2
        doc: |
          Minimum match length for MTF pointers: 2 or 3 bytes.
          Only meaningful when mtf_entry_count > 0.

      reserved_zero:
        value: raw >> 20
        doc: |
          Reserved bits, must be 0. The decoder rejects blocks where
          this field is non-zero (src/Xpress9DecLz77.c line 698).
          A non-zero value here indicates either file corruption or
          a format version mismatch.

      warmup_blocks:
        value: |
          (window_size + _root.chunks[0].uncompressed - 1) / _root.chunks[0].uncompressed
        doc: |
          Number of additional blocks to decompress before a target
          block in order to fill the LZ77 sliding window with valid
          history. Required for reliable partial decompression from
          the middle or end of a stream.

          Formula: ceil(window_size / chunk_uncompressed_size)

          Example with 2 MB chunks and 4 MB window: 2 warmup blocks.
          To decompress the last 4 blocks, start 2 blocks earlier
          (6 total) and discard the warmup output.

enums:
  mtf_entries_enum:
    0: no_entries
    1: two_entries
    2: four_entries
    3: reserved