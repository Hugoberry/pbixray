from .column_data.idf import ColumnDataIdf
from .column_data.idfmeta import IdfmetaParser
from .column_data.hidx import ColumnDataHidx
from .column_data.dictionary import ColumnDataDictionary
from .abf.backup_log import BackupLog
from .abf.virtual_directory import VirtualDirectory
from kaitaistruct import KaitaiStream
import io

def read_bitpacked(sub_segment, bit_width, min_data_id):
    mask = (1 << bit_width) - 1
    res = []
    for u8le in sub_segment:
        for _ in range(64 // bit_width):
            res.append((min_data_id + (u8le & mask)))
            u8le >>= bit_width

    return res

def extract_strings(buffer):
    """Extract zero-terminated strings from buffer."""
    strings = buffer.split('\0')
    return strings[:-1]  # remove the last empty string

def read_rle_bit_packed_hybrid(buffer, entries, min_data_id, bit_width ):
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
                bitpacked_values = read_bitpacked(column_data.segments[0].sub_segment,bit_width, min_data_id)

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

def read_idfmeta(buffer):
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

def read_hash_table(buffer):
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

def read_dictionary(buffer,min_data_id):
    with io.BytesIO(buffer) as f:
        dictionary = ColumnDataDictionary.from_io(f)

    # Extract data based on the dictionary type
    if dictionary.dictionary_type == ColumnDataDictionary.DictionaryTypes.xm_type_string:
        # Create a hashtable for string-based dictionaries
        hashtable = {}
        
        page = dictionary.data.dictionary_pages  # Accessing the singular dictionary_page
        strings = extract_strings(page.string_store.uncompressed_character_buffer)
        hashtable = {i: val for i, val in enumerate(strings, start=min_data_id)}

        return hashtable

    elif dictionary.dictionary_type in [ColumnDataDictionary.DictionaryTypes.xm_type_long, ColumnDataDictionary.DictionaryTypes.xm_type_real]:
        # Return the values of vectorOfVectorsInfo
        vector_values = dictionary.data.vector_of_vectors_info.values
        return {i: val for i, val  in enumerate(vector_values, start=min_data_id)}

    return None

def get_storage_path_and_log_details(backup_log: BackupLog, virtual_directory: VirtualDirectory, path_suffix:str) -> tuple:
    storage_path = None
    size = None
    offset = None
    
    # Find the storage path
    for file in  virtual_directory.FileGroups[1].FileList:
        if file.Path.endswith(path_suffix):
            storage_path = file.StoragePath
            break

    # Find the log details
    for log in backup_log.BackupFiles:
        if log.Path == storage_path:
            size = log.Size
            offset = log.m_cbOffsetHeader
            break

    return size, offset