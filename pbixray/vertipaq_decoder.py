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
import numpy as np
import pandas as pd
from decimal import Decimal
from .abf.data_model import DataModel

from .huffman import decompress_encode_array, build_huffman_table, decode_substrings, _swap_bitstream
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

    def _read_bitpacked(self, sub_segment, bit_width, min_data_id):
        if len(sub_segment) == 0:
            return np.array([], dtype=np.int64)
        values_per_word = 64 // bit_width
        mask = np.uint64((1 << bit_width) - 1)
        arr = np.asarray(sub_segment, dtype=np.uint64)
        shifts = np.arange(values_per_word, dtype=np.uint64) * np.uint64(bit_width)
        result = ((arr[:, None] >> shifts[None, :]) & mask).ravel()
        return result.astype(np.int64) + min_data_id

    def _extract_strings(self,buffer):
        """Extract zero-terminated strings from buffer."""
        strings = buffer.split('\0')
        return strings[:-1]  # remove the last empty string

    def _read_rle_bit_packed_hybrid(self, buffer, segments_meta):
        with io.BytesIO(buffer) as f:
            column_data = ColumnDataIdf(KaitaiStream(f))

            # First pass: compute total output length, capping each segment at
            # its declared 'records'. The primary_segment array on disk is
            # over-allocated and trailing entries can contain stale garbage with
            # arbitrary repeat_values (this is harmless when capped properly,
            # but produces multi-GB allocations if summed blindly).
            total_len = 0
            seg_real_repeats = []
            for seg_idx, seg_meta in enumerate(segments_meta):
                segment = column_data.segments[seg_idx]
                cap = seg_meta.get('records', 0) or 0
                acc = 0
                per_entry = []
                for entry in segment.primary_segment:
                    if cap and acc >= cap:
                        per_entry.append(0)
                        continue
                    rv = entry.repeat_value
                    if cap and acc + rv > cap:
                        rv = cap - acc
                    per_entry.append(rv)
                    acc += rv
                seg_real_repeats.append(per_entry)
                total_len += acc

            vector = np.empty(total_len, dtype=np.int64)
            pos = 0

            for seg_idx, seg_meta in enumerate(segments_meta):
                segment = column_data.segments[seg_idx]
                entries = seg_meta['count_bit_packed']
                min_data_id = seg_meta['min_data_id']
                bit_width = seg_meta['bit_width']
                per_entry = seg_real_repeats[seg_idx]

                bitpacked_values = np.array([], dtype=np.int64)
                bit_packed_offset = 0

                if entries > 0 and bit_width > 0:
                    size = segment.sub_segment_size
                    sub_segment_arr = np.frombuffer(segment.sub_segment, dtype='<u8')
                    if sub_segment_arr[-1] == 0 and size == 1:
                        bitpacked_values = np.full(entries, min_data_id, dtype=np.int64)
                    else:
                        bitpacked_values = self._read_bitpacked(sub_segment_arr, bit_width, min_data_id)

                for entry, count in zip(segment.primary_segment, per_entry):
                    if count == 0:
                        continue
                    if entry.data_value + bit_packed_offset == 0xFFFFFFFF:
                        vector[pos:pos + count] = bitpacked_values[bit_packed_offset:bit_packed_offset + count]
                        bit_packed_offset += count
                        pos += count
                    else:
                        vector[pos:pos + count] = entry.data_value
                        pos += count

            return vector

    def _read_idfmeta(self,buffer):
        """Reads idfmeta from a buffer."""
        # Use io.BytesIO to wrap the bytearray
        with io.BytesIO(buffer) as f:
            metadata = IdfmetaParser.from_io(f)

            segments_meta = []
            for segment in metadata.column_partition.segments:
                segments_meta.append({
                    'min_data_id': segment.ss.min_data_id,
                    'count_bit_packed': segment.subsegment.records if segment.has_subsegment != 0 else 0,
                    'bit_width': segment.bit_width,
                    'records': segment.records,
                })

            return segments_meta

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
            raw_handles = dictionary.data.dictionary_record_handles_vector_info.vector_of_record_handle_structures
            record_handles_map = defaultdict(list)

            dt = np.dtype([('bit_or_byte_offset', '<u4'), ('page_id', '<u4')])
            handles = np.frombuffer(raw_handles, dtype=dt)
            page_ids = handles['page_id']
            offsets_arr = handles['bit_or_byte_offset']
            for pid in np.unique(page_ids):
                record_handles_map[int(pid)] = offsets_arr[page_ids == pid].tolist()

            for page_id, page in enumerate(pages):
                if page.page_compressed:
                    compressed_store = page.string_store
                    encode_array = compressed_store.encode_array
                    store_total_bits = compressed_store.store_total_bits
                    compressed_string_buffer = compressed_store.compressed_string_buffer

                    full_encode_array = decompress_encode_array(encode_array)
                    table, max_len = build_huffman_table(full_encode_array)
                    swapped = _swap_bitstream(compressed_string_buffer)

                    if page_id in record_handles_map:
                        page_offsets = record_handles_map[page_id]
                        is_general = compressed_store.character_set_type_identifier == _HUFFMAN_GENERAL
                        decoded = decode_substrings(swapped, table, max_len, page_offsets, store_total_bits)
                        if is_general:
                            for s in decoded:
                                b = s.encode('latin-1')
                                hashtable[index] = b[:len(b) & ~1].decode('utf-16-le', errors='ignore')
                                index += 1
                        else:
                            for s in decoded:
                                hashtable[index] = s
                                index += 1
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

    def _get_column_data(self, column_metadata, segments_meta):
        """Extracts column data based on the given column metadata and meta information."""
        if pd.notnull(column_metadata["Dictionary"]):
            dictionary_buffer = get_data_slice(self._data_model,column_metadata["Dictionary"])
            null_adjustment = 1 if column_metadata["IsNullable"] else 0
            # Read and construct the dictionary with appropriate minimum data ID
            segments_meta_adj = [
                {**segment, 'min_data_id': segment['min_data_id'] - null_adjustment}
                for segment in segments_meta
            ]
            dictionary = self._read_dictionary(dictionary_buffer, min_data_id=segments_meta[0]['min_data_id'])
            data_slice = get_data_slice(self._data_model,column_metadata["IDF"])
            return pd.Series(self._read_rle_bit_packed_hybrid(data_slice, segments_meta_adj)).map(dictionary)
        elif pd.notnull(column_metadata["HIDX"]):
            data_slice = get_data_slice(self._data_model,column_metadata["IDF"])
            return pd.Series(self._read_rle_bit_packed_hybrid(data_slice, segments_meta)).add(column_metadata["BaseId"]) / column_metadata["Magnitude"]
        else:
            # Column has no dictionary or HIDX (e.g. empty column, all-null column,
            # or calculated column without independently stored data).
            total_rows = sum(segment['count_bit_packed'] for segment in segments_meta)
            return pd.Series([None] * total_rows)

        
    def _handle_special_cases(self, column_data, data_type):
        if data_type == 9 or data_type == 'Date':
            # Convert to datetime
            return pd.to_datetime(column_data, unit='D', origin='1899-12-30')
        elif data_type == 10 or data_type == 'Currency':
            # Handle decimal.Decimal type
            return column_data.apply(lambda x: Decimal(x)/10000 if pd.notnull(x) else None)
        return column_data
        
    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table."""
        table_metadata_df = self._meta.schema_df[self._meta.schema_df['TableName'] == table_name]
        dataframe_data = {}
        is_xlsx = self._data_model.file_type == "xlsx"

        for _, column_metadata in table_metadata_df.iterrows():
            if is_xlsx:
                meta = self._meta.get_segments_meta(
                    column_metadata["DimensionID"],
                    column_metadata.get("StorageName") or column_metadata["ColumnName"],
                )
            else:
                idfmeta_buffer = get_data_slice(self._data_model,column_metadata["IDF"] + 'meta')
                meta = self._read_idfmeta(idfmeta_buffer)

            column_data = self._get_column_data(column_metadata, meta)
            # Handle special cases for certain data types
            type_key = column_metadata["SSASType"] if is_xlsx and "SSASType" in column_metadata else column_metadata["DataType"]
            column_data = self._handle_special_cases(column_data, type_key)

            if is_xlsx:
                pandas_dtype = column_metadata["DataType"] or "object"
            else:
                pandas_dtype = AMO_PANDAS_TYPE_MAPPING.get(column_metadata["DataType"], "object")  # default to object if no mapping is found

            # If it's a decimal type, keep it as object since pandas doesn't support Decimal natively
            if pandas_dtype == 'decimal.Decimal':
                pandas_dtype = 'object'
            try:
                dataframe_data[column_metadata["ColumnName"]] = column_data.astype(pandas_dtype)
            except (TypeError, ValueError):
                dataframe_data[column_metadata["ColumnName"]] = column_data

        return pd.DataFrame(dataframe_data)
