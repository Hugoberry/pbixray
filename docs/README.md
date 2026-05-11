# docs/ — internal format references

Specs and schemas backing the PBIXRay parser. Most users want
[../README.md](../README.md) (usage) or [../AGENTS.md](../AGENTS.md)
(agent-oriented API brief); the files here are for working on the
parser itself or understanding the underlying file formats.

- [xlsx-parsing.md](xlsx-parsing.md) — End-to-end spec for parsing XLSX
  Power Pivot models: file detection, ABF stream, XML metadata walk,
  segment metadata in lieu of `.idfmeta`, trailing-garbage cap, Xpress8
  stored-as-is chunk fix.
- [MS-XLDM.md](MS-XLDM.md) — Reference notes on Microsoft's XLDM
  (XML for Analysis / data-model) format used inside XLSX workbooks.
- [TMSCHEMA_MAPPING.md](TMSCHEMA_MAPPING.md) — Mapping from PBIXRay
  `tmschema_*` endpoints to the Analysis Services
  `$System.TMSCHEMA_*` DMVs and their columns.
- [metadata.sqlitedb.csv](metadata.sqlitedb.csv) — Reference dump of
  the SQLite metadata schema PBIX embeds.
- [idf.ksy](idf.ksy) — Kaitai Struct schema for VertiPaq `.idf` column
  data files.
- [idfmeta.ksy](idfmeta.ksy) — Kaitai Struct schema for `.idfmeta`
  per-column metadata (PBIX side).
- [dictionary.ksy](dictionary.ksy) — Kaitai Struct schema for VertiPaq
  `.dictionary` files.
