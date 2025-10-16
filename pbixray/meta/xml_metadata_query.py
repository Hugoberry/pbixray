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

class XmlMetadataQuery:
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
        self._build_dax_tables()
        self._build_dax_measures()
        self._build_dax_columns()
        self._build_relationships()
        
        self.m_df = pd.DataFrame()
        self.m_parameters_df = pd.DataFrame()
        self.metadata_df = pd.DataFrame()
        self.rls_df = pd.DataFrame()
    
    def _parse_cube(self):
        cube_pattern = re.compile(r'Model\.\d+\.cub\.xml')
        for file_entry in self.data_model.file_log:
            if cube_pattern.match(file_entry['FileName']):
                cube_content = get_data_slice(self.data_model, file_entry['FileName'])
                cube_xml = CubXmlLoad.from_xml_string(cube_content.decode('utf-8'))
                self._cube = cube_xml.Cube
                return
        raise RuntimeError("Model .cub.xml file not found in the data model")
    
    def _extract_dimension_metadata(self):
        dim_pattern = re.compile(r'(.+)\.(\d+)\.dim\.xml')
        for file_entry in self.data_model.file_log:
            match = dim_pattern.match(file_entry['FileName'])
            if match:
                dimension_id = match.group(1)
                try:
                    dim_content = get_data_slice(self.data_model, file_entry['FileName'])
                    dim_xml = DimensionXmlLoad.from_xml_string(dim_content.decode('utf-8'))
                    self._dimensions[dimension_id] = dim_xml.Dimension
                except Exception as e:
                    print(f"Error parsing dimension file {file_entry['FileName']}: {e}")
    
    def _extract_partition_metadata(self):
        prt_pattern = re.compile(r'(.+)\.(\d+)\.prt\.xml')
        for file_entry in self.data_model.file_log:
            match = prt_pattern.match(file_entry['FileName'])
            if match:
                dimension_id = match.group(1)
                try:
                    prt_content = get_data_slice(self.data_model, file_entry['FileName'])
                    prt_xml = PartitionXmlLoad.from_xml_string(prt_content.decode('utf-8'))
                    self._partitions[dimension_id] = prt_xml.Partition
                except Exception as e:
                    print(f"Error parsing partition file {file_entry['FileName']}: {e}")
    
    def _extract_measure_group_metadata(self):
        det_pattern = re.compile(r'(.+)\.(\d+)\.det\.xml')
        for file_entry in self.data_model.file_log:
            match = det_pattern.match(file_entry['FileName'])
            if match:
                dimension_id = match.group(1)
                try:
                    det_content = get_data_slice(self.data_model, file_entry['FileName'])
                    det_xml = MeasureGroupXmlLoad.from_xml_string(det_content.decode('utf-8'))
                    self._measure_groups[dimension_id] = det_xml.MeasureGroup
                except Exception as e:
                    print(f"Error parsing measure group file {file_entry['FileName']}: {e}")
    
    def _extract_mdx_script(self):
        scr_pattern = re.compile(r'MdxScript\.\d+\.scr\.xml')
        for file_entry in self.data_model.file_log:
            if scr_pattern.match(file_entry['FileName']):
                try:
                    scr_content = get_data_slice(self.data_model, file_entry['FileName'])
                    scr_xml = MdxScriptXmlLoad.from_xml_string(scr_content.decode('utf-8'))
                    self._mdx_script = scr_xml.MdxScript
                    return
                except Exception as e:
                    print(f"Error parsing MDX script file {file_entry['FileName']}: {e}")
    
    def _extract_data_sources(self):
        ds_pattern = re.compile(r'([a-f0-9\-]+)\.\d+\.ds\.xml')
        for file_entry in self.data_model.file_log:
            match = ds_pattern.match(file_entry['FileName'])
            if match:
                ds_id = match.group(1)
                try:
                    ds_content = get_data_slice(self.data_model, file_entry['FileName'])
                    ds_xml = DataSourceXmlLoad.from_xml_string(ds_content.decode('utf-8'))
                    self._data_sources[ds_id] = ds_xml.DataSource
                except Exception as e:
                    print(f"Error parsing data source file {file_entry['FileName']}: {e}")
    
    def _extract_data_source_view(self):
        dsv_pattern = re.compile(r'.+\.\d+\.dsv\.xml')
        for file_entry in self.data_model.file_log:
            if dsv_pattern.match(file_entry['FileName']):
                try:
                    dsv_content = get_data_slice(self.data_model, file_entry['FileName'])
                    dsv_xml = DataSourceViewXmlLoad.from_xml_string(dsv_content.decode('utf-8'))
                    self._data_source_view = dsv_xml.DataSourceView
                    return
                except Exception as e:
                    print(f"Error parsing data source view file {file_entry['FileName']}: {e}")
    
    def _extract_tbl_metadata(self):
        tbl_pattern = re.compile(r'^([^H$R$][^$]*?)\.(\d+)\.tbl\.xml$')
        for file_entry in self.data_model.file_log:
            match = tbl_pattern.match(file_entry['FileName'])
            if match:
                dimension_id = match.group(1)
                try:
                    tbl_content = get_data_slice(self.data_model, file_entry['FileName'])
                    tbl_doc = XMObjectDocument.from_xml_string(tbl_content.decode('utf-8'))
                    self._tbl_objects[dimension_id] = tbl_doc.root_object
                except Exception as e:
                    print(f"Error parsing table file {file_entry['FileName']}: {e}")
    
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
                        column_name = attr.Name
                        stats = self._get_column_stats_from_tbl(tbl_obj, column_name)
                        file_info = self._find_column_files(dimension_id, column_name)
                        data_type = self._map_attribute_type_to_pandas(attr)
                        
                        column_data = {
                            'TableName': table_name,
                            'ColumnName': column_name,
                            'Dictionary': file_info.get('dictionary', ''),
                            'HIDX': file_info.get('hidx', ''),
                            'IDF': file_info.get('idf', ''),
                            'Cardinality': stats.get('cardinality', 0),
                            'DataType': data_type,
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
    
    def _get_column_stats_from_tbl(self, tbl_obj, column_name):
        stats = {
            'cardinality': 0,
            'base_id': 0,
            'magnitude': 0,
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
                        for member in xm_obj.members:
                            if member.Name == "Statistics" and member.XMObject:
                                stats_obj = member.XMObject
                                if stats_obj.properties and hasattr(stats_obj.properties, 'DistinctStates'):
                                    stats['cardinality'] = stats_obj.properties.DistinctStates
                                    stats['min_data_id'] = stats_obj.properties.MinDataID
                                    stats['max_data_id'] = stats_obj.properties.MaxDataID
                                    stats['has_nulls'] = stats_obj.properties.HasNulls
                                    stats['rle_runs'] = stats_obj.properties.RLERuns
                                    stats['compression_type'] = stats_obj.properties.CompressionType
                        break
        return stats
    
    def _map_attribute_type_to_pandas(self, attr):
        if attr.KeyColumns:
            for key_col in attr.KeyColumns:
                if key_col.DataType:
                    return self._map_ssas_type_to_pandas(key_col.DataType)
        return 'object'
    
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
        for dimension_id, tbl_obj in self._tbl_objects.items():
            if not tbl_obj or not tbl_obj.collections:
                continue
            table_name = self._dimensions.get(dimension_id).Name if dimension_id in self._dimensions else dimension_id
            for collection in tbl_obj.collections:
                if collection.Name == "Relationships":
                    for rel_obj in collection.XMObjects:
                        if rel_obj.class_name == "XMRelationship" and rel_obj.properties:
                            from_table = table_name
                            from_column = rel_obj.properties.ForeignColumn if hasattr(rel_obj.properties, 'ForeignColumn') else ''
                            
                            # Map PrimaryTable DimensionID to table name
                            primary_table_id = rel_obj.properties.PrimaryTable if hasattr(rel_obj.properties, 'PrimaryTable') else ''
                            to_table = self._dimensions.get(primary_table_id).Name if primary_table_id and primary_table_id in self._dimensions else primary_table_id
                            
                            to_column = rel_obj.properties.PrimaryColumn if hasattr(rel_obj.properties, 'PrimaryColumn') else ''
                            relationships_data.append({
                                'FromTableName': from_table,
                                'FromColumnName': from_column,
                                'ToTableName': to_table,
                                'ToColumnName': to_column,
                                'IsActive': True,
                                'Cardinality': 'M:1',
                                'CrossFilteringBehavior': 'Single',
                                'FromKeyCount': 0,
                                'ToKeyCount': 0,
                                'RelyOnReferentialIntegrity': False
                            })
        self.relationships_df = pd.DataFrame(relationships_data)