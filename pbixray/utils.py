from .abf.data_model import DataModel
import datetime
from .xpress8 import Xpress8

# ---------- CONSTANTS ----------
AMO_PANDAS_TYPE_MAPPING = {
    2: 'string',
    6: 'Int64',
    8: 'Float64',
    9: 'datetime64[ns]',
    10: 'decimal.Decimal',
    11: 'bool',
    17: 'bytes'
}

# Windows epoch start date
WINDOWS_EPOCH_START = datetime.datetime(1601, 1, 1)

# ---------- UTILITY FUNCTIONS ----------
def get_data_slice(data_model:DataModel, file_name:str) -> bytes:
    """Gets a data slice based on a file name from the file log."""
    file_ref = next((x for x in data_model.file_log if x['FileName'] == file_name), None)
    if not file_ref:
        raise ValueError(f"File reference not found for filename: {file_name}.")
    # if error_code trim last 4 bytes
    if data_model.error_code:
        raw_slice =  data_model.decompressed_data[file_ref['m_cbOffsetHeader']:file_ref['m_cbOffsetHeader'] + file_ref['Size']-4]
    else:
        raw_slice =  data_model.decompressed_data[file_ref['m_cbOffsetHeader']:file_ref['m_cbOffsetHeader'] + file_ref['Size']]

    if data_model.apply_compression:
        decompressed_data = Xpress8.decompress_chunked(raw_slice)
        
        # Validate the size of the decompressed data against the expected size from log
        if len(decompressed_data) != file_ref['SizeFromLog']:
            raise ValueError(
                f"Decompression size mismatch for file '{file_name}': "
                f"Expected {file_ref['SizeFromLog']} bytes, got {len(decompressed_data)} bytes"
            )
            
        return decompressed_data
    return raw_slice