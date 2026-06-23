from .sqlite_source import SqliteMetadataSource
from .xml_source import XmlMetadataSource
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
            self._meta = SqliteMetadataSource(self._data_model)

    def _compute_statistics(self):
        """Computes statistics from the metadata schema."""
        self._stats = self._meta.schema_df[['TableName', 'ColumnName', 'Cardinality']].copy()
        data_size = self._meta.schema_df['IDFs'].map(self._sum_file_sizes_from_log) \
            if 'IDFs' in self._meta.schema_df.columns \
            else self._meta.schema_df['IDF'].map(self._get_file_size_from_log)
        self._stats = self._stats.assign(
            Dictionary=self._meta.schema_df['Dictionary'].map(self._get_file_size_from_log),
            HashIndex=self._meta.schema_df['HIDX'].map(self._get_file_size_from_log),
            # DataSize sums every partition's IDF so multi-partition columns
            # report their full on-disk data size, not just the first partition.
            DataSize=data_size,
            ModifiedTime=self._meta.schema_df['ModifiedTime'],
            StructureModifiedTime=self._meta.schema_df['StructureModifiedTime'],
        )

    def _get_file_size_from_log(self, file_name):
        file_ref = next((x for x in self._data_model.file_log if x['FileName'] == file_name), None)
        return file_ref['Size'] if file_ref else 0

    def _sum_file_sizes_from_log(self, file_names):
        """Total size of a column's IDF files across all partitions.

        ``file_names`` is the ordered ``IDFs`` list; falls back gracefully for a
        missing/non-list value (empty schema row) by treating it as no files.
        """
        if not isinstance(file_names, (list, tuple)):
            return 0
        return sum(self._get_file_size_from_log(name) for name in file_names)

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
        return self._meta.schema_df[['TableName', 'ColumnName', 'PandasDataType']].copy()

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
