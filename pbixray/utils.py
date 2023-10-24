# ---------- CONSTANTS ----------
AMO_PANDAS_TYPE_MAPPING = {
    2: 'string',
    6: 'int64',
    8: 'float64',
    9: 'datetime64[ns]',
    10: 'decimal.Decimal',
    11: 'bool',
    17: 'bytes'
}

# ---------- UTILITY FUNCTIONS ----------
def get_data_slice(file_log, decompressed_data, file_name):
    """Gets a data slice based on a file name from the file log."""
    file_ref = next((x for x in file_log if x['FileName'] == file_name), None)
    if not file_ref:
        raise ValueError(f"File reference not found for filename: {file_name}.")
    return decompressed_data[file_ref['m_cbOffsetHeader']:file_ref['m_cbOffsetHeader'] + file_ref['Size']]
