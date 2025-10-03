# ---------- IMPORTS ----------

from .pbix_unpacker import PbixUnpacker
from .vertipaq_decoder import VertiPaqDecoder
from .meta.metadata_handler import MetadataHandler
from .utils import WINDOWS_EPOCH_START
import datetime

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
        df = self._metadata_handler.metadata.m_parameters_df
        return df if df.empty else df.assign(
            ModifiedTime=lambda df: df['ModifiedTime'].apply(
                lambda x: WINDOWS_EPOCH_START + datetime.timedelta(seconds=x / 1e7)
            )
        )

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
        return  self._metadata_handler.schema
    
    @property
    def relationships(self):
        return self._metadata_handler.metadata.relationships_df
    
    @property
    def rls(self):
        return self._metadata_handler.metadata.rls_df
