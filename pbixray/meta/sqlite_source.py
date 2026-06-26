import apsw
import io
import logging
import pandas as pd
import warnings

from ..abf.data_model import DataModel
from ..column_data.idfmeta import IdfmetaParser
from ..utils import AMO_PANDAS_TYPE_MAPPING, convert_time_columns, get_data_slice


# AMO numeric DataType codes that need post-decode special handling.
_AMO_SEMANTIC_TYPES = {9: "Date", 10: "Currency"}

logger = logging.getLogger(__name__)


class _SqliteReader:
    """In-memory APSW connection over a serialized SQLite blob."""

    def __init__(self, sqlite_buffer):
        self.conn = apsw.Connection(":memory:")
        self.conn.deserialize("main", sqlite_buffer)

    def query(self, sql):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                return pd.read_sql_query(sql, self.conn)
            except apsw.ExecutionCompleteError:
                return pd.DataFrame()
            except apsw.SQLError as e:
                logger.debug("SQL error executing query: %s — %s", sql, e)
                return pd.DataFrame()
            except (apsw.Error, pd.errors.DatabaseError) as e:
                logger.debug("Database error executing query: %s — %s", sql, e)
                return pd.DataFrame()

    def close(self):
        self.conn.close()


class SqliteMetadataSource:
    # Canonical columns produced by ``__populate_schema``. Used to give an
    # empty (no-matching-rows) schema a stable shape.
    _SCHEMA_COLUMNS = [
        'TableName', 'ColumnName', 'Dictionary', 'HIDX', 'IDF', 'IDFs',
        'Cardinality', 'DataType', 'BaseId', 'Magnitude', 'IsNullable',
        'ModifiedTime', 'StructureModifiedTime',
    ]

    # Friendly, resolved aggregations view (see ``__populate_aggregations``).
    _AGGREGATIONS_COLUMNS = [
        'AggregationTable', 'AggregationColumn', 'Summarization',
        'DetailTable', 'DetailColumn',
    ]

    # ``AlternateOf.Summarization`` enum -> human label.
    _SUMMARIZATION_LABELS = {
        0: 'GroupBy', 1: 'Sum', 2: 'Count', 3: 'Min', 4: 'Max',
    }

    def __init__(self, data_model: DataModel):
        self._data_model = data_model
        self._db = _SqliteReader(get_data_slice(data_model, 'metadata.sqlitedb'))

        # ``schema_df`` is needed eagerly by VertiPaqDecoder, statistics and the
        # table list, so it is built (and normalized) up front. Every other
        # dataframe is loaded lazily on first access (see ``__getattr__``) and
        # cached, so merely opening a model no longer runs ~40 queries.
        schema_df = convert_time_columns(self.__populate_schema())
        # A query that matches no rows (e.g. a model with only calculated tables,
        # measures, or a DirectQuery source) comes back column-less from the APSW
        # wrapper. Reindex to the canonical columns so downstream consumers can
        # always select them and the model still opens (with an empty schema).
        self.schema_df = schema_df.reindex(columns=self._SCHEMA_COLUMNS)
        self.__normalize_schema()

        # Map each lazy ``*_df`` attribute to the method that builds it. The
        # bound methods resolve name-mangled private populators correctly.
        self._lazy_populators = {
            'm_df':                          self.__populate_m,
            'm_parameters_df':               self.__populate_m_parameters,
            'dax_tables_df':                 self.__populate_dax_tables,
            'dax_measures_df':               self.__populate_dax_measures,
            'dax_columns_df':                self.__populate_dax_columns,
            'metadata_df':                   self.__populate_metadata,
            'relationships_df':              self.__populate_relationships,
            'rls_df':                        self.__populate_rls,
            'model_df':                      self.__populate_model,
            'tables_df':                     self.__populate_tables,
            'columns_df':                    self.__populate_columns,
            'partitions_df':                 self.__populate_partitions,
            'hierarchies_df':                self.__populate_hierarchies,
            'levels_df':                     self.__populate_levels,
            'datasources_df':                self.__populate_datasources,
            'perspectives_df':               self.__populate_perspectives,
            'perspective_tables_df':         self.__populate_perspective_tables,
            'perspective_columns_df':        self.__populate_perspective_columns,
            'perspective_hierarchies_df':    self.__populate_perspective_hierarchies,
            'perspective_measures_df':       self.__populate_perspective_measures,
            'kpis_df':                       self.__populate_kpis,
            'annotations_df':                self.__populate_annotations,
            'extended_properties_df':        self.__populate_extended_properties,
            'cultures_df':                   self.__populate_cultures,
            'translations_df':               self.__populate_translations,
            'linguistic_metadata_df':        self.__populate_linguistic_metadata,
            'query_groups_df':               self.__populate_query_groups,
            'calculation_groups_df':         self.__populate_calculation_groups,
            'calculation_items_df':          self.__populate_calculation_items,
            'calculation_expressions_df':    self.__populate_calculation_expressions,
            'variations_df':                 self.__populate_variations,
            'attribute_hierarchies_df':      self.__populate_attribute_hierarchies,
            'sets_df':                       self.__populate_sets,
            'refresh_policies_df':           self.__populate_refresh_policies,
            'detail_rows_definitions_df':    self.__populate_detail_rows_definitions,
            'format_string_definitions_df':  self.__populate_format_string_definitions,
            'functions_df':                  self.__populate_functions,
            'calendars_df':                  self.__populate_calendars,
            'calendar_column_groups_df':     self.__populate_calendar_column_groups,
            'calendar_column_refs_df':       self.__populate_calendar_column_refs,
            'alternate_of_df':               self.__populate_alternate_of,
            'aggregations_df':               self.__populate_aggregations,
            'related_column_details_df':     self.__populate_related_column_details,
            'group_by_columns_df':           self.__populate_group_by_columns,
            'binding_info_df':               self.__populate_binding_info,
            'analytics_ai_metadata_df':      self.__populate_analytics_ai_metadata,
            'data_coverage_definitions_df':  self.__populate_data_coverage_definitions,
            'role_memberships_df':           self.__populate_role_memberships,
        }

    def __getattr__(self, name):
        """Lazily build, timestamp-convert and cache ``*_df`` attributes.

        Invoked only when normal attribute lookup fails, so cached results (set
        below) and eager attributes bypass it entirely.
        """
        populators = self.__dict__.get('_lazy_populators')
        if populators and name in populators:
            df = convert_time_columns(populators[name]())
            setattr(self, name, df)  # cache for subsequent access
            return df
        raise AttributeError(
            f"{type(self).__name__!r} object has no attribute {name!r}"
        )

    def close(self):
        """Close the in-memory SQLite connection. Safe to call repeatedly."""
        db = self.__dict__.get('_db')
        if db is not None:
            db.close()
            self._db = None

    def _has_column(self, table, column):
        """Return True if ``table`` has ``column`` in this database.

        Metadata schemas evolve across Power BI versions: some columns the
        queries reference (e.g. ``Column.Type``) simply do not exist in older
        schemas. Column sets are cached per table on first lookup. ``table`` is
        always a fixed internal identifier, never user input.
        """
        cache = self.__dict__.setdefault('_column_cache', {})
        if table not in cache:
            cache[table] = {
                row[1]
                for row in self._db.conn.cursor().execute(
                    f'PRAGMA table_info("{table}")'
                )
            }
        return column in cache[table]

    def _col_or_null(self, table, column, alias):
        """SELECT-list fragment producing ``alias``.

        Emits the qualified ``column`` (e.g. ``c.DisplayFolder``) when its bare
        name exists on ``table``, else ``NULL``. Always aliased to the modern
        name so downstream column access stays stable across schema versions.
        Legacy schemas (SCHEMAVERSION < ~18) simply lack some modern columns;
        those degrade to ``None`` instead of failing the whole statement.
        """
        bare = column.split('.')[-1]
        if self._has_column(table, bare):
            return f"{column} AS {alias}"
        return f"NULL AS {alias}"

    def _column_type_col(self):
        """``Column.Type`` (1=Data, 2=Calculated, 3=RowNumber,
        4=CalculatedTableColumn) on modern schemas; legacy schemas store the
        same role enumeration in ``Column.BindingType``."""
        return "c.Type" if self._has_column("Column", "Type") else "c.BindingType"

    def _rel_col(self, modern):
        """Map a modern ``Relationship`` endpoint column to its legacy name.

        On legacy schemas the four endpoint columns and two cardinalities gained
        an ``End`` infix after the ``From``/``To`` prefix
        (``FromColumnID`` -> ``FromEndColumnID``). Detected via the presence of
        the modern ``FromColumnID`` column.
        """
        if self._has_column("Relationship", "FromColumnID"):
            return modern  # modern schema
        if modern.startswith("From"):
            return "FromEnd" + modern[len("From"):]
        if modern.startswith("To"):
            return "ToEnd" + modern[len("To"):]
        return modern

    def __normalize_schema(self):
        """Add format-agnostic ``PandasDataType`` and ``SemanticType`` columns
        so downstream code never has to know this came from a pbix."""
        if 'DataType' not in self.schema_df.columns:
            # Empty or unexpected schema (e.g. a query that found no matching
            # columns). Keep a stable shape instead of raising KeyError.
            self.schema_df = self.schema_df.assign(
                PandasDataType=pd.Series(dtype='object'),
                SemanticType=pd.Series(dtype='object'),
            )
            return
        dt = self.schema_df['DataType']
        self.schema_df = self.schema_df.assign(
            PandasDataType=dt.map(AMO_PANDAS_TYPE_MAPPING).fillna('object'),
            SemanticType=dt.map(_AMO_SEMANTIC_TYPES).fillna('Other'),
        )

    def get_segment_meta(self, column_row, idf=None):
        """Parse the ``.idfmeta`` blob for one partition IDF into per-segment dicts.

        ``idf`` selects which partition's IDF to read; it defaults to the column's
        first partition (``column_row["IDF"]``) so the single-partition contract is
        unchanged. The decoder iterates ``column_row["IDFs"]`` and passes each in
        turn to read that partition's segments.
        """
        buffer = get_data_slice(self._data_model, (idf or column_row["IDF"]) + 'meta')
        with io.BytesIO(buffer) as f:
            parsed = IdfmetaParser.from_io(f)
            return [
                {
                    'min_data_id': seg.ss.min_data_id,
                    'count_bit_packed': seg.subsegment.records if seg.has_subsegment != 0 else 0,
                    'bit_width': seg.bit_width,
                    'records': seg.records,
                }
                for seg in parsed.column_partition.segments
            ]

    # -------------------------------------------------------------------------
    # Original endpoints
    # -------------------------------------------------------------------------

    def __populate_schema(self):
        type_col = self._column_type_col()
        # A column's effective data type is its ExplicitDataType unless that is
        # Automatic (1) — typical for calculated columns — in which case the real
        # type lives in InferredDataType. Without this, a calculated currency
        # column (e.g. Internet Sales[Margin], ExplicitDataType=1 /
        # InferredDataType=10) is read as 'Other' and never gets the currency
        # /10000 scaling, decoding 10000x too large. Legacy schemas without
        # InferredDataType fall back to ExplicitDataType.
        if self._has_column("Column", "InferredDataType"):
            data_type_col = (
                "CASE WHEN c.ExplicitDataType = 1 THEN c.InferredDataType "
                "ELSE c.ExplicitDataType END"
            )
        else:
            data_type_col = "c.ExplicitDataType"
        # ``ColumnPartitionStorage`` has one row per (column, partition), so a
        # multi-partition table yields N rows per column — one IDF each. Order
        # them by ``PartitionStorage.StoragePosition`` (a per-table partition
        # ordering, present even on legacy schemas) so partitions concatenate in
        # storage order; the grouping below collapses them back to one row/column.
        sql = f"""
        SELECT
            t.Name AS TableName,
            c.ExplicitName AS ColumnName,
            sfd.FileName AS Dictionary,
            sfh.FileName AS HIDX,
            sfi.FileName AS IDF,
            cs.Statistics_DistinctStates as Cardinality,
            {data_type_col} AS DataType,
            --ds.DataType,
            ds.BaseId,
            ds.Magnitude,
            ds.IsNullable,
            c.ModifiedTime,
            c.StructureModifiedTime,
            cs.StoragePosition AS _ColumnPosition,
            ps.StoragePosition AS _PartitionPosition
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
        --IDF (one per partition)
        JOIN ColumnPartitionStorage cps ON cps.ColumnStorageID = cs.ID
        JOIN StorageFile sfi ON sfi.ID = cps.StorageFileID
        JOIN PartitionStorage ps ON ps.ID = cps.PartitionStorageID
        WHERE {type_col} IN (1,2)
        ORDER BY t.Name, cs.StoragePosition, ps.StoragePosition
        """
        return self.__collapse_partitions(self._db.query(sql))

    @staticmethod
    def __collapse_partitions(df):
        """Collapse the per-partition rows from the schema query into one row per
        column, attaching the ordered list of partition IDF files as ``IDFs``.

        Rows arrive ordered by column then partition ``StoragePosition``; every
        non-IDF field is identical across a column's partition rows (the dictionary,
        HIDX, cardinality, etc. are shared), so we keep the first of each and
        aggregate only the IDF file names. ``IDF`` stays as the first partition for
        backward compatibility.
        """
        if df.empty:
            return df
        # Stable group order = first appearance, which already reflects the
        # ``ORDER BY t.Name, cs.StoragePosition`` column ordering.
        idfs = (
            df.groupby(['TableName', 'ColumnName'], sort=False)['IDF']
            .apply(list)
            .rename('IDFs')
        )
        collapsed = df.drop_duplicates(subset=['TableName', 'ColumnName'], keep='first').copy()
        collapsed = collapsed.merge(idfs, on=['TableName', 'ColumnName'], how='left')
        return collapsed.drop(columns=['_ColumnPosition', '_PartitionPosition'])

    def __populate_m(self):
        # ``Partition.Type`` is absent on legacy schemas; without it M (4) and
        # calculated (2) partitions can't be distinguished, so there are none.
        where = "WHERE p.Type = 4" if self._has_column("Partition", "Type") else "WHERE 0"
        sql = f"""
        SELECT
            t.Name AS 'TableName',
            p.QueryDefinition AS 'Expression'
        FROM partition p
        JOIN [Table] t ON t.ID = p.TableID
        {where};
        """
        return self._db.query(sql)

    def __populate_m_parameters(self):
        sql = """
        SELECT
            Name as ParameterName,
            Description,
            Expression,
            ModifiedTime
        FROM Expression;
        """
        return self._db.query(sql)

    def __populate_dax_tables(self):
        # See ``__populate_m``: no ``Partition.Type`` -> no calculated tables.
        where = "WHERE p.Type = 2" if self._has_column("Partition", "Type") else "WHERE 0"
        sql = f"""
        SELECT
            t.Name AS 'TableName',
            p.QueryDefinition AS 'Expression'
        FROM partition p
        JOIN [Table] t ON t.ID = p.TableID
        {where};
        """
        return self._db.query(sql)

    def __populate_dax_measures(self):
        sql = f"""
        SELECT
            t.Name AS TableName,
            m.Name,
            m.Expression,
            {self._col_or_null("Measure", "m.DisplayFolder", "DisplayFolder")},
            m.Description
        FROM Measure m
        JOIN [Table] t ON m.TableID = t.ID;
        """
        return self._db.query(sql)

    def __populate_dax_columns(self):
        type_col = self._column_type_col()
        sql = f"""
        SELECT
            t.Name AS TableName,
            c.ExplicitName AS ColumnName,
            c.Expression
        FROM Column c
        JOIN [Table] t ON c.TableID = t.ID
        WHERE {type_col} = 2;
        """
        return self._db.query(sql)

    def __populate_metadata(self):
        sql = """
        SELECT Name,Value
        FROM Annotation
        WHERE ObjectType = 1
        """
        return self._db.query(sql)

    def __populate_relationships(self):
        # Legacy schemas rename the endpoint columns with an ``End`` infix
        # (``FromColumnID`` -> ``FromEndColumnID``); resolve via ``_rel_col``.
        from_table = self._rel_col("FromTableID")
        from_column = self._rel_col("FromColumnID")
        to_table = self._rel_col("ToTableID")
        to_column = self._rel_col("ToColumnID")
        from_cardinality = self._rel_col("FromCardinality")
        to_cardinality = self._rel_col("ToCardinality")
        sql = f"""
        SELECT
            ft.Name AS FromTableName,
            fc.ExplicitName AS FromColumnName,
            tt.Name AS ToTableName,
            tc.ExplicitName AS ToColumnName,
            rel.IsActive,
            CASE
                WHEN rel.{from_cardinality} = 2 THEN 'M'
                ELSE '1'
            END || ':' ||
            CASE
                WHEN rel.{to_cardinality} = 2 THEN 'M'
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
            LEFT JOIN [Table] ft ON rel.{from_table} = ft.id
            LEFT JOIN [Column] fc ON rel.{from_column} = fc.id
            LEFT JOIN [Table] tt ON rel.{to_table} = tt.id
            LEFT JOIN [Column] tc ON rel.{to_column} = tc.id
            LEFT JOIN RelationshipStorage rs ON rs.id = rel.RelationshipStorageID
            LEFT JOIN RelationshipIndexStorage rid ON rs.RelationshipIndexStorageID = rid.id
            LEFT JOIN RelationshipStorage rs2 ON rs2.id = rel.RelationshipStorage2ID
            LEFT JOIN RelationshipIndexStorage rid2 ON rs2.RelationshipIndexStorageID = rid2.id
        WHERE ft.SystemFlags = 0 AND tt.SystemFlags = 0
        """
        return self._db.query(sql)

    def __populate_rls(self):
        sql = f"""
        SELECT
            t.Name as TableName,
            r.Name as RoleName,
            r.Description as RoleDescription,
            tp.FilterExpression,
            tp.State,
            {self._col_or_null("TablePermission", "tp.MetadataPermission", "MetadataPermission")}
        FROM TablePermission tp
        JOIN [Table] t on t.ID = tp.TableID
        JOIN Role r on r.ID = tp.RoleID
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_MODEL
    # -------------------------------------------------------------------------

    def __populate_model(self):
        sql = "SELECT * FROM Model;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_TABLES
    # -------------------------------------------------------------------------

    def __populate_tables(self):
        sql = f"""
        SELECT
            t.ID,
            t.Name,
            t.Description,
            t.DataCategory,
            t.IsHidden,
            t.IsPrivate,
            t.ShowAsVariationsOnly,
            {self._col_or_null("Table", "t.LineageTag", "LineageTag")},
            {self._col_or_null("Table", "t.SourceLineageTag", "SourceLineageTag")},
            t.ModifiedTime,
            t.StructureModifiedTime
        FROM [Table] t
        WHERE t.SystemFlags = 0;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_COLUMNS
    # -------------------------------------------------------------------------

    def __populate_columns(self):
        type_col = self._column_type_col()
        sql = f"""
        SELECT
            c.ID,
            t.Name              AS TableName,
            c.TableID,
            COALESCE(c.ExplicitName, c.InferredName) AS Name,
            {type_col} AS Type,
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
            {self._col_or_null("Column", "c.DisplayFolder", "DisplayFolder")},
            c.IsAvailableInMDX,
            {self._col_or_null("Column", "c.EncodingHint", "EncodingHint")},
            {self._col_or_null("Column", "c.LineageTag", "LineageTag")},
            {self._col_or_null("Column", "c.SourceLineageTag", "SourceLineageTag")},
            c.DisplayOrdinal,
            c.ModifiedTime,
            c.StructureModifiedTime
        FROM [Column] c
        JOIN [Table] t ON c.TableID = t.ID
        WHERE {type_col} IN (1, 2)
        ORDER BY t.Name, c.DisplayOrdinal;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PARTITIONS
    # -------------------------------------------------------------------------

    def __populate_partitions(self):
        # Legacy ``Partition`` has neither ``Type`` nor ``Mode``; their legacy
        # analogues (``BindingType``/``CacheMode``) carry different semantics, so
        # degrade to NULL rather than reuse them.
        sql = f"""
        SELECT
            p.ID,
            t.Name          AS TableName,
            p.TableID,
            p.Name,
            p.Description,
            {self._col_or_null("Partition", "p.Type", "Type")},
            p.State,
            {self._col_or_null("Partition", "p.Mode", "Mode")},
            p.DataView,
            p.DataSourceID,
            p.QueryDefinition,
            p.SystemFlags,
            p.ModifiedTime,
            p.RefreshedTime
        FROM [Partition] p
        JOIN [Table] t ON p.TableID = t.ID;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_HIERARCHIES
    # -------------------------------------------------------------------------

    def __populate_hierarchies(self):
        sql = f"""
        SELECT
            h.ID,
            t.Name  AS TableName,
            h.TableID,
            h.Name,
            h.Description,
            h.IsHidden,
            h.State,
            {self._col_or_null("Hierarchy", "h.DisplayFolder", "DisplayFolder")},
            {self._col_or_null("Hierarchy", "h.HideMembers", "HideMembers")},
            h.HierarchyStorageID,
            {self._col_or_null("Hierarchy", "h.LineageTag", "LineageTag")},
            {self._col_or_null("Hierarchy", "h.SourceLineageTag", "SourceLineageTag")},
            h.ModifiedTime,
            h.StructureModifiedTime,
            h.RefreshedTime
        FROM Hierarchy h
        JOIN [Table] t ON h.TableID = t.ID;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_LEVELS
    # -------------------------------------------------------------------------

    def __populate_levels(self):
        # Legacy ``Level`` stores the position in ``Index`` (modern ``Ordinal``)
        # and lacks the lineage-tag columns.
        ordinal = "l.Ordinal" if self._has_column("Level", "Ordinal") else "l.[Index] AS Ordinal"
        sql = f"""
        SELECT
            l.ID,
            h.Name              AS HierarchyName,
            l.HierarchyID,
            t.Name              AS TableName,
            {ordinal},
            l.Name,
            l.Description,
            COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
            l.ColumnID,
            {self._col_or_null("Level", "l.LineageTag", "LineageTag")},
            {self._col_or_null("Level", "l.SourceLineageTag", "SourceLineageTag")},
            l.ModifiedTime
        FROM Level l
        JOIN Hierarchy  h ON l.HierarchyID = h.ID
        JOIN [Table]    t ON h.TableID     = t.ID
        JOIN [Column]   c ON l.ColumnID    = c.ID;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_DATASOURCES
    # -------------------------------------------------------------------------

    def __populate_datasources(self):
        sql = "SELECT * FROM DataSource;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_PERSPECTIVES
    # -------------------------------------------------------------------------

    def __populate_perspectives(self):
        sql = "SELECT * FROM Perspective;"
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_ANNOTATIONS
    # -------------------------------------------------------------------------

    def __populate_annotations(self):
        sql = "SELECT * FROM Annotation;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_EXTENDED_PROPERTIES
    # -------------------------------------------------------------------------

    def __populate_extended_properties(self):
        sql = "SELECT * FROM ExtendedProperty;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_CULTURES
    # -------------------------------------------------------------------------

    def __populate_cultures(self):
        sql = "SELECT * FROM Culture;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_OBJECT_TRANSLATIONS
    # -------------------------------------------------------------------------

    def __populate_translations(self):
        sql = f"""
        SELECT
            ot.ID,
            ot.CultureID,
            cu.Name  AS CultureName,
            ot.ObjectID,
            ot.ObjectType,
            ot.Property,
            ot.Value,
            {self._col_or_null("ObjectTranslation", "ot.Altered", "Altered")},
            ot.ModifiedTime
        FROM ObjectTranslation ot
        JOIN Culture cu ON ot.CultureID = cu.ID;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_LINGUISTIC_METADATA
    # -------------------------------------------------------------------------

    def __populate_linguistic_metadata(self):
        sql = f"""
        SELECT
            lm.ID,
            lm.CultureID,
            cu.Name     AS CultureName,
            lm.Content,
            {self._col_or_null("LinguisticMetadata", "lm.ContentType", "ContentType")},
            lm.ModifiedTime
        FROM LinguisticMetadata lm
        JOIN Culture cu ON lm.CultureID = cu.ID;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_QUERY_GROUPS
    # -------------------------------------------------------------------------

    def __populate_query_groups(self):
        sql = "SELECT * FROM QueryGroup;"
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_REFRESH_POLICIES
    # -------------------------------------------------------------------------

    def __populate_refresh_policies(self):
        # ``RefreshPolicy.Mode`` (import vs. hybrid/DirectQuery refresh) was added
        # in a later schema version; older models (e.g. SCHEMAVERSION 76) lack it,
        # so emit it defensively to keep a stable output shape.
        mode = self._col_or_null("RefreshPolicy", "rp.Mode", "Mode")
        sql = f"""
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
            {mode}
        FROM RefreshPolicy rp
        JOIN [Table] t ON rp.TableID = t.ID;
        """
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_DETAIL_ROWS_DEFINITIONS
    # -------------------------------------------------------------------------

    def __populate_detail_rows_definitions(self):
        sql = "SELECT * FROM DetailRowsDefinition;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_FORMAT_STRING_DEFINITIONS
    # -------------------------------------------------------------------------

    def __populate_format_string_definitions(self):
        sql = "SELECT * FROM FormatStringDefinition;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_FUNCTIONS
    # -------------------------------------------------------------------------

    def __populate_functions(self):
        sql = "SELECT * FROM [Function];"
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # Aggregations (friendly view over AlternateOf)
    # -------------------------------------------------------------------------

    def __populate_aggregations(self):
        """Resolved aggregation mappings — one row per aggregation-table column.

        Friendly layer over ``AlternateOf``: ``Summarization`` is the human
        label and ``DetailTable`` is resolved from the base column's *own*
        ``TableID`` (``AlternateOf.BaseTableID`` is ``0`` for column mappings,
        populated only for the count-rows case). See the count-rows fallback via
        the ``bt`` join.
        """
        sql = """
        SELECT
            at.Name                                     AS AggregationTable,
            COALESCE(ac.ExplicitName, ac.InferredName)  AS AggregationColumn,
            ao.Summarization                            AS Summarization,
            COALESCE(bct.Name, bt.Name)                 AS DetailTable,
            COALESCE(bc.ExplicitName, bc.InferredName)  AS DetailColumn
        FROM AlternateOf ao
        JOIN [Column] ac  ON ac.ID  = ao.ColumnID
        JOIN [Table]  at  ON at.ID  = ac.TableID
        LEFT JOIN [Column] bc  ON bc.ID  = ao.BaseColumnID
        LEFT JOIN [Table]  bct ON bct.ID = bc.TableID
        LEFT JOIN [Table]  bt  ON bt.ID  = ao.BaseTableID;
        """
        df = self._db.query(sql)
        if df.empty:
            # Missing ``AlternateOf`` (legacy schema) or no aggregations: give a
            # stable shape so callers can always select the canonical columns.
            return df.reindex(columns=self._AGGREGATIONS_COLUMNS)
        df['Summarization'] = df['Summarization'].map(self._SUMMARIZATION_LABELS)
        return df

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
        return self._db.query(sql)

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
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_BINDING_INFO
    # -------------------------------------------------------------------------

    def __populate_binding_info(self):
        sql = "SELECT * FROM BindingInfo;"
        return self._db.query(sql)

    # -------------------------------------------------------------------------
    # TMSCHEMA_ANALYTICS_AI_METADATA
    # -------------------------------------------------------------------------

    def __populate_analytics_ai_metadata(self):
        sql = "SELECT * FROM AnalyticsAIMetadata;"
        return self._db.query(sql)

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
        return self._db.query(sql)

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
        return self._db.query(sql)
