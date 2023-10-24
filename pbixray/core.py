# ---------- IMPORTS ----------

from .pbix_unpacker import PbixUnpacker
from .vertipaq_decoder import VertiPaqDecoder
from .meta.metadata_handler import MetadataHandler

# ---------- MAIN CLASS ----------

class PBIXRay:
    def __init__(self, file_path):
        unpacker = PbixUnpacker(file_path)
        
        self._metadata_handler = MetadataHandler(unpacker.file_log, unpacker.decompressed_data)
        self._vertipaq_decoder = VertiPaqDecoder(self._metadata_handler.metadata, unpacker.file_log, unpacker.decompressed_data)
        
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
    def dax_tables(self):
        return self._metadata_handler.metadata.dax_tables_df
    
    @property
    def dax_measures(self):
        return self._metadata_handler.metadata.dax_measures_df
    
    @property
    def metadata(self):
        return self._metadata_handler.metadata.metadata_df
    
    @property
    def size(self):
        return self._metadata_handler.size
    
    @property
    def schema(self):
        return  self._metadata_handler.schema
