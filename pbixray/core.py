# ---------- IMPORTS ----------

from .unpack import PbixUnpacker
from .meta.metadata_query import MetadataQuery
from .meta.sqlite_handler import SQLiteHandler
from . import decode
import pandas as pd


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


# ---------- MAIN CLASS ----------

class PBIXRay:
    def __init__(self, file_path):
        unpacker = PbixUnpacker(file_path)
        self._file_log = unpacker.file_log
        self._decompressed_data = unpacker.decompressed_data

        self._load_metadata()
        self._compute_statistics()

    def _load_metadata(self):
        """Loads metadata for the given PBIX file."""
        sqliteBuffer = self._get_data_slice('metadata.sqlitedb')
        sqliteHandler = SQLiteHandler(sqliteBuffer)
        self._meta = MetadataQuery(sqliteHandler)

    def _compute_statistics(self):
        """Computes statistics from the metadata schema."""
        self._stats = self._meta.schema_df[['TableName', 'ColumnName', 'Cardinality']].copy()
        self._stats = self._stats.assign(
            Dictionary=self._meta.schema_df['Dictionary'].map(self._get_file_size_from_log),
            HashIndex=self._meta.schema_df['HIDX'].map(self._get_file_size_from_log),
            DataSize=self._meta.schema_df['IDF'].map(self._get_file_size_from_log)
        )

    def _get_file_size_from_log(self, file_name):
        """Utility to get the size of a file from the log using 'FileName'."""
        file_ref = next((x for x in self._file_log if x['FileName'] == file_name), None)
        return file_ref['Size'] if file_ref else 0

    def _get_data_slice(self, file_name):
        """Gets a data slice based on a file name from the file log."""
        file_ref = next((x for x in self._file_log if x['FileName'] == file_name), None)
        if not file_ref:
            raise ValueError(f"File reference not found for filename: {file_name}.")
        return self._decompressed_data[file_ref['m_cbOffsetHeader']:file_ref['m_cbOffsetHeader'] + file_ref['Size']]

    def _get_column_data(self, column_metadata, meta):
        """Extracts column data based on the given column metadata and meta information."""
        if pd.notnull(column_metadata["Dictionary"]):
            dictionary_buffer = self._get_data_slice(column_metadata["Dictionary"])
            dictionary = decode.read_dictionary(dictionary_buffer, min_data_id=meta['min_data_id'])
            data_slice = self._get_data_slice(column_metadata["IDF"])
            return pd.Series(decode.read_rle_bit_packed_hybrid(data_slice, meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])).map(dictionary)
        elif pd.notnull(column_metadata["HIDX"]):
            data_slice = self._get_data_slice(column_metadata["IDF"])
            return pd.Series(decode.read_rle_bit_packed_hybrid(data_slice, meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])).add(column_metadata["BaseId"]) / column_metadata["Magnitude"]
        else:
            raise ValueError(f"Neither dictionary nor hidx found for column {column_metadata['ColumnName']} in table.")

    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table."""
        table_metadata_df = self._meta.schema_df[self._meta.schema_df['TableName'] == table_name]
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():
            idfmeta_buffer = self._get_data_slice(column_metadata["IDF"] + 'meta')
            meta = decode.read_idfmeta(idfmeta_buffer)
            
            column_data = self._get_column_data(column_metadata, meta)
            pandas_dtype = AMO_PANDAS_TYPE_MAPPING.get(column_metadata["DataType"], "object")  # default to object if no mapping is found
            dataframe_data[column_metadata["ColumnName"]] = column_data.astype(pandas_dtype)

        return pd.DataFrame(dataframe_data)

    # ---------- PROPERTIES ----------

    @property   
    def tables(self):
        return self._meta.schema_df['TableName'].unique()
    
    @property
    def statistics(self):
        return self._stats
    
    @property
    def power_query(self):
        return self._meta.m_df
    
    @property
    def dax_tables(self):
        return self._meta.dax_tables_df
    
    @property
    def dax_measures(self):
        return self._meta.dax_measures_df
    
    @property
    def metadata(self):
        return self._meta.metadata_df
    
    @property
    def size(self):
        return sum([x['Size'] for x in self._file_log])
    
    @property
    def schema(self):
        return  pd.DataFrame({
            'TableName': self._meta.schema_df['TableName'],
            'ColumnName': self._meta.schema_df['ColumnName'],
            'PandasDataType': self._meta.schema_df['DataType'].map(AMO_PANDAS_TYPE_MAPPING).fillna('object')
        })
