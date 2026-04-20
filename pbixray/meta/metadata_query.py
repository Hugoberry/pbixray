from ..utils import convert_time_columns


class MetadataQuery:
    def __init__(self, sqlite_handler):
        self.handler = sqlite_handler

        # Populate dataframes upon instantiation
        self.schema_df = self.__populate_schema()
        self.m_df = self.__populate_m()
        self.m_parameters_df = self.__populate_m_parameters()
        self.dax_tables_df = self.__populate_dax_tables()
        self.dax_measures_df = self.__populate_dax_measures()
        self.dax_columns_df = self.__populate_dax_columns()
        self.metadata_df = self.__populate_metadata()
        self.relationships_df = self.__populate_relationships()
        self.rls_df = self.__populate_rls()

        # TMSCHEMA_* DMV equivalents
        self.model_df                     = self.__populate_model()
        self.tables_df                    = self.__populate_tables()
        self.columns_df                   = self.__populate_columns()
        self.partitions_df                = self.__populate_partitions()
        self.hierarchies_df               = self.__populate_hierarchies()
        self.levels_df                    = self.__populate_levels()
        self.datasources_df               = self.__populate_datasources()
        self.perspectives_df              = self.__populate_perspectives()
        self.perspective_tables_df        = self.__populate_perspective_tables()
        self.perspective_columns_df       = self.__populate_perspective_columns()
        self.perspective_hierarchies_df   = self.__populate_perspective_hierarchies()
        self.perspective_measures_df      = self.__populate_perspective_measures()
        self.kpis_df                      = self.__populate_kpis()
        self.annotations_df               = self.__populate_annotations()
        self.extended_properties_df       = self.__populate_extended_properties()
        self.cultures_df                  = self.__populate_cultures()
        self.translations_df              = self.__populate_translations()
        self.linguistic_metadata_df       = self.__populate_linguistic_metadata()
        self.query_groups_df              = self.__populate_query_groups()
        self.calculation_groups_df        = self.__populate_calculation_groups()
        self.calculation_items_df         = self.__populate_calculation_items()
        self.calculation_expressions_df   = self.__populate_calculation_expressions()
        self.variations_df                = self.__populate_variations()
        self.attribute_hierarchies_df     = self.__populate_attribute_hierarchies()
        self.sets_df                      = self.__populate_sets()
        self.refresh_policies_df          = self.__populate_refresh_policies()
        self.detail_rows_definitions_df   = self.__populate_detail_rows_definitions()
        self.format_string_definitions_df = self.__populate_format_string_definitions()
        self.functions_df                 = self.__populate_functions()
        self.calendars_df                 = self.__populate_calendars()
        self.calendar_column_groups_df    = self.__populate_calendar_column_groups()
        self.calendar_column_refs_df      = self.__populate_calendar_column_refs()
        self.alternate_of_df              = self.__populate_alternate_of()
        self.related_column_details_df    = self.__populate_related_column_details()
        self.group_by_columns_df          = self.__populate_group_by_columns()
        self.binding_info_df              = self.__populate_binding_info()
        self.analytics_ai_metadata_df     = self.__populate_analytics_ai_metadata()
        self.data_coverage_definitions_df = self.__populate_data_coverage_definitions()
        self.role_memberships_df          = self.__populate_role_memberships()

        self.__convert_timestamps()
        self.handler.close_connection()

    def __convert_timestamps(self):
        for attr, df in vars(self).items():
            if attr.endswith('_df') and hasattr(df, 'columns'):
                setattr(self, attr, convert_time_columns(df))

    # -------------------------------------------------------------------------
    # Original endpoints
    # -------------------------------------------------------------------------

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
        WHERE c.Type IN (1,2)
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

    def __populate_m_parameters(self):
        sql = """
        SELECT
            Name as ParameterName,
            Description,
            Expression,
            ModifiedTime
        FROM Expression;
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

    def __populate_dax_columns(self):
        sql = """
        SELECT
            t.Name AS TableName,
            c.ExplicitName AS ColumnName,
            c.Expression
        FROM Column c
        JOIN [Table] t ON c.TableID = t.ID
        WHERE c.Type = 2;
        """
        return self.handler.execute_query(sql)

    def __populate_metadata(self):
        sql = """
        SELECT Name,Value
        FROM Annotation
        WHERE ObjectType = 1
        """
        return self.handler.execute_query(sql)

    def __populate_relationships(self):
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

    def __populate_rls(self):
        sql = """
        SELECT
            t.Name as TableName,
            r.Name as RoleName,
            r.Description as RoleDescription,
            tp.FilterExpression,
            tp.State,
            tp.MetadataPermission
        FROM TablePermission tp
        JOIN [Table] t on t.ID = tp.TableID
        JOIN Role r on r.ID = tp.RoleID
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_MODEL
    # -------------------------------------------------------------------------

    def __populate_model(self):
        sql = "SELECT * FROM Model;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_TABLES
    # -------------------------------------------------------------------------

    def __populate_tables(self):
        sql = """
        SELECT
            t.ID,
            t.Name,
            t.Description,
            t.DataCategory,
            t.IsHidden,
            t.IsPrivate,
            t.ShowAsVariationsOnly,
            t.LineageTag,
            t.SourceLineageTag,
            t.ModifiedTime,
            t.StructureModifiedTime
        FROM [Table] t
        WHERE t.SystemFlags = 0;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_COLUMNS
    # -------------------------------------------------------------------------

    def __populate_columns(self):
        sql = """
        SELECT
            c.ID,
            t.Name              AS TableName,
            c.TableID,
            COALESCE(c.ExplicitName, c.InferredName) AS Name,
            c.Type,
            COALESCE(c.ExplicitDataType, c.InferredDataType) AS DataType,
            c.DataCategory,
            c.Description,
            c.IsHidden,
            c.IsKey,
            c.IsUnique,
            c.IsNullable,
            c.SummarizeBy,
            c.SourceColumn,
            c.Expression,
            c.FormatString,
            c.DisplayFolder,
            c.IsAvailableInMDX,
            c.EncodingHint,
            c.LineageTag,
            c.SourceLineageTag,
            c.DisplayOrdinal,
            c.ModifiedTime,
            c.StructureModifiedTime
        FROM [Column] c
        JOIN [Table] t ON c.TableID = t.ID
        WHERE c.Type IN (1, 2)
        ORDER BY t.Name, c.DisplayOrdinal;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PARTITIONS
    # -------------------------------------------------------------------------

    def __populate_partitions(self):
        sql = """
        SELECT
            p.ID,
            t.Name          AS TableName,
            p.TableID,
            p.Name,
            p.Description,
            p.Type,
            p.State,
            p.Mode,
            p.DataView,
            p.DataSourceID,
            p.QueryDefinition,
            p.SystemFlags,
            p.ModifiedTime,
            p.RefreshedTime
        FROM [Partition] p
        JOIN [Table] t ON p.TableID = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_HIERARCHIES
    # -------------------------------------------------------------------------

    def __populate_hierarchies(self):
        sql = """
        SELECT
            h.ID,
            t.Name  AS TableName,
            h.TableID,
            h.Name,
            h.Description,
            h.IsHidden,
            h.State,
            h.DisplayFolder,
            h.HideMembers,
            h.HierarchyStorageID,
            h.LineageTag,
            h.SourceLineageTag,
            h.ModifiedTime,
            h.StructureModifiedTime,
            h.RefreshedTime
        FROM Hierarchy h
        JOIN [Table] t ON h.TableID = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_LEVELS
    # -------------------------------------------------------------------------

    def __populate_levels(self):
        sql = """
        SELECT
            l.ID,
            h.Name              AS HierarchyName,
            l.HierarchyID,
            t.Name              AS TableName,
            l.Ordinal,
            l.Name,
            l.Description,
            COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
            l.ColumnID,
            l.LineageTag,
            l.SourceLineageTag,
            l.ModifiedTime
        FROM Level l
        JOIN Hierarchy  h ON l.HierarchyID = h.ID
        JOIN [Table]    t ON h.TableID     = t.ID
        JOIN [Column]   c ON l.ColumnID    = c.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_DATASOURCES
    # -------------------------------------------------------------------------

    def __populate_datasources(self):
        sql = "SELECT * FROM DataSource;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PERSPECTIVES
    # -------------------------------------------------------------------------

    def __populate_perspectives(self):
        sql = "SELECT * FROM Perspective;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PERSPECTIVE_TABLES
    # -------------------------------------------------------------------------

    def __populate_perspective_tables(self):
        sql = """
        SELECT
            pt.ID,
            p.Name  AS PerspectiveName,
            pt.PerspectiveID,
            t.Name  AS TableName,
            pt.TableID,
            pt.IncludeAll,
            pt.ModifiedTime
        FROM PerspectiveTable pt
        JOIN Perspective p ON pt.PerspectiveID = p.ID
        JOIN [Table]     t ON pt.TableID       = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PERSPECTIVE_COLUMNS
    # -------------------------------------------------------------------------

    def __populate_perspective_columns(self):
        sql = """
        SELECT
            pc.ID,
            pt.PerspectiveID,
            p.Name              AS PerspectiveName,
            pc.ColumnID,
            COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
            t.Name              AS TableName,
            pc.ModifiedTime
        FROM PerspectiveColumn  pc
        JOIN PerspectiveTable   pt ON pc.PerspectiveTableID = pt.ID
        JOIN Perspective        p  ON pt.PerspectiveID      = p.ID
        JOIN [Column]           c  ON pc.ColumnID           = c.ID
        JOIN [Table]            t  ON c.TableID             = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PERSPECTIVE_HIERARCHIES
    # -------------------------------------------------------------------------

    def __populate_perspective_hierarchies(self):
        sql = """
        SELECT
            ph.ID,
            pt.PerspectiveID,
            p.Name  AS PerspectiveName,
            ph.HierarchyID,
            h.Name  AS HierarchyName,
            t.Name  AS TableName,
            ph.ModifiedTime
        FROM PerspectiveHierarchy ph
        JOIN PerspectiveTable     pt ON ph.PerspectiveTableID = pt.ID
        JOIN Perspective          p  ON pt.PerspectiveID      = p.ID
        JOIN Hierarchy            h  ON ph.HierarchyID        = h.ID
        JOIN [Table]              t  ON h.TableID             = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PERSPECTIVE_MEASURES
    # -------------------------------------------------------------------------

    def __populate_perspective_measures(self):
        sql = """
        SELECT
            pm.ID,
            pt.PerspectiveID,
            p.Name  AS PerspectiveName,
            pm.MeasureID,
            m.Name  AS MeasureName,
            t.Name  AS TableName,
            pm.ModifiedTime
        FROM PerspectiveMeasure pm
        JOIN PerspectiveTable   pt ON pm.PerspectiveTableID = pt.ID
        JOIN Perspective        p  ON pt.PerspectiveID      = p.ID
        JOIN Measure            m  ON pm.MeasureID          = m.ID
        JOIN [Table]            t  ON m.TableID             = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_KPIS
    # -------------------------------------------------------------------------

    def __populate_kpis(self):
        sql = """
        SELECT
            k.ID,
            m.Name  AS MeasureName,
            k.MeasureID,
            t.Name  AS TableName,
            k.Description,
            k.TargetDescription,
            k.TargetExpression,
            k.TargetFormatString,
            k.StatusGraphic,
            k.StatusDescription,
            k.StatusExpression,
            k.TrendGraphic,
            k.TrendDescription,
            k.TrendExpression,
            k.ModifiedTime
        FROM KPI k
        JOIN Measure m ON k.MeasureID = m.ID
        JOIN [Table] t ON m.TableID   = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_ANNOTATIONS
    # -------------------------------------------------------------------------

    def __populate_annotations(self):
        sql = "SELECT * FROM Annotation;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_EXTENDED_PROPERTIES
    # -------------------------------------------------------------------------

    def __populate_extended_properties(self):
        sql = "SELECT * FROM ExtendedProperty;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CULTURES
    # -------------------------------------------------------------------------

    def __populate_cultures(self):
        sql = "SELECT * FROM Culture;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_OBJECT_TRANSLATIONS
    # -------------------------------------------------------------------------

    def __populate_translations(self):
        sql = """
        SELECT
            ot.ID,
            ot.CultureID,
            cu.Name  AS CultureName,
            ot.ObjectID,
            ot.ObjectType,
            ot.Property,
            ot.Value,
            ot.Altered,
            ot.ModifiedTime
        FROM ObjectTranslation ot
        JOIN Culture cu ON ot.CultureID = cu.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_LINGUISTIC_METADATA
    # -------------------------------------------------------------------------

    def __populate_linguistic_metadata(self):
        sql = """
        SELECT
            lm.ID,
            lm.CultureID,
            cu.Name     AS CultureName,
            lm.Content,
            lm.ContentType,
            lm.ModifiedTime
        FROM LinguisticMetadata lm
        JOIN Culture cu ON lm.CultureID = cu.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_QUERY_GROUPS
    # -------------------------------------------------------------------------

    def __populate_query_groups(self):
        sql = "SELECT * FROM QueryGroup;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CALCULATION_GROUPS
    # -------------------------------------------------------------------------

    def __populate_calculation_groups(self):
        sql = """
        SELECT
            cg.ID,
            t.Name  AS TableName,
            cg.TableID,
            cg.Description,
            cg.Precedence,
            cg.ModifiedTime
        FROM CalculationGroup cg
        JOIN [Table] t ON cg.TableID = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CALCULATION_ITEMS
    # -------------------------------------------------------------------------

    def __populate_calculation_items(self):
        sql = """
        SELECT
            ci.ID,
            cg.TableID,
            t.Name              AS TableName,
            ci.CalculationGroupID,
            ci.Name,
            ci.Description,
            ci.Expression,
            ci.Ordinal,
            ci.State,
            ci.ErrorMessage,
            ci.FormatStringDefinitionID,
            ci.ModifiedTime
        FROM CalculationItem  ci
        JOIN CalculationGroup cg ON ci.CalculationGroupID = cg.ID
        JOIN [Table]          t  ON cg.TableID            = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CALCULATION_EXPRESSIONS
    # -------------------------------------------------------------------------

    def __populate_calculation_expressions(self):
        sql = """
        SELECT
            ce.ID,
            ce.CalculationGroupID,
            cg.TableID,
            t.Name  AS TableName,
            ce.Description,
            ce.Expression,
            ce.SelectionMode,
            ce.State,
            ce.ErrorMessage,
            ce.FormatStringDefinitionID,
            ce.ModifiedTime
        FROM CalculationExpression ce
        JOIN CalculationGroup      cg ON ce.CalculationGroupID = cg.ID
        JOIN [Table]               t  ON cg.TableID            = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_VARIATIONS
    # -------------------------------------------------------------------------

    def __populate_variations(self):
        sql = """
        SELECT
            v.ID,
            v.ColumnID,
            COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
            t.Name  AS TableName,
            v.Name,
            v.Description,
            v.RelationshipID,
            v.DefaultHierarchyID,
            v.DefaultColumnID,
            v.IsDefault
        FROM Variation v
        JOIN [Column] c ON v.ColumnID = c.ID
        JOIN [Table]  t ON c.TableID  = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_ATTRIBUTE_HIERARCHIES
    # -------------------------------------------------------------------------

    def __populate_attribute_hierarchies(self):
        sql = """
        SELECT
            ah.ID,
            ah.ColumnID,
            COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
            t.Name  AS TableName,
            ah.State,
            ah.AttributeHierarchyStorageID,
            ah.ModifiedTime,
            ah.RefreshedTime
        FROM AttributeHierarchy ah
        JOIN [Column] c ON ah.ColumnID = c.ID
        JOIN [Table]  t ON c.TableID   = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_SETS
    # -------------------------------------------------------------------------

    def __populate_sets(self):
        sql = """
        SELECT
            s.ID,
            t.Name  AS TableName,
            s.TableID,
            s.Name,
            s.Description,
            s.Expression,
            s.IsDynamic,
            s.IsHidden,
            s.DisplayFolder,
            s.State,
            s.ErrorMessage,
            s.ModifiedTime,
            s.StructureModifiedTime
        FROM [Set] s
        JOIN [Table] t ON s.TableID = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_REFRESH_POLICIES
    # -------------------------------------------------------------------------

    def __populate_refresh_policies(self):
        sql = """
        SELECT
            rp.ID,
            t.Name  AS TableName,
            rp.TableID,
            rp.PolicyType,
            rp.RollingWindowGranularity,
            rp.RollingWindowPeriods,
            rp.IncrementalGranularity,
            rp.IncrementalPeriods,
            rp.IncrementalPeriodsOffset,
            rp.PollingExpression,
            rp.SourceExpression,
            rp.Mode
        FROM RefreshPolicy rp
        JOIN [Table] t ON rp.TableID = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_DETAIL_ROWS_DEFINITIONS
    # -------------------------------------------------------------------------

    def __populate_detail_rows_definitions(self):
        sql = "SELECT * FROM DetailRowsDefinition;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_FORMAT_STRING_DEFINITIONS
    # -------------------------------------------------------------------------

    def __populate_format_string_definitions(self):
        sql = "SELECT * FROM FormatStringDefinition;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_FUNCTIONS
    # -------------------------------------------------------------------------

    def __populate_functions(self):
        sql = "SELECT * FROM [Function];"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CALENDARS
    # -------------------------------------------------------------------------

    def __populate_calendars(self):
        sql = """
        SELECT
            cal.ID,
            t.Name  AS TableName,
            cal.TableID,
            cal.Name,
            cal.Description,
            cal.LineageTag,
            cal.SourceLineageTag,
            cal.ModifiedTime
        FROM Calendar cal
        JOIN [Table] t ON cal.TableID = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CALENDAR_COLUMN_GROUPS
    # -------------------------------------------------------------------------

    def __populate_calendar_column_groups(self):
        sql = """
        SELECT
            ccg.ID,
            ccg.CalendarID,
            cal.Name    AS CalendarName,
            t.Name      AS TableName,
            ccg.TimeUnit,
            ccg.ModifiedTime
        FROM CalendarColumnGroup ccg
        JOIN Calendar cal ON ccg.CalendarID = cal.ID
        JOIN [Table]  t   ON cal.TableID    = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CALENDAR_COLUMN_REFERENCES
    # -------------------------------------------------------------------------

    def __populate_calendar_column_refs(self):
        sql = """
        SELECT
            ccr.ID,
            ccr.CalendarColumnGroupID,
            ccr.ColumnID,
            COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
            t.Name  AS TableName,
            ccr.IsPrimaryColumn,
            ccr.ModifiedTime
        FROM CalendarColumnReference ccr
        JOIN [Column] c ON ccr.ColumnID = c.ID
        JOIN [Table]  t ON c.TableID    = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_ALTERNATE_OF
    # -------------------------------------------------------------------------

    def __populate_alternate_of(self):
        sql = """
        SELECT
            ao.ID,
            ao.ColumnID,
            COALESCE(c.ExplicitName,  c.InferredName)  AS ColumnName,
            t.Name                                      AS TableName,
            ao.BaseColumnID,
            COALESCE(bc.ExplicitName, bc.InferredName) AS BaseColumnName,
            ao.BaseTableID,
            bt.Name                                     AS BaseTableName,
            ao.Summarization
        FROM AlternateOf   ao
        JOIN [Column]  c  ON ao.ColumnID     = c.ID
        JOIN [Table]   t  ON c.TableID       = t.ID
        LEFT JOIN [Column] bc ON ao.BaseColumnID = bc.ID
        LEFT JOIN [Table]  bt ON ao.BaseTableID  = bt.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_RELATED_COLUMN_DETAILS
    # -------------------------------------------------------------------------

    def __populate_related_column_details(self):
        sql = """
        SELECT
            rcd.ID,
            rcd.ColumnID,
            COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
            t.Name  AS TableName,
            rcd.ModifiedTime
        FROM RelatedColumnDetails rcd
        JOIN [Column] c ON rcd.ColumnID = c.ID
        JOIN [Table]  t ON c.TableID    = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_GROUP_BY_COLUMNS
    # -------------------------------------------------------------------------

    def __populate_group_by_columns(self):
        sql = """
        SELECT
            gbc.ID,
            gbc.RelatedColumnDetailsID,
            rcd.ColumnID                                AS OwnerColumnID,
            COALESCE(oc.ExplicitName, oc.InferredName) AS OwnerColumnName,
            gbc.GroupingColumnID,
            COALESCE(gc.ExplicitName, gc.InferredName) AS GroupingColumnName,
            t.Name                                      AS TableName,
            gbc.ModifiedTime
        FROM GroupByColumn         gbc
        JOIN RelatedColumnDetails  rcd ON gbc.RelatedColumnDetailsID = rcd.ID
        JOIN [Column] oc ON rcd.ColumnID         = oc.ID
        JOIN [Column] gc ON gbc.GroupingColumnID = gc.ID
        JOIN [Table]  t  ON oc.TableID           = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_BINDING_INFO
    # -------------------------------------------------------------------------

    def __populate_binding_info(self):
        sql = "SELECT * FROM BindingInfo;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_ANALYTICS_AI_METADATA
    # -------------------------------------------------------------------------

    def __populate_analytics_ai_metadata(self):
        sql = "SELECT * FROM AnalyticsAIMetadata;"
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_DATA_COVERAGE_DEFINITIONS
    # -------------------------------------------------------------------------

    def __populate_data_coverage_definitions(self):
        sql = """
        SELECT
            dcd.ID,
            p.Name  AS PartitionName,
            dcd.PartitionID,
            t.Name  AS TableName,
            dcd.Description,
            dcd.Expression,
            dcd.State,
            dcd.ErrorMessage,
            dcd.ModifiedTime
        FROM DataCoverageDefinition dcd
        JOIN [Partition] p ON dcd.PartitionID = p.ID
        JOIN [Table]   t ON p.TableID       = t.ID;
        """
        return self.handler.execute_query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_ROLE_MEMBERSHIPS
    # -------------------------------------------------------------------------

    def __populate_role_memberships(self):
        sql = """
        SELECT
            rm.ID,
            r.Name  AS RoleName,
            rm.RoleID,
            rm.MemberName,
            rm.MemberID,
            rm.IdentityProvider,
            rm.MemberType,
            rm.ModifiedTime
        FROM RoleMembership rm
        JOIN Role r ON rm.RoleID = r.ID;
        """
        return self.handler.execute_query(sql)
