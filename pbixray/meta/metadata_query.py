
class MetadataQuery:
    def __init__(self, sqlite_handler):
        self.handler = sqlite_handler
        
        # Populate dataframes upon instantiation
        self.schema_df = self.__populate_schema()
        self.m_df = self.__populate_m()
        self.dax_tables_df = self.__populate_dax_tables()
        self.dax_measures_df = self.__populate_dax_measures()
        self.metadata_df = self.populate_metadata()
        self.relationships_df = self.populate_relationships()
        self.handler.close_connection()

    def __populate_schema(self):
        sql = """ 
        SELECT 
            t.Name AS TableName,
            c.ExplicitName AS ColumnName,
            sfd.FileName AS Dictionary, 
            sfh.FileName AS HIDX, 
            sfi.FileName AS IDF,
            cs.Statistics_DistinctStates as Cardinality,
            c.ExplicitDataType AS DataType,
            --ds.DataType,
            ds.BaseId,
            ds.Magnitude,
            ds.IsNullable,
            c.ModifiedTime,
            c.StructureModifiedTime
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
        return self.handler.execute_query(sql)

    def __populate_m(self):
        sql = """ 
        SELECT 
            t.Name AS 'TableName', 
            p.QueryDefinition AS 'Expression'
        FROM partition p 
        JOIN [Table] t ON t.ID = p.TableID 
        WHERE p.Type = 4;
        """
        return self.handler.execute_query(sql)

    def __populate_dax_tables(self):
        sql = """ 
        SELECT 
            t.Name AS 'TableName', 
            p.QueryDefinition AS 'Expression'
        FROM partition p 
        JOIN [Table] t ON t.ID = p.TableID 
        WHERE p.Type = 2;
        """
        return self.handler.execute_query(sql)

    def __populate_dax_measures(self):
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
        return self.handler.execute_query(sql)

    def populate_metadata(self):
        sql = """
        SELECT Name,Value 
        FROM Annotation 
        WHERE ObjectType = 1
        """
        return self.handler.execute_query(sql)
    
    def populate_relationships(self):
        sql = """
        SELECT 
            ft.Name AS FromTableName,
            fc.ExplicitName AS FromColumnName,
            tt.Name AS ToTableName,
            tc.ExplicitName AS ToColumnName,
            rel.IsActive,
            CASE 
                WHEN rel.FromCardinality = 2 THEN 'M'
                ELSE '1'
            END || ':' || 
            CASE 
                WHEN rel.ToCardinality = 2 THEN 'M'
                ELSE '1'
            END AS Cardinality,
            CASE 
                WHEN rel.CrossFilteringBehavior = 1 THEN 'Single'
                WHEN rel.CrossFilteringBehavior = 2 THEN 'Both'
                ELSE CAST(rel.CrossFilteringBehavior AS TEXT)
            END AS CrossFilteringBehavior,
            rid.RecordCount as FromKeyCount,
            rid2.RecordCount AS ToKeyCount,
            rel.RelyOnReferentialIntegrity
        FROM Relationship rel
            LEFT JOIN [Table] ft ON rel.FromTableID = ft.id
            LEFT JOIN [Column] fc ON rel.FromColumnID = fc.id
            LEFT JOIN [Table] tt ON rel.ToTableID = tt.id AND tt.systemflags = 0
            LEFT JOIN [Column] tc ON rel.ToColumnID = tc.id
            LEFT JOIN RelationshipStorage rs ON rs.id = rel.RelationshipStorageID
            LEFT JOIN RelationshipIndexStorage rid ON rs.RelationshipIndexStorageID = rid.id
            LEFT JOIN RelationshipStorage rs2 ON rs2.id = rel.RelationshipStorage2ID
            LEFT JOIN RelationshipIndexStorage rid2 ON rs2.RelationshipIndexStorageID = rid2.id
        """
        return self.handler.execute_query(sql)