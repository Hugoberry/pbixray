"""Tests for the opt-in on-disk (mmap) loading path and related lifecycle.

Covers Phase 1 (on_disk spill + mmap, cleanup, context manager), Phase 2 (lazy
metadata) and Phase 3 (column selection) of the large-model optimization work.
"""
import gc
import glob
import os
import sys

import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pbix')))

from pbixray import PBIXRay

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# A small PBIX and the XLSX model exercise both container types / decoders.
_FILES = [
    os.path.join(DATA_DIR, "work.pbix"),
    os.path.join(DATA_DIR, "Supplier Quality Analysis Sample-no-PV.xlsx"),
]


def _all_tables_frames(model):
    return {t: model.get_table(t) for t in model.tables}


@pytest.mark.parametrize("path", _FILES)
def test_on_disk_matches_in_memory(path):
    """get_table output must be identical between on_disk=False and on_disk=True."""
    ram = PBIXRay(path, on_disk=False)
    disk = PBIXRay(path, on_disk=True)
    try:
        assert list(ram.tables) == list(disk.tables)
        for table in ram.tables:
            pd.testing.assert_frame_equal(
                ram.get_table(table), disk.get_table(table),
                check_dtype=True,
            )
    finally:
        ram.close()
        disk.close()


def test_spill_file_created_under_temp_dir_and_cleaned_up(tmp_path):
    """The spill file lands in temp_dir and is unlinked on close()."""
    model = PBIXRay(os.path.join(DATA_DIR, "work.pbix"), on_disk=True, temp_dir=str(tmp_path))
    spilled = glob.glob(os.path.join(str(tmp_path), "*.pbixray"))
    assert spilled, "expected a spill file to be created under temp_dir"

    # Force a decode so the mmap is actually exercised before teardown.
    model.get_table(model.tables[0])

    model.close()
    assert not glob.glob(os.path.join(str(tmp_path), "*.pbixray")), \
        "spill file should be removed after close()"


def test_spill_file_cleaned_up_on_gc(tmp_path):
    """Without an explicit close(), the weakref finalizer removes the spill file."""
    model = PBIXRay(os.path.join(DATA_DIR, "work.pbix"), on_disk=True, temp_dir=str(tmp_path))
    assert glob.glob(os.path.join(str(tmp_path), "*.pbixray"))
    del model
    gc.collect()
    assert not glob.glob(os.path.join(str(tmp_path), "*.pbixray"))


def test_context_manager(tmp_path):
    """`with PBIXRay(...) as m` works and releases the spill file on exit."""
    with PBIXRay(os.path.join(DATA_DIR, "work.pbix"), on_disk=True, temp_dir=str(tmp_path)) as model:
        assert model.get_table(model.tables[0]) is not None
        assert glob.glob(os.path.join(str(tmp_path), "*.pbixray"))
    assert not glob.glob(os.path.join(str(tmp_path), "*.pbixray"))


def test_close_is_idempotent(tmp_path):
    model = PBIXRay(os.path.join(DATA_DIR, "work.pbix"), on_disk=True, temp_dir=str(tmp_path))
    model.close()
    model.close()  # must not raise


def test_column_selection():
    """get_table(columns=[...]) returns only the requested columns, matching the full decode."""
    model = PBIXRay(os.path.join(DATA_DIR, "work.pbix"))
    table = model.tables[0]
    full = model.get_table(table)
    some = list(full.columns[:1])

    subset = model.get_table(table, columns=some)
    assert list(subset.columns) == some
    pd.testing.assert_series_equal(subset[some[0]], full[some[0]])


def test_column_selection_unknown_raises():
    model = PBIXRay(os.path.join(DATA_DIR, "work.pbix"))
    table = model.tables[0]
    with pytest.raises(ValueError):
        model.get_table(table, columns=["__definitely_not_a_column__"])


def test_metadata_loaded_lazily():
    """Constructing PBIXRay must not eagerly build the tmschema_* dataframes."""
    model = PBIXRay(os.path.join(DATA_DIR, "work.pbix"))
    source = model._metadata.source
    # SqliteMetadataSource defers everything except schema_df.
    if hasattr(source, "_lazy_populators"):
        assert "kpis_df" not in source.__dict__, "kpis_df should not be built until accessed"
        _ = model.tmschema_kpis  # triggers lazy load
        assert "kpis_df" in source.__dict__, "kpis_df should be cached after access"
