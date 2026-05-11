from .sqlite_source import SqliteMetadataSource
from .xml_source import XmlMetadataSource
from ..utils import AMO_PANDAS_TYPE_MAPPING, get_data_slice
import pandas as pd
from ..abf.data_model import DataModel, Container


class Metadata:
    """Facade that loads the appropriate metadata source for a data model and
    exposes derived views (schema, statistics, size)."""

    def __init__(self, data_model: DataModel):
        self._data_model = data_model
        self._load_metadata()
        self._compute_statistics()

    def _load_metadata(self):
        if self._data_model.container == Container.XLSX:
            self._meta = XmlMetadataSource(self._data_model)
        else:
            sqlite_buffer = get_data_slice(self._data_model, 'metadata.sqlitedb')
            self._meta = SqliteMetadataSource(sqlite_buffer)

    def _compute_statistics(self):
        """Computes statistics from the metadata schema."""
        self._stats = self._meta.schema_df[['TableName', 'ColumnName', 'Cardinality']].copy()
        self._stats = self._stats.assign(
            Dictionary=self._meta.schema_df['Dictionary'].map(self._get_file_size_from_log),
            HashIndex=self._meta.schema_df['HIDX'].map(self._get_file_size_from_log),
            DataSize=self._meta.schema_df['IDF'].map(self._get_file_size_from_log),
            ModifiedTime=self._meta.schema_df['ModifiedTime'],
            StructureModifiedTime=self._meta.schema_df['StructureModifiedTime'],
        )

    def _get_file_size_from_log(self, file_name):
        file_ref = next((x for x in self._data_model.file_log if x['FileName'] == file_name), None)
        return file_ref['Size'] if file_ref else 0

    @property
    def source(self):
        return self._meta

    @property
    def stats(self):
        return self._stats

    @property
    def size(self):
        return sum(x['Size'] for x in self._data_model.file_log)

    @property
    def schema(self):
        # For XLSX files, DataType is already a pandas type string from _map_ssas_type_to_pandas
        # For PBIX files, DataType is a numeric code that needs mapping through AMO_PANDAS_TYPE_MAPPING
        if self._data_model.container == Container.XLSX:
            return pd.DataFrame({
                'TableName': self._meta.schema_df['TableName'],
                'ColumnName': self._meta.schema_df['ColumnName'],
                'PandasDataType': self._meta.schema_df['DataType'],
            })
        else:
            return pd.DataFrame({
                'TableName': self._meta.schema_df['TableName'],
                'ColumnName': self._meta.schema_df['ColumnName'],
                'PandasDataType': self._meta.schema_df['DataType'].map(AMO_PANDAS_TYPE_MAPPING).fillna('object'),
            })

    @property
    def tables(self):
        return self._meta.schema_df['TableName'].unique()

    @property
    def dax_measures(self):
        return self._meta.dax_measures_df

    @property
    def dax_tables(self):
        return self._meta.dax_tables_df

    @property
    def dax_columns(self):
        return self._meta.dax_columns_df

    @property
    def relationships(self):
        return self._meta.relationships_df
