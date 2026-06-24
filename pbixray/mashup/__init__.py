"""Parsing for the PBIX ``DataMashup`` (Power Query) part.

Public entry point: :func:`parse_data_mashup`, which decodes the QDEFF binary
stream and tokenizes ``Section1.m`` into queries and parameters.
"""
from dataclasses import dataclass, field
from typing import List, Optional

from . import qdeff
from .section_document import MQuery, parse_section_document

__all__ = ["DataMashup", "MQuery", "parse_data_mashup"]


@dataclass
class DataMashup:
    """Parsed contents of a PBIX ``DataMashup`` part."""
    version: int
    queries: List[MQuery] = field(default_factory=list)
    section_m: Optional[str] = None
    metadata_xml: Optional[str] = None
    permissions: Optional[str] = None

    @property
    def parameters(self):
        return [q for q in self.queries if q.is_parameter]


def parse_data_mashup(blob):
    """Decode a raw ``DataMashup`` blob into a :class:`DataMashup`.

    Raises :class:`pbixray.exceptions.DataMashupError` on a malformed stream.
    """
    parts = qdeff.decode(blob)
    return DataMashup(
        version=parts["version"],
        queries=parse_section_document(parts["section_m"]),
        section_m=parts["section_m"],
        metadata_xml=parts["metadata_xml"],
        permissions=parts["permissions"],
    )
