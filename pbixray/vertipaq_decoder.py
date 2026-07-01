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

from collections import defaultdict, namedtuple
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

# Decoded dictionary: ``values`` maps data_id -> value; ``is_string`` tells
# whether values came from a string store (only those may become Categorical).
_DecodedDictionary = namedtuple('_DecodedDictionary', ['values', 'is_string'])


class _DictionaryLookup:
    """Data-id-ordered dictionary values plus the id→position mapping.

    ``categories`` holds the values ordered by data_id. Data ids are
    contiguous by construction (assigned sequentially from ``dict_min`` while
    decoding pages), so the common lookup is a dense ``id - dict_min``;
    ``key_arr`` is only set in the defensive non-contiguous case, where
    lookups go through ``np.searchsorted``.
    """

    def __init__(self, values):
        keys = sorted(values)
        self.categories = np.empty(len(keys), dtype=object)
        for i, k in enumerate(keys):
            self.categories[i] = values[k]
        self.dict_min = keys[0] if keys else 0
        if keys and keys[-1] - self.dict_min + 1 != len(keys):
            self.key_arr = np.array(keys, dtype=np.int64)
        else:
            self.key_arr = None
        self._categorical = None

    def categorical_dtype_and_inverse(self):
        """Cached ``(CategoricalDtype, inverse)`` for Categorical output.

        Real-world dictionaries can carry duplicate values (observed in the
        wild), which ``CategoricalDtype`` rejects; in that case ``inverse``
        maps each position of ``categories`` to its first occurrence in the
        deduplicated dtype. ``inverse`` is None when values are unique.
        Building the dtype once also means per-chunk ``from_codes`` calls
        skip re-validating the categories.
        """
        if self._categorical is None:
            inverse, uniques = pd.factorize(self.categories)
            if len(uniques) == len(self.categories):
                self._categorical = (pd.CategoricalDtype(self.categories), None)
            else:
                self._categorical = (pd.CategoricalDtype(uniques), inverse.astype(np.int64))
        return self._categorical


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

    def _parse_idf(self, buffer):
        """Parses an .idf buffer into its Kaitai struct (eager, one pass)."""
        with io.BytesIO(buffer) as f:
            return ColumnDataIdf(KaitaiStream(f))

    def _segment_real_repeats(self, segment, seg_meta):
        """Per-RLE-entry output counts for one segment, capped at its
        declared 'records' (from the column's XML metadata — idfmeta
        SS.row_count for PBIX, XMColumnSegment.Records for XLSX).

        Trailing primary_segment slots SHOULD be zero-padded per
        MS-XLDM §2.3.1.1 ("Any unused trailing bytes within a segment
        are padded with zeros"), in which case summing every repeat_value
        would be harmless. Some XLSX Power Pivot writers leave stale
        memory there instead — observed e.g. on Metrics.Sub Category ID,
        where a single garbage slot held repeat_value=4_294_967_295 and
        blindly summing produced a 32 GB allocation. The cap keeps us
        correct under both spec-compliant and spec-deviant padding.

        Returns ``(per_entry, real_len)``.
        """
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
        return per_entry, acc

    def _decode_idf_segment(self, segment, seg_meta, per_entry, real_len):
        """Decodes one segment's RLE + bit-packed hybrid into int64 data ids."""
        entries = seg_meta['count_bit_packed']
        min_data_id = seg_meta['min_data_id']
        bit_width = seg_meta['bit_width']

        vector = np.empty(real_len, dtype=np.int64)
        pos = 0

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

    def _read_rle_bit_packed_hybrid(self, buffer, segments_meta):
        column_data = self._parse_idf(buffer)
        parts = []
        for seg_idx, seg_meta in enumerate(segments_meta):
            segment = column_data.segments[seg_idx]
            per_entry, real_len = self._segment_real_repeats(segment, seg_meta)
            parts.append(self._decode_idf_segment(segment, seg_meta, per_entry, real_len))
        if not parts:
            return np.empty(0, dtype=np.int64)
        return np.concatenate(parts)

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
                return _DecodedDictionary(hashtable, is_string=True)

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

            return _DecodedDictionary(hashtable, is_string=True)
        elif dictionary.dictionary_type in [ColumnDataDictionary.DictionaryTypes.xm_type_long, ColumnDataDictionary.DictionaryTypes.xm_type_real]:
            vector_values = dictionary.data.vector_of_vectors_info.values
            values = {i: val for i, val in enumerate(vector_values, start=min_data_id)}
            return _DecodedDictionary(values, is_string=False)

        return None

    def _column_idfs(self, column_metadata):
        """Ordered list of partition IDF files for a column.

        Falls back to the single ``IDF`` when ``IDFs`` is absent/empty so any
        metadata source that predates the partition-aware schema still decodes.
        """
        idfs = column_metadata.get("IDFs") if hasattr(column_metadata, "get") else None
        if idfs is not None and len(idfs) > 0:
            return list(idfs)
        return [column_metadata["IDF"]]

    @staticmethod
    def _ids_to_codes(ids, lookup):
        """Maps data ids to 0-based category codes; unknown ids become -1.

        Ids below ``dict_min`` (e.g. the null id of nullable columns) or past
        the dictionary's end land on -1, mirroring the NaN that ``.map``
        produced for them.
        """
        if lookup.key_arr is None:
            codes = ids - lookup.dict_min
            np.putmask(codes, (codes < 0) | (codes >= len(lookup.categories)), -1)
            return codes
        pos = np.searchsorted(lookup.key_arr, ids)
        pos_clipped = np.clip(pos, 0, len(lookup.key_arr) - 1)
        return np.where(lookup.key_arr[pos_clipped] == ids, pos_clipped, -1)

    @staticmethod
    def _codes_to_series(codes, lookup, as_categorical):
        """Materializes category codes as a Series.

        Categorical keeps each distinct value stored once (codes + shared
        categories array); the default path fancy-indexes a lookup table,
        producing the same object-dtype output as the old per-row ``.map``.
        """
        if as_categorical:
            dtype, inverse = lookup.categorical_dtype_and_inverse()
            if inverse is not None:
                codes = np.where(
                    codes >= 0, inverse[np.clip(codes, 0, len(inverse) - 1)], -1
                )
            return pd.Series(pd.Categorical.from_codes(codes, dtype=dtype))
        categories = lookup.categories
        lut = np.append(categories, np.nan)  # extra slot for missing ids
        return pd.Series(lut[np.where(codes >= 0, codes, len(categories))])

    def _get_column_data(self, column_metadata, strings_as_categorical=False):
        """Extract a column's data, concatenating all partitions in storage order.

        Each partition has its own IDF value stream and per-segment ``.idfmeta``
        (min_data_id / bit_width / records); the dictionary is shared across a
        column's partitions, so it is read once. Single-partition columns reduce
        to the original single-IDF behavior.
        """
        decoder = _ColumnDecoder(self, column_metadata)
        parts = []
        for seg_idx, seg_len in enumerate(decoder.segment_lengths()):
            seg_codes = decoder.decode_segment_codes(seg_idx)
            parts.append(decoder.slice_values(seg_codes, 0, seg_len, strings_as_categorical))
        if not parts:
            return pd.Series([], dtype=object)
        if len(parts) == 1:
            return parts[0]
        return pd.concat(parts, ignore_index=True)

        
    def _handle_special_cases(self, column_data, semantic_type, column_name=None):
        if semantic_type == 'Date':
            # Force numeric so empty / all-None / object-dtype series don't
            # trip pd.to_datetime's origin-compatibility check.
            numeric = pd.to_numeric(column_data, errors='coerce')
            try:
                return pd.to_datetime(numeric, unit='D', origin='1899-12-30')
            except pd.errors.OutOfBoundsDatetime:
                # Day-counts outside pandas' datetime64[ns] range
                # (~1677..2262). Fall back to datetime64[s] resolution, which
                # covers up to year 9999, so far-future dates that DAX
                # surfaces verbatim (e.g. 8525-01-01) round-trip as real
                # Timestamps instead of being dropped.
                days = numeric.to_numpy(dtype='float64')
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

    def _select_table_metadata(self, table_name, columns):
        """Filters schema_df to the requested table and (optionally) columns.

        Unknown column names raise a ``ValueError``; an unknown table simply
        yields an empty selection.
        """
        table_metadata_df = self._meta.schema_df[self._meta.schema_df['TableName'] == table_name]
        if columns is not None:
            available = set(table_metadata_df['ColumnName'])
            missing = [c for c in columns if c not in available]
            if missing:
                raise ValueError(
                    f"Column(s) {missing} not found in table {table_name!r}. "
                    f"Available: {sorted(available)}"
                )
            wanted = set(columns)
            table_metadata_df = table_metadata_df[table_metadata_df['ColumnName'].isin(wanted)]
        return table_metadata_df

    def _finalize_series(self, column_data, column_metadata):
        """Applies semantic-type conversion and the target pandas dtype."""
        column_data = self._handle_special_cases(
            column_data, column_metadata["SemanticType"], column_metadata["ColumnName"]
        )
        if isinstance(column_data.dtype, pd.CategoricalDtype):
            return column_data
        pandas_dtype = column_metadata["PandasDataType"] or "object"
        # pandas doesn't support Decimal natively; keep as object
        if pandas_dtype == 'decimal.Decimal':
            pandas_dtype = 'object'
        try:
            return column_data.astype(pandas_dtype)
        except (TypeError, ValueError):
            return column_data

    def get_table(self, table_name, columns=None, strings_as_categorical=False):
        """Generates a DataFrame representation of the specified table.

        When ``columns`` is provided, only those columns are decoded; unknown
        names raise a ``ValueError``. With ``strings_as_categorical`` string
        columns come back as ``pd.Categorical`` (each distinct value stored
        once) instead of object-dtype str.
        """
        table_metadata_df = self._select_table_metadata(table_name, columns)
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():
            col_name = column_metadata["ColumnName"]
            try:
                column_data = self._get_column_data(column_metadata, strings_as_categorical)
                dataframe_data[col_name] = self._finalize_series(column_data, column_metadata)
            except Exception as e:
                raise type(e)(
                    f"[pbixray] while decoding column {table_name!r}.{col_name!r} "
                    f"(SemanticType={column_metadata['SemanticType']!r}): {e}"
                ) from e

        # All columns are concatenated using the same partition (StoragePosition)
        # order, so every decoded column must have the same length; a mismatch
        # means a partition was dropped or misaligned — fail loudly rather than
        # let pandas broadcast/raise an opaque error.
        lengths = {name: len(series) for name, series in dataframe_data.items()}
        if len(set(lengths.values())) > 1:
            raise ValueError(
                f"[pbixray] column length mismatch decoding table {table_name!r}; "
                f"partitions misaligned across columns: {lengths}"
            )

        return pd.DataFrame(dataframe_data)

    def iter_table(self, table_name, columns=None, chunk_size=None, strings_as_categorical=True):
        """Yields the table as a sequence of DataFrame chunks.

        Chunks follow VertiPaq segment boundaries (partitions flattened in
        storage order); ``chunk_size`` further splits each segment into at
        most that many rows (chunks never span segments, so tail chunks may
        be shorter). Dictionaries are decoded once per column up front and
        shared across all chunks; only the current chunk's values are
        materialized.
        """
        if chunk_size is not None and chunk_size < 1:
            raise ValueError("chunk_size must be a positive integer or None")
        table_metadata_df = self._select_table_metadata(table_name, columns)
        if table_metadata_df.empty:
            return

        def _wrap(column_metadata, exc):
            return type(exc)(
                f"[pbixray] while decoding column {table_name!r}."
                f"{column_metadata['ColumnName']!r} "
                f"(SemanticType={column_metadata['SemanticType']!r}): {exc}"
            )

        decoders = []
        for _, column_metadata in table_metadata_df.iterrows():
            try:
                decoders.append(_ColumnDecoder(self, column_metadata))
            except Exception as e:
                raise _wrap(column_metadata, e) from e

        # Segments are partition row windows, so every column of a table
        # should expose identical per-segment row counts; guard against
        # malformed files rather than yielding misaligned rows.
        canonical = decoders[0].segment_lengths()
        for dec in decoders[1:]:
            lengths = dec.segment_lengths()
            if lengths != canonical:
                raise ValueError(
                    f"Segments are not row-aligned across columns of table {table_name!r}: "
                    f"{decoders[0].column_metadata['ColumnName']!r} has row counts {canonical} "
                    f"but {dec.column_metadata['ColumnName']!r} has {lengths}"
                )

        row_offset = 0
        for seg_idx, seg_len in enumerate(canonical):
            seg_codes = []
            for dec in decoders:
                try:
                    seg_codes.append(dec.decode_segment_codes(seg_idx))
                except Exception as e:
                    raise _wrap(dec.column_metadata, e) from e

            step = chunk_size or seg_len
            for lo in range(0, seg_len, step):
                hi = min(lo + step, seg_len)
                data = {}
                for dec, codes in zip(decoders, seg_codes):
                    try:
                        values = dec.slice_values(codes, lo, hi, strings_as_categorical)
                        data[dec.column_metadata["ColumnName"]] = self._finalize_series(
                            values, dec.column_metadata
                        )
                    except Exception as e:
                        raise _wrap(dec.column_metadata, e) from e
                chunk = pd.DataFrame(data)
                chunk.index = pd.RangeIndex(row_offset + lo, row_offset + hi)
                yield chunk
            row_offset += seg_len


class _ColumnDecoder:
    """Per-column decode state reused across the chunks of one table read.

    Heavy one-off work (dictionary decode, .idf parse, RLE repeat capping)
    happens in the constructor; ``decode_segment_codes`` then yields one
    segment's worth of cheap int64 codes and ``slice_values`` materializes
    any row range of it. Segments of every partition are flattened in storage
    order, matching the concatenation order of ``get_table``.
    """

    def __init__(self, decoder, column_metadata):
        self._decoder = decoder
        self.column_metadata = column_metadata

        if pd.notnull(column_metadata["Dictionary"]):
            self.mode = 'dictionary'
        elif pd.notnull(column_metadata["HIDX"]):
            self.mode = 'hidx'
        else:
            # Column has no dictionary or HIDX (e.g. empty column, all-null
            # column, or calculated column without independently stored data).
            self.mode = 'none'

        idfs = decoder._column_idfs(column_metadata)
        per_idf_meta = [
            (idf, decoder._meta.get_segment_meta(column_metadata, idf))
            for idf in idfs
        ]

        null_adjustment = 0
        if self.mode == 'dictionary':
            # Decode ids with the null-adjusted minimum while the dictionary
            # keeps the unadjusted one, so null rows land below dict_min. The
            # dictionary is shared across a column's partitions; its base
            # index is the (identical) min_data_id of the first partition.
            null_adjustment = 1 if column_metadata["IsNullable"] else 0
            dictionary_buffer = get_data_slice(decoder._data_model, column_metadata["Dictionary"])
            decoded = decoder._read_dictionary(
                dictionary_buffer, min_data_id=per_idf_meta[0][1][0]['min_data_id']
            )
            self._lookup = _DictionaryLookup(decoded.values)
            self._is_string = decoded.is_string

        # Flatten (segment struct, null-adjusted meta, capped repeats) across
        # partitions in storage order. 'none' columns have no stored .idf
        # data; only their per-segment row counts are kept — 'records' (total
        # rows), not 'count_bit_packed', which is 0 for pure-RLE segments —
        # so they stay aligned with their dictionary/HIDX peers.
        self._segments = []  # (segment | None, seg_meta, per_entry, real_len)
        for idf, segments_meta in per_idf_meta:
            if self.mode == 'none':
                for seg_meta in segments_meta:
                    self._segments.append(
                        (None, seg_meta, None, seg_meta.get('records', 0) or 0)
                    )
                continue
            parsed_idf = decoder._parse_idf(get_data_slice(decoder._data_model, idf))
            for seg_idx, seg_meta in enumerate(segments_meta):
                # The null adjustment uses this partition's own .idfmeta.
                seg_meta_dec = {**seg_meta, 'min_data_id': seg_meta['min_data_id'] - null_adjustment}
                segment = parsed_idf.segments[seg_idx]
                per_entry, real_len = decoder._segment_real_repeats(segment, seg_meta_dec)
                self._segments.append((segment, seg_meta_dec, per_entry, real_len))

    def segment_lengths(self):
        """Output row count of each segment, partitions flattened in order."""
        return [real_len for _, _, _, real_len in self._segments]

    def decode_segment_codes(self, seg_idx):
        """Decodes one segment to int64 codes/ids (8 bytes per row)."""
        if self.mode == 'none':
            return None
        segment, seg_meta, per_entry, real_len = self._segments[seg_idx]
        ids = self._decoder._decode_idf_segment(segment, seg_meta, per_entry, real_len)
        if self.mode == 'dictionary':
            return self._decoder._ids_to_codes(ids, self._lookup)
        return ids

    def slice_values(self, seg_codes, lo, hi, strings_as_categorical):
        """Materializes rows [lo, hi) of a decoded segment as a Series."""
        if self.mode == 'dictionary':
            return self._decoder._codes_to_series(
                seg_codes[lo:hi],
                self._lookup,
                strings_as_categorical and self._is_string,
            )
        if self.mode == 'hidx':
            return (
                pd.Series(seg_codes[lo:hi]).add(self.column_metadata["BaseId"])
                / self.column_metadata["Magnitude"]
            )
        return pd.Series([None] * (hi - lo))
