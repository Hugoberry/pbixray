# TMSCHEMA DMV ↔ SQLite Metadata Query Mapping

Power BI Tabular models expose metadata through Analysis Services DMVs — queries against
`$System.TMSCHEMA_*` rowsets available in DAX Studio, SSMS, or any XMLA endpoint.
The pbixray library reads the identical data directly from `metadata.sqlitedb` embedded in
the PBIX file.

This document maps each DMV to its SQLite equivalent so the queries can become named
endpoints in the `pbixray` module.

> **Note on existing endpoints** — several DMVs are already covered (with storage stats or
> filtered views) by `MetadataQuery` in `pbixray/meta/metadata_query.py`:
> `schema_df` ≈ COLUMNS, `m_df` / `dax_tables_df` ≈ PARTITIONS,
> `dax_measures_df` ≈ MEASURES, `relationships_df` ≈ RELATIONSHIPS,
> `rls_df` ≈ TABLE_PERMISSIONS. The full unfiltered equivalents are included below for
> completeness.

---

## TMSCHEMA_MODEL

Model-level settings and properties.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_MODEL
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    Description,
    Culture,
    Collation,
    DefaultMode,
    DefaultDataView,
    DiscourageImplicitMeasures,
    DiscourageReportMeasures,
    DirectLakeBehavior,
    ForceUniqueNames,
    DisableAutoExists,
    ModifiedTime,
    StructureModifiedTime
FROM Model;
```

---

## TMSCHEMA_TABLES

All user-facing tables in the model (system tables excluded).

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_TABLES
```

**SQLite**
```sql
SELECT
    t.ID,
    t.Name,
    t.Description,
    t.DataCategory,
    t.IsHidden,
    t.IsPrivate,
    t.ShowAsVariationsOnly,
    t.SystemManaged,
    t.ExcludeFromModelRefresh,
    t.ExcludeFromAutomaticAggregations,
    t.LineageTag,
    t.SourceLineageTag,
    t.ModifiedTime,
    t.StructureModifiedTime
FROM [Table] t
WHERE t.SystemFlags = 0;
```

---

## TMSCHEMA_COLUMNS

All imported and calculated columns with their data types and display properties.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_COLUMNS
```

**SQLite**
```sql
SELECT
    c.ID,
    t.Name   AS TableName,
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
WHERE c.Type IN (1, 2)   -- 1 = data column, 2 = calculated column
ORDER BY t.Name, c.DisplayOrdinal;
```

---

## TMSCHEMA_MEASURES

All DAX measures with their expressions and display metadata.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_MEASURES
```

**SQLite**
```sql
SELECT
    m.ID,
    t.Name AS TableName,
    m.TableID,
    m.Name,
    m.Description,
    m.DataType,
    m.Expression,
    m.FormatString,
    m.IsHidden,
    m.IsSimpleMeasure,
    m.DisplayFolder,
    m.DataCategory,
    m.LineageTag,
    m.SourceLineageTag,
    m.ModifiedTime,
    m.StructureModifiedTime
FROM Measure m
JOIN [Table] t ON m.TableID = t.ID;
```

---

## TMSCHEMA_HIERARCHIES

User-defined hierarchies defined on tables.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_HIERARCHIES
```

**SQLite**
```sql
SELECT
    h.ID,
    t.Name AS TableName,
    h.TableID,
    h.Name,
    h.Description,
    h.IsHidden,
    h.DisplayFolder,
    h.HideMembers,
    h.LineageTag,
    h.SourceLineageTag,
    h.ModifiedTime,
    h.StructureModifiedTime
FROM Hierarchy h
JOIN [Table] t ON h.TableID = t.ID;
```

---

## TMSCHEMA_LEVELS

Individual levels within each hierarchy.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_LEVELS
```

**SQLite**
```sql
SELECT
    l.ID,
    h.Name AS HierarchyName,
    l.HierarchyID,
    l.Ordinal,
    l.Name,
    l.Description,
    c.ExplicitName AS ColumnName,
    l.ColumnID,
    l.LineageTag,
    l.SourceLineageTag,
    l.ModifiedTime
FROM Level l
JOIN Hierarchy h ON l.HierarchyID = h.ID
JOIN [Column]  c ON l.ColumnID    = c.ID;
```

---

## TMSCHEMA_RELATIONSHIPS

All relationships between tables including cardinality and cross-filter direction.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_RELATIONSHIPS
```

**SQLite**
```sql
SELECT
    rel.ID,
    rel.Name,
    rel.IsActive,
    rel.Type,
    rel.CrossFilteringBehavior,
    rel.JoinOnDateBehavior,
    rel.RelyOnReferentialIntegrity,
    rel.SecurityFilteringBehavior,
    ft.Name  AS FromTableName,
    rel.FromTableID,
    fc.ExplicitName AS FromColumnName,
    rel.FromColumnID,
    CASE WHEN rel.FromCardinality = 2 THEN 'Many' ELSE 'One' END AS FromCardinality,
    tt.Name  AS ToTableName,
    rel.ToTableID,
    tc.ExplicitName AS ToColumnName,
    rel.ToColumnID,
    CASE WHEN rel.ToCardinality = 2 THEN 'Many' ELSE 'One' END AS ToCardinality,
    rel.ModifiedTime
FROM Relationship rel
LEFT JOIN [Table]  ft ON rel.FromTableID  = ft.ID
LEFT JOIN [Column] fc ON rel.FromColumnID = fc.ID
LEFT JOIN [Table]  tt ON rel.ToTableID    = tt.ID
LEFT JOIN [Column] tc ON rel.ToColumnID   = tc.ID;
```

---

## TMSCHEMA_DATASOURCES

Data sources used for table partitions.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_DATASOURCES
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    Description,
    Type,
    ConnectionString,
    ImpersonationMode,
    MaxConnections,
    Timeout,
    Provider,
    ConnectionDetails,
    ModifiedTime
FROM DataSource;
```

---

## TMSCHEMA_PARTITIONS

All partitions per table, including their query definition and refresh state.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_PARTITIONS
```

**SQLite**
```sql
SELECT
    p.ID,
    t.Name AS TableName,
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
FROM Partition p
JOIN [Table] t ON p.TableID = t.ID;
```

---

## TMSCHEMA_ROLES

Security roles defined in the model.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_ROLES
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    Description,
    ModelPermission,
    ModifiedTime
FROM Role;
```

---

## TMSCHEMA_ROLE_MEMBERSHIPS

Users and groups assigned to each role.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_ROLE_MEMBERSHIPS
```

**SQLite**
```sql
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
```

---

## TMSCHEMA_TABLE_PERMISSIONS

Row-level security filter expressions per role per table.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_TABLE_PERMISSIONS
```

**SQLite**
```sql
SELECT
    tp.ID,
    r.Name  AS RoleName,
    tp.RoleID,
    t.Name  AS TableName,
    tp.TableID,
    tp.FilterExpression,
    tp.MetadataPermission,
    tp.State,
    tp.ErrorMessage,
    tp.ModifiedTime
FROM TablePermission tp
JOIN Role    r ON tp.RoleID  = r.ID
JOIN [Table] t ON tp.TableID = t.ID;
```

---

## TMSCHEMA_COLUMN_PERMISSIONS

Column-level metadata permissions per role.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_COLUMN_PERMISSIONS
```

**SQLite**
```sql
SELECT
    cp.ID,
    tp.RoleID,
    r.Name         AS RoleName,
    cp.ColumnID,
    c.ExplicitName AS ColumnName,
    t.Name         AS TableName,
    cp.MetadataPermission,
    cp.ModifiedTime
FROM ColumnPermission cp
JOIN TablePermission tp ON cp.TablePermissionID = tp.ID
JOIN Role            r  ON tp.RoleID    = r.ID
JOIN [Column]        c  ON cp.ColumnID  = c.ID
JOIN [Table]         t  ON c.TableID    = t.ID;
```

---

## TMSCHEMA_PERSPECTIVES

Perspectives (named subsets of the model).

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_PERSPECTIVES
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    Description,
    ModifiedTime
FROM Perspective;
```

---

## TMSCHEMA_PERSPECTIVE_TABLES

Which tables are visible in each perspective.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_PERSPECTIVE_TABLES
```

**SQLite**
```sql
SELECT
    pt.ID,
    p.Name  AS PerspectiveName,
    pt.PerspectiveID,
    t.Name  AS TableName,
    pt.TableID,
    pt.IncludeAll,
    pt.ModifiedTime
FROM PerspectiveTable pt
JOIN Perspective p  ON pt.PerspectiveID = p.ID
JOIN [Table]     t  ON pt.TableID       = t.ID;
```

---

## TMSCHEMA_PERSPECTIVE_COLUMNS

Which columns are visible in each perspective.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_PERSPECTIVE_COLUMNS
```

**SQLite**
```sql
SELECT
    pc.ID,
    pt.PerspectiveID,
    p.Name         AS PerspectiveName,
    pc.ColumnID,
    c.ExplicitName AS ColumnName,
    t.Name         AS TableName,
    pc.ModifiedTime
FROM PerspectiveColumn pc
JOIN PerspectiveTable pt ON pc.PerspectiveTableID = pt.ID
JOIN Perspective      p  ON pt.PerspectiveID      = p.ID
JOIN [Column]         c  ON pc.ColumnID           = c.ID
JOIN [Table]          t  ON c.TableID             = t.ID;
```

---

## TMSCHEMA_PERSPECTIVE_HIERARCHIES

Which hierarchies are visible in each perspective.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_PERSPECTIVE_HIERARCHIES
```

**SQLite**
```sql
SELECT
    ph.ID,
    pt.PerspectiveID,
    p.Name  AS PerspectiveName,
    ph.HierarchyID,
    h.Name  AS HierarchyName,
    t.Name  AS TableName,
    ph.ModifiedTime
FROM PerspectiveHierarchy ph
JOIN PerspectiveTable pt ON ph.PerspectiveTableID = pt.ID
JOIN Perspective      p  ON pt.PerspectiveID      = p.ID
JOIN Hierarchy        h  ON ph.HierarchyID        = h.ID
JOIN [Table]          t  ON h.TableID             = t.ID;
```

---

## TMSCHEMA_PERSPECTIVE_MEASURES

Which measures are visible in each perspective.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_PERSPECTIVE_MEASURES
```

**SQLite**
```sql
SELECT
    pm.ID,
    pt.PerspectiveID,
    p.Name  AS PerspectiveName,
    pm.MeasureID,
    m.Name  AS MeasureName,
    t.Name  AS TableName,
    pm.ModifiedTime
FROM PerspectiveMeasure pm
JOIN PerspectiveTable pt ON pm.PerspectiveTableID = pt.ID
JOIN Perspective      p  ON pt.PerspectiveID      = p.ID
JOIN Measure          m  ON pm.MeasureID          = m.ID
JOIN [Table]          t  ON m.TableID             = t.ID;
```

---

## TMSCHEMA_KPIS

KPI definitions (target, status, trend) attached to measures.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_KPIS
```

**SQLite**
```sql
SELECT
    k.ID,
    m.Name  AS MeasureName,
    k.MeasureID,
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
JOIN Measure m ON k.MeasureID = m.ID;
```

---

## TMSCHEMA_ANNOTATIONS

Custom annotations attached to any model object.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_ANNOTATIONS
```

**SQLite**
```sql
SELECT
    ID,
    ObjectID,
    ObjectType,
    Name,
    Value,
    ModifiedTime
FROM Annotation;
```

---

## TMSCHEMA_EXTENDED_PROPERTIES

Extended custom properties attached to model objects.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_EXTENDED_PROPERTIES
```

**SQLite**
```sql
SELECT
    ID,
    ObjectID,
    ObjectType,
    Name,
    Type,
    Value,
    ModifiedTime
FROM ExtendedProperty;
```

---

## TMSCHEMA_EXPRESSIONS

Shared Power Query parameters and named expressions.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_EXPRESSIONS
```

**SQLite**
```sql
SELECT
    e.ID,
    e.Name,
    e.Description,
    e.Kind,
    e.Expression,
    qg.Folder AS QueryGroup,
    e.QueryGroupID,
    e.LineageTag,
    e.SourceLineageTag,
    e.ModifiedTime
FROM Expression e
LEFT JOIN QueryGroup qg ON e.QueryGroupID = qg.ID;
```

---

## TMSCHEMA_CALCULATION_GROUPS

Calculation groups (used for time intelligence and measure modifiers).

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_CALCULATION_GROUPS
```

**SQLite**
```sql
SELECT
    cg.ID,
    t.Name  AS TableName,
    cg.TableID,
    cg.Description,
    cg.Precedence,
    cg.ModifiedTime
FROM CalculationGroup cg
JOIN [Table] t ON cg.TableID = t.ID;
```

---

## TMSCHEMA_CALCULATION_ITEMS

Individual items within each calculation group.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_CALCULATION_ITEMS
```

**SQLite**
```sql
SELECT
    ci.ID,
    cg.TableID,
    t.Name  AS TableName,
    ci.CalculationGroupID,
    ci.Name,
    ci.Description,
    ci.Expression,
    ci.Ordinal,
    ci.State,
    ci.ErrorMessage,
    ci.ModifiedTime
FROM CalculationItem ci
JOIN CalculationGroup cg ON ci.CalculationGroupID = cg.ID
JOIN [Table]          t  ON cg.TableID            = t.ID;
```

---

## TMSCHEMA_CALCULATION_EXPRESSIONS

Scalar expressions associated with calculation groups (newer format).

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_CALCULATION_EXPRESSIONS
```

**SQLite**
```sql
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
    ce.ModifiedTime
FROM CalculationExpression ce
JOIN CalculationGroup cg ON ce.CalculationGroupID = cg.ID
JOIN [Table]          t  ON cg.TableID            = t.ID;
```

---

## TMSCHEMA_VARIATIONS

Column variations — alternate data paths via a related table.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_VARIATIONS
```

**SQLite**
```sql
SELECT
    v.ID,
    v.ColumnID,
    c.ExplicitName AS ColumnName,
    t.Name         AS TableName,
    v.Name,
    v.Description,
    v.RelationshipID,
    v.DefaultHierarchyID,
    v.DefaultColumnID,
    v.IsDefault
FROM Variation v
JOIN [Column] c ON v.ColumnID = c.ID
JOIN [Table]  t ON c.TableID  = t.ID;
```

---

## TMSCHEMA_ATTRIBUTE_HIERARCHIES

Internal attribute hierarchies created on each column for MDX compatibility.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_ATTRIBUTE_HIERARCHIES
```

**SQLite**
```sql
SELECT
    ah.ID,
    ah.ColumnID,
    c.ExplicitName AS ColumnName,
    t.Name         AS TableName,
    ah.State,
    ah.ModifiedTime,
    ah.RefreshedTime
FROM AttributeHierarchy ah
JOIN [Column] c ON ah.ColumnID = c.ID
JOIN [Table]  t ON c.TableID   = t.ID;
```

---

## TMSCHEMA_SETS

Named sets with DAX expressions.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_SETS
```

**SQLite**
```sql
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
```

---

## TMSCHEMA_REFRESH_POLICIES

Incremental refresh (rolling window) policies per table.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_REFRESH_POLICIES
```

**SQLite**
```sql
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
```

---

## TMSCHEMA_DETAIL_ROWS_DEFINITIONS

"Show details" drill-through expressions for measures and tables.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_DETAIL_ROWS_DEFINITIONS
```

**SQLite**
```sql
SELECT
    ID,
    ObjectID,
    ObjectType,
    Expression,
    State,
    ErrorMessage,
    ModifiedTime
FROM DetailRowsDefinition;
```

---

## TMSCHEMA_FORMAT_STRING_DEFINITIONS

Dynamic format string expressions for measures and columns.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_FORMAT_STRING_DEFINITIONS
```

**SQLite**
```sql
SELECT
    ID,
    ObjectID,
    ObjectType,
    Expression,
    State,
    ErrorMessage,
    ModifiedTime
FROM FormatStringDefinition;
```

---

## TMSCHEMA_CULTURES

Cultures (languages) defined on the model.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_CULTURES
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    LinguisticMetadataID,
    ModifiedTime,
    StructureModifiedTime
FROM Culture;
```

---

## TMSCHEMA_OBJECT_TRANSLATIONS

Translated names and descriptions for model objects per culture.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_OBJECT_TRANSLATIONS
```

**SQLite**
```sql
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
```

---

## TMSCHEMA_LINGUISTIC_METADATA

Q&A linguistic metadata (synonyms, phrasings) per culture.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_LINGUISTIC_METADATA
```

**SQLite**
```sql
SELECT
    lm.ID,
    lm.CultureID,
    cu.Name AS CultureName,
    lm.Content,
    lm.ContentType,
    lm.ModifiedTime
FROM LinguisticMetadata lm
JOIN Culture cu ON lm.CultureID = cu.ID;
```

---

## TMSCHEMA_QUERY_GROUPS

Organizational folders for Power Query queries.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_QUERY_GROUPS
```

**SQLite**
```sql
SELECT
    ID,
    Folder,
    Description
FROM QueryGroup;
```

---

## TMSCHEMA_FUNCTIONS

User-defined DAX functions.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_FUNCTIONS
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    Description,
    Expression,
    IsHidden,
    State,
    ErrorMessage,
    LineageTag,
    SourceLineageTag,
    ModifiedTime,
    StructureModifiedTime
FROM [Function];
```

---

## TMSCHEMA_CALENDARS

Auto date/time calendar definitions for time intelligence.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_CALENDARS
```

**SQLite**
```sql
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
```

---

## TMSCHEMA_CALENDAR_COLUMN_GROUPS

Time unit groupings within a calendar definition.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_CALENDAR_COLUMN_GROUPS
```

**SQLite**
```sql
SELECT
    ccg.ID,
    ccg.CalendarID,
    cal.Name AS CalendarName,
    ccg.TimeUnit,
    ccg.ModifiedTime
FROM CalendarColumnGroup ccg
JOIN Calendar cal ON ccg.CalendarID = cal.ID;
```

---

## TMSCHEMA_CALENDAR_COLUMN_REFERENCES

Column references within each calendar column group.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_CALENDAR_COLUMN_REFERENCES
```

**SQLite**
```sql
SELECT
    ccr.ID,
    ccr.CalendarColumnGroupID,
    ccr.ColumnID,
    c.ExplicitName AS ColumnName,
    t.Name         AS TableName,
    ccr.IsPrimaryColumn,
    ccr.ModifiedTime
FROM CalendarColumnReference ccr
JOIN [Column] c ON ccr.ColumnID = c.ID
JOIN [Table]  t ON c.TableID    = t.ID;
```

---

## TMSCHEMA_ALTERNATE_OF

Alternate column declarations for aggregation tables.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_ALTERNATE_OF
```

**SQLite**
```sql
SELECT
    ao.ID,
    ao.ColumnID,
    c.ExplicitName  AS ColumnName,
    t.Name          AS TableName,
    ao.BaseColumnID,
    bc.ExplicitName AS BaseColumnName,
    ao.BaseTableID,
    bt.Name         AS BaseTableName,
    ao.Summarization
FROM AlternateOf ao
JOIN [Column]  c  ON ao.ColumnID     = c.ID
JOIN [Table]   t  ON c.TableID       = t.ID
LEFT JOIN [Column] bc ON ao.BaseColumnID = bc.ID
LEFT JOIN [Table]  bt ON ao.BaseTableID  = bt.ID;
```

---

## TMSCHEMA_RELATED_COLUMN_DETAILS

Group-by column grouping ownership metadata.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_RELATED_COLUMN_DETAILS
```

**SQLite**
```sql
SELECT
    rcd.ID,
    rcd.ColumnID,
    c.ExplicitName AS ColumnName,
    t.Name         AS TableName,
    rcd.ModifiedTime
FROM RelatedColumnDetails rcd
JOIN [Column] c ON rcd.ColumnID = c.ID
JOIN [Table]  t ON c.TableID    = t.ID;
```

---

## TMSCHEMA_GROUP_BY_COLUMNS

Columns used for grouping in related column details.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_GROUP_BY_COLUMNS
```

**SQLite**
```sql
SELECT
    gbc.ID,
    gbc.RelatedColumnDetailsID,
    rcd.ColumnID    AS OwnerColumnID,
    oc.ExplicitName AS OwnerColumnName,
    gbc.GroupingColumnID,
    gc.ExplicitName AS GroupingColumnName,
    t.Name          AS TableName,
    gbc.ModifiedTime
FROM GroupByColumn gbc
JOIN RelatedColumnDetails rcd ON gbc.RelatedColumnDetailsID = rcd.ID
JOIN [Column] oc ON rcd.ColumnID         = oc.ID
JOIN [Column] gc ON gbc.GroupingColumnID = gc.ID
JOIN [Table]  t  ON oc.TableID           = t.ID;
```

---

## TMSCHEMA_BINDING_INFO

Data source binding information (used in Direct Lake / composite models).

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_BINDING_INFO
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    Description,
    Type,
    ConnectionId
FROM BindingInfo;
```

---

## TMSCHEMA_ANALYTICS_AI_METADATA

AI-powered analytics definitions (Key Influencers, Q&A measures).

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_ANALYTICS_AI_METADATA
```

**SQLite**
```sql
SELECT
    ID,
    Name,
    MeasureAnalysisDefinition
FROM AnalyticsAIMetadata;
```

---

## TMSCHEMA_DATA_COVERAGE_DEFINITIONS

Data coverage expressions for incremental refresh partitions.

**DMV**
```sql
SELECT * FROM $System.TMSCHEMA_DATA_COVERAGE_DEFINITIONS
```

**SQLite**
```sql
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
JOIN Partition p ON dcd.PartitionID = p.ID
JOIN [Table]   t ON p.TableID       = t.ID;
```

---

## Suggested `MetadataQuery` endpoints

The table below maps each DMV above to a suggested Python property name following the
`__populate_*` / `*_df` convention already used in
[`pbixray/meta/metadata_query.py`](pbixray/meta/metadata_query.py).

| Property (`*_df`)          | DMV                                  | Notes                                  |
|----------------------------|--------------------------------------|----------------------------------------|
| `model_df`                 | TMSCHEMA_MODEL                       | new                                    |
| `tables_df`                | TMSCHEMA_TABLES                      | new (schema_df has storage overlay)    |
| `columns_df`               | TMSCHEMA_COLUMNS                     | new (schema_df has storage overlay)    |
| `partitions_df`            | TMSCHEMA_PARTITIONS                  | new (m_df / dax_tables_df are filtered)|
| `hierarchies_df`           | TMSCHEMA_HIERARCHIES                 | new                                    |
| `levels_df`                | TMSCHEMA_LEVELS                      | new                                    |
| `datasources_df`           | TMSCHEMA_DATASOURCES                 | new                                    |
| `perspectives_df`          | TMSCHEMA_PERSPECTIVES                | new                                    |
| `perspective_tables_df`    | TMSCHEMA_PERSPECTIVE_TABLES          | new                                    |
| `perspective_columns_df`   | TMSCHEMA_PERSPECTIVE_COLUMNS         | new                                    |
| `perspective_hierarchies_df` | TMSCHEMA_PERSPECTIVE_HIERARCHIES   | new                                    |
| `perspective_measures_df`  | TMSCHEMA_PERSPECTIVE_MEASURES        | new                                    |
| `kpis_df`                  | TMSCHEMA_KPIS                        | new                                    |
| `annotations_df`           | TMSCHEMA_ANNOTATIONS                 | new (metadata_df filters ObjectType=1) |
| `extended_properties_df`   | TMSCHEMA_EXTENDED_PROPERTIES         | new                                    |
| `cultures_df`              | TMSCHEMA_CULTURES                    | new                                    |
| `translations_df`          | TMSCHEMA_OBJECT_TRANSLATIONS         | new                                    |
| `linguistic_metadata_df`   | TMSCHEMA_LINGUISTIC_METADATA         | new                                    |
| `query_groups_df`          | TMSCHEMA_QUERY_GROUPS                | new                                    |
| `calculation_groups_df`    | TMSCHEMA_CALCULATION_GROUPS          | new                                    |
| `calculation_items_df`     | TMSCHEMA_CALCULATION_ITEMS           | new                                    |
| `calculation_expressions_df` | TMSCHEMA_CALCULATION_EXPRESSIONS   | new                                    |
| `variations_df`            | TMSCHEMA_VARIATIONS                  | new                                    |
| `attribute_hierarchies_df` | TMSCHEMA_ATTRIBUTE_HIERARCHIES       | new                                    |
| `sets_df`                  | TMSCHEMA_SETS                        | new                                    |
| `refresh_policies_df`      | TMSCHEMA_REFRESH_POLICIES            | new                                    |
| `detail_rows_definitions_df` | TMSCHEMA_DETAIL_ROWS_DEFINITIONS   | new                                    |
| `format_string_definitions_df` | TMSCHEMA_FORMAT_STRING_DEFINITIONS | new                                  |
| `functions_df`             | TMSCHEMA_FUNCTIONS                   | new                                    |
| `calendars_df`             | TMSCHEMA_CALENDARS                   | new                                    |
| `calendar_column_groups_df` | TMSCHEMA_CALENDAR_COLUMN_GROUPS     | new                                    |
| `calendar_column_refs_df`  | TMSCHEMA_CALENDAR_COLUMN_REFERENCES  | new                                    |
| `alternate_of_df`          | TMSCHEMA_ALTERNATE_OF                | new                                    |
| `related_column_details_df` | TMSCHEMA_RELATED_COLUMN_DETAILS     | new                                    |
| `group_by_columns_df`      | TMSCHEMA_GROUP_BY_COLUMNS            | new                                    |
| `binding_info_df`          | TMSCHEMA_BINDING_INFO                | new                                    |
| `analytics_ai_metadata_df` | TMSCHEMA_ANALYTICS_AI_METADATA       | new                                    |
| `data_coverage_definitions_df` | TMSCHEMA_DATA_COVERAGE_DEFINITIONS | new                                  |
| — *(existing)*             | TMSCHEMA_MEASURES                    | → `dax_measures_df`                    |
| — *(existing)*             | TMSCHEMA_RELATIONSHIPS               | → `relationships_df`                   |
| — *(existing)*             | TMSCHEMA_TABLE_PERMISSIONS           | → `rls_df`                             |
| — *(existing)*             | TMSCHEMA_EXPRESSIONS                 | → `m_parameters_df`                    |
