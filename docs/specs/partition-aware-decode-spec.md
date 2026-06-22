# Spec: Partition-aware table decoding

**Status:** Ready for implementation
**Area:** `pbixray` data-decode path (VertiPaq column reading)
**Severity:** High — silent data loss (wrong row counts, no error)

---

## 1. Summary

`PBIXRay.get_table()` returns the rows of **only one partition** when a table has
more than one partition. It does so **silently** — no error, no warning. Metadata
endpoints (`tmschema_partitions`) are correct; the bug is purely in the column
**decode** path.

Single-partition models (the overwhelming majority of authored `.pbix` files) are
unaffected, which is why this has gone unnoticed. It surfaces on multi-partition
tabular models (classic SSAS partitioning, and incremental-refresh partitions).

---

## 2. Reproduction

Test model: the **AdventureWorks Internet Sales** tabular sample backup
(`Adventure Works Internet Sales Database.abf`). Its `Internet Sales` table has
**5 partitions** (`Internet Sales 2010` … `2014`).

Because the current `DataModelLoader` only accepts zip containers (pbix/xlsx),
wrap the raw `.abf` as a one-entry pbix so the public API can open it:

```python
import zipfile
with zipfile.ZipFile("AdvWorks.pbix", "w", zipfile.ZIP_DEFLATED) as z:
    z.write("Adventure Works Internet Sales Database.abf", "DataModel")

from pbixray import PBIXRay
m = PBIXRay("AdvWorks.pbix")
print(len(m.tmschema_partitions[m.tmschema_partitions.TableName == "Internet Sales"]))  # 5  ✔
print(len(m.get_table("Internet Sales")))                                               # 1970 �’ should be 60398
```

(The `.abf` decompresses through the existing internal path — `__detect_compression`
reports `uncompressed`/`STREAM_STORAGE` — so no new decompression code is needed to
reproduce; only the zip wrapper.)

### Observed vs. expected

Per-partition record counts (from `SegmentMapStorage.RecordCount` in
`metadata.sqlitedb`):

| Partition | Records |
|---|---:|
| Internet Sales 2010 | 14 |
| Internet Sales 2011 | 2,216 |
| Internet Sales 2012 | 3,397 |
| Internet Sales 2013 | 52,801 |
| Internet Sales 2014 | 1,970 |
| **Total (expected)** | **60,398** |

`get_table("Internet Sales")` returns **1,970** rows — exactly the **last**
partition (`2014`). The other 58,428 rows are dropped.

---

## 3. Root cause

Each column stores one **IDF** data file **per partition**. In the backup the
files are suffixed with the partition index, e.g. for `Internet Sales[Order Quantity]`:

```
1.Internet Sales (28).Order Quantity (135).1.idf   ← partition 1
1.Internet Sales (28).Order Quantity (135).2.idf   ← partition 2
1.Internet Sales (28).Order Quantity (135).3.idf   ← partition 3
1.Internet Sales (28).Order Quantity (135).4.idf   ← partition 4
1.Internet Sales (28).Order Quantity (135).5.idf   ← partition 5
```

Two code locations assume **one IDF per column**:

1. **`pbixray/meta/sqlite_source.py` → `__populate_schema()`** (≈ line 157).
   The query joins:
   ```sql
   JOIN ColumnPartitionStorage cps ON cps.ColumnStorageID = cs.ID
   JOIN StorageFile sfi ON sfi.ID = cps.StorageFileID
   ```
   `ColumnPartitionStorage` has **one row per (column, partition)**, so for a
   5-partition table this returns **5 rows per column** (IDF `.1` … `.5`). The
   result is not aggregated — `schema_df` ends up with duplicate column rows.

2. **`pbixray/vertipaq_decoder.py` → `get_table()`** (≈ line 298).
   It iterates `table_metadata_df` rows and writes into a dict keyed by column
   name:
   ```python
   dataframe_data[column_metadata["ColumnName"]] = column_data.astype(...)
   ```
   With 5 duplicate rows per column, each successive partition **overwrites** the
   previous one in the dict. The last row wins → only partition `.5` (2014, 1,970
   rows) remains. `_get_column_data` / `get_segment_meta` each read the single
   `column_metadata["IDF"]` (and its `.idfmeta`), so even per-row it only ever sees
   one partition's segments.

Net effect: silent "last-partition-wins" instead of a concatenation across
partitions.

Note: the dictionary is keyed off `ColumnStorage` (`cs.DictionaryStorageID`),
which is **shared across partitions** — so the value dictionary is the same for
every partition of a column. Only the IDF segment data and per-segment `.idfmeta`
(min_data_id / bit_width / records) differ per partition.

---

## 4. Required behavior

`get_table(table_name)` (and `iter_table`, if it shares the path) must return the
**concatenation of all partitions** in **partition storage order**, with every
column aligned to the same row ordering.

Concretely, for the repro: `len(get_table("Internet Sales")) == 60398`, columns
unchanged (24), values correct for spot-checked rows in each partition's date
range.

Single-partition tables must be byte-for-byte unchanged (no regressions).

---

## 5. Implementation plan

The cleanest approach keeps one logical row per column in `schema_df` and attaches
the **ordered list of partition IDF files** (plus their `.idfmeta`) to that row.

### 5.1 Schema: collect IDFs per column, ordered by partition

In `__populate_schema()` (sqlite_source.py) and the equivalent in
`xml_source.py`:

- Aggregate the per-partition IDF rows into **one row per column**, with an ordered
  list of IDF file names, e.g. add a column `IDFs` (list[str]) while keeping `IDF`
  as the first partition for backward compatibility.
- Order the IDFs by partition storage order. Use
  `ColumnPartitionStorage.PartitionStorageID → PartitionStorage.StoragePosition`
  (and/or `Partition` ordering) so partitions concatenate in a stable, correct
  order. Do **not** rely on the filename numeric suffix alone, though it is a
  useful cross-check.
- Keep `cs.StoragePosition` as the column ordering key (unchanged).

Implementation options (pick one, keep it simple):
- Do the grouping in SQL (`GROUP BY` column with `group_concat(... ORDER BY StoragePosition)`),
  or
- Return the joined rows and group in pandas inside `__populate_schema()`.

`Cardinality`, `Dictionary`, `HIDX`, `BaseId`, `Magnitude`, `IsNullable`,
`DataType` are per-column (or per-ColumnStorage) and must collapse to a single
value per column (they are identical across the duplicate rows today).

### 5.2 Segment meta: per partition

`get_segment_meta(column_row)` currently parses one `column_row["IDF"] + 'meta'`.
Add a method (or extend it) to return **segments per partition**, i.e. parse
`idf + 'meta'` for **each** IDF in the ordered `IDFs` list and return either a
flat list (concatenated in partition order) or a list-of-lists keyed by partition.
Whatever shape is chosen must be consumed consistently in 5.3.

### 5.3 Decode: concatenate partitions per column

In `vertipaq_decoder.py`:

- `_get_column_data(column_metadata, segments_meta)` reads a single
  `column_metadata["IDF"]`. Generalize so that, for each partition IDF in order,
  it reads `get_data_slice(self._data_model, idf)` with that partition's
  `segments_meta`, then concatenates the resulting Series in partition order.
- The **dictionary** lookup is shared (read once per column from the column's
  single `DictionaryStorage`); only the RLE/bit-packed value stream and the
  `min_data_id` / `bit_width` adjustments are per-partition-segment. Preserve the
  existing `null_adjustment` / `min_data_id` logic **per partition** (the
  adjustment uses that partition's `.idfmeta`, not a global one).
- In `get_table()`, remove the implicit dict-overwrite: there is now exactly one
  row per column again, so the existing `dataframe_data[name] = ...` is fine once
  `_get_column_data` returns the full concatenated column.

### 5.4 Row alignment (critical)

All columns must be concatenated using the **same partition order** so that row *i*
of every column belongs to the same source row. Since ordering is driven by
`PartitionStorage.StoragePosition` (a per-table ordering applied uniformly to every
column), this is consistent as long as every column uses the same ordering key.
Add an assertion/sanity check that all decoded columns have equal length before
building the DataFrame; raise a clear error if they diverge.

### 5.5 Statistics & other endpoints

`statistics` / `_compute_statistics` derive from `schema_df[['TableName',
'ColumnName','Cardinality']]`. Once `schema_df` is one-row-per-column again, the
duplicate-row inflation disappears automatically. Verify `m.statistics` shows each
`Internet Sales` column once.

---

## 6. Edge cases / things not to break

- **Single-partition tables:** must be unchanged. Easiest guarantee: the new path
  with a 1-element IDF list reduces to current behavior.
- **XLSX source** (`xml_source.py`): apply the analogous fix; xlsx Power Pivot
  models can also be multi-partition. Keep `base.py` interface consistent across
  both sources.
- **Calculated tables / calculated columns** (`Column.Type` / `Partition.Type`):
  calculated tables (`Partition.Type = 4`) typically have a single partition;
  confirm they still decode. Don't accidentally treat calc partitions as data
  partitions.
- **Null handling / `IsNullable`:** the per-column null adjustment must be applied
  per partition segment, consistent with today's logic.
- **`columns=` argument** to `get_table`: must still work (decode only requested
  columns, all partitions).
- **`iter_table` / on-disk (`on_disk=True`) path:** ensure the concatenation works
  with the `MappedBuffer` backing too.
- **Empty partitions:** a partition with 0 records (none here, but possible) must
  contribute 0 rows without error.

---

## 7. Tests to add

Add a fixture and assertions (the AdventureWorks abf wrapped as pbix is the
canonical case; commit a small wrapper or a pre-wrapped fixture under `samples/`
or `test/`):

1. **Row count:** `len(get_table("Internet Sales")) == 60398`.
2. **Per-partition presence:** group decoded rows by `Order Date` year (or join to
   the SQL `WHERE` ranges) and assert each partition's expected count is present:
   `{2010:14, 2011:2216, 2012:3397, 2013:52801, 2014:1970}` (map to the actual
   date ranges in each partition's `QueryDefinition`).
3. **Column alignment:** all columns equal length; spot-check a known row from the
   largest partition (2013) and the smallest (2010).
4. **Metadata unchanged:** `len(tmschema_partitions[...=="Internet Sales"]) == 5`.
5. **Statistics dedup:** each `Internet Sales` column appears once in
   `m.statistics`.
6. **Regression:** an existing single-partition sample still returns identical
   rows/shape as before the change.

---

## 8. Acceptance criteria

- `get_table` returns the full multi-partition row set (60,398 for the repro),
  rows correctly aligned across columns, partitions in storage order.
- No regression on single-partition pbix/xlsx fixtures.
- New tests (Section 7) pass.
- No silent path remains where extra partitions are dropped — if partitions can't
  be ordered/decoded, raise an explicit error rather than returning a subset.

---

## 9. Reference: code locations

- `pbixray/meta/sqlite_source.py`
  - `__populate_schema()` ≈ line 157 (the `ColumnPartitionStorage`/`StorageFile`
    join that yields one row per partition)
  - `get_segment_meta()` ≈ line 138
- `pbixray/meta/xml_source.py`
  - `get_segment_meta()` ≈ line 302 (+ its schema population)
- `pbixray/vertipaq_decoder.py`
  - `get_table()` ≈ line 298 (dict-overwrite)
  - `_get_column_data()` ≈ line 250 (single-IDF read)
- `pbixray/utils.py` → `get_data_slice(data_model, file_name)` (file-log lookup)
- Relevant metadata tables: `ColumnPartitionStorage`, `StorageFile`,
  `PartitionStorage`, `SegmentMapStorage` (`RecordCount`, `StoragePosition`).

---

## 10. Out of scope

- Native standalone `.abf` loading in `DataModelLoader` (currently zip-only). The
  wrapper trick is sufficient for the fixture. If desired, track separately.
- Incremental-refresh policy semantics; this fix is about reading whatever
  partitions exist, regardless of how they were created.
