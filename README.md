# PBIXRay

**Read Power BI semantic models without Power BI.**

[![PyPI](https://img.shields.io/pypi/v/pbixray)](https://pypi.org/project/pbixray/)
[![Downloads](https://static.pepy.tech/badge/pbixray)](https://pepy.tech/project/pbixray)
[![Python](https://img.shields.io/pypi/pyversions/pbixray)](https://pypi.org/project/pbixray/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

No Power BI Desktop. No Analysis Services instance. No XMLA endpoint, no Premium capacity, no workspace, no restore. Just a file path.

```python
from pbixray import PBIXRay

model = PBIXRay("sales.pbix")

model.dax_measures         # every measure, as a DataFrame
model.relationships        # the full model graph
model.power_query          # all M code
model.get_table("Sales")   # actual decoded rows
```

PBIXRay is a Python reader for the VertiPaq engine's on-disk format. It parses `.pbix` files, `.abf` Analysis Services backups and `.xlsx` PowerPivot workbooks, which are three containers around the same storage engine, and returns pandas DataFrames. Read-only, offline, cross-platform, with no Microsoft runtime involved at any stage.

Every other way to inspect a model needs something running. Desktop open, a server connected, a backup restored, a capacity licensed. PBIXRay needs a file.

---

## Install

```bash
pip install pbixray
```

Python 3.8 through 3.13, on macOS, Linux and Windows. Prebuilt wheels, so there is nothing to compile.

---

## What you can pull out

| | |
|---|---|
| **Model logic** | measures, calculated columns, calculated tables, calculation groups |
| **Transformations** | Power Query / M, M parameters, DataMashup queries (DirectQuery and native SQL) |
| **Structure** | tables, columns, schema, relationships, hierarchies, perspectives, aggregations |
| **Security** | row-level security, object-level security, roles and role memberships |
| **Storage** | per-column cardinality, dictionary / hash-index / data sizes, total model size |
| **Data** | decoded table contents, whole or streamed in chunks |
| **Everything else** | all 40 `$System.TMSCHEMA_*` DMVs |

Full reference and examples at **[pbixray.com/docs](https://www.pbixray.com/docs/)**.

---

## Three formats, one API

File type is detected from the contents, so the same code works across all three.

| Input | What it is |
|---|---|
| `.pbix` | Power BI Desktop file |
| `.abf` | Analysis Services backup, readable without provisioning a server or restoring |
| `.xlsx` | Excel workbook with an embedded PowerPivot model |

```python
PBIXRay("report.pbix")
PBIXRay("nightly-backup.abf")
PBIXRay("legacy-powerpivot.xlsx")
```

ABF support turns a backup archive into something queryable without a restore. That covers retention audits, migration inventories, and answering "what was in this model in 2019" without standing anything up.

---

## The 40 DMVs, from a file

Analysis Services exposes model metadata through `$System.TMSCHEMA_*` DMVs, normally reachable only over a live connection. PBIXRay reads all forty straight from the embedded metadata database.

```python
model.tmschema_refresh_policies    # incremental refresh configuration
model.tmschema_role_memberships    # who is in which security role
model.tmschema_column_permissions  # object-level permissions
model.tmschema_partitions          # partition definitions and sources
```

<details>
<summary><strong>All 40 endpoints</strong></summary>

`tmschema_model` · `tmschema_tables` · `tmschema_columns` · `tmschema_partitions` · `tmschema_hierarchies` · `tmschema_levels` · `tmschema_datasources` · `tmschema_perspectives` · `tmschema_perspective_tables` · `tmschema_perspective_columns` · `tmschema_perspective_hierarchies` · `tmschema_perspective_measures` · `tmschema_kpis` · `tmschema_annotations` · `tmschema_extended_properties` · `tmschema_cultures` · `tmschema_translations` · `tmschema_linguistic_metadata` · `tmschema_query_groups` · `tmschema_calculation_groups` · `tmschema_calculation_items` · `tmschema_calculation_expressions` · `tmschema_variations` · `tmschema_attribute_hierarchies` · `tmschema_sets` · `tmschema_refresh_policies` · `tmschema_detail_rows_definitions` · `tmschema_format_string_definitions` · `tmschema_functions` · `tmschema_calendars` · `tmschema_calendar_column_groups` · `tmschema_calendar_column_refs` · `tmschema_alternate_of` · `tmschema_related_column_details` · `tmschema_group_by_columns` · `tmschema_binding_info` · `tmschema_analytics_ai_metadata` · `tmschema_data_coverage_definitions` · `tmschema_role_memberships` · `tmschema_column_permissions`

</details>

This makes governance tooling possible in places a live connection is not available. A pull request, a Lambda function, an air-gapped audit, a laptop with no license.

---

## Models bigger than your RAM

Decompressed models are memory-mapped from disk rather than loaded whole, and tables stream by VertiPaq segment. Column projection and categorical strings cut memory further.

```python
with PBIXRay("20gb-model.pbix", on_disk=True) as model:
    for chunk in model.iter_table("FactSales", chunk_size=1_000_000):
        process(chunk)
```

Dictionary decoding runs on a native Huffman kernel ([xmhuffman](https://github.com/Hugoberry/xmhuffman-cython)) and fans out across cores.

---

## Built on PBIXRay


### 🖥️ [PBIXRay for macOS](https://apps.apple.com/app/pbixray/id6787160588?mt=12)

A native model inspector for Mac. Open a `.pbix` and browse tables, measures, relationships and storage statistics, with no Windows VM, no Parallels and no Power BI Desktop. It streams one table at a time, so models too large for memory open fine. Spotlight integration finds measures by name.

Built for the Mac-based BI consultants Microsoft has never shipped a tool for.

### 🌐 [pbix.info](https://pbix.info)

Drop a model into the browser and explore it straight away. Metadata only, with no data or statistics extracted, focused on data origin and Power Query lineage. Nothing to install.

### 🦆 [DuckDB extension](https://github.com/Hugoberry/duckdb-pbix-extension)

Query PBIX files directly in SQL.

---

## Scope

PBIXRay is a read-only extractor for the data model. It does not:

- write, modify or repack files
- evaluate DAX, so expressions come back as source text
- run a query engine
- connect to Power BI Service, Analysis Services, gateways or workspaces
- refresh anything
- parse the report layer, meaning visuals, pages, bookmarks and themes
- support `.pbit`, `.pbids` or `.pbip`

Read-only is a deliberate choice. A library that cannot write to a model also cannot corrupt one, which is what makes it safe to point at production artifacts and client files.

---

## Contributing

The PBIX format is undocumented and reverse-engineered, so the test corpus is the specification. The most valuable contribution is a model that parses incorrectly.

If you find one, [open an issue](https://github.com/Hugoberry/pbixray/issues) with the failure output and the structural details, such as encoding type, column metadata and offsets. Please never send file contents you do not own. A minimal reproduction is more useful than a real model and safer for everyone.

---

## Built on

Decompression uses Microsoft's own MIT-licensed Xpress reference implementations, wrapped for Python as [xpress8](https://github.com/Hugoberry/xpress8-python) and [xpress9](https://github.com/Hugoberry/xpress9-python). Huffman dictionary decoding lives in [xmhuffman](https://github.com/Hugoberry/xmhuffman-cython). All three are kept in separate repositories so the Cython build and wheel distribution stay out of the main library.

---

## Links

[Documentation](https://www.pbixray.com/docs/) · [Interactive demo](https://www.pbixray.com/demo/) · [PyPI](https://pypi.org/project/pbixray/) · [Support](https://www.pbixray.com/support/)

MIT licensed. Built in London by [Alphaverse Limited](https://www.pbixray.com/).

*Not affiliated with or endorsed by Microsoft. Power BI, Excel and Analysis Services are trademarks of Microsoft Corporation.*