# pbixray — internal map

Internal map of the package. The public surface is `pbixray.PBIXRay`;
everything else is implementation detail.

## Pipeline

```
file.pbix / file.xlsx
        │
        ▼
  DataModelLoader ──▶  DataModel(file_log, decompressed_data, container)
   (loader.py)              │
                            ├──▶ Metadata        ──▶ schema, stats, DAX, M, …
                            │    (meta/)
                            │
                            └──▶ VertiPaqDecoder ──▶ get_table(name) → DataFrame
                                 (vertipaq_decoder.py)
```

`PBIXRay.__init__` (`core.py`) wires those three together. Everything the
public API exposes is a thin passthrough.

## Containers

Two ZIP-based containers feed the same downstream pipeline:

| Container       | Inner stream            | Metadata source            |
| --------------- | ----------------------- | -------------------------- |
| `Container.PBIX` | `DataModel`             | embedded SQLite blob       |
| `Container.XLSX` | `xl/model/item.data`    | a set of `*.xml` documents |

Detection lives in `DataModelLoader.__get_data_model_path` and is the only
place that distinguishes the two formats by filename. Stream decompression
(Xpress9, single- or multi-threaded) is orthogonal and detected by
signature in `__detect_compression`.

## Decompressed stream layout (`abf/`)

The decompressed bytes are an **ABF** (Analysis services BackuP) stream:

- `backup_log.py` — header + per-file size/offset table
- `virtual_directory.py` — directory structure within the stream
- `parser.py` — populates `DataModel.file_log` so downstream code can slice
  out any inner file by name via `utils.get_data_slice(data_model, name)`

After parsing, `DataModel.file_log` is the in-memory index of everything
the container holds.

## Metadata (`meta/`)

`Metadata` (`meta/metadata.py`) is a facade. It picks one implementation of
the `MetadataSource` protocol (`meta/base.py`) based on `container`:

- `SqliteMetadataSource` (`meta/sqlite_source.py`) — pbix path. Loads the
  embedded `metadata.sqlitedb` blob into an in-memory APSW connection and
  populates ~40 DataFrames via SQL.
- `XmlMetadataSource` (`meta/xml_source.py`) — xlsx path. Parses the
  `.cub.xml`, `.dim.xml`, `.prt.xml`, `.det.xml`, `.scr.xml`, `.ds.xml`,
  `.dsv.xml`, `.tbl.xml` documents (kaitai-generated readers live in
  `xldm/`) and reconstructs the equivalent DataFrames. PBIX-only views (M,
  RLS, TMSCHEMA_*) are exposed as empty DataFrames.

Both implementations normalize `schema_df` to expose:

- `PandasDataType` — ready for `astype` (e.g. `"Int64"`, `"datetime64[ns]"`)
- `SemanticType` — `"Date"` / `"Currency"` / `"Other"` for post-decode
  special-casing

…so callers never branch on container format. They also implement
`get_segment_meta(column_row)` — the format-specific lookup that tells the
decoder how a column's segments are laid out.

## VertiPaq decoding (`vertipaq_decoder.py`, `column_data/`)

`get_table(name)` iterates over the schema rows for that table and rebuilds
each column from three on-disk artefacts:

| Artefact              | Parser                       | Purpose                       |
| --------------------- | ---------------------------- | ----------------------------- |
| `*.dictionary`        | `column_data/dictionary.py`  | value dictionary (strings, ints) |
| `*.hidx`              | `column_data/hidx.py`        | hash index → dictionary key   |
| `*.idf` + `*.idfmeta` | `column_data/idf.py` + `idfmeta.py` | RLE / bit-packed data IDs     |

The decoder runs a hybrid RLE + bit-packed read
(`_read_rle_bit_packed_hybrid`), looks values up via the dictionary, then
applies semantic conversions (`Date` → datetime, `Currency` → Decimal/10000).
Huffman-compressed string dictionaries are inflated in `huffman.py` (pure
Python over NumPy).

All four modules in `column_data/` (`dictionary.py`, `hidx.py`, `idf.py`,
`idfmeta.py`) are **generated from Kaitai Struct `.ksy` schemas**. The
schemas for `dictionary`, `idf`, and `idfmeta` live in [`/docs`](../docs);
each generated Python file starts with the
`# This is a generated file!` banner. Do not hand-edit the generated
modules — change the `.ksy` and regenerate with
`kaitai-struct-compiler -t python <file>.ksy`.

## XLDM (`xldm/`)

The kaitai-generated and hand-written XML readers used only by the XLSX
path: `Cube`, `Dimension`, `Partition`, `MeasureGroup`, `MdxScript`,
`DataSource`, `DataSourceView`, plus the generic `XMObjectDocument` used
for `.tbl.xml`.

## Where format-awareness lives

After the refactor, only two sites read `DataModel.container`:

1. `loader.py` — sets it during detection (the boundary)
2. `meta/metadata.py` — picks `SqliteMetadataSource` vs `XmlMetadataSource`

The decoder, the facade's `schema` property, and every public API
passthrough are format-agnostic.

## Module quick-reference

```
core.py               PBIXRay — public facade
loader.py             DataModelLoader — zip → DataModel
vertipaq_decoder.py   column-store decoding
utils.py              AMO_PANDAS_TYPE_MAPPING, get_data_slice, filetime helpers
huffman.py            string-dictionary decompression

abf/                  ABF stream parsing (file_log)
column_data/          .dictionary / .hidx / .idf(meta) kaitai parsers
meta/                 metadata sources + facade
xldm/                 XLSX XML model readers
```
