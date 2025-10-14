import xml.etree.ElementTree as ET
import pandas as pd
import re
import datetime
from ..utils import get_data_slice

class XmlMetadataQuery:
    """Handles metadata extraction from XML files in XLSX Power Pivot models."""
    
    def __init__(self, data_model):
        self.data_model = data_model
        self._model_xml_content = None
        self._dimension_data = {}  # Cache for dimension information
        self._find_model_xml()
        
        # Parse the XML and populate dataframes
        self._parse_model_xml()
        
        # Extract data from additional XML files
        self._extract_dimension_metadata()
        self._extract_partition_metadata()
        self._extract_measure_metadata()
        
        # Initialize empty dataframes for compatibility with existing code
        self.m_df = pd.DataFrame()
        self.m_parameters_df = pd.DataFrame()
        self.dax_tables_df = pd.DataFrame()
        self.metadata_df = pd.DataFrame()
        self.rls_df = pd.DataFrame()
    
    def _find_model_xml(self):
        """Find the Model.{number}.cub.xml file in the data model."""
        model_pattern = re.compile(r'Model\.\d+\.cub\.xml')
        
        for file_entry in self.data_model.file_log:
            if model_pattern.match(file_entry['FileName']):
                # Found the model XML file, extract its content
                self._model_xml_content = get_data_slice(self.data_model, file_entry['FileName'])
                return
        
        raise RuntimeError("Model.{number}.cub.xml file not found in the data model")
    
    def _parse_model_xml(self):
        """Parse the Model XML and extract schema information."""
        if not self._model_xml_content:
            raise RuntimeError("Model XML content not loaded")
        
        # Parse the XML
        root = ET.fromstring(self._model_xml_content.decode('utf-8'))
        
        # Define namespace map - the default namespace is the Analysis Services namespace
        namespaces = {
            'as': 'http://schemas.microsoft.com/analysisservices/2003/engine'
        }
        
        # Find the Cube element within ObjectDefinition
        cube = root.find('.//as:ObjectDefinition/as:Cube', namespaces)
        if cube is None:
            raise RuntimeError("Could not find Cube element in Model XML")
        
        # Extract dimensions (tables) and their attributes (columns)
        self._extract_schema_from_xml(cube, namespaces)
    
    def _extract_schema_from_xml(self, cube, namespaces):
        """Extract schema information from the XML cube definition."""
        schema_data = []
        
        # Find all dimensions
        dimensions = cube.findall('.//as:Dimension', namespaces)
        
        for dimension in dimensions:
            # Get dimension information
            dimension_id = dimension.find('as:ID', namespaces)
            dimension_name = dimension.find('as:Name', namespaces)
            dimension_visible = dimension.find('as:Visible', namespaces)
            
            if dimension_id is None or dimension_name is None:
                continue
                
            table_name = dimension_name.text
            table_id = dimension_id.text
            is_visible = dimension_visible.text.lower() == 'true' if dimension_visible is not None else True
            
            # Store dimension info for later use
            self._dimension_data[table_id] = {
                'name': table_name,
                'visible': is_visible,
                'id': table_id
            }
            
            # Get columns from .tbl.xml files first for accurate column structure
            table_columns = self._extract_columns_from_tbl_xml(table_id)
            
            schema_data.extend(table_columns)
        
        # Create the schema DataFrame
        self.schema_df = pd.DataFrame(schema_data)
    
    def _extract_columns_from_tbl_xml(self, dimension_id):
        """Extract column information from .tbl.xml files."""
        columns_data = []
        
        # Find the main table XML file for this dimension
        tbl_pattern = re.compile(f'{re.escape(dimension_id)}\.\\d+\.tbl\.xml')
        
        for file_entry in self.data_model.file_log:
            if tbl_pattern.match(file_entry['FileName']):
                try:
                    tbl_content = get_data_slice(self.data_model, file_entry['FileName'])
                    root = ET.fromstring(tbl_content.decode('utf-8'))
                    
                    # Define namespaces for tbl.xml
                    tbl_namespaces = {
                        'xm': 'http://schemas.microsoft.com/analysisservices/imbi'
                    }
                    
                    # Find all columns
                    columns = root.findall('.//xm:XMObject[@class="XMRawColumn"]', tbl_namespaces)
                    
                    for column in columns:
                        column_name = column.get('name')
                        if not column_name:
                            continue
                        
                        # Extract column statistics
                        stats = self._extract_column_stats(column)
                        
                        # Find corresponding files for this column
                        file_info = self._find_column_files(dimension_id, column_name)
                        
                        column_data = {
                            'TableName': self._dimension_data[dimension_id]['name'],
                            'ColumnName': column_name,
                            'Dictionary': file_info.get('dictionary', ''),
                            'HIDX': file_info.get('hidx', ''),
                            'IDF': file_info.get('idf', ''),
                            'Cardinality': stats.get('cardinality', 0),
                            'DataType': stats.get('data_type', 'object'),
                            'BaseId': stats.get('base_id', 0),
                            'Magnitude': stats.get('magnitude', 0),
                            'IsNullable': stats.get('is_nullable', True),
                            'ModifiedTime': stats.get('modified_time', 0),
                            'StructureModifiedTime': stats.get('structure_modified_time', 0),
                            'DimensionID': dimension_id,
                            'Visible': self._dimension_data[dimension_id]['visible'],
                            'RLERuns': stats.get('rle_runs', 0),
                            'MinDataID': stats.get('min_data_id', 0),
                            'MaxDataID': stats.get('max_data_id', 0),
                            'CompressionType': stats.get('compression_type', 0),
                            'HasNulls': stats.get('has_nulls', False)
                        }
                        
                        columns_data.append(column_data)
                        
                except Exception as e:
                    print(f"Error parsing {file_entry['FileName']}: {e}")
                    continue
                    
                break  # Found the main table file
        
        return columns_data
    
    def _extract_column_stats(self, column_element):
        """Extract statistics from XMRawColumn element."""
        stats = {}
        
        # Find ColumnStats element
        column_stats = column_element.find('.//xm:XMObject[@class="XMColumnStats"]', 
                                         {'xm': 'http://schemas.microsoft.com/analysisservices/imbi'})
        
        if column_stats is not None:
            properties = column_stats.find('xm:Properties', 
                                         {'xm': 'http://schemas.microsoft.com/analysisservices/imbi'})
            
            if properties is not None:
                # Extract various statistics
                for prop in properties:
                    if prop.tag.endswith('DistinctStates'):
                        stats['cardinality'] = int(prop.text) if prop.text else 0
                    elif prop.tag.endswith('MinDataID'):
                        stats['min_data_id'] = int(prop.text) if prop.text else 0
                    elif prop.tag.endswith('MaxDataID'):
                        stats['max_data_id'] = int(prop.text) if prop.text else 0
                    elif prop.tag.endswith('HasNulls'):
                        stats['has_nulls'] = prop.text.lower() == 'true' if prop.text else False
                    elif prop.tag.endswith('RLERuns'):
                        stats['rle_runs'] = int(prop.text) if prop.text else 0
                    elif prop.tag.endswith('CompressionType'):
                        stats['compression_type'] = int(prop.text) if prop.text else 0
                    elif prop.tag.endswith('DBType'):
                        # Map DBType to pandas-compatible types
                        db_type = int(prop.text) if prop.text else 0
                        stats['data_type'] = self._map_dbtype_to_pandas(db_type)
        
        # Set defaults
        stats.setdefault('cardinality', 0)
        stats.setdefault('data_type', 'object')
        stats.setdefault('base_id', 0)
        stats.setdefault('magnitude', 0)
        stats.setdefault('is_nullable', True)
        stats.setdefault('modified_time', 0)
        stats.setdefault('structure_modified_time', 0)
        stats.setdefault('rle_runs', 0)
        stats.setdefault('min_data_id', 0)
        stats.setdefault('max_data_id', 0)
        stats.setdefault('compression_type', 0)
        stats.setdefault('has_nulls', False)
        
        return stats
    
    def _map_dbtype_to_pandas(self, db_type):
        """Map Analysis Services DBType to pandas-compatible type."""
        # Common DBType mappings
        type_map = {
            3: 'int64',      # DBTYPE_I4
            5: 'float64',    # DBTYPE_R8
            6: 'object',     # DBTYPE_CY
            7: 'datetime64[ns]',  # DBTYPE_DATE
            8: 'object',     # DBTYPE_BSTR / string
            11: 'bool',      # DBTYPE_BOOL
            128: 'object',   # DBTYPE_BYTES
            129: 'object',   # DBTYPE_STR
            130: 'object'    # DBTYPE_WSTR
        }
        return type_map.get(db_type, 'object')
    
    def _find_column_files(self, dimension_id, column_name):
        """Find dictionary, hidx, and idf files for a specific column."""
        files = {'dictionary': '', 'hidx': '', 'idf': ''}
        
        # More precise pattern matching using dimension ID
        for file_entry in self.data_model.file_log:
            file_name = file_entry['FileName']
            
            # Check if this file belongs to this dimension and column
            if dimension_id in file_name and column_name in file_name:
                if '.dictionary' in file_name:
                    files['dictionary'] = file_name
                elif '.hidx' in file_name:
                    files['hidx'] = file_name
                elif '.idf' in file_name and '.ID_TO_POS.' not in file_name and '.POS_TO_ID.' not in file_name:
                    files['idf'] = file_name
        
        return files
    
    def _extract_dimension_metadata(self):
        """Extract additional metadata from .dim.xml files."""
        dimension_metadata = []
        
        # Find all .dim.xml files
        dim_pattern = re.compile(r'(.+)\.(\d+)\.dim\.xml')
        
        for file_entry in self.data_model.file_log:
            match = dim_pattern.match(file_entry['FileName'])
            if match:
                dimension_id = match.group(1)
                
                try:
                    dim_content = get_data_slice(self.data_model, file_entry['FileName'])
                    root = ET.fromstring(dim_content.decode('utf-8'))
                    
                    # Analysis Services namespaces
                    namespaces = {
                        'as': 'http://schemas.microsoft.com/analysisservices/2003/engine'
                    }
                    
                    # Extract dimension information
                    dimension = root.find('.//as:ObjectDefinition/as:Dimension', namespaces)
                    if dimension is not None:
                        name = dimension.find('as:Name', namespaces)
                        last_processed = dimension.find('as:LastProcessed', namespaces)
                        estimated_size = dimension.find('as:EstimatedSize', namespaces)
                        created_timestamp = dimension.find('as:CreatedTimestamp', namespaces)
                        last_schema_update = dimension.find('as:LastSchemaUpdate', namespaces)
                        
                        metadata = {
                            'DimensionID': dimension_id,
                            'Name': name.text if name is not None else '',
                            'LastProcessed': last_processed.text if last_processed is not None else '',
                            'EstimatedSize': int(estimated_size.text) if estimated_size is not None and estimated_size.text else 0,
                            'CreatedTimestamp': created_timestamp.text if created_timestamp is not None else '',
                            'LastSchemaUpdate': last_schema_update.text if last_schema_update is not None else ''
                        }
                        
                        dimension_metadata.append(metadata)
                        
                except Exception as e:
                    print(f"Error parsing dimension file {file_entry['FileName']}: {e}")
                    continue
        
        # Store as DataFrame for later use
        self.dimension_metadata_df = pd.DataFrame(dimension_metadata)
    
    def _extract_partition_metadata(self):
        """Extract query definitions from .prt.xml files."""
        partition_data = []
        
        # Find all .prt.xml files
        prt_pattern = re.compile(r'(.+)\.(\d+)\.prt\.xml')
        
        for file_entry in self.data_model.file_log:
            match = prt_pattern.match(file_entry['FileName'])
            if match:
                dimension_id = match.group(1)
                
                try:
                    prt_content = get_data_slice(self.data_model, file_entry['FileName'])
                    root = ET.fromstring(prt_content.decode('utf-8'))
                    
                    # Analysis Services namespaces
                    namespaces = {
                        'as': 'http://schemas.microsoft.com/analysisservices/2003/engine'
                    }
                    
                    # Extract partition information
                    partition = root.find('.//as:ObjectDefinition/as:Partition', namespaces)
                    if partition is not None:
                        name = partition.find('as:Name', namespaces)
                        query_def = partition.find('.//as:QueryDefinition', namespaces)
                        last_processed = partition.find('as:LastProcessed', namespaces)
                        
                        partition_info = {
                            'DimensionID': dimension_id,
                            'TableName': name.text if name is not None else '',
                            'QueryDefinition': query_def.text if query_def is not None else '',
                            'LastProcessed': last_processed.text if last_processed is not None else ''
                        }
                        
                        partition_data.append(partition_info)
                        
                except Exception as e:
                    print(f"Error parsing partition file {file_entry['FileName']}: {e}")
                    continue
        
        # Store as DataFrame - this can be used for M query equivalents
        self.dax_tables_df = pd.DataFrame(partition_data)
    
    def _extract_measure_metadata(self):
        """Extract measures and relationships from .det.xml files."""
        measures_data = []
        relationships_data = []
        
        # Find all .det.xml files
        det_pattern = re.compile(r'(.+)\.(\d+)\.det\.xml')
        
        for file_entry in self.data_model.file_log:
            match = det_pattern.match(file_entry['FileName'])
            if match:
                dimension_id = match.group(1)
                
                try:
                    det_content = get_data_slice(self.data_model, file_entry['FileName'])
                    root = ET.fromstring(det_content.decode('utf-8'))
                    
                    # Analysis Services namespaces
                    namespaces = {
                        'as': 'http://schemas.microsoft.com/analysisservices/2003/engine'
                    }
                    
                    # Extract measures
                    measure_group = root.find('.//as:ObjectDefinition/as:MeasureGroup', namespaces)
                    if measure_group is not None:
                        table_name = measure_group.find('as:Name', namespaces)
                        table_name_text = table_name.text if table_name is not None else ''
                        
                        measures = measure_group.findall('.//as:Measure', namespaces)
                        for measure in measures:
                            measure_name = measure.find('as:Name', namespaces)
                            measure_id = measure.find('as:ID', namespaces)
                            aggregate_function = measure.find('as:AggregateFunction', namespaces)
                            data_type = measure.find('as:DataType', namespaces)
                            visible = measure.find('as:Visible', namespaces)
                            
                            measure_info = {
                                'TableName': table_name_text,
                                'Name': measure_name.text if measure_name is not None else '',
                                'ID': measure_id.text if measure_id is not None else '',
                                'AggregateFunction': aggregate_function.text if aggregate_function is not None else '',
                                'DataType': data_type.text if data_type is not None else '',
                                'Visible': visible.text.lower() == 'true' if visible is not None else True,
                                'Expression': '',  # Measures in XLSX typically don't have DAX expressions
                                'DisplayFolder': '',
                                'Description': ''
                            }
                            
                            measures_data.append(measure_info)
                        
                        # Extract relationship information from dimensions
                        dimensions = measure_group.findall('.//as:Dimension', namespaces)
                        for dimension in dimensions:
                            cube_dimension_id = dimension.find('as:CubeDimensionID', namespaces)
                            if cube_dimension_id is not None and cube_dimension_id.text != dimension_id:
                                # This indicates a relationship
                                relationship_info = {
                                    'FromTableName': table_name_text,
                                    'FromColumnName': '',  # Would need more analysis to determine
                                    'ToTableName': self._dimension_data.get(cube_dimension_id.text, {}).get('name', ''),
                                    'ToColumnName': '',    # Would need more analysis to determine
                                    'IsActive': True,      # Default assumption
                                    'Cardinality': 'M:1',  # Default assumption for fact to dimension
                                    'CrossFilteringBehavior': 'Single',
                                    'FromKeyCount': 0,
                                    'ToKeyCount': 0,
                                    'RelyOnReferentialIntegrity': False
                                }
                                
                                relationships_data.append(relationship_info)
                        
                except Exception as e:
                    print(f"Error parsing measure group file {file_entry['FileName']}: {e}")
                    continue
        
        # Store as DataFrames
        self.dax_measures_df = pd.DataFrame(measures_data)
        self.dax_columns_df = pd.DataFrame()  # Would need additional analysis for calculated columns
        self.relationships_df = pd.DataFrame(relationships_data)