from .metadata_query import MetadataQuery
from .sqlite_handler import SQLiteHandler
from ..utils import AMO_PANDAS_TYPE_MAPPING, WINDOWS_EPOCH_START, get_data_slice
import pandas as pd
from ..abf.data_model import DataModel
import datetime

# ---------- METADATA HANDLER ----------

class MetadataHandler:
    def __init__(self, data_model:DataModel):
        self._data_model=data_model
        self._load_metadata()
        self._compute_statistics()
        
    def _load_metadata(self):
        """Loads metadata for the given PBIX file."""
        sqliteBuffer = get_data_slice(self._data_model,'metadata.sqlitedb')
        sqliteHandler = SQLiteHandler(sqliteBuffer)
        self._meta = MetadataQuery(sqliteHandler)
    
    def _compute_statistics(self):
        """Computes statistics from the metadata schema."""
        self._stats = self._meta.schema_df[['TableName', 'ColumnName', 'Cardinality']].copy()
        self._stats = self._stats.assign(
            Dictionary=self._meta.schema_df['Dictionary'].map(self._get_file_size_from_log),
            HashIndex=self._meta.schema_df['HIDX'].map(self._get_file_size_from_log),
            DataSize=self._meta.schema_df['IDF'].map(self._get_file_size_from_log),
            ModifiedTime=self._meta.schema_df['ModifiedTime'].apply(
                lambda x: WINDOWS_EPOCH_START + datetime.timedelta(seconds=x / 1e7)),
            StructureModifiedTime=self._meta.schema_df['StructureModifiedTime'].apply(
                lambda x: WINDOWS_EPOCH_START + datetime.timedelta(seconds=x / 1e7))
        )

    def _get_file_size_from_log(self, file_name):
        """Utility to get the size of a file from the log using 'FileName'."""
        file_ref = next((x for x in self._data_model.file_log if x['FileName'] == file_name), None)
        return file_ref['Size'] if file_ref else 0 
    
    @property
    def metadata(self):
        return self._meta
    
    @property
    def stats(self):
        return self._stats
    
    @property
    def size(self):
        return sum([x['Size'] for x in self._data_model.file_log])
    
    @property
    def schema(self):
        return  pd.DataFrame({
            'TableName': self._meta.schema_df['TableName'],
            'ColumnName': self._meta.schema_df['ColumnName'],
            'PandasDataType': self._meta.schema_df['DataType'].map(AMO_PANDAS_TYPE_MAPPING).fillna('object'),
        })

    @property   
    def tables(self):
        return self._meta.schema_df['TableName'].unique()