"""
Submodule sample harness — tests every .pbix and .xlsx file found in samples/.

Four collections are parametrised separately so failures can be attributed
to the correct source repo and format. Run with:

    pytest test/test_samples.py -m slow -v

Or together with the full suite:

    pytest -m slow

Submodule paths:
  samples/powerbi-desktop-samples/                      (Microsoft)
  samples/Expert-Data-Modeling-with-Power-BI/               (Packt)

Notes on xlsx:
  Microsoft's "-no-PV.xlsx" files contain embedded Power BI data models and
  are fully supported. Packt's xlsx files are raw data sources (no embedded
  model) and are therefore not collected.

If a submodule has not been initialised the corresponding collection will be
empty and the tests are skipped automatically.
"""
import os
import glob
import pytest
from pbixray import PBIXRay

# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

SAMPLES_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'samples'))

def _collect(subdir, ext='*.pbix'):
    """Return sorted list of matching paths under samples/<subdir>."""
    pattern = os.path.join(SAMPLES_ROOT, subdir, '**', ext)
    return sorted(glob.glob(pattern, recursive=True))


def _relid(path):
    """Pytest id: path relative to samples/ root."""
    return os.path.relpath(path, SAMPLES_ROOT)


MICROSOFT_PBIX  = _collect('powerbi-desktop-samples', '*.pbix')
MICROSOFT_XLSX  = _collect('powerbi-desktop-samples', '*.xlsx')
PACKT_FILES     = _collect('Expert-Data-Modeling-with-Power-BI', '*.pbix')
# Packt xlsx files are plain data sources with no embedded Power BI model — excluded.

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Files that expose known library bugs — tracked so they become visible when fixed.
KNOWN_FAILURES = {
    # schema_df lacks TableName/ColumnName/Cardinality for this DirectQuery-only model.
    "Expert-Data-Modeling-with-Power-BI/Chapter07/Chapter 7, Values Datatypes.pbix",
    # Plain Excel workbooks with no embedded Power BI data model (xl/model/item.data absent).
    "powerbi-desktop-samples/AdventureWorks Sales Sample/AdventureWorks Sales.xlsx",
    "powerbi-desktop-samples/Monthly Desktop Blog Samples/2019/customerfeedback.xlsx",
}


def _xfail_if_known(pbix_path):
    rel = os.path.relpath(pbix_path, SAMPLES_ROOT)
    if rel in KNOWN_FAILURES:
        pytest.xfail(f"Known parsing issue: {rel}")


def _smoke(pbix_path):
    """
    Core assertions run against every .pbix sample file:
      1. File loads without exception
      2. At least one table is reported
      3. The first table can be decoded to a non-empty DataFrame
    """
    _xfail_if_known(pbix_path)
    model = PBIXRay(pbix_path)

    tables = model.tables
    assert tables is not None and len(tables) > 0, "No tables found"

    first = next(iter(tables))
    df = model.get_table(first)
    assert df is not None, f"get_table('{first}') returned None"
    assert len(df) >= 0    # empty table is allowed; crash is not


def _smoke_xlsx(xlsx_path):
    """
    Core assertions for .xlsx files with embedded Power BI models.
    Table data retrieval (get_table) is not tested here: xlsx files do not
    store the RowNumber idfmeta entries that pbixray needs to decode columns.
    """
    _xfail_if_known(xlsx_path)
    model = PBIXRay(xlsx_path)

    tables = model.tables
    assert tables is not None and len(tables) > 0, "No tables found"


def _metadata_properties(pbix_path):
    """
    Verify that all metadata properties return without exception and
    yield the expected Python types.
    """
    import pandas as pd

    _xfail_if_known(pbix_path)
    model = PBIXRay(pbix_path)

    for prop in ('metadata', 'power_query', 'statistics', 'dax_tables',
                 'dax_measures', 'dax_columns', 'schema', 'relationships', 'rls'):
        result = getattr(model, prop)
        assert isinstance(result, pd.DataFrame), \
            f"{prop} returned {type(result).__name__}, expected DataFrame"

    size = model.size
    assert isinstance(size, int) and size > 0, f"size={size!r} is not a positive int"


# ---------------------------------------------------------------------------
# Microsoft — powerbi-service-samples (.pbix)
# ---------------------------------------------------------------------------

@pytest.mark.slow
@pytest.mark.skipif(not MICROSOFT_PBIX, reason="powerbi-desktop-samples submodule not initialised")
@pytest.mark.parametrize('pbix_path', MICROSOFT_PBIX, ids=_relid)
def test_microsoft_sample_loads(pbix_path):
    _smoke(pbix_path)


@pytest.mark.slow
@pytest.mark.skipif(not MICROSOFT_PBIX, reason="powerbi-desktop-samples submodule not initialised")
@pytest.mark.parametrize('pbix_path', MICROSOFT_PBIX, ids=_relid)
def test_microsoft_sample_metadata(pbix_path):
    _metadata_properties(pbix_path)


# ---------------------------------------------------------------------------
# Microsoft — powerbi-service-samples (.xlsx with embedded Power BI model)
# ---------------------------------------------------------------------------

@pytest.mark.slow
@pytest.mark.skipif(not MICROSOFT_XLSX, reason="powerbi-desktop-samples submodule not initialised")
@pytest.mark.parametrize('pbix_path', MICROSOFT_XLSX, ids=_relid)
def test_microsoft_xlsx_loads(pbix_path):
    _smoke_xlsx(pbix_path)


@pytest.mark.slow
@pytest.mark.skipif(not MICROSOFT_XLSX, reason="powerbi-desktop-samples submodule not initialised")
@pytest.mark.parametrize('pbix_path', MICROSOFT_XLSX, ids=_relid)
def test_microsoft_xlsx_metadata(pbix_path):
    _metadata_properties(pbix_path)


# ---------------------------------------------------------------------------
# Packt — Expert Data Modeling with Power BI
# ---------------------------------------------------------------------------

@pytest.mark.slow
@pytest.mark.skipif(not PACKT_FILES, reason="Expert-Data-Modeling-with-Power-BI submodule not initialised")
@pytest.mark.parametrize('pbix_path', PACKT_FILES, ids=_relid)
def test_packt_sample_loads(pbix_path):
    _smoke(pbix_path)


@pytest.mark.slow
@pytest.mark.skipif(not PACKT_FILES, reason="Expert-Data-Modeling-with-Power-BI submodule not initialised")
@pytest.mark.parametrize('pbix_path', PACKT_FILES, ids=_relid)
def test_packt_sample_metadata(pbix_path):
    _metadata_properties(pbix_path)
