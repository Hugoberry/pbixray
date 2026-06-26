# ---------- IMPORTS ----------

import pandas as pd

from .loader import DataModelLoader
from .vertipaq_decoder import VertiPaqDecoder
from .meta import Metadata
from .mashup import parse_data_mashup

# ---------- MAIN CLASS ----------

class PBIXRay:
    def __init__(self, file_path, *, on_disk=False, temp_dir=None):
        """Open a PBIX/XLSX data model.

        Args:
            file_path: Path to the ``.pbix`` or ``.xlsx`` file.
            on_disk: When ``True``, the decompressed data model is spilled to a
                temporary file and memory-mapped instead of being held in a
                single in-process buffer. Use this for models whose uncompressed
                size approaches or exceeds available RAM. Default ``False``
                preserves the original fully-in-memory behavior.
            temp_dir: Directory for the spill file when ``on_disk=True``
                (defaults to the system temp directory). Ignored otherwise.
        """
        loader = DataModelLoader(file_path, on_disk=on_disk, temp_dir=temp_dir)
        self._data_model = loader.data_model
        self._connections = loader.connections
        self._data_mashup_bytes = loader.data_mashup_bytes
        self._data_mashup = None  # parsed lazily on first access

        self._metadata = Metadata(self._data_model)
        self._vertipaq_decoder = VertiPaqDecoder(self._metadata.source, self._data_model)

    def get_table(self, table_name, columns=None):
        """Generates a DataFrame representation of the specified table.

        Args:
            table_name: Name of the table to decode.
            columns: Optional list of column names to decode. When provided, only
                those columns are decoded (useful for wide tables); ``None``
                decodes every column.
        """
        return self._vertipaq_decoder.get_table(table_name, columns=columns)

    def close(self):
        """Release OS resources (memory-map / temp file, metadata connection).

        Safe to call multiple times. Only has an effect for ``on_disk=True``
        models and the metadata SQLite connection.
        """
        source = getattr(self._metadata, 'source', None)
        if source is not None and hasattr(source, 'close'):
            source.close()
        self._data_model.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False

    # ---------- PROPERTIES ----------

    @property
    def tables(self):
        return self._metadata.tables

    @property
    def statistics(self):
        return self._metadata.stats

    @property
    def power_query(self):
        return self._metadata.source.m_df

    @property
    def m_parameters(self):
        return self._metadata.source.m_parameters_df

    @property
    def dax_tables(self):
        return self._metadata.source.dax_tables_df

    @property
    def dax_measures(self):
        return self._metadata.source.dax_measures_df

    @property
    def dax_columns(self):
        return self._metadata.source.dax_columns_df

    @property
    def aggregations(self):
        """Resolved aggregation mappings as a DataFrame.

        Columns: ``AggregationTable, AggregationColumn, Summarization,
        DetailTable, DetailColumn``. One row per aggregation-table column mapped
        to its detail (base) table; ``DetailColumn`` is ``None`` for the
        "Count table rows" case. Empty (with those columns) when the model has
        no aggregations. Friendly layer over ``tmschema_alternate_of``.
        """
        return self._metadata.source.aggregations_df

    @property
    def metadata(self):
        return self._metadata.source.metadata_df

    @property
    def size(self):
        return self._metadata.size

    @property
    def schema(self):
        return self._metadata.schema

    @property
    def relationships(self):
        return self._metadata.source.relationships_df

    @property
    def connections(self):
        """Parsed entries from the report's ``Connections`` manifest (list of dicts).

        Self-contained (import) models usually return an empty list. Thin/live
        reports have no embedded model and instead raise ``LiveConnectionError``
        on construction; that exception carries the same connection details.
        """
        return self._connections

    @property
    def data_mashup(self):
        """Parsed Power Query ``DataMashup`` part, or ``None`` when absent.

        Returns a :class:`pbixray.mashup.DataMashup` with the section ``queries``
        (including parameters), the raw ``section_m`` and metadata XML. Surfaces
        the M for models — e.g. DirectQuery/native-SQL — that keep their queries
        and parameters only in the mashup rather than the AS metadata. Raises
        :class:`pbixray.exceptions.DataMashupError` if the part is malformed.
        """
        if self._data_mashup is None and self._data_mashup_bytes is not None:
            self._data_mashup = parse_data_mashup(self._data_mashup_bytes)
        return self._data_mashup

    @property
    def mashup_queries(self):
        """Power Query queries/parameters from the ``DataMashup`` as a DataFrame.

        Columns: ``Name, Kind, IsParameter, Expression, Type, DefaultValue,
        AllowedValues``. Empty (with those columns) when the file has no mashup.
        """
        columns = ['Name', 'Kind', 'IsParameter', 'Expression',
                   'Type', 'DefaultValue', 'AllowedValues']
        mashup = self.data_mashup
        if mashup is None:
            return pd.DataFrame(columns=columns)
        rows = [
            {
                'Name': q.name,
                'Kind': q.kind,
                'IsParameter': q.is_parameter,
                'Expression': q.expression,
                'Type': q.param_type,
                'DefaultValue': q.default_value,
                'AllowedValues': q.allowed_values,
            }
            for q in mashup.queries
        ]
        return pd.DataFrame(rows, columns=columns)

    @property
    def rls(self):
        return self._metadata.source.rls_df

    # -------------------------------------------------------------------------
    # TMSCHEMA_* DMV equivalents
    # -------------------------------------------------------------------------

    @property
    def tmschema_model(self):
        return self._metadata.source.model_df

    @property
    def tmschema_tables(self):
        """Full table metadata (SystemFlags=0). Use .tables for a simple name list."""
        return self._metadata.source.tables_df

    @property
    def tmschema_columns(self):
        return self._metadata.source.columns_df

    @property
    def tmschema_partitions(self):
        return self._metadata.source.partitions_df

    @property
    def tmschema_hierarchies(self):
        return self._metadata.source.hierarchies_df

    @property
    def tmschema_levels(self):
        return self._metadata.source.levels_df

    @property
    def tmschema_datasources(self):
        return self._metadata.source.datasources_df

    @property
    def tmschema_perspectives(self):
        return self._metadata.source.perspectives_df

    @property
    def tmschema_perspective_tables(self):
        return self._metadata.source.perspective_tables_df

    @property
    def tmschema_perspective_columns(self):
        return self._metadata.source.perspective_columns_df

    @property
    def tmschema_perspective_hierarchies(self):
        return self._metadata.source.perspective_hierarchies_df

    @property
    def tmschema_perspective_measures(self):
        return self._metadata.source.perspective_measures_df

    @property
    def tmschema_kpis(self):
        return self._metadata.source.kpis_df

    @property
    def tmschema_annotations(self):
        return self._metadata.source.annotations_df

    @property
    def tmschema_extended_properties(self):
        return self._metadata.source.extended_properties_df

    @property
    def tmschema_cultures(self):
        return self._metadata.source.cultures_df

    @property
    def tmschema_translations(self):
        return self._metadata.source.translations_df

    @property
    def tmschema_linguistic_metadata(self):
        return self._metadata.source.linguistic_metadata_df

    @property
    def tmschema_query_groups(self):
        return self._metadata.source.query_groups_df

    @property
    def tmschema_calculation_groups(self):
        return self._metadata.source.calculation_groups_df

    @property
    def tmschema_calculation_items(self):
        return self._metadata.source.calculation_items_df

    @property
    def tmschema_calculation_expressions(self):
        return self._metadata.source.calculation_expressions_df

    @property
    def tmschema_variations(self):
        return self._metadata.source.variations_df

    @property
    def tmschema_attribute_hierarchies(self):
        return self._metadata.source.attribute_hierarchies_df

    @property
    def tmschema_sets(self):
        return self._metadata.source.sets_df

    @property
    def tmschema_refresh_policies(self):
        return self._metadata.source.refresh_policies_df

    @property
    def tmschema_detail_rows_definitions(self):
        return self._metadata.source.detail_rows_definitions_df

    @property
    def tmschema_format_string_definitions(self):
        return self._metadata.source.format_string_definitions_df

    @property
    def tmschema_functions(self):
        return self._metadata.source.functions_df

    @property
    def tmschema_calendars(self):
        return self._metadata.source.calendars_df

    @property
    def tmschema_calendar_column_groups(self):
        return self._metadata.source.calendar_column_groups_df

    @property
    def tmschema_calendar_column_refs(self):
        return self._metadata.source.calendar_column_refs_df

    @property
    def tmschema_alternate_of(self):
        return self._metadata.source.alternate_of_df

    @property
    def tmschema_related_column_details(self):
        return self._metadata.source.related_column_details_df

    @property
    def tmschema_group_by_columns(self):
        return self._metadata.source.group_by_columns_df

    @property
    def tmschema_binding_info(self):
        return self._metadata.source.binding_info_df

    @property
    def tmschema_analytics_ai_metadata(self):
        return self._metadata.source.analytics_ai_metadata_df

    @property
    def tmschema_data_coverage_definitions(self):
        return self._metadata.source.data_coverage_definitions_df

    @property
    def tmschema_role_memberships(self):
        return self._metadata.source.role_memberships_df
