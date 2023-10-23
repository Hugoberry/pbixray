from .unpack import PbixUnpacker
from .meta.metadata_query import MetadataQuery
from .meta.sqlite_handler import SQLiteHandler
from . import decode
import pandas as pd

AMO_PANDAS_TYPE_MAPPING ={
    2: 'string',
    6: 'int64',
    8: 'float64',
    9: 'datetime64[ns]',
    10: 'decimal.Decimal',
    11: 'bool',
    17: 'bytes'
}

class PBIXRay:
    def __init__(self, file_path):
        unpacker = PbixUnpacker(file_path)

        self._file_log = unpacker.file_log
        self._decompressed_data = unpacker.decompressed_data
        
        self._load_metadata()
        self._compute_statistics()

    def _load_metadata(self):
        #sqliteRef = self._file_log[-1]
        #sqliteRef is the entry in _file_log with the Path metadata.sqlite
        sqliteRef = [x for x in self._file_log if x['Path'] == 'metadata.sqlitedb'][0]
        sqliteHandler = SQLiteHandler(self._decompressed_data[sqliteRef['m_cbOffsetHeader']:sqliteRef['m_cbOffsetHeader']+sqliteRef['Size']])
        self._meta = MetadataQuery(sqliteHandler)
    
    def _compute_statistics(self):
        # Extract required columns from schema_df
        self._stats = self._meta.schema_df[['TableName', 'ColumnName', 'Cardinality']].copy()

        # Map the file sizes using the '_get_file_size_from_log' method
        self._stats = self._stats.assign(
            Dictionary=self._meta.schema_df['Dictionary'].map(self._get_file_size_from_log),
            HashIndex=self._meta.schema_df['HIDX'].map(self._get_file_size_from_log),
            DataSize=self._meta.schema_df['IDF'].map(self._get_file_size_from_log)
        )

    def _get_file_size_from_log(self, file_name):
        """Utility method to get the size of a file from self._file_log using 'FileName'."""
        matched_entry = next((entry for entry in self._file_log if entry['FileName'] == file_name), None)
        if matched_entry:
            return matched_entry['Size']
        return 0  # Returns 0 if no match is found



    def _get_data_slice(self, filename):
        file_ref = next((x for x in self._file_log if x['FileName'] == filename), None)
        if not file_ref:
            raise ValueError(f"File reference not found for filename: {filename}.")
        return self._decompressed_data[file_ref['m_cbOffsetHeader']:file_ref['m_cbOffsetHeader'] + file_ref['Size']]

    def _get_column_data(self, column_metadata, meta):
        if pd.notnull(column_metadata["Dictionary"]):
            dictionary_buffer = self._get_data_slice(column_metadata["Dictionary"])
            dictionary = decode.read_dictionary(dictionary_buffer, min_data_id=meta['min_data_id'])
            return pd.Series(decode.read_rle_bit_packed_hybrid(self._get_data_slice(column_metadata["IDF"]), 
                                   meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])).map(dictionary)
        
        elif pd.notnull(column_metadata["HIDX"]):
            return pd.Series(decode.read_rle_bit_packed_hybrid(self._get_data_slice(column_metadata["IDF"]), 
                                   meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])).add(column_metadata["BaseId"])/column_metadata["Magnitude"]
        
        else:
            raise ValueError(f"Neither dictionary nor hidx found for column {column_metadata['ColumnName']} in table.")

    def get_table(self, table_name):
        table_metadata_df = self._meta.schema_df[self._meta.schema_df['TableName'] == table_name]
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():
            idfmeta_buffer = self._get_data_slice(column_metadata["IDF"] + 'meta')
            meta = decode.read_idfmeta(idfmeta_buffer)
            
            column_data = self._get_column_data(column_metadata, meta)

            # Convert the series data type using the mapping
            pandas_dtype = AMO_PANDAS_TYPE_MAPPING.get(column_metadata["DataType"], "object")  # default to object if no mapping is found
            column_data = column_data.astype(pandas_dtype)

            dataframe_data[column_metadata["ColumnName"]] = column_data

        return pd.DataFrame(dataframe_data)

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
