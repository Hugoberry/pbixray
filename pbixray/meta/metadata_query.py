
class MetadataQuery:
    def __init__(self, sqlite_handler):
        self.handler = sqlite_handler
        
        # Initialize dataframes as class attributes
        self.schema_df = None
        self.m_df = None
        self.dax_tables_df = None
        self.dax_measures_df = None

    def populate_schema(self):
        sql = """ 
        SELECT 
            t.Name AS TableName,
            c.ExplicitName AS ColumnName,
            sfd.FileName AS Dictionary, 
            sfh.FileName AS HIDX, 
            sfi.FileName AS IDF,
            cs.Statistics_DistinctStates as Cardinality,
            ds.DataType,
            ds.BaseId,
            ds.Magnitude
        FROM Column c 
        JOIN [Table] t ON c.TableId = t.ID
        JOIN ColumnStorage cs ON c.ColumnStorageID = cs.ID
        --HIDX
        JOIN AttributeHierarchy ah ON ah.ColumnID = c.ID
        JOIN AttributeHierarchyStorage ahs ON ah.AttributeHierarchyStorageID = ahs.ID
        LEFT JOIN StorageFile sfh ON sfh.ID = ahs.StorageFileID
        --Dictionary
        LEFT JOIN DictionaryStorage ds ON ds.ID = cs.DictionaryStorageID
        LEFT JOIN StorageFile sfd ON sfd.ID = ds.StorageFileID
        --IDF
        JOIN ColumnPartitionStorage cps ON cps.ColumnStorageID = cs.ID
        JOIN StorageFile sfi ON sfi.ID = cps.StorageFileID
        WHERE c.Type = 1
        ORDER BY t.Name, cs.StoragePosition
        """
        self.schema_df = self.handler.execute_query(sql)

    def populate_m(self):
        sql = """ 
        SELECT 
            t.Name AS 'TableName', 
            p.QueryDefinition AS 'Expression'
        FROM partition p 
        JOIN [Table] t ON t.ID = p.TableID 
        WHERE p.Type = 4;
        """
        self.m_df = self.handler.execute_query(sql)

    def populate_dax_tables(self):
        sql = """ 
        SELECT 
            t.Name AS 'TableName', 
            p.QueryDefinition AS 'Expression'
        FROM partition p 
        JOIN [Table] t ON t.ID = p.TableID 
        WHERE p.Type = 2;
        """
        self.dax_tables_df = self.handler.execute_query(sql)

    def populate_dax_measures(self):
        sql = """ 
        SELECT 
            t.Name AS TableName,
            m.Name,
            m.Expression,
            m.DisplayFolder,
            m.Description
        FROM Measure m 
        JOIN [Table] t ON m.TableID = t.ID;
        """
        self.dax_measures_df = self.handler.execute_query(sql)

    def populate_all_dataframes(self):
        self.populate_schema()
        self.populate_m()
        self.populate_dax_tables()
        self.populate_dax_measures()
        self.handler.close_connection()
