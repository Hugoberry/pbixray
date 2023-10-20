from ..unpack import PbixUnpacker
from ..meta.metadata_query import MetadataQuery
from ..meta.sqlite_handler import SQLiteHandler
import pandas as pd
from .. import decode
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

    def get_table(self, table_name):
        table_metadata_df = self._metadata.schema_df[self._metadata.schema_df['TableName'] == table_name]
        dataframe_data = {}

        for _, column_metadata in table_metadata_df.iterrows():
            # Read the IDF file
            idfmeta_path = column_metadata["IDF"]+'meta'
            idfmeta_ref = [x for x in self._file_log if x['FileName'] == idfmeta_path][0]
            meta = decode.read_idfmeta(self._decompressed_data[idfmeta_ref['m_cbOffsetHeader']:idfmeta_ref['m_cbOffsetHeader']+idfmeta_ref['Size']])

            # Read the IDF file
            idf_ref = [x for x in self._file_log if x['FileName'] == column_metadata["IDF"]][0]
            idf_bufer = self._decompressed_data[idf_ref['m_cbOffsetHeader']:idf_ref['m_cbOffsetHeader']+idf_ref['Size']]
            idf = decode.read_rle_bit_packed_hybrid(idf_bufer, meta['count_bit_packed'], meta['min_data_id'], meta['bit_width'])
            idf_series = pd.Series(idf)  # Convert the list to a pandas Series

            # Check if we need to use dictionary or hidx
            if pd.notnull(column_metadata["Dictionary"]):
                dictionary_ref = [x for x in self._file_log if x['FileName'] == column_metadata["Dictionary"]][0]
                dictionary_buffer = self._decompressed_data[dictionary_ref['m_cbOffsetHeader']:dictionary_ref['m_cbOffsetHeader']+dictionary_ref['Size']]
                dictionary = decode.read_dictionary(dictionary_buffer, min_data_id=meta['min_data_id'])
                dataframe_data[column_metadata["ColumnName"]] = idf_series.map(dictionary)

            elif pd.notnull(column_metadata["HIDX"]):
                dataframe_data[column_metadata["ColumnName"]] = idf_series.add(column_metadata["BaseId"])/column_metadata["Magnitude"]
            else:
                print(f"Neither dictionary nor hidx found for column {column_metadata['ColumnName']} in table {table_name}.")
                return None

        df = pd.DataFrame(dataframe_data)
        return df


    # You can also include some utility methods for users to easily access certain functionalities:
    def list_tables(self):
        return self._metadata.schema_df['TableName'].unique()

    def list_columns(self, table_name):
        columns = self._metadata.schema_df[self._metadata.schema_df['TableName'] == table_name]['ColumnName']
        return columns.unique()


