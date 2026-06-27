# AGENTS.md — PBIXRay for LLM agents

Dense, recipe-shaped reference for agents using this library. For
narrative docs see [README.md](README.md); for internals see
[docs/](docs/).

## What this is

Read-only Python parser for Power BI `.pbix` files and Excel `.xlsx`
workbooks with embedded Power Pivot models. Returns pandas DataFrames.
No network, no Power BI / Excel install required.

## Install + minimal example

```bash
pip install pbixray
```

```python
from pbixray import PBIXRay

model = PBIXRay("data/Adventure Works DW 2020.pbix")  # or any .xlsx with Power Pivot
print(model.tables)                  # list of table names
print(model.schema.head())           # column metadata
print(model.get_table(model.tables[0]).head())
```

File type (PBIX vs XLSX) is auto-detected from contents. Same API either
way.

## Memory model / large files

By default the whole decompressed data model is held in one in-memory
buffer for the life of the `PBIXRay` object, and metadata is loaded
lazily on first property access. For models that approach or exceed host
RAM, construct with `on_disk=True` (optionally `temp_dir=...`): the
decompressed data is streamed to a temp file and `mmap`-ed, so only the
pages a requested table touches are resident. `PBIXRay` is a context
manager; use `with PBIXRay(path, on_disk=True) as model:` or call
`model.close()` to release the mapping and temp file deterministically.
`get_table(name, columns=[...])` decodes only the listed columns.

## Decision tree — "I want X → use Y"

| I want…                              | Use                                                |
| ------------------------------------ | -------------------------------------------------- |
| List of table names                  | `model.tables`                                     |
| Row data of one table                | `model.get_table(name)`                            |
| Column types per table               | `model.schema`                                     |
| DAX measures                         | `model.dax_measures`                               |
| DAX calculated columns               | `model.dax_columns`                                |
| DAX calculated tables                | `model.dax_tables`                                 |
| M / Power Query source               | `model.power_query`, `model.m_parameters`          |
| Relationships                        | `model.relationships`                              |
| Row-Level Security                   | `model.rls`                                        |
| Object-Level Security                | `model.ols`                                        |
| Perspectives (consolidated members)  | `model.perspectives`                               |
| Model build / locale metadata        | `model.metadata`                                   |
| Per-column size breakdown            | `model.statistics`                                 |
| Total model size (bytes, int)        | `model.size`                                       |
| Raw Analysis Services DMV-equivalents| `model.tmschema_*` (40 properties; PBIX only)      |

## API surface

Source of truth: [pbixray/core.py](pbixray/core.py).

### Core endpoints

| Attribute              | Return              | Notable columns / shape                                                                                                  |
| ---------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `tables`               | `numpy.ndarray[str]`| Table names                                                                                                              |
| `get_table(name)`      | `DataFrame`         | Row data; `RowNumber` excluded; unknown name → empty DataFrame (no exception)                                            |
| `schema`               | `DataFrame`         | `TableName`, `ColumnName`, `PandasDataType`                                                                              |
| `statistics`           | `DataFrame`         | `TableName`, `ColumnName`, `Cardinality`, `Dictionary`, `HashIndex`, `DataSize`                                          |
| `size`                 | `int`               | Total model size in bytes                                                                                                |
| `relationships`        | `DataFrame`         | `FromTableName`, `FromColumnName`, `ToTableName`, `ToColumnName`, `IsActive`, `Cardinality`, `CrossFilteringBehavior`, … |
| `power_query`          | `DataFrame`         | `TableName`, `Expression` (M code)                                                                                       |
| `m_parameters`         | `DataFrame`         | `ParameterName`, `Description`, `Expression`, `ModifiedTime`                                                             |
| `dax_tables`           | `DataFrame`         | `TableName`, `Expression`                                                                                                |
| `dax_measures`         | `DataFrame`         | `TableName`, `Name`, `Expression`, `DisplayFolder`, `Description`                                                        |
| `dax_columns`          | `DataFrame`         | `TableName`, `ColumnName`, `Expression`                                                                                  |
| `rls`                  | `DataFrame`         | `TableName`, `RoleName`, `RoleDescription`, `FilterExpression`, `State`, `MetadataPermission`                            |
| `ols`                  | `DataFrame`         | `RoleName`, `TableName`, `ColumnName`, `Scope` (`Table`/`Column`), `Permission` (`None`/`Read`/`Default`); excludes plain RLS rows |
| `perspectives`         | `DataFrame`         | `PerspectiveName`, `ObjectType` (`Table`/`Column`/`Measure`/`Hierarchy`), `TableName`, `ObjectName`, `IncludeAll`        |
| `metadata`             | `DataFrame`         | Build / locale / version key-value rows                                                                                  |

### TMSCHEMA endpoints (PBIX only)

40 properties named `tmschema_<entity>` mirror the Analysis Services
`$System.TMSCHEMA_*` DMVs (e.g. `tmschema_columns`, `tmschema_partitions`,
`tmschema_refresh_policies`, `tmschema_role_memberships`,
`tmschema_column_permissions`). Full list with
DMV mapping: [README.md §Tabular Model Schema Endpoints](README.md#tabular-model-schema-tmschema-endpoints)
and [docs/TMSCHEMA_MAPPING.md](docs/TMSCHEMA_MAPPING.md).

## PBIX vs XLSX capability matrix

| Endpoint                                  | PBIX        | XLSX                       |
| ----------------------------------------- | ----------- | -------------------------- |
| `tables`, `schema`, `statistics`, `size`  | Populated   | Populated                  |
| `get_table(name)`                         | Real data   | Real data (no `RowNumber`) |
| `relationships`                           | Populated   | Populated                  |
| `dax_tables`                              | Populated   | Populated (from partitions)|
| `dax_measures`                            | Populated   | Populated (measure groups) |
| `dax_columns`                             | Populated   | Empty                      |
| `power_query`, `m_parameters`             | Populated   | Empty                      |
| `metadata`, `rls`, `ols`, `perspectives`  | Populated   | Empty                      |
| `tmschema_*` (all 40)                     | Populated   | Empty                      |

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
- **XLSX calculated columns** can have a display name different from the
  internal storage name (e.g. `Category` ↔ `CalculatedColumn1`). PBIXRay
  resolves these so `schema.ColumnName` and `get_table()` use the
  display name; the storage name is used only internally for column
  file lookup.
- **No streaming.** `get_table()` materialises the whole table into a
  DataFrame; large fact tables can be memory-heavy.
- **`tables` returns a numpy array**, not a Python list — iterates fine,
  but `model.tables == [...]` won't work as a plain equality check.

## Does NOT do

- No writing — cannot save, modify, or repack PBIX/XLSX files.
- No DAX evaluation — measure and calculated-column expressions are
  returned as source text only.
- No query engine — no support for evaluating DAX/MDX/M against the
  model.
- No live connection — does not talk to Power BI Service, Analysis
  Services, datasets, gateways, or workspaces.
- No model refresh.
- No `.pbit` template, `.pbids` connection, or `.pbip` project format
  support — only `.pbix` and `.xlsx` (Power Pivot) are recognised.
- No report-layer parsing (visuals, pages, bookmarks, themes) — data
  model only.

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
- [data/](data/) — sample PBIX and XLSX files for self-testing.
- [test/](test/) — usage patterns; `test_xlsx.py` is a good example of
  endpoint expectations.

## Version / compat

- Python ≥ 3.8 (tested through 3.13). Source: [setup.py](setup.py).
- Runtime deps: `xpress9`, `kaitaistruct`, `numpy`, `pandas`, `apsw`.
- File formats: `.pbix` (current Power BI Desktop) and `.xlsx` with an
  embedded Power Pivot data model under `xl/model/item.data`. Workbooks
  without a Power Pivot model are not supported.
