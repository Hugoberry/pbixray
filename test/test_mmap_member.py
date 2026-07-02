"""Direct mmap of the STORED DataModel zip member.

The DataModel member of a .pbix/.xlsx is normally STORED (it is already
XPress9-compressed), so the loader maps its byte range in place instead of
streaming it through ZipExtFile. An *uncompressed* member combined with
``on_disk=True`` skips the temp-file copy entirely: the mapping itself becomes
``decompressed_data``. Deflated members and file-like inputs fall back to the
streaming path.
"""
import io
import os
import zipfile

import pandas as pd
import pytest

from pbixray import PBIXRay
import pbixray.loader as loader_mod
from pbixray.loader import DataModelLoader
from pbixray.abf.mapped_buffer import MappedFileWindow

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
WORK_PBIX = os.path.join(DATA_DIR, 'work.pbix')


def _spy_on_windows(monkeypatch):
    """Patch loader's MappedFileWindow with a subclass recording instantiations."""
    calls = []

    class Spy(MappedFileWindow):
        def __init__(self, *args, **kwargs):
            calls.append(args)
            super().__init__(*args, **kwargs)

    monkeypatch.setattr(loader_mod, 'MappedFileWindow', Spy)
    return calls


def _assert_tables_match(model, reference):
    for table_name in reference.tables:
        pd.testing.assert_frame_equal(
            model.get_table(table_name), reference.get_table(table_name)
        )


@pytest.fixture(scope='module')
def work_decompressed():
    """The fully decompressed ABF stream of work.pbix (in-memory load)."""
    data = bytes(DataModelLoader(WORK_PBIX).data_model.decompressed_data)
    # The raw ABF stream carries the storage signature the loader detects the
    # uncompressed format by; the repack fixtures below depend on it.
    assert DataModelLoader.STREAM_STORAGE_SIGNATURE in data[:72]
    return data


def _repack(dst, data_model_bytes, compress_type):
    """Copy work.pbix with its DataModel member replaced/recompressed."""
    with zipfile.ZipFile(WORK_PBIX) as zin, zipfile.ZipFile(dst, 'w') as zout:
        for item in zin.infolist():
            if item.filename == 'DataModel':
                zout.writestr(
                    zipfile.ZipInfo('DataModel'), data_model_bytes,
                    compress_type=compress_type,
                )
            else:
                zout.writestr(item, zin.read(item.filename))
    return dst


@pytest.fixture(scope='module')
def uncompressed_pbix(tmp_path_factory, work_decompressed):
    """work.pbix with a STORED, *uncompressed* (raw ABF) DataModel member."""
    dst = tmp_path_factory.mktemp('mmap') / 'work-uncompressed.pbix'
    return str(_repack(dst, work_decompressed, zipfile.ZIP_STORED))


@pytest.fixture(scope='module')
def deflated_pbix(tmp_path_factory):
    """work.pbix with its (XPress9) DataModel member re-zipped as DEFLATED."""
    with zipfile.ZipFile(WORK_PBIX) as zin:
        member = zin.read('DataModel')
    dst = tmp_path_factory.mktemp('mmap') / 'work-deflated.pbix'
    return str(_repack(dst, member, zipfile.ZIP_DEFLATED))


# ---------- the mapped path is actually taken ----------

def test_stored_member_uses_mmap(monkeypatch, work_model):
    calls = _spy_on_windows(monkeypatch)
    model = PBIXRay(WORK_PBIX)
    assert calls, "STORED member should be mapped, not streamed"
    _assert_tables_match(model, work_model)


def test_mapped_window_matches_streamed_member():
    with zipfile.ZipFile(WORK_PBIX) as z:
        expected = z.read('DataModel')
        info = z.getinfo('DataModel')
    with open(WORK_PBIX, 'rb') as f:
        f.seek(info.header_offset)
        header = f.read(30)
    data_offset = (info.header_offset + 30
                   + int.from_bytes(header[26:28], 'little')
                   + int.from_bytes(header[28:30], 'little'))
    window = MappedFileWindow(WORK_PBIX, data_offset, info.compress_size)
    try:
        assert len(window) == len(expected)
        assert window[:64] == expected[:64]
        assert window[-64:] == expected[-64:]
        assert window.read() == expected
        # ZipExtFile-style seek/read round-trip used by the loader
        assert window.seek(0, 2) == len(expected)
        window.seek(102)
        assert window.tell() == 102
        assert window.read(8) == expected[102:110]
    finally:
        window.close()


# ---------- uncompressed member + on_disk: zero temp copy ----------

def test_uncompressed_on_disk_adopts_mapping(uncompressed_pbix, work_model):
    with PBIXRay(uncompressed_pbix, on_disk=True) as model:
        assert isinstance(model._data_model.decompressed_data, MappedFileWindow)
        _assert_tables_match(model, work_model)
    # close() released the mapping but must not touch the user's file
    assert os.path.exists(uncompressed_pbix)
    _assert_tables_match(PBIXRay(uncompressed_pbix), work_model)


def test_uncompressed_in_memory_unchanged(uncompressed_pbix, work_model):
    model = PBIXRay(uncompressed_pbix)
    assert isinstance(model._data_model.decompressed_data, (bytes, bytearray))
    _assert_tables_match(model, work_model)


# ---------- fallbacks ----------

def test_deflated_member_falls_back_to_streaming(monkeypatch, deflated_pbix, work_model):
    calls = _spy_on_windows(monkeypatch)
    model = PBIXRay(deflated_pbix)
    assert not calls, "DEFLATED member cannot be mapped in place"
    _assert_tables_match(model, work_model)


def test_file_like_input_falls_back_to_streaming(monkeypatch, work_model):
    calls = _spy_on_windows(monkeypatch)
    with open(WORK_PBIX, 'rb') as f:
        model = PBIXRay(io.BytesIO(f.read()))
    assert not calls, "file-like input has no path to map"
    _assert_tables_match(model, work_model)
