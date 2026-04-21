# TMSCHEMA DMV ↔ SQLite Metadata Query Mapping

Power BI Tabular models expose metadata through Analysis Services DMVs — queries against
`$System.TMSCHEMA_*` rowsets available in DAX Studio, SSMS, or any XMLA endpoint.
The pbixray library reads the identical data directly from `metadata.sqlitedb` embedded in
the PBIX file.

---

## TMSCHEMA_MODEL

```sql
SELECT * FROM Model;
```

---

## TMSCHEMA_TABLES

```sql
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
```

---

## TMSCHEMA_COLUMNS

```sql
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
```

---

## TMSCHEMA_MEASURES

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

```sql
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
```

---

## TMSCHEMA_LEVELS

```sql
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
```

---

## TMSCHEMA_RELATIONSHIPS

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

```sql
SELECT * FROM DataSource;
```

---

## TMSCHEMA_PARTITIONS

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
FROM [Partition] p
JOIN [Table] t ON p.TableID = t.ID;
```

---

## TMSCHEMA_ROLES

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

```sql
SELECT * FROM Perspective;
```

---

## TMSCHEMA_PERSPECTIVE_TABLES

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

```sql
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
```

---

## TMSCHEMA_PERSPECTIVE_HIERARCHIES

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
JOIN PerspectiveTable     pt ON ph.PerspectiveTableID = pt.ID
JOIN Perspective          p  ON pt.PerspectiveID      = p.ID
JOIN Hierarchy            h  ON ph.HierarchyID        = h.ID
JOIN [Table]              t  ON h.TableID             = t.ID;
```

---

## TMSCHEMA_PERSPECTIVE_MEASURES

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
JOIN PerspectiveTable   pt ON pm.PerspectiveTableID = pt.ID
JOIN Perspective        p  ON pt.PerspectiveID      = p.ID
JOIN Measure            m  ON pm.MeasureID          = m.ID
JOIN [Table]            t  ON m.TableID             = t.ID;
```

---

## TMSCHEMA_KPIS

```sql
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
```

---

## TMSCHEMA_ANNOTATIONS

```sql
SELECT * FROM Annotation;
```

---

## TMSCHEMA_EXTENDED_PROPERTIES

```sql
SELECT * FROM ExtendedProperty;
```

---

## TMSCHEMA_EXPRESSIONS

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

```sql
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
```

---

## TMSCHEMA_CALCULATION_EXPRESSIONS

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
    ce.FormatStringDefinitionID,
    ce.ModifiedTime
FROM CalculationExpression ce
JOIN CalculationGroup      cg ON ce.CalculationGroupID = cg.ID
JOIN [Table]               t  ON cg.TableID            = t.ID;
```

---

## TMSCHEMA_VARIATIONS

```sql
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
```

---

## TMSCHEMA_ATTRIBUTE_HIERARCHIES

```sql
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
```

---

## TMSCHEMA_SETS

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

```sql
SELECT * FROM DetailRowsDefinition;
```

---

## TMSCHEMA_FORMAT_STRING_DEFINITIONS

```sql
SELECT * FROM FormatStringDefinition;
```

---

## TMSCHEMA_CULTURES

```sql
SELECT * FROM Culture;
```

---

## TMSCHEMA_OBJECT_TRANSLATIONS

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

```sql
SELECT
    lm.ID,
    lm.CultureID,
    cu.Name     AS CultureName,
    lm.Content,
    lm.ContentType,
    lm.ModifiedTime
FROM LinguisticMetadata lm
JOIN Culture cu ON lm.CultureID = cu.ID;
```

---

## TMSCHEMA_QUERY_GROUPS

```sql
SELECT * FROM QueryGroup;
```

---

## TMSCHEMA_FUNCTIONS

```sql
SELECT * FROM [Function];
```

---

## TMSCHEMA_CALENDARS

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

```sql
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
```

---

## TMSCHEMA_CALENDAR_COLUMN_REFERENCES

```sql
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
```

---

## TMSCHEMA_ALTERNATE_OF

```sql
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
```

---

## TMSCHEMA_RELATED_COLUMN_DETAILS

```sql
SELECT
    rcd.ID,
    rcd.ColumnID,
    COALESCE(c.ExplicitName, c.InferredName) AS ColumnName,
    t.Name  AS TableName,
    rcd.ModifiedTime
FROM RelatedColumnDetails rcd
JOIN [Column] c ON rcd.ColumnID = c.ID
JOIN [Table]  t ON c.TableID    = t.ID;
```

---

## TMSCHEMA_GROUP_BY_COLUMNS

```sql
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
```

---

## TMSCHEMA_BINDING_INFO

```sql
SELECT * FROM BindingInfo;
```

---

## TMSCHEMA_ANALYTICS_AI_METADATA

```sql
SELECT * FROM AnalyticsAIMetadata;
```

---

## TMSCHEMA_DATA_COVERAGE_DEFINITIONS

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
JOIN [Partition] p ON dcd.PartitionID = p.ID
JOIN [Table]     t ON p.TableID       = t.ID;
```
