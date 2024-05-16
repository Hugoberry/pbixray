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
from .abf.data_model import DataModel

from .huffman import decompress_encode_array,build_huffman_tree, decode_substring
from collections import defaultdict

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

    def _read_idfmeta(self,buffer):
        """Reads idfmeta from a buffer."""
        # Use io.BytesIO to wrap the bytearray
        with io.BytesIO(buffer) as f:
            metadata = IdfmetaParser.from_io(f)
            
            # Extract the necessary data from the Kaitai Struct
            row_data = {
                'min_data_id': metadata.blocks.cp.cs.ss.min_data_id,
                'count_bit_packed': metadata.blocks.cp.cs.cs.count_bit_packed,
                'bit_width': metadata.bit_width,
            }
            
            return row_data

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
                            hashtable[min_data_id + i] = decompressed
                    del huffman_tree
                else:
                    uncompressed_store = page.string_store
                    uncompressed = uncompressed_store.uncompressed_character_buffer
                    strings = self._extract_strings(uncompressed)
                    for i, token in enumerate(strings):
                        hashtable[min_data_id + i] = token

            return hashtable
        elif dictionary.dictionary_type in [ColumnDataDictionary.DictionaryTypes.xm_type_long, ColumnDataDictionary.DictionaryTypes.xm_type_real]:
            vector_values = dictionary.data.vector_of_vectors_info.values
            return {i: val for i, val in enumerate(vector_values, start=min_data_id)}

        return None    
        
    def _get_column_data(self, column_metadata, meta):
        """Extracts column data based on the given column metadata and meta information."""
        if pd.notnull(column_metadata["Dictionary"]):
            dictionary_buffer = get_data_slice(self._data_model,column_metadata["Dictionary"])
            dictionary = self._read_dictionary(dictionary_buffer, min_data_id=meta['min_data_id'])
            data_slice = get_data_slice(self._data_model,column_metadata["IDF"])
            return pd.Series(self._read_rle_bit_packed_hybrid(data_slice, meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])).map(dictionary)
        elif pd.notnull(column_metadata["HIDX"]):
            data_slice = get_data_slice(self._data_model,column_metadata["IDF"])
            return pd.Series(self._read_rle_bit_packed_hybrid(data_slice, meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])).add(column_metadata["BaseId"]) / column_metadata["Magnitude"]
        else:
            raise ValueError(f"Neither dictionary nor hidx found for column {column_metadata['ColumnName']} in table.")
        
    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table."""
        table_metadata_df = self._meta.schema_df[self._meta.schema_df['TableName'] == table_name]
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():
            idfmeta_buffer = get_data_slice(self._data_model,column_metadata["IDF"] + 'meta')
            meta = self._read_idfmeta(idfmeta_buffer)
            
            column_data = self._get_column_data(column_metadata, meta)
            pandas_dtype = AMO_PANDAS_TYPE_MAPPING.get(column_metadata["DataType"], "object")  # default to object if no mapping is found
            dataframe_data[column_metadata["ColumnName"]] = column_data.astype(pandas_dtype)

        return pd.DataFrame(dataframe_data)