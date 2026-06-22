"""Parsing for the ``Connections`` manifest embedded in PBIX reports.

The ``Connections`` entry is a small JSON document listing the report's data
connections. For self-contained (import) models it is usually absent or empty;
for thin/live-connection reports it describes the external model the report is
bound to.
"""
import json


def parse_connections(zip_ref):
    """Return the ``Connections`` entries of an open PBIX zip as a list of dicts.

    Returns an empty list when the entry is absent, empty, or unparseable.
    """
    if "Connections" not in zip_ref.namelist():
        return []
    raw = zip_ref.read("Connections")
    if not raw:
        return []
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        text = raw.decode("utf-16")
    else:
        text = raw.decode("utf-8-sig")
    try:
        document = json.loads(text)
    except json.JSONDecodeError:
        return []
    connections = document.get("Connections", [])
    return connections if isinstance(connections, list) else []
