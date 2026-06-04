# Roadmap

Deferred ideas for handling large models (those whose uncompressed data model
approaches or exceeds host RAM) more efficiently. The first wave —
opt-in on-disk/mmap loading (`on_disk=True`), lazy metadata, and column
selection in `get_table` — has shipped; see the README for usage. The items
below are the next candidates.

## Arrow output endpoints

Add Arrow-native output alongside the existing pandas `get_table`:

- `get_table_arrow(table_name, columns=None) -> pyarrow.Table`.
- Emit string columns as `DictionaryArray` so each distinct value is stored once
  instead of once per row (today they are materialized as Python `str` objects in
  an object-dtype Series).
- Represent currency as native `decimal128` and dates as `timestamp`, avoiding the
  per-value Python `Decimal` / datetime conversion loops.

This would add `pyarrow` as a dependency and is purely additive — the pandas
`get_table` contract stays unchanged.

## Direct mmap of the uncompressed-ABF zip member

When the `DataModel` member is *stored* (not deflated) inside the `.pbix`/`.xlsx`
zip, compute its byte range and `mmap` the container file directly, skipping the
temp-file copy that `on_disk=True` currently performs for the uncompressed path.
Falls back to the temp-file copy when the member is deflated.

## RecordBatch streaming

`iter_table_batches(table_name)` yielding per-segment `pyarrow.RecordBatch`es, so
tables too large to materialize whole can be consumed incrementally.
