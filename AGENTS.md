# AGENTS.md — PBIXRay for LLM agents

Dense, recipe-shaped reference for agents using this library. For
narrative docs see [README.md](README.md); for internals see
[docs/](docs/).

## What this is

Read-only Python parser for Power BI `.pbix` files, Excel `.xlsx`
workbooks with embedded Power Pivot models, and Analysis Services
`.abf` backups. Returns pandas DataFrames. No network, no Power BI /
Excel install required.

## Install + minimal example

```bash
pip install pbixray
```

```python
from pbixray import PBIXRay

model = PBIXRay("data/Adventure Works DW 2020.pbix")  # or .xlsx / .abf
print(model.tables)                  # list of table names
print(model.schema.head())           # column metadata
print(model.get_table(model.tables[0]).head())
```

File type is auto-detected from contents, not extension. Same API for
all three formats. An `.abf` is the same data model as a `.pbix`
without the zip envelope; multi-partition tables (classic SSAS
partitioning and incremental-refresh partitions) are decoded in full —
`get_table` concatenates every partition in storage order.

## Memory model / large files

By default the whole decompressed data model is held in one in-memory
buffer for the life of the `PBIXRay` object, and metadata is loaded
lazily on first property access. For models that approach or exceed host
RAM, construct with `on_disk=True` (optionally `temp_dir=...`): the
decompressed data is streamed to a temp file and `mmap`-ed, so only the
pages a requested table touches are resident. (When the container's
`DataModel` member is stored uncompressed — a raw ABF inside the zip —
`on_disk=True` serves it directly from the `.pbix`/`.xlsx` with no
temp-file copy at all.) `PBIXRay` is a context manager; use
`with PBIXRay(path, on_disk=True) as model:` or call `model.close()` to
release the mapping and temp file deterministically.

Per-table levers:

- `get_table(name, columns=[...])` decodes only the listed columns.
- `get_table(name, strings_as_categorical=True)` returns string columns
  as `pd.Categorical` — each distinct value stored once, not once per
  row.
- `iter_table(name, chunk_size=..., columns=[...])` streams the table
  as DataFrame chunks instead of materialising it whole (see below).

Dictionary decode runs on a native Huffman kernel
([xmhuffman](https://github.com/Hugoberry/xmhuffman-cython)) and fans
out across cores automatically for large dictionaries.

## Decision tree — "I want X → use Y"

| I want…                              | Use                                                |
| ------------------------------------ | -------------------------------------------------- |
| List of table names                  | `model.tables`                                     |
| Row data of one table                | `model.get_table(name)`                            |
| Row data, too big to hold at once    | `model.iter_table(name, chunk_size=...)`           |
| Column types per table               | `model.schema`                                     |
| DAX measures                         | `model.dax_measures`                               |
| DAX calculated columns               | `model.dax_columns`                                |
| DAX calculated tables                | `model.dax_tables`                                 |
| M / Power Query source               | `model.power_query`, `model.m_parameters`          |
| M from DirectQuery / native-SQL models | `model.mashup_queries`, `model.data_mashup`      |
| Relationships                        | `model.relationships`                              |
| Aggregations ("Manage aggregations") | `model.aggregations`                               |
| Row-Level Security                   | `model.rls`                                        |
| Object-Level Security                | `model.ols`                                        |
| Perspectives (consolidated members)  | `model.perspectives`                               |
| Report's data-connection manifest    | `model.connections`                                |
| Model build / locale metadata        | `model.metadata`                                   |
| Per-column size breakdown            | `model.statistics`                                 |
| Total model size (bytes, int)        | `model.size`                                       |
| Raw Analysis Services DMV-equivalents| `model.tmschema_*` (40 properties; PBIX/ABF only)  |

## API surface

Source of truth: [pbixray/core.py](pbixray/core.py).

### Core endpoints

| Attribute              | Return              | Notable columns / shape                                                                                                  |
| ---------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `tables`               | `numpy.ndarray[str]`| Table names                                                                                                              |
| `get_table(name, columns=None, strings_as_categorical=False)` | `DataFrame` | Row data; `RowNumber` excluded; unknown name → empty DataFrame (no exception)             |
| `iter_table(name, columns=None, chunk_size=None, strings_as_categorical=True)` | iterator of `DataFrame` | Chunks follow VertiPaq segment boundaries; `chunk.index` is the global row range |
| `schema`               | `DataFrame`         | `TableName`, `ColumnName`, `PandasDataType`                                                                              |
| `statistics`           | `DataFrame`         | `TableName`, `ColumnName`, `Cardinality`, `Dictionary`, `HashIndex`, `DataSize`                                          |
| `size`                 | `int`               | Total model size in bytes                                                                                                |
| `relationships`        | `DataFrame`         | `FromTableName`, `FromColumnName`, `ToTableName`, `ToColumnName`, `IsActive`, `Cardinality`, `CrossFilteringBehavior`, … |
| `power_query`          | `DataFrame`         | `TableName`, `Expression` (M code, from AS metadata — import models)                                                     |
| `m_parameters`         | `DataFrame`         | `ParameterName`, `Description`, `Expression`, `ModifiedTime`                                                             |
| `mashup_queries`       | `DataFrame`         | `Name`, `Kind`, `IsParameter`, `Expression`, `Type`, `DefaultValue`, `AllowedValues` (from the `DataMashup` part)        |
| `data_mashup`          | `DataMashup \| None`| Parsed MS-QDEFF part (`.queries`, `.parameters`, `.section_m`, `.version`); `None` when the file has no mashup           |
| `dax_tables`           | `DataFrame`         | `TableName`, `Expression`                                                                                                |
| `dax_measures`         | `DataFrame`         | `TableName`, `Name`, `Expression`, `DisplayFolder`, `Description`                                                        |
| `dax_columns`          | `DataFrame`         | `TableName`, `ColumnName`, `Expression`                                                                                  |
| `aggregations`         | `DataFrame`         | `AggregationTable`, `AggregationColumn`, `Summarization` (`GroupBy`/`Sum`/`Count`/`Min`/`Max`), `DetailTable`, `DetailColumn` (`None` for "Count table rows") |
| `rls`                  | `DataFrame`         | `TableName`, `RoleName`, `RoleDescription`, `FilterExpression`, `State`, `MetadataPermission`                            |
| `ols`                  | `DataFrame`         | `RoleName`, `TableName`, `ColumnName`, `Scope` (`Table`/`Column`), `Permission` (`None`/`Read`/`Default`); excludes plain RLS rows |
| `perspectives`         | `DataFrame`         | `PerspectiveName`, `ObjectType` (`Table`/`Column`/`Measure`/`Hierarchy`), `TableName`, `ObjectName`, `IncludeAll`        |
| `connections`          | `list[dict]`        | Report's `Connections` manifest; usually `[]` for self-contained (import) models                                        |
| `metadata`             | `DataFrame`         | Build / locale / version key-value rows                                                                                  |

### `power_query` vs `mashup_queries`

`power_query` / `m_parameters` read M from the Analysis Services
metadata, which works for **import** models. **DirectQuery / native
SQL** models often keep queries and parameters only in the report's
`DataMashup` part — use `mashup_queries` / `data_mashup` for those.
The accessors are additive; neither replaces the other.

### TMSCHEMA endpoints (PBIX/ABF only)

40 properties named `tmschema_<entity>` mirror the Analysis Services
`$System.TMSCHEMA_*` DMVs (e.g. `tmschema_columns`, `tmschema_partitions`,
`tmschema_refresh_policies`, `tmschema_role_memberships`,
`tmschema_column_permissions`). Full list with
DMV mapping: [README.md §Tabular Model Schema Endpoints](README.md#tabular-model-schema-tmschema-endpoints)
and [docs/TMSCHEMA_MAPPING.md](docs/TMSCHEMA_MAPPING.md).

## Exceptions

Exported from `pbixray`; hierarchy is
`LiveConnectionError` → `NoEmbeddedModelError` → `PBIXRayError`
(the first two also subclass `RuntimeError` for backward compatibility).

- **`LiveConnectionError`** — raised on construction for *thin reports*
  that live-connect to an external Analysis Services server
  (`analysisServicesDatabaseLive`) or Power BI Service dataset
  (`pbiServiceLive`). There is no model on disk to parse. The exception
  carries `connection_type`, `connection_string`, `database_name`, and
  the full `connections` manifest, so you can still identify what the
  report points at:

  ```python
  from pbixray import PBIXRay, LiveConnectionError

  try:
      model = PBIXRay("thin-report.pbix")
  except LiveConnectionError as e:
      print(e.connection_type)   # e.g. 'pbiServiceLive'
      print(e.database_name)     # remote dataset id, when available
  ```

- **`NoEmbeddedModelError`** — file has no embedded model *and* no
  connection manifest explaining why.
- **`DataMashupError`** — the `DataMashup` part exists but is malformed.

## PBIX vs XLSX capability matrix

`.abf` behaves like PBIX for all model endpoints (same SQLite-backed
metadata); it has no zip envelope, so report-layer parts
(`connections` → `[]`, `data_mashup` → `None`) are absent.

| Endpoint                                  | PBIX / ABF  | XLSX                       |
| ----------------------------------------- | ----------- | -------------------------- |
| `tables`, `schema`, `statistics`, `size`  | Populated   | Populated                  |
| `get_table(name)`, `iter_table(name)`     | Real data   | Real data (no `RowNumber`) |
| `relationships`                           | Populated   | Populated                  |
| `dax_tables`                              | Populated   | Populated (from partitions)|
| `dax_measures`                            | Populated   | Populated (measure groups) |
| `dax_columns`                             | Populated   | Empty                      |
| `power_query`, `m_parameters`             | Populated   | Empty                      |
| `mashup_queries`, `data_mashup`           | Populated when the file has a `DataMashup` part | Empty / `None` |
| `connections`                             | Populated (PBIX) / `[]` (ABF) | `[]`     |
| `metadata`, `rls`                         | Populated   | Empty                      |
| `aggregations`, `ols`, `perspectives`     | Populated   | Empty                      |
| `tmschema_*`                              | Populated   | Empty                      |

Empty here means a zero-row DataFrame, not `None` and not an exception.

## Gotchas

- **`RowNumber` is dropped** from `get_table()` output. It's a VertiPaq
  internal position, not user data.
- **Row order is storage order, not sheet/insertion order.** VertiPaq
  sorts rows by lowest-cardinality columns first for RLE. Two calls are
  stable, but order will differ from CSVs exported from Excel. For row
  equivalence, compare as multisets:
  `df.sort_values(list(df.columns)).reset_index(drop=True)`.
- **Unknown table name → empty DataFrame**, not an exception. Validate
  against `model.tables` if you need to detect bad names.
- **Thin/live-connection reports raise on construction** — wrap
  `PBIXRay(...)` in `try/except LiveConnectionError` if the input file
  might be a live-connected report (see Exceptions).
- **`get_table` and `iter_table` default `strings_as_categorical`
  differently** — `get_table` defaults to `False` (plain object dtype),
  `iter_table` defaults to `True` (shared `pd.Categorical` across
  chunks). Pass the flag explicitly if the dtype matters downstream.
- **`iter_table` decodes all selected dictionaries up front** and keeps
  them for the whole iteration — on dictionary-heavy models (wide
  free-text columns) pass `columns` to project only what you need.
  Chunks never span two VertiPaq segments, so tail chunks may be
  shorter than `chunk_size`.
- **XLSX calculated columns** can have a display name different from the
  internal storage name (e.g. `Category` ↔ `CalculatedColumn1`). PBIXRay
  resolves these so `schema.ColumnName` and `get_table()` use the
  display name; the storage name is used only internally for column
  file lookup.
- **`tables` returns a numpy array**, not a Python list — iterates fine,
  but `model.tables == [...]` won't work as a plain equality check.

## Does NOT do

- No writing — cannot save, modify, or repack PBIX/XLSX/ABF files.
- No DAX evaluation — measure and calculated-column expressions are
  returned as source text only.
- No query engine — no support for evaluating DAX/MDX/M against the
  model.
- No live connection — does not talk to Power BI Service, Analysis
  Services, datasets, gateways, or workspaces. Thin reports that
  live-connect raise `LiveConnectionError` with the connection details.
- No model refresh.
- No `.pbit` template, `.pbids` connection, or `.pbip` project format
  support — only `.pbix`, `.xlsx` (Power Pivot), and `.abf` are
  recognised.
- No report-layer parsing (visuals, pages, bookmarks, themes) — data
  model plus the `Connections` and `DataMashup` parts only.

## Where to look next

- [README.md](README.md) — narrative docs, full TMSCHEMA list with DMV
  equivalents.
- [docs/README.md](docs/README.md) — index of internal-format docs.
- [docs/xlsx-parsing.md](docs/xlsx-parsing.md) — XLSX Power Pivot
  parsing spec (ABF stream, XML metadata, segment metadata, Xpress8
  caveats).
- [docs/TMSCHEMA_MAPPING.md](docs/TMSCHEMA_MAPPING.md) — TMSCHEMA → DMV
  column mapping.
- [docs/MS-XLDM.md](docs/MS-XLDM.md) — Microsoft XLDM format reference.
- [data/](data/) — sample PBIX, XLSX, and ABF files for self-testing
  (including live-connection and DirectQuery samples).
- [test/](test/) — usage patterns; `test_xlsx.py` is a good example of
  endpoint expectations.

## Version / compat

- Python ≥ 3.8 (tested through 3.13). Source: [setup.py](setup.py).
- Runtime deps: `xpress8`, `xpress9`, `xmhuffman>=0.3.0`,
  `kaitaistruct`, `numpy`, `pandas`, `apsw`.
- File formats: `.pbix` (current Power BI Desktop), `.xlsx` with an
  embedded Power Pivot data model under `xl/model/item.data`, and raw
  `.abf` Analysis Services backups. Workbooks without a Power Pivot
  model are not supported.
