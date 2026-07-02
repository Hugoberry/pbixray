# PBIXRay
[![Downloads](https://static.pepy.tech/badge/pbixray)](https://pepy.tech/project/pbixray)
## Overview

PBIXRay is a Python library designed to parse and analyze PBIX files, which are used with Microsoft Power BI. This library provides a straightforward way to extract valuable information from PBIX files, including tables, metadata, Power Query code, and more.

This library is the Python implementation of the logic embedded in the DuckDB extension [duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension/).

> **Note:** PBIXRay also supports Excel (XLSX) files with embedded PowerPivot models. You can use the same API to extract and analyze data models from XLSX files that contain PowerPivot data.

> **Note:** Analysis Services backup files (`.abf`) are also accepted. An `.abf`
> holds the same data model as a `.pbix`, just without the zip envelope, so the
> same `PBIXRay('path/to/backup.abf')` API applies. Multi-partition tables
> (classic SSAS partitioning and incremental-refresh partitions) are decoded in
> full — `get_table` concatenates every partition in storage order.

## Installation

Install with pip:

```bash
pip install pbixray
```

## Getting Started
To start using PBIXRay, import the module and initialize it with the path to your PBIX file:
```python
from pbixray import PBIXRay

model = PBIXRay('path/to/your/file.pbix')
```

### Large models (on-disk loading)
By default the entire decompressed data model is held in memory. For models whose
uncompressed size approaches or exceeds available RAM, pass `on_disk=True`: the
decompressed data is streamed to a temporary file and memory-mapped, so only the
pages a requested table actually touches are faulted in. Use `temp_dir` to control
where the spill file is created (defaults to the system temp directory).

```python
# Spill to disk + mmap instead of holding everything in RAM.
with PBIXRay('path/to/large.pbix', on_disk=True, temp_dir='/fast/scratch') as model:
    df = model.get_table('Sales')
# leaving the `with` block releases the mapping and removes the temp file
```

`PBIXRay` is also a context manager; `model.close()` (or exiting the `with` block)
deterministically releases the memory map and the metadata connection. When
`on_disk=False` (the default) behavior is unchanged. Metadata (DAX, TMSCHEMA_*, etc.)
is loaded lazily on first access, so simply opening a file is cheap.

The `DataModel` member is read in place from the container file whenever it is
STORED in the zip (the normal case — it carries its own compression). If the
member is additionally *uncompressed* (a raw ABF backup inside the zip),
`on_disk=True` serves it directly from the `.pbix`/`.xlsx` with no temp-file
copy at all.

## Features and Usage
### Tables
To list all tables in the model:
```python
tables = model.tables
print(tables)
```
### Metadata
To get metadata about the Power BI configuration used during model creation:
```python
metadata = model.metadata
print(metadata)
```
### Power Query
To display all M/Power Query code used for data transformation, in a dataframe with `TableName` and `Expression` columns:
```python
power_query = model.power_query
print(power_query)
```
### M Parameters
To display all M Parameters values in a dataframe with `ParameterName`, `Description`, `Expression` and `ModifiedTime` columns:
```python
m_parameters = model.m_parameters
print(m_parameters)
```
### Model Size
To find out the model size in bytes:
```python
size = model.size
print(f"Model size: {size} bytes")
```
### DAX Calculated Tables
To view DAX calculated tables in a dataframe with `TableName` and `Expression` columns:
```python
dax_tables = model.dax_tables
print(dax_tables)
```
### DAX Measures
To access DAX measures in a dataframe with `TableName`, `Name`, `Expression`, `DisplayFolder`, and `Description` columns:
```python
dax_measures = model.dax_measures
print(dax_measures)
```
### Calculated Columns
To access calculated column DAX expressions in a dataframe with `TableName`,`ColumnName` and `Expression` columns:
```python
dax_columns = model.dax_columns
print(dax_columns)
```
### Aggregations
To inspect Power BI aggregations (the "Manage aggregations" feature) as a resolved dataframe with `AggregationTable`, `AggregationColumn`, `Summarization`, `DetailTable`, and `DetailColumn` columns:
```python
aggregations = model.aggregations
print(aggregations)
```
Each row maps one aggregation-table column to a detail (base) table. `Summarization` is the human label (`GroupBy`, `Sum`, `Count`, `Min`, `Max`); `DetailColumn` is `None` for the "Count table rows" case. A model with no aggregations returns an empty dataframe with these columns.
### Schema
To get details about the data model schema and column types in a dataframe with `TableName`, `ColumnName`, and `PandasDataType` columns:
```python
schema = model.schema
print(schema)
```
### Relationships
To get the details about the data model relationships in a dataframe with `FromTableName`, `FromColumnName`, `ToTableName`, `ToColumnName`, `IsActive`, `Cardinality`, `CrossFilteringBehavior`, `FromKeyCount`, `ToKeyCount` and `RelyOnReferentialIntegrity` columns:
```python
relationships = model.relationships
print(relationships)
```
### Row-Level Security (RLS)
To get the details about Row-Level Security roles and permissions in a dataframe with `TableName`, `RoleName`, `RoleDescription`, `FilterExpression`, `State` and `MetadataPermission` columns:
```python
rls = model.rls
print(rls)
```
### Object-Level Security (OLS)
To get object-level security restrictions as a resolved dataframe with `RoleName`, `TableName`, `ColumnName`, `Scope` and `Permission` columns:
```python
ols = model.ols
print(ols)
```
Each row is one secured object: `Scope='Column'` rows hide or expose a single column, `Scope='Table'` rows (where `ColumnName` is `None`) a whole table. `Permission` is `None` (hidden), `Read` (visible) or `Default`. Plain row-level-security rows are excluded — see `model.rls`. A model with no OLS returns an empty dataframe with these columns.
### Perspectives
To inspect perspective membership as a single consolidated dataframe with `PerspectiveName`, `ObjectType`, `TableName`, `ObjectName` and `IncludeAll` columns:
```python
perspectives = model.perspectives
print(perspectives)
```
Each row is one object included in a perspective; `ObjectType` is `Table`, `Column`, `Measure` or `Hierarchy`, and `IncludeAll` is populated only for `Table` rows. This is a friendly roll-up over the raw `tmschema_perspective_*` endpoints. A model with no perspectives returns an empty dataframe with these columns.
### Get Table Contents
To retrieve the contents of a specified table:
```python
table_name = 'YourTableName'
table_contents = model.get_table(table_name)
print(table_contents)
```
To decode only a subset of columns from a wide table (decoding the others is skipped),
pass `columns`:
```python
table_contents = model.get_table(table_name, columns=['ProductKey', 'Sales'])
```
With `strings_as_categorical=True` string columns come back as `pd.Categorical`,
so each distinct value is stored once instead of once per row — a large memory
saving on low-cardinality string columns:
```python
table_contents = model.get_table(table_name, strings_as_categorical=True)
```
Dictionary decode runs on a native Huffman kernel ([xmhuffman](https://github.com/Hugoberry/xmhuffman-cython)) and fans out across cores automatically for large dictionaries.
### Stream Large Tables in Chunks
For tables too large to materialize whole, `iter_table` yields DataFrame chunks
instead of one DataFrame. Chunks follow VertiPaq segment boundaries, and
`chunk_size` further splits each segment (chunks never span two segments, so
tail chunks may be shorter). String columns default to `pd.Categorical`,
sharing one categories array across all chunks; pass
`strings_as_categorical=False` for plain object-dtype strings.
```python
with PBIXRay('path/to/large.pbix', on_disk=True) as model:
    for chunk in model.iter_table('Sales', chunk_size=1_000_000):
        process(chunk)  # chunk.index is the global row range
```
The dictionaries of every selected column are decoded up front and kept for the
whole iteration, so on dictionary-heavy models (e.g. wide free-text columns)
pass `columns` to project only what you need. Combine with `on_disk=True` to
also keep the decompressed model itself out of RAM.
### Statistics
To get statistics about the model, including column cardinality and byte sizes of dictionary, hash index, and data components, in a dataframe with columns `TableName`, `ColumnName`, `Cardinality`, `Dictionary`, `HashIndex`, and `DataSize`:
```python
statistics = model.statistics
print(statistics)
```

### Connections
Reports expose their `Connections` manifest — the list of data connections
declared by the report — as a list of dictionaries:
```python
print(model.connections)
```
Self-contained (import) models usually return an empty list.

### Live-connection (thin) reports
Some `.pbix` files are *thin reports* with no embedded model: they live-connect
to an external Analysis Services server (`analysisServicesDatabaseLive`) or a
Power BI Service dataset (`pbiServiceLive`). Because the model lives on a remote
server, there is nothing to extract on disk, and constructing `PBIXRay` raises
`LiveConnectionError`. The exception carries the parsed connection details so you
can still identify what the report points at:
```python
from pbixray import PBIXRay, LiveConnectionError, NoEmbeddedModelError

try:
    model = PBIXRay("thin-report.pbix")
except LiveConnectionError as e:
    print(e.connection_type)   # e.g. 'pbiServiceLive'
    print(e.database_name)     # remote dataset id, when available
    print(e.connections)       # full manifest (list of dicts)
```
The exception hierarchy is `LiveConnectionError` → `NoEmbeddedModelError` →
`PBIXRayError`. `NoEmbeddedModelError` is raised when a file has no model and no
connection manifest. Both also subclass `RuntimeError` for backward
compatibility.

### Power Query (DataMashup)
`power_query` and `m_parameters` read the M from the Analysis Services metadata,
which works for **import** models. Some models — notably **DirectQuery / native
SQL** — keep their queries and parameters only in the report's `DataMashup` part
([MS-QDEFF]). `model.data_mashup` and `model.mashup_queries` parse that part
directly:
```python
df = model.mashup_queries        # Name, Kind, IsParameter, Expression, Type, DefaultValue, AllowedValues
params = df[df["IsParameter"]]   # the Power Query parameters and their metadata

mashup = model.data_mashup       # None when the file has no DataMashup part
if mashup is not None:
    print(mashup.version)
    for q in mashup.parameters:  # MQuery objects
        print(q.name, q.param_type, q.default_value, q.allowed_values)
```
`data_mashup` is `None` for files without a mashup, and raises `DataMashupError`
if the part is malformed. These accessors are additive — `power_query` and
`m_parameters` keep their existing AS-metadata behavior.

## Tabular Model Schema (TMSCHEMA) Endpoints

Full equivalents of the Analysis Services `$System.TMSCHEMA_*` DMVs, read directly from the embedded SQLite metadata database.

| Property | DMV equivalent |
|---|---|
| `model.tmschema_model` | `TMSCHEMA_MODEL` |
| `model.tmschema_tables` | `TMSCHEMA_TABLES` |
| `model.tmschema_columns` | `TMSCHEMA_COLUMNS` |
| `model.tmschema_partitions` | `TMSCHEMA_PARTITIONS` |
| `model.tmschema_hierarchies` | `TMSCHEMA_HIERARCHIES` |
| `model.tmschema_levels` | `TMSCHEMA_LEVELS` |
| `model.tmschema_datasources` | `TMSCHEMA_DATASOURCES` |
| `model.tmschema_perspectives` | `TMSCHEMA_PERSPECTIVES` |
| `model.tmschema_perspective_tables` | `TMSCHEMA_PERSPECTIVE_TABLES` |
| `model.tmschema_perspective_columns` | `TMSCHEMA_PERSPECTIVE_COLUMNS` |
| `model.tmschema_perspective_hierarchies` | `TMSCHEMA_PERSPECTIVE_HIERARCHIES` |
| `model.tmschema_perspective_measures` | `TMSCHEMA_PERSPECTIVE_MEASURES` |
| `model.tmschema_kpis` | `TMSCHEMA_KPIS` |
| `model.tmschema_annotations` | `TMSCHEMA_ANNOTATIONS` |
| `model.tmschema_extended_properties` | `TMSCHEMA_EXTENDED_PROPERTIES` |
| `model.tmschema_cultures` | `TMSCHEMA_CULTURES` |
| `model.tmschema_translations` | `TMSCHEMA_OBJECT_TRANSLATIONS` |
| `model.tmschema_linguistic_metadata` | `TMSCHEMA_LINGUISTIC_METADATA` |
| `model.tmschema_query_groups` | `TMSCHEMA_QUERY_GROUPS` |
| `model.tmschema_calculation_groups` | `TMSCHEMA_CALCULATION_GROUPS` |
| `model.tmschema_calculation_items` | `TMSCHEMA_CALCULATION_ITEMS` |
| `model.tmschema_calculation_expressions` | `TMSCHEMA_CALCULATION_EXPRESSIONS` |
| `model.tmschema_variations` | `TMSCHEMA_VARIATIONS` |
| `model.tmschema_attribute_hierarchies` | `TMSCHEMA_ATTRIBUTE_HIERARCHIES` |
| `model.tmschema_sets` | `TMSCHEMA_SETS` |
| `model.tmschema_refresh_policies` | `TMSCHEMA_REFRESH_POLICIES` |
| `model.tmschema_detail_rows_definitions` | `TMSCHEMA_DETAIL_ROWS_DEFINITIONS` |
| `model.tmschema_format_string_definitions` | `TMSCHEMA_FORMAT_STRING_DEFINITIONS` |
| `model.tmschema_functions` | `TMSCHEMA_FUNCTIONS` |
| `model.tmschema_calendars` | `TMSCHEMA_CALENDARS` |
| `model.tmschema_calendar_column_groups` | `TMSCHEMA_CALENDAR_COLUMN_GROUPS` |
| `model.tmschema_calendar_column_refs` | `TMSCHEMA_CALENDAR_COLUMN_REFERENCES` |
| `model.tmschema_alternate_of` | `TMSCHEMA_ALTERNATE_OF` |
| `model.tmschema_related_column_details` | `TMSCHEMA_RELATED_COLUMN_DETAILS` |
| `model.tmschema_group_by_columns` | `TMSCHEMA_GROUP_BY_COLUMNS` |
| `model.tmschema_binding_info` | `TMSCHEMA_BINDING_INFO` |
| `model.tmschema_analytics_ai_metadata` | `TMSCHEMA_ANALYTICS_AI_METADATA` |
| `model.tmschema_data_coverage_definitions` | `TMSCHEMA_DATA_COVERAGE_DEFINITIONS` |
| `model.tmschema_role_memberships` | `TMSCHEMA_ROLE_MEMBERSHIPS` |
| `model.tmschema_column_permissions` | `TMSCHEMA_COLUMN_PERMISSIONS` |

```python
# Example — list all columns with their tables
print(model.tmschema_columns[["TableName", "Name", "DataType", "IsHidden"]])

# Example — inspect incremental refresh policies
print(model.tmschema_refresh_policies)

# Example — list all security roles and their members
print(model.tmschema_role_memberships)
```

