# ---------- IMPORTS ----------

from .loader import DataModelLoader
from .vertipaq_decoder import VertiPaqDecoder
from .meta import Metadata

# ---------- MAIN CLASS ----------

class PBIXRay:
    def __init__(self, file_path):
        loader = DataModelLoader(file_path)

        self._metadata = Metadata(loader.data_model)
        self._vertipaq_decoder = VertiPaqDecoder(self._metadata.source, loader.data_model)

    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table."""
        return self._vertipaq_decoder.get_table(table_name)

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
