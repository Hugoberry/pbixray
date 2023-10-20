from .unpack import PbixUnpacker
from .meta.metadata_query import MetadataQuery
from .meta.sqlite_handler import SQLiteHandler
from . import decode
import pandas as pd

class PBIXRay:
    def __init__(self, file_path):
        self.file_path = file_path
        self.unpacker = PbixUnpacker(self.file_path)

        self._file_log = self.unpacker.file_log
        self._decompressed_data = self.unpacker.decompressed_data

        self.tables = self._load_metadata()

    def _load_metadata(self):
        #sqliteRef = self._file_log[-1]
        #sqliteRef is the entry in _file_log with the Path metadata.sqlite
        sqliteRef = [x for x in self._file_log if x['Path'] == 'metadata.sqlitedb'][0]
        sqliteHandler = SQLiteHandler(self._decompressed_data[sqliteRef['m_cbOffsetHeader']:sqliteRef['m_cbOffsetHeader']+sqliteRef['Size']])
        self._metadata = MetadataQuery(sqliteHandler)

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
        table_metadata_df = self._metadata.schema_df[self._metadata.schema_df['TableName'] == table_name]
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():
            idfmeta_buffer = self._get_data_slice(column_metadata["IDF"] + 'meta')
            meta = decode.read_idfmeta(idfmeta_buffer)
            
            column_data = self._get_column_data(column_metadata, meta)
            dataframe_data[column_metadata["ColumnName"]] = column_data

        return pd.DataFrame(dataframe_data)


    # You can also include some utility methods for users to easily access certain functionalities:
    def list_tables(self):
        return self._metadata.schema_df['TableName'].unique()

    def list_columns(self, table_name):
        columns = self._metadata.schema_df[self._metadata.schema_df['TableName'] == table_name]['ColumnName']
        return columns.unique()


