import xml.etree.ElementTree as ET
import pandas as pd
import re
from ..utils import get_data_slice

class XmlMetadataQuery:
    """Handles metadata extraction from XML files in XLSX Power Pivot models."""
    
    def __init__(self, data_model):
        self.data_model = data_model
        self._model_xml_content = None
        self._find_model_xml()
        
        # Parse the XML and populate dataframes
        self._parse_model_xml()
        
        # Initialize empty dataframes for compatibility with existing code
        self.m_df = pd.DataFrame()
        self.m_parameters_df = pd.DataFrame()
        self.dax_tables_df = pd.DataFrame()
        self.dax_measures_df = pd.DataFrame()
        self.dax_columns_df = pd.DataFrame()
        self.metadata_df = pd.DataFrame()
        self.relationships_df = pd.DataFrame()
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
            
            # Find all attributes (columns) in this dimension
            attributes = dimension.findall('.//as:Attribute', namespaces)
            
            for attribute in attributes:
                attribute_id = attribute.find('as:AttributeID', namespaces)
                if attribute_id is None:
                    continue
                
                column_name = attribute_id.text
                
                # Check if attribute hierarchy is visible
                attr_visible = attribute.find('as:AttributeHierarchyVisible', namespaces)
                column_visible = attr_visible.text.lower() == 'true' if attr_visible is not None else True
                
                # For xlsx files, we'll look for actual files in the file log
                # and match them to this dimension/attribute combination
                dictionary_file = ""
                hidx_file = ""
                idf_file = ""
                
                # Try to find matching files in the file log
                for file_entry in self.data_model.file_log:
                    file_name = file_entry['FileName']
                    # Look for files that contain this table and column information
                    if table_name in file_name and column_name in file_name:
                        if '.dictionary' in file_name:
                            dictionary_file = file_name
                        elif '.hidx' in file_name:
                            hidx_file = file_name
                        elif '.idf' in file_name and '.ID_TO_POS.' not in file_name and '.POS_TO_ID.' not in file_name:
                            idf_file = file_name
                
                schema_data.append({
                    'TableName': table_name,
                    'ColumnName': column_name,
                    'Dictionary': dictionary_file,
                    'HIDX': hidx_file,
                    'IDF': idf_file,
                    'Cardinality': 0,  # Will need to be computed from actual data files
                    'DataType': 'object',  # Default, will need better detection
                    'BaseId': 0,
                    'Magnitude': 0,
                    'IsNullable': True,
                    'ModifiedTime': 0,
                    'StructureModifiedTime': 0,
                    'DimensionID': table_id,
                    'Visible': is_visible and column_visible
                })
        
        # Create the schema DataFrame
        self.schema_df = pd.DataFrame(schema_data)