"""Decoder for the QDEFF binary ``DataMashup`` stream ([MS-QDEFF]).

Top-level binary stream (section 2.2), little-endian, every variable field
preceded by a 4-byte unsigned length:

    Version (4)                =0
    PackagePartsLength (4)
    PackageParts (variable)    OPC zip: Config/Package.xml, Formulas/Section1.m, Content/<GUID>
    PermissionsLength (4)
    Permissions (variable)     UTF-8 XML
    MetadataLength (4)
    Metadata (variable)        Version(4) | MetadataXmlLength(4) | MetadataXML | ContentLength(4) | Content(OPC)
    PermissionBindingsLength (4)
    PermissionBindings (variable)   DPAPI checksum — ignored

Only the parts pbixray needs are surfaced: ``Section1.m`` (the Power Query M)
and the metadata XML. The DPAPI ``PermissionBindings`` block is never decrypted.
"""
import io
import struct
import zipfile

from ..exceptions import DataMashupError


def _read_uint32(buf, offset):
    if offset + 4 > len(buf):
        raise DataMashupError("Truncated DataMashup: expected a 4-byte length field.")
    return struct.unpack_from("<I", buf, offset)[0], offset + 4


def _read_length_prefixed(buf, offset):
    length, offset = _read_uint32(buf, offset)
    end = offset + length
    if end > len(buf):
        raise DataMashupError("Truncated DataMashup: declared length exceeds the stream.")
    return buf[offset:end], end


def _read_section_m(package_parts):
    """Return the text of ``Formulas/Section1.m`` from the package-parts zip."""
    try:
        with zipfile.ZipFile(io.BytesIO(package_parts)) as zf:
            for name in zf.namelist():
                if name.replace("\\", "/").lower().endswith("formulas/section1.m"):
                    return zf.read(name).decode("utf-8-sig")
    except zipfile.BadZipFile as exc:
        raise DataMashupError("DataMashup PackageParts is not a valid zip.") from exc
    return None


def _read_metadata_xml(metadata):
    """Extract the ``MetadataXML`` document from the metadata sub-stream."""
    if len(metadata) < 8:
        return None
    # Version (4) | MetadataXmlLength (4) | MetadataXML | ...
    _version, offset = _read_uint32(metadata, 0)
    xml, _offset = _read_length_prefixed(metadata, offset)
    return xml.decode("utf-8-sig")


def decode(blob):
    """Decode a raw ``DataMashup`` blob into its component parts.

    Returns a dict with ``version``, ``section_m`` (str or None),
    ``permissions`` (str or None), ``metadata_xml`` (str or None) and the raw
    ``package_parts`` bytes.
    """
    if len(blob) < 8:
        raise DataMashupError("DataMashup blob is too small to contain a header.")
    version, offset = _read_uint32(blob, 0)
    package_parts, offset = _read_length_prefixed(blob, offset)
    permissions, offset = _read_length_prefixed(blob, offset)
    metadata, offset = _read_length_prefixed(blob, offset)
    # PermissionBindings follows but is a DPAPI checksum we intentionally ignore.

    return {
        "version": version,
        "package_parts": package_parts,
        "section_m": _read_section_m(package_parts),
        "permissions": permissions.decode("utf-8-sig") if permissions else None,
        "metadata_xml": _read_metadata_xml(metadata),
    }
