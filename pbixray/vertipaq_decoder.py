# ---------- IMPORTS ----------
from .column_data.idf import ColumnDataIdf
from .column_data.hidx import ColumnDataHidx
from .column_data.dictionary import ColumnDataDictionary
from .abf.backup_log import BackupLog
from .abf.virtual_directory import VirtualDirectory
from kaitaistruct import KaitaiStream
from .utils import get_data_slice
import io
import numpy as np
import pandas as pd
from decimal import Decimal
from .abf.data_model import DataModel

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import os
import xmhuffman

# xmhuffman v0.3.0+ decodes a whole page inside one `with nogil:` block
# (xmh_decode_page), so concurrent ThreadPoolExecutor calls now scale with
# physical cores. Threshold avoids pool spin-up cost for small dictionaries.
_PARALLEL_PAGE_THRESHOLD = 16
_MAX_WORKERS = min(os.cpu_count() or 1, 8)

# Compression class IDs from the dictionary format (character_set_type_identifier):
#   0x000aba91 = charset-based Huffman — strings are single-byte (encoded per the
#                character_set_used byte, commonly ANSI/latin-1 for Latin scripts).
#   0x000aba92 = general Huffman — Huffman tree operates on raw bytes whose sequence
#                is UTF-16LE; no character_set_used field.
_HUFFMAN_CHARSET_BASED = 0x000aba91  # single-byte charset Huffman (latin-1 output)
_HUFFMAN_GENERAL       = 0x000aba92  # UTF-16LE bytes via general Huffman


def _decode_compressed_page(args):
    """Run xmhuffman.decode_page + per-string charset decode for one page.

    Pure function so it can be submitted to a ThreadPoolExecutor without
    sharing any mutable state. The kernel releases the GIL, so multiple
    instances of this run in parallel; only the trailing ``bytes.decode``
    list-comprehension is GIL-bound.
    """
    bitstream, encode_array, offsets, total_bits, is_general, charset_byte = args
    if is_general:
        decoded = xmhuffman.decode_page(
            bitstream, encode_array, offsets, total_bits, swap=True,
        )
        return [b[:len(b) & ~1].decode('utf-16-le', errors='ignore') for b in decoded]
    if charset_byte == 0:
        decoded = xmhuffman.decode_page(
            bitstream, encode_array, offsets, total_bits, swap=True,
        )
        return [b.decode('latin-1') for b in decoded]
    decoded = xmhuffman.decode_page(
        bitstream, encode_array, offsets, total_bits, swap=True,
        charset_mode='single', charset_byte=charset_byte,
    )
    return [b.decode('utf-16-le') for b in decoded]

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
            # its declared 'records' (from the column's XML metadata —
            # idfmeta SS.row_count for PBIX, XMColumnSegment.Records for XLSX).
            #
            # Trailing primary_segment slots SHOULD be zero-padded per
            # MS-XLDM §2.3.1.1 ("Any unused trailing bytes within a segment
            # are padded with zeros"), in which case summing every repeat_value
            # would be harmless. Some XLSX Power Pivot writers leave stale
            # memory there instead — observed e.g. on Metrics.Sub Category ID,
            # where a single garbage slot held repeat_value=4_294_967_295 and
            # blindly summing produced a 32 GB allocation. The cap keeps us
            # correct under both spec-compliant and spec-deviant padding.
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

            # Plan pass: assign each page a base index and collect work items.
            # Compressed pages dominate; their decode releases the GIL inside
            # the xmhuffman kernel, so they fan out across a thread pool.
            # Uncompressed pages are rare and cheap; we fill them inline.
            compressed_tasks = []  # (base_index, args_for_worker)
            for page_id, page in enumerate(pages):
                if page.page_compressed:
                    if page_id not in record_handles_map:
                        continue
                    cs = page.string_store
                    offsets = record_handles_map[page_id]
                    is_general = cs.character_set_type_identifier == _HUFFMAN_GENERAL
                    charset_byte = 0 if is_general else cs.character_set_used
                    args = (
                        bytes(cs.compressed_string_buffer),
                        bytes(cs.encode_array),
                        offsets,
                        cs.store_total_bits,
                        is_general,
                        charset_byte,
                    )
                    compressed_tasks.append((index, args))
                    index += len(offsets)
                else:
                    strings = self._extract_strings(page.string_store.uncompressed_character_buffer)
                    for token in strings:
                        hashtable[index] = token
                        index += 1

            if not compressed_tasks:
                return hashtable

            if len(compressed_tasks) < _PARALLEL_PAGE_THRESHOLD:
                # Serial path: avoids ThreadPoolExecutor spin-up cost on
                # small dictionaries (few pages, e.g. XLSX, small PBIX).
                for base, args in compressed_tasks:
                    for off, s in enumerate(_decode_compressed_page(args)):
                        hashtable[base + off] = s
            else:
                with ThreadPoolExecutor(max_workers=_MAX_WORKERS) as ex:
                    for base, result in zip(
                        (t[0] for t in compressed_tasks),
                        ex.map(_decode_compressed_page, (t[1] for t in compressed_tasks)),
                    ):
                        for off, s in enumerate(result):
                            hashtable[base + off] = s

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

        
    def _handle_special_cases(self, column_data, semantic_type, column_name=None):
        if semantic_type == 'Date':
            try:
                return pd.to_datetime(column_data, unit='D', origin='1899-12-30')
            except pd.errors.OutOfBoundsDatetime:
                # Day-counts outside pandas' datetime64[ns] range
                # (~1677..2262). Fall back to datetime64[s] resolution, which
                # covers up to year 9999, so far-future dates that DAX
                # surfaces verbatim (e.g. 8525-01-01) round-trip as real
                # Timestamps instead of being dropped.
                days = pd.to_numeric(column_data, errors='coerce').to_numpy(dtype='float64')
                mask = ~np.isnan(days)
                secs = np.zeros(len(days), dtype='int64')
                secs[mask] = np.rint(days[mask] * 86400.0).astype('int64')
                origin = np.datetime64('1899-12-30T00:00:00', 's')
                out = np.full(len(days), np.datetime64('NaT', 's'), dtype='datetime64[s]')
                out[mask] = origin + secs[mask].astype('timedelta64[s]')
                return pd.Series(out, index=column_data.index)
        if semantic_type == 'Currency':
            return column_data.apply(lambda x: Decimal(x)/10000 if pd.notnull(x) else None)
        return column_data

    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table."""
        table_metadata_df = self._meta.schema_df[self._meta.schema_df['TableName'] == table_name]
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():
            col_name = column_metadata["ColumnName"]
            try:
                meta = self._meta.get_segment_meta(column_metadata)
                column_data = self._get_column_data(column_metadata, meta)
                column_data = self._handle_special_cases(column_data, column_metadata["SemanticType"], col_name)
            except Exception as e:
                raise type(e)(
                    f"[pbixray] while decoding column {table_name!r}.{col_name!r} "
                    f"(SemanticType={column_metadata['SemanticType']!r}): {e}"
                ) from e

            pandas_dtype = column_metadata["PandasDataType"] or "object"
            # pandas doesn't support Decimal natively; keep as object
            if pandas_dtype == 'decimal.Decimal':
                pandas_dtype = 'object'
            try:
                dataframe_data[column_metadata["ColumnName"]] = column_data.astype(pandas_dtype)
            except (TypeError, ValueError):
                dataframe_data[column_metadata["ColumnName"]] = column_data

        return pd.DataFrame(dataframe_data)
