import pandas as pd
import re
from datetime import datetime
from ..utils import get_data_slice
from ..xldm import (
    CubXmlLoad,
    DimensionXmlLoad,
    PartitionXmlLoad,
    MeasureGroupXmlLoad,
    MdxScriptXmlLoad,
    DataSourceXmlLoad,
    DataSourceViewXmlLoad
)
from ..xldm.xmobject import XMObjectDocument


# DataFrames that come from PBIX-only sources (M / RLS / metadata.sqlitedb DMVs)
# and have no equivalent in the XLSX XML model. Exposed as empty DataFrames so
# callers see a uniform attribute surface across both sources.
_EMPTY_DF_STUBS = (
    'm_df', 'm_parameters_df', 'metadata_df', 'rls_df',
    'model_df', 'tables_df', 'columns_df', 'partitions_df',
    'hierarchies_df', 'levels_df', 'datasources_df',
    'perspectives_df', 'perspective_tables_df', 'perspective_columns_df',
    'perspective_hierarchies_df', 'perspective_measures_df',
    'kpis_df', 'annotations_df', 'extended_properties_df',
    'cultures_df', 'translations_df', 'linguistic_metadata_df',
    'query_groups_df', 'calculation_groups_df', 'calculation_items_df',
    'calculation_expressions_df', 'variations_df', 'attribute_hierarchies_df',
    'sets_df', 'refresh_policies_df', 'detail_rows_definitions_df',
    'format_string_definitions_df', 'functions_df', 'calendars_df',
    'calendar_column_groups_df', 'calendar_column_refs_df', 'alternate_of_df',
    'related_column_details_df', 'group_by_columns_df', 'binding_info_df',
    'analytics_ai_metadata_df', 'data_coverage_definitions_df',
    'role_memberships_df',
)


class XmlMetadataSource:
    """Handles metadata extraction from XML files in XLSX Power Pivot models."""
    
    def __init__(self, data_model):
        self.data_model = data_model
        self._cube = None
        self._dimensions = {}
        self._partitions = {}
        self._measure_groups = {}
        self._mdx_script = None
        self._data_sources = {}
        self._data_source_view = None
        self._tbl_objects = {}
        
        self._parse_cube()
        self._extract_dimension_metadata()
        self._extract_partition_metadata()
        self._extract_measure_group_metadata()
        self._extract_mdx_script()
        self._extract_data_sources()
        self._extract_data_source_view()
        self._extract_tbl_metadata()
        
        self._build_schema()
        self._normalize_schema()
        self._build_dax_tables()
        self._build_dax_measures()
        self._build_dax_columns()
        self._build_relationships()
        
        # PBIX-only sources have no XML equivalent; expose empty DataFrames so
        # the MetadataSource surface is uniform.
        for attr in _EMPTY_DF_STUBS:
            setattr(self, attr, pd.DataFrame())

    def close(self):
        """No resources to release (XLSX metadata is parsed eagerly from
        already-decompressed XML). Present for interface parity with
        SqliteMetadataSource."""
        return None
    
    def _load_xml_singleton(self, pattern, parse, label):
        """Find the first file matching ``pattern`` and parse it; return the
        parsed object or ``None``. ``parse`` takes a decoded XML string."""
        for entry in self.data_model.file_log:
            if pattern.match(entry['FileName']):
                try:
                    content = get_data_slice(self.data_model, entry['FileName'])
                    return parse(content.decode('utf-8'))
                except Exception as e:
                    print(f"Error parsing {label} file {entry['FileName']}: {e}")
                    return None
        return None

    def _load_xml_collection(self, pattern, parse, store, label):
        """Parse every file matching ``pattern`` (capture group 1 is the id)
        and insert into ``store`` keyed by that id."""
        for entry in self.data_model.file_log:
            match = pattern.match(entry['FileName'])
            if not match:
                continue
            try:
                content = get_data_slice(self.data_model, entry['FileName'])
                store[match.group(1)] = parse(content.decode('utf-8'))
            except Exception as e:
                print(f"Error parsing {label} file {entry['FileName']}: {e}")

    def _parse_cube(self):
        self._cube = self._load_xml_singleton(
            re.compile(r'Model\.\d+\.cub\.xml'),
            lambda s: CubXmlLoad.from_xml_string(s).Cube,
            'cube',
        )
        if self._cube is None:
            raise RuntimeError("Model .cub.xml file not found in the data model")

    def _extract_dimension_metadata(self):
        self._load_xml_collection(
            re.compile(r'(.+)\.(\d+)\.dim\.xml'),
            lambda s: DimensionXmlLoad.from_xml_string(s).Dimension,
            self._dimensions, 'dimension',
        )

    def _extract_partition_metadata(self):
        self._load_xml_collection(
            re.compile(r'(.+)\.(\d+)\.prt\.xml'),
            lambda s: PartitionXmlLoad.from_xml_string(s).Partition,
            self._partitions, 'partition',
        )

    def _extract_measure_group_metadata(self):
        self._load_xml_collection(
            re.compile(r'(.+)\.(\d+)\.det\.xml'),
            lambda s: MeasureGroupXmlLoad.from_xml_string(s).MeasureGroup,
            self._measure_groups, 'measure group',
        )

    def _extract_mdx_script(self):
        self._mdx_script = self._load_xml_singleton(
            re.compile(r'MdxScript\.\d+\.scr\.xml'),
            lambda s: MdxScriptXmlLoad.from_xml_string(s).MdxScript,
            'MDX script',
        )

    def _extract_data_sources(self):
        self._load_xml_collection(
            re.compile(r'([a-f0-9\-]+)\.\d+\.ds\.xml'),
            lambda s: DataSourceXmlLoad.from_xml_string(s).DataSource,
            self._data_sources, 'data source',
        )

    def _extract_data_source_view(self):
        self._data_source_view = self._load_xml_singleton(
            re.compile(r'.+\.\d+\.dsv\.xml'),
            lambda s: DataSourceViewXmlLoad.from_xml_string(s).DataSourceView,
            'data source view',
        )

    def _extract_tbl_metadata(self):
        self._load_xml_collection(
            re.compile(r'^([^H$R$][^$]*?)\.(\d+)\.tbl\.xml$'),
            lambda s: XMObjectDocument.from_xml_string(s).root_object,
            self._tbl_objects, 'table',
        )
    
    def _build_schema(self):
        schema_data = []
        if self._cube and self._cube.Dimensions:
            for cube_dim in self._cube.Dimensions:
                dimension_id = cube_dim.DimensionID
                table_name = cube_dim.Name
                is_visible = cube_dim.Visible
                dimension = self._dimensions.get(dimension_id)
                tbl_obj = self._tbl_objects.get(dimension_id)
                
                if dimension and dimension.Attributes:
                    for attr in dimension.Attributes:
                        # Skip VertiPaq's implicit RowNumber column — it's the
                        # storage position, not insertion order, and the
                        # DataFrame's own index already provides 0..n-1.
                        if attr.Name == "RowNumber" or attr.ID == "RowNumber":
                            continue
                        column_name = attr.Name
                        # Storage uses the attribute ID (e.g. "CalculatedColumn1"),
                        # which differs from the display Name for renamed/calculated columns.
                        storage_name = attr.ID or attr.Name
                        stats = self._get_column_stats_from_tbl(tbl_obj, storage_name)
                        file_info = self._find_column_files(dimension_id, storage_name)
                        data_type = self._map_attribute_type_to_pandas(attr)
                        ssas_type = self._get_attribute_ssas_type(attr)

                        idf = file_info.get('idf') or None
                        column_data = {
                            'TableName': table_name,
                            'ColumnName': column_name,
                            'StorageName': storage_name,
                            'Dictionary': file_info.get('dictionary') or None,
                            'HIDX': file_info.get('hidx') or None,
                            'IDF': idf,
                            # xlsx stores one IDF per column (multi-segment in-file,
                            # already concatenated by the decoder). The single-element
                            # list keeps the partition-aware decode path uniform with
                            # the sqlite source.
                            'IDFs': [idf] if idf is not None else [],
                            'Cardinality': stats.get('cardinality', 0),
                            'DataType': data_type,
                            'SSASType': ssas_type,
                            'BaseId': stats.get('base_id', 0),
                            'Magnitude': stats.get('magnitude', 0),
                            'IsNullable': stats.get('is_nullable', True),
                            'ModifiedTime': dimension.LastProcessed,
                            'StructureModifiedTime': dimension.LastSchemaUpdate,
                            'DimensionID': dimension_id,
                            'Visible': is_visible,
                            'RLERuns': stats.get('rle_runs', 0),
                            'MinDataID': stats.get('min_data_id', 0),
                            'MaxDataID': stats.get('max_data_id', 0),
                            'CompressionType': stats.get('compression_type', 0),
                            'HasNulls': stats.get('has_nulls', False)
                        }
                        schema_data.append(column_data)
        self.schema_df = pd.DataFrame(schema_data)

    def _normalize_schema(self):
        """Add format-agnostic ``PandasDataType`` and ``SemanticType`` columns.
        XLSX ``DataType`` is already a pandas dtype string; ``SSASType`` carries
        the semantic hint (Date / Currency / ...)."""
        if self.schema_df.empty:
            self.schema_df = self.schema_df.assign(PandasDataType=pd.Series(dtype='object'),
                                                   SemanticType=pd.Series(dtype='object'))
            return
        self.schema_df = self.schema_df.assign(
            PandasDataType=self.schema_df['DataType'].fillna('object'),
            SemanticType=self.schema_df['SSASType'].where(
                self.schema_df['SSASType'].isin(['Date', 'Currency']),
                'Other',
            ),
        )

    def _get_column_stats_from_tbl(self, tbl_obj, column_name):
        stats = {
            'cardinality': 0,
            'base_id': 0,
            'magnitude': 1,
            'is_nullable': True,
            'rle_runs': 0,
            'min_data_id': 0,
            'max_data_id': 0,
            'compression_type': 0,
            'has_nulls': False
        }
        
        if not tbl_obj or not tbl_obj.collections:
            return stats
        
        for collection in tbl_obj.collections:
            if collection.Name == "Columns":
                for xm_obj in collection.XMObjects:
                    if xm_obj.name == column_name and xm_obj.class_name == "XMRawColumn":
                        # BaseId/Magnitude live on the XMRawColumn's own data objects
                        # (XMValueDataDictionary). For dictionary-encoded columns the
                        # data object is XMHashDataDictionary and BaseId/Magnitude
                        # are absent — keep the defaults.
                        for data_object in xm_obj.data_objects:
                            inner = data_object.XMObject
                            if inner is None or inner.properties is None:
                                continue
                            if hasattr(inner.properties, 'BaseId'):
                                stats['base_id'] = inner.properties.BaseId
                            if hasattr(inner.properties, 'Magnitude'):
                                stats['magnitude'] = inner.properties.Magnitude
                            if hasattr(inner.properties, 'Nullable'):
                                stats['is_nullable'] = inner.properties.Nullable
                        # Get cardinality from Hierarchy member (DistinctDataIDs)
                        for member in xm_obj.members:
                            if member.Name == "IntrinsicHierarchy" and member.XMObject:
                                hierarchy_obj = member.XMObject
                                if hierarchy_obj.properties and hasattr(hierarchy_obj.properties, 'DistinctDataIDs'):
                                    stats['cardinality'] = hierarchy_obj.properties.DistinctDataIDs
                            elif member.Name == "ColumnStats" and member.XMObject:
                                stats_obj = member.XMObject
                                if stats_obj.properties:
                                    if hasattr(stats_obj.properties, 'MinDataID'):
                                        stats['min_data_id'] = stats_obj.properties.MinDataID
                                    if hasattr(stats_obj.properties, 'MaxDataID'):
                                        stats['max_data_id'] = stats_obj.properties.MaxDataID
                                    if hasattr(stats_obj.properties, 'HasNulls'):
                                        stats['has_nulls'] = stats_obj.properties.HasNulls
                                    if hasattr(stats_obj.properties, 'RLERuns'):
                                        stats['rle_runs'] = stats_obj.properties.RLERuns
                                    if hasattr(stats_obj.properties, 'CompressionType'):
                                        stats['compression_type'] = stats_obj.properties.CompressionType
                        break
        return stats
    
    def _map_attribute_type_to_pandas(self, attr):
        if attr.KeyColumns:
            for key_col in attr.KeyColumns:
                if key_col.DataType:
                    return self._map_ssas_type_to_pandas(key_col.DataType)
        return 'object'

    def _get_attribute_ssas_type(self, attr):
        if attr.KeyColumns:
            for key_col in attr.KeyColumns:
                if key_col.DataType:
                    return key_col.DataType
        return ''

    def get_segment_meta(self, column_row, idf=None):
        """Build segments_meta for a column from the parsed .tbl.xml tree.

        Returns a list of dicts matching the shape produced by
        SqliteMetadataSource.get_segment_meta: {min_data_id, count_bit_packed, bit_width}.

        ``idf`` is accepted for signature parity with the sqlite source but ignored:
        xlsx stores a single IDF per column whose in-file segments are returned in
        full here.
        """
        dimension_id = column_row["DimensionID"]
        column_name = column_row.get("StorageName") or column_row["ColumnName"]
        tbl_obj = self._tbl_objects.get(dimension_id)
        segments_meta = []
        if not tbl_obj or not tbl_obj.collections:
            return segments_meta

        columns_collection = next(
            (c for c in tbl_obj.collections if c.Name == "Columns"), None
        )
        if columns_collection is None:
            return segments_meta

        column_obj = next(
            (
                x for x in columns_collection.XMObjects
                if x.name == column_name and x.class_name == "XMRawColumn"
            ),
            None,
        )
        if column_obj is None:
            return segments_meta

        segments_collection = next(
            (c for c in column_obj.collections if c.Name == "Segments"), None
        )
        if segments_collection is None:
            return segments_meta

        for seg in segments_collection.XMObjects:
            sub_member = next(
                (m for m in seg.members if m.Name == "SubSegment"), None
            )
            min_data_id = 0
            count_bit_packed = 0
            bit_width = 0
            records = seg.properties.Records if (seg.properties is not None and hasattr(seg.properties, 'Records')) else 0
            if sub_member is not None and sub_member.XMObject is not None:
                sub = sub_member.XMObject
                if sub.properties is not None and hasattr(sub.properties, 'Records'):
                    count_bit_packed = sub.properties.Records
                ci_member = next(
                    (m for m in sub.members if m.Name == "CompressionInfo"), None
                )
                if ci_member is not None and ci_member.XMObject is not None:
                    ci = ci_member.XMObject
                    bit_width = self._bit_width_from_class(ci.class_name)
                    if ci.properties is not None and hasattr(ci.properties, 'Min'):
                        min_data_id = ci.properties.Min
            segments_meta.append({
                'min_data_id': min_data_id,
                'count_bit_packed': count_bit_packed,
                'bit_width': bit_width,
                'records': records,
            })
        return segments_meta

    @staticmethod
    def _bit_width_from_class(class_name):
        """Extract the bit-width N from a CompressionInfo class name like
        'XMRENoSplitCompressionInfo<12>' or
        'XMHybridRLECompressionInfo<class XMRENoSplitCompressionInfo<12>>'."""
        if not class_name:
            return 0
        # Innermost <N> takes precedence
        match = re.findall(r'<(\d+)>', class_name)
        if match:
            return int(match[-1])
        return 0
    
    def _map_ssas_type_to_pandas(self, ssas_type):
        type_map = {
            'WChar': 'string',
            'Integer': 'int64',
            'BigInt': 'int64',
            'Double': 'float64',
            'Date': 'datetime64[ns]',
            'Boolean': 'bool',
            'Currency': 'float64',
            'Variant': 'object',
            'Empty': 'object'  # Empty/null data type
        }
        return type_map.get(ssas_type, 'object')
    
    def _find_column_files(self, dimension_id, column_name):
        files = {'dictionary': '', 'hidx': '', 'idf': ''}
        for file_entry in self.data_model.file_log:
            file_name = file_entry['FileName']
            if (dimension_id in file_name or f"H${dimension_id}" in file_name) and column_name in file_name:
                if '.dictionary' in file_name and not '.ID_TO_POS.' in file_name and not '.POS_TO_ID.' in file_name:
                    if f".{column_name}.0.idf.dictionary" in file_name or f".{column_name}.dictionary" in file_name:
                        files['dictionary'] = file_name
                elif '.hidx' in file_name:
                    if f"${column_name}.hidx" in file_name or f"${column_name}.POS_TO_ID.0.idf.hidx" in file_name:
                        files['hidx'] = file_name
                elif '.idf' in file_name and '.ID_TO_POS.' not in file_name and '.POS_TO_ID.' not in file_name and '.hidx' not in file_name:
                    if f".{column_name}.0.idf" in file_name:
                        files['idf'] = file_name
        return files
    
    def _build_dax_tables(self):
        dax_tables_data = []
        for dimension_id, partition in self._partitions.items():
            if partition and partition.Source:
                dimension = self._dimensions.get(dimension_id)
                table_name = dimension.Name if dimension else dimension_id
                query_definition = self._extract_query_from_source(partition.Source)
                if query_definition:
                    dax_tables_data.append({
                        'TableName': table_name,
                        'Expression': query_definition
                    })
        self.dax_tables_df = pd.DataFrame(dax_tables_data)
    
    def _extract_query_from_source(self, source):
        if not source:
            return None
        if hasattr(source, 'QueryDefinition'):
            return source.QueryDefinition
        if hasattr(source, 'Source') and source.Source:
            if hasattr(source.Source, 'ColumnID'):
                return f"[{source.Source.ColumnID}]"
        return None
    
    def _build_dax_measures(self):
        measures_data = []
        for dimension_id, measure_group in self._measure_groups.items():
            if measure_group and measure_group.Measures:
                dimension = self._dimensions.get(dimension_id)
                table_name = dimension.Name if dimension else dimension_id
                for measure in measure_group.Measures:
                    measures_data.append({
                        'TableName': table_name,
                        'Name': measure.Name,
                        'Expression': measure.MeasureExpression if measure.MeasureExpression else '',
                        'DisplayFolder': measure.DisplayFolder if measure.DisplayFolder else '',
                        'Description': measure.Description if measure.Description else ''
                    })
        self.dax_measures_df = pd.DataFrame(measures_data)
    
    def _build_dax_columns(self):
        self.dax_columns_df = pd.DataFrame()
    
    def _build_relationships(self):
        relationships_data = []
        
        # Iterate through dimensions and their relationships
        for dimension_id, dimension in self._dimensions.items():
            if not dimension or not dimension.Relationships:
                continue
            
            # Get the table name for the current dimension (from relationship end)
            from_table_name = dimension.Name if dimension.Name else dimension_id
            
            for relationship in dimension.Relationships:
                if not relationship.FromRelationshipEnd or not relationship.ToRelationshipEnd:
                    continue
                
                # Get From (foreign key) information
                from_dimension_id = relationship.FromRelationshipEnd.DimensionID
                from_attributes = relationship.FromRelationshipEnd.Attributes
                from_multiplicity = relationship.FromRelationshipEnd.Multiplicity
                
                # Get To (primary key) information
                to_dimension_id = relationship.ToRelationshipEnd.DimensionID
                to_attributes = relationship.ToRelationshipEnd.Attributes
                to_multiplicity = relationship.ToRelationshipEnd.Multiplicity
                
                # Map dimension IDs to table names
                from_table = self._dimensions.get(from_dimension_id).Name if from_dimension_id in self._dimensions else from_dimension_id
                to_table = self._dimensions.get(to_dimension_id).Name if to_dimension_id in self._dimensions else to_dimension_id
                
                # Get column names from attributes
                from_column = from_attributes[0].AttributeID if from_attributes else ''
                to_column = to_attributes[0].AttributeID if to_attributes else ''
                
                # Map attribute IDs to actual column names
                if from_dimension_id in self._dimensions:
                    from_dim = self._dimensions[from_dimension_id]
                    for attr in from_dim.Attributes:
                        if attr.ID == from_column:
                            from_column = attr.Name
                            break
                
                if to_dimension_id in self._dimensions:
                    to_dim = self._dimensions[to_dimension_id]
                    for attr in to_dim.Attributes:
                        if attr.ID == to_column:
                            to_column = attr.Name
                            break
                
                # Determine cardinality from multiplicities
                cardinality = self._map_multiplicity_to_cardinality(from_multiplicity, to_multiplicity)
                
                relationships_data.append({
                    'FromTableName': from_table,
                    'FromColumnName': from_column,
                    'ToTableName': to_table,
                    'ToColumnName': to_column,
                    'IsActive': relationship.Visible,
                    'Cardinality': cardinality,
                    'CrossFilteringBehavior': 'Single',
                    'FromKeyCount': 0,
                    'ToKeyCount': 0,
                    'RelyOnReferentialIntegrity': False
                })
        
        self.relationships_df = pd.DataFrame(relationships_data)
    
    def _map_multiplicity_to_cardinality(self, from_multiplicity, to_multiplicity):
        """Map relationship multiplicities to Power BI cardinality notation."""
        if from_multiplicity == 'Many' and to_multiplicity == 'One':
            return 'M:1'
        elif from_multiplicity == 'One' and to_multiplicity == 'Many':
            return '1:M'
        elif from_multiplicity == 'One' and to_multiplicity == 'One':
            return '1:1'
        elif from_multiplicity == 'Many' and to_multiplicity == 'Many':
            return 'M:M'
        else:
            return 'M:1'  # Default fallback