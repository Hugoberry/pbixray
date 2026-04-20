# ---------- IMPORTS ----------

from .pbix_unpacker import PbixUnpacker
from .vertipaq_decoder import VertiPaqDecoder
from .meta.metadata_handler import MetadataHandler

# ---------- MAIN CLASS ----------

class PBIXRay:
    def __init__(self, file_path):
        unpacker = PbixUnpacker(file_path)

        self._metadata_handler = MetadataHandler(unpacker.data_model)
        self._vertipaq_decoder = VertiPaqDecoder(self._metadata_handler.metadata, unpacker.data_model)

    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table."""
        return self._vertipaq_decoder.get_table(table_name)

    # ---------- PROPERTIES ----------

    @property
    def tables(self):
        return self._metadata_handler.tables

    @property
    def statistics(self):
        return self._metadata_handler.stats

    @property
    def power_query(self):
        return self._metadata_handler.metadata.m_df

    @property
    def m_parameters(self):
        return self._metadata_handler.metadata.m_parameters_df

    @property
    def dax_tables(self):
        return self._metadata_handler.metadata.dax_tables_df

    @property
    def dax_measures(self):
        return self._metadata_handler.metadata.dax_measures_df

    @property
    def dax_columns(self):
        return self._metadata_handler.metadata.dax_columns_df

    @property
    def metadata(self):
        return self._metadata_handler.metadata.metadata_df

    @property
    def size(self):
        return self._metadata_handler.size

    @property
    def schema(self):
        return self._metadata_handler.schema

    @property
    def relationships(self):
        return self._metadata_handler.metadata.relationships_df

    @property
    def rls(self):
        return self._metadata_handler.metadata.rls_df

    # -------------------------------------------------------------------------
    # TMSCHEMA_* DMV equivalents
    # -------------------------------------------------------------------------

    @property
    def tmschema_model(self):
        return self._metadata_handler.metadata.model_df

    @property
    def tmschema_tables(self):
        """Full table metadata (SystemFlags=0). Use .tables for a simple name list."""
        return self._metadata_handler.metadata.tables_df

    @property
    def tmschema_columns(self):
        return self._metadata_handler.metadata.columns_df

    @property
    def tmschema_partitions(self):
        return self._metadata_handler.metadata.partitions_df

    @property
    def tmschema_hierarchies(self):
        return self._metadata_handler.metadata.hierarchies_df

    @property
    def tmschema_levels(self):
        return self._metadata_handler.metadata.levels_df

    @property
    def tmschema_datasources(self):
        return self._metadata_handler.metadata.datasources_df

    @property
    def tmschema_perspectives(self):
        return self._metadata_handler.metadata.perspectives_df

    @property
    def tmschema_perspective_tables(self):
        return self._metadata_handler.metadata.perspective_tables_df

    @property
    def tmschema_perspective_columns(self):
        return self._metadata_handler.metadata.perspective_columns_df

    @property
    def tmschema_perspective_hierarchies(self):
        return self._metadata_handler.metadata.perspective_hierarchies_df

    @property
    def tmschema_perspective_measures(self):
        return self._metadata_handler.metadata.perspective_measures_df

    @property
    def tmschema_kpis(self):
        return self._metadata_handler.metadata.kpis_df

    @property
    def tmschema_annotations(self):
        return self._metadata_handler.metadata.annotations_df

    @property
    def tmschema_extended_properties(self):
        return self._metadata_handler.metadata.extended_properties_df

    @property
    def tmschema_cultures(self):
        return self._metadata_handler.metadata.cultures_df

    @property
    def tmschema_translations(self):
        return self._metadata_handler.metadata.translations_df

    @property
    def tmschema_linguistic_metadata(self):
        return self._metadata_handler.metadata.linguistic_metadata_df

    @property
    def tmschema_query_groups(self):
        return self._metadata_handler.metadata.query_groups_df

    @property
    def tmschema_calculation_groups(self):
        return self._metadata_handler.metadata.calculation_groups_df

    @property
    def tmschema_calculation_items(self):
        return self._metadata_handler.metadata.calculation_items_df

    @property
    def tmschema_calculation_expressions(self):
        return self._metadata_handler.metadata.calculation_expressions_df

    @property
    def tmschema_variations(self):
        return self._metadata_handler.metadata.variations_df

    @property
    def tmschema_attribute_hierarchies(self):
        return self._metadata_handler.metadata.attribute_hierarchies_df

    @property
    def tmschema_sets(self):
        return self._metadata_handler.metadata.sets_df

    @property
    def tmschema_refresh_policies(self):
        return self._metadata_handler.metadata.refresh_policies_df

    @property
    def tmschema_detail_rows_definitions(self):
        return self._metadata_handler.metadata.detail_rows_definitions_df

    @property
    def tmschema_format_string_definitions(self):
        return self._metadata_handler.metadata.format_string_definitions_df

    @property
    def tmschema_functions(self):
        return self._metadata_handler.metadata.functions_df

    @property
    def tmschema_calendars(self):
        return self._metadata_handler.metadata.calendars_df

    @property
    def tmschema_calendar_column_groups(self):
        return self._metadata_handler.metadata.calendar_column_groups_df

    @property
    def tmschema_calendar_column_refs(self):
        return self._metadata_handler.metadata.calendar_column_refs_df

    @property
    def tmschema_alternate_of(self):
        return self._metadata_handler.metadata.alternate_of_df

    @property
    def tmschema_related_column_details(self):
        return self._metadata_handler.metadata.related_column_details_df

    @property
    def tmschema_group_by_columns(self):
        return self._metadata_handler.metadata.group_by_columns_df

    @property
    def tmschema_binding_info(self):
        return self._metadata_handler.metadata.binding_info_df

    @property
    def tmschema_analytics_ai_metadata(self):
        return self._metadata_handler.metadata.analytics_ai_metadata_df

    @property
    def tmschema_data_coverage_definitions(self):
        return self._metadata_handler.metadata.data_coverage_definitions_df

    @property
    def tmschema_role_memberships(self):
        return self._metadata_handler.metadata.role_memberships_df
