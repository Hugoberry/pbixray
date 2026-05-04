# ---------- IMPORTS ----------
from .column_data.idf import ColumnDataIdf
from .column_data.idfmeta import IdfmetaParser
from .column_data.hidx import ColumnDataHidx
from .column_data.dictionary import ColumnDataDictionary
from .abf.backup_log import BackupLog
from .abf.virtual_directory import VirtualDirectory
from kaitaistruct import KaitaiStream
from .utils import AMO_PANDAS_TYPE_MAPPING, get_data_slice
import io
import pandas as pd
from decimal import Decimal
from .abf.data_model import DataModel

from .huffman import decompress_encode_array,build_huffman_tree, decode_substring
from collections import defaultdict

# Compression class IDs from the dictionary format (character_set_type_identifier):
#   0x000aba91 = charset-based Huffman — strings are single-byte (encoded per the
#                character_set_used byte, commonly ANSI/latin-1 for Latin scripts).
#   0x000aba92 = general Huffman — Huffman tree operates on raw bytes whose sequence
#                is UTF-16LE; no character_set_used field.
_HUFFMAN_CHARSET_BASED = 0x000aba91  # single-byte charset Huffman (latin-1 output)
_HUFFMAN_GENERAL       = 0x000aba92  # UTF-16LE bytes via general Huffman

# ---------- VertiPaq CLASS ----------

class VertiPaqDecoder:
    def __init__(self, metadata, data_model:DataModel):
        self._meta = metadata
        self._data_model = data_model

    def _read_bitpacked(self,sub_segment, bit_width, min_data_id):
        """Reads bitpacked values from a sub_segment."""
        mask = (1 << bit_width) - 1
        res = []
        for u8le in sub_segment:
            for _ in range(64 // bit_width):
                res.append((min_data_id + (u8le & mask)))
                u8le >>= bit_width

        return res

    def _extract_strings(self,buffer):
        """Extract zero-terminated strings from buffer."""
        strings = buffer.split('\0')
        return strings[:-1]  # remove the last empty string

    def _read_rle_bit_packed_hybrid(self,buffer, entries, min_data_id, bit_width ):
        """Reads RLE bit packed hybrid values from a buffer."""
        with io.BytesIO(buffer) as f:
            # Parse the binary data
            column_data = ColumnDataIdf(KaitaiStream(f))
            
            bitpacked_values = []
            vector = []
            bit_packed_entries = None
            bit_packed_offset = 0
            
            if entries > 0:
                # Get bit width
                size = column_data.segments[0].sub_segment_size
                # case if it's a column with empty strings
                if column_data.segments[0].sub_segment[-1].bit_length() == 0 and size == 1:
                    bitpacked_values = [min_data_id] * entries
                else:
                    # read the bitpacked values from the sub_segment
                    bitpacked_values = self._read_bitpacked(column_data.segments[0].sub_segment,bit_width, min_data_id)

            # consider only the first primary segment + sub segment combination
            # for segment in column_data.segments: 
            for entry in column_data.segments[0].primary_segment:
                if entry.data_value+bit_packed_offset== 0xFFFFFFFF: # bit pack marker
                    bit_packed_entries = entry.repeat_value
                    bitpacked_values_slice = bitpacked_values[bit_packed_offset:bit_packed_offset+bit_packed_entries]
                    bit_packed_offset += bit_packed_entries
                    vector+=bitpacked_values_slice
                else:
                    rle = [entry.data_value] * entry.repeat_value
                    vector+=rle

            return vector

    def _read_idfmeta(self, buffer):
        """Reads idfmeta from a buffer. Handles multi-segment columns.

        Previously used the Kaitai-generated IdfmetaParser which crashed with a
        ValidationNotEqualError on files that contain more than one VertiPaq
        segment (i.e. tables with more than ~1 M rows).  Replaced with a
        manual parser that loops over all CP blocks.  Returns only the first
        segment's dict for backwards-compatibility; get_table() calls
        _parse_idfmeta_all() directly.
        """
        segs = self._parse_idfmeta_all(buffer)
        if not segs:
            raise ValueError("No CS segments found in idfmeta buffer")
        return segs[0]

    def _parse_idfmeta_all(self, buffer):
        """Return a list of metadata dicts, one per VertiPaq segment.

        Each dict contains:
            min_data_id      – minimum encoded value in this segment
            count_bit_packed – number of bit-packed values
            bit_width        – bits used per encoded value
        """
        import struct
        f = io.BytesIO(buffer)
        def rb(n): return f.read(n)
        def ru4(): return struct.unpack('<I', f.read(4))[0]
        def ru8(): return struct.unpack('<Q', f.read(8))[0]
        def rs8(): return struct.unpack('<q', f.read(8))[0]

        rb(6); ru8()   # outer CP tag + version
        segs = []
        while True:
            peek = rb(6)
            if not peek or peek == b'CP:1>\x00':
                break
            elif peek == b'<1:CS\x00':
                f.seek(f.tell() - 6)
                rb(6); ru8(); ru8()              # cs_tag, records, one
                aba5a = ru4(); iterator = ru4()  # a_b_a_5_a, iterator
                ru8(); ru8(); ru8(); rb(1); ru4()                       # bookmark, alloc, used, resize, compress
                rb(6); ru8(); min_id = ru4()                            # SS tag, distinct_states, min_data_id
                ru4(); ru4(); rs8(); ru8(); rb(1); ru8(); ru8(); rb(6)  # rest of SS element
                rb(1); rb(6); cnt_bp = ru8(); rb(9); rb(6); rb(6)      # hbp, CS1, CS0 end tag
                segs.append({
                    'min_data_id':      min_id,
                    'count_bit_packed': cnt_bp,
                    'bit_width':        (36 - aba5a) + iterator,
                })
        return segs

    def _read_hash_table(self,buffer):
        """Reads a hash table from a buffer."""
        with io.BytesIO(buffer) as f:
            # Parse the .hidx file using the Kaitai Struct
            parsed_hidx = ColumnDataHidx.from_io(f)

            # Create a hash table to store the results
            result_hash_table = {}

            # Iterate over each hash_bin entry
            for hash_bin in parsed_hidx.hash_bin_entries:
                # Iterate over each m_rg_local_entry inside hash_bin
                for local_entry in hash_bin.m_rg_local_entries:
                    # If the m_hash is non-zero, add it to the result hash table
                    if local_entry.m_hash != 0:
                        result_hash_table[local_entry.m_hash] =  local_entry.m_key
            
            # Iterate over the overflow_hash_entries
            for overflow_entry in parsed_hidx.overflow_hash_entries:
                # If the m_hash is non-zero, add it to the result hash table
                if overflow_entry.m_hash != 0:
                    result_hash_table[overflow_entry.m_hash] = overflow_entry.m_key 

            return result_hash_table

 
    def _read_dictionary(self, buffer, min_data_id):
        """Reads a dictionary from a buffer."""
        with io.BytesIO(buffer) as f:
            dictionary = ColumnDataDictionary.from_io(f)

        if dictionary.dictionary_type == ColumnDataDictionary.DictionaryTypes.xm_type_string:
            hashtable = {}
            index = min_data_id

            pages = dictionary.data.dictionary_pages
            record_handles = dictionary.data.dictionary_record_handles_vector_info.vector_of_record_handle_structures
            record_handles_map = defaultdict(list)

            for handle in record_handles:
                record_handles_map[handle.page_id].append(handle.bit_or_byte_offset)

            for page_id, page in enumerate(pages):
                if page.page_compressed:
                    compressed_store = page.string_store
                    encode_array = compressed_store.encode_array
                    store_total_bits = compressed_store.store_total_bits
                    compressed_string_buffer = compressed_store.compressed_string_buffer
                    ui_decode_bits = compressed_store.ui_decode_bits

                    full_encode_array = decompress_encode_array(encode_array)
                    huffman_tree = build_huffman_tree(full_encode_array)

                    if page_id in record_handles_map:
                        offsets = record_handles_map[page_id]
                        for i in range(len(offsets)):
                            start_bit = offsets[i]
                            end_bit = offsets[i + 1] if i + 1 < len(offsets) else store_total_bits
                            decompressed = decode_substring(compressed_string_buffer, huffman_tree, start_bit, end_bit)
                            if compressed_store.character_set_type_identifier == _HUFFMAN_GENERAL:
                                # General Huffman (0xaba92): the Huffman tree operates on raw bytes
                                # whose sequence is UTF-16LE.  Re-encode to bytes via the lossless
                                # latin-1 identity map, then decode as UTF-16LE.  Strip any trailing
                                # odd byte from Huffman padding before decoding.
                                b = decompressed.encode('latin-1')
                                decompressed = b[:len(b) & ~1].decode('utf-16-le', errors='ignore')
                            hashtable[index] = decompressed
                            index += 1
                    del huffman_tree
                else:
                    uncompressed_store = page.string_store
                    uncompressed = uncompressed_store.uncompressed_character_buffer
                    strings = self._extract_strings(uncompressed)
                    for i, token in enumerate(strings):
                        hashtable[index] = token
                        index += 1

            return hashtable
        elif dictionary.dictionary_type in [ColumnDataDictionary.DictionaryTypes.xm_type_long, ColumnDataDictionary.DictionaryTypes.xm_type_real]:
            vector_values = dictionary.data.vector_of_vectors_info.values
            return {i: val for i, val in enumerate(vector_values, start=min_data_id)}

        return None    
        
    def _get_column_data(self, column_metadata, meta):
        """Extracts column data based on the given column metadata and meta information."""
        if pd.notnull(column_metadata["Dictionary"]):
            dictionary_buffer = get_data_slice(self._data_model,column_metadata["Dictionary"])
            null_adjustment = 1 if column_metadata["IsNullable"] else 0
            # Read and construct the dictionary with appropriate minimum data ID
            min_data_id_adj = meta['min_data_id'] - null_adjustment
            dictionary = self._read_dictionary(dictionary_buffer, min_data_id=meta['min_data_id'])
            data_slice = get_data_slice(self._data_model,column_metadata["IDF"])
            return pd.Series(self._read_rle_bit_packed_hybrid(data_slice, meta['count_bit_packed'], min_data_id_adj , meta['bit_width'])).map(dictionary)
        elif pd.notnull(column_metadata["HIDX"]):
            data_slice = get_data_slice(self._data_model,column_metadata["IDF"])
            return pd.Series(self._read_rle_bit_packed_hybrid(data_slice, meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])).add(column_metadata["BaseId"]) / column_metadata["Magnitude"]
        else:
            # Column has no dictionary or HIDX (e.g. empty column, all-null column,
            # or calculated column without independently stored data).
            return pd.Series([None] * meta['count_bit_packed'])
        
    def _handle_special_cases(self, column_data, data_type):
        if data_type == 9:
            # Convert to datetime
            return pd.to_datetime(column_data, unit='D', origin='1899-12-30')
        elif data_type == 10:
            # Handle decimal.Decimal type
            return column_data.apply(lambda x: Decimal(x)/10000 if pd.notnull(x) else None)
        return column_data
        
    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table.

        Fixed to read ALL VertiPaq segments instead of only the first one.
        The original implementation hardcoded segments[0] in
        _read_rle_bit_packed_hybrid and used _read_idfmeta (which crashed on
        multi-segment files).  For tables larger than ~1 M rows the data is
        split across multiple segments; the old code silently returned only
        the first ~1 M rows, making every aggregation incorrect.

        Also fixes a secondary bug in the HIDX branch where the original code
        called .add() on a pandas IntegerArray, which is not supported;
        replaced with numpy arithmetic.
        """
        import numpy as np

        table_metadata_df = self._meta.schema_df[self._meta.schema_df['TableName'] == table_name]
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():

            # One metadata dict per segment (was: single dict, crashed on >1 segment)
            meta_buf     = get_data_slice(self._data_model, column_metadata['IDF'] + 'meta')
            all_seg_meta = self._parse_idfmeta_all(meta_buf)

            # The dictionary is shared across all segments
            dictionary = None
            if pd.notnull(column_metadata['Dictionary']):
                dict_buf   = get_data_slice(self._data_model, column_metadata['Dictionary'])
                dictionary = self._read_dictionary(dict_buf, min_data_id=all_seg_meta[0]['min_data_id'])

            # All segments are stored in the single .idf file
            idf_data = get_data_slice(self._data_model, column_metadata['IDF'])
            col_idf  = ColumnDataIdf(KaitaiStream(io.BytesIO(idf_data)))

            all_values = []
            for i, seg_meta in enumerate(all_seg_meta):
                seg        = col_idf.segments[i]
                cnt_bp     = seg_meta['count_bit_packed']
                min_id     = seg_meta['min_data_id']
                bw         = seg_meta['bit_width']
                null_adj   = 1 if column_metadata['IsNullable'] else 0
                min_id_adj = min_id - null_adj

                if pd.notnull(column_metadata['Dictionary']):
                    if cnt_bp > 0:
                        empty   = (seg.sub_segment[-1].bit_length() == 0
                                   and seg.sub_segment_size == 1)
                        bp_vals = ([min_id_adj] * cnt_bp if empty
                                   else self._read_bitpacked(seg.sub_segment, bw, min_id_adj))
                    else:
                        bp_vals = []

                    bp_offset = 0
                    vector    = []
                    for entry in seg.primary_segment:
                        if entry.data_value + bp_offset == 0xFFFFFFFF:
                            n          = entry.repeat_value
                            vector    += bp_vals[bp_offset:bp_offset + n]
                            bp_offset += n
                        else:
                            vector += [entry.data_value] * entry.repeat_value

                    all_values += list(pd.Series(vector).map(dictionary))

                elif pd.notnull(column_metadata['HIDX']):
                    bp_vals = (self._read_bitpacked(seg.sub_segment, bw, min_id)
                               if cnt_bp > 0 else [])
                    bp_offset = 0
                    vector    = []
                    for entry in seg.primary_segment:
                        if entry.data_value + bp_offset == 0xFFFFFFFF:
                            n          = entry.repeat_value
                            vector    += bp_vals[bp_offset:bp_offset + n]
                            bp_offset += n
                        else:
                            vector += [entry.data_value] * entry.repeat_value

                    # Original used pd.Series.add() on IntegerArray — not supported.
                    arr         = np.array(vector, dtype='float64')
                    all_values += list(
                        (arr + column_metadata['BaseId']) / column_metadata['Magnitude']
                    )

                else:
                    all_values += [None] * cnt_bp

            pandas_dtype = AMO_PANDAS_TYPE_MAPPING.get(column_metadata['DataType'], 'object')
            if pandas_dtype == 'decimal.Decimal':
                pandas_dtype = 'object'
            try:
                dataframe_data[column_metadata['ColumnName']] = pd.array(
                    all_values, dtype=pandas_dtype
                )
            except (TypeError, ValueError):
                dataframe_data[column_metadata['ColumnName']] = all_values

        return pd.DataFrame(dataframe_data)