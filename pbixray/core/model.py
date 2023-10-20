from ..unpack import PbixUnpacker
from ..meta.metadata_query import MetadataQuery
from ..meta.sqlite_handler import SQLiteHandler
import json
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
        for table in self.tables:
            if table.name == table_name:
                return table
        return None

    def model_to_arrow(self):
        # Logic to convert the entire model to an Arrow table (if applicable)
        pass

    # You can also include some utility methods for users to easily access certain functionalities:
    def list_tables(self):
        return [table.name for table in self.tables]

    def list_columns(self, table_name):
        table = self.get_table(table_name)
        return [column.name for column in table.columns] if table else []

