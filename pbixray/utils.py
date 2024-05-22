from .abf.data_model import DataModel

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

# ---------- UTILITY FUNCTIONS ----------
def get_data_slice(data_model:DataModel, file_name:str) -> bytes:
    """Gets a data slice based on a file name from the file log."""
    file_ref = next((x for x in data_model.file_log if x['FileName'] == file_name), None)
    if not file_ref:
        raise ValueError(f"File reference not found for filename: {file_name}.")
    # if error_code trim last 4 bytes
    if data_model.error_code:
        return data_model.decompressed_data[file_ref['m_cbOffsetHeader']:file_ref['m_cbOffsetHeader'] + file_ref['Size']-4]
    else:
        return data_model.decompressed_data[file_ref['m_cbOffsetHeader']:file_ref['m_cbOffsetHeader'] + file_ref['Size']]
