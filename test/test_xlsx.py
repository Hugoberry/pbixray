"""
Tests for xlsx parsing support.

PBIXRay accepts Excel workbooks (.xlsx) in addition to .pbix files — the same
API surface applies. The fixture is provided by conftest.py (xlsx_model).
"""
import glob
import os
import re

import pandas as pd
import pytest

from pbixray import PBIXRay

CSV_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "xlsx")


def _is_nonempty_df(obj):
    return isinstance(obj, pd.DataFrame) and not obj.empty


def _is_df(obj):
    return isinstance(obj, pd.DataFrame)


def _load_fixture(name):
    df = pd.read_csv(os.path.join(CSV_DIR, f"{name}.csv"))
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    return df


def _row_multiset_equal(got, expected):
    """VertiPaq stores rows in RLE-friendly order, not insertion order.
    Compare as a multiset: sort both by every column and check equality.
    """
    cols = list(expected.columns)
    assert list(got.columns) == cols, (
        f"column mismatch: got {list(got.columns)} expected {cols}"
    )
    # Align dtypes via the expected fixture's dtypes
    got = got.copy()
    for c in cols:
        if got[c].dtype != expected[c].dtype:
            got[c] = got[c].astype(expected[c].dtype)
    a = got.sort_values(cols).reset_index(drop=True)
    b = expected.sort_values(cols).reset_index(drop=True)
    return a.equals(b)


def test_xlsx_tables(xlsx_model):
    assert len(xlsx_model.tables) > 0


def test_xlsx_statistics(xlsx_model):
    assert _is_nonempty_df(xlsx_model.statistics)


def test_xlsx_dax_tables(xlsx_model):
    assert _is_df(xlsx_model.dax_tables)


def test_xlsx_dax_measures(xlsx_model):
    assert _is_df(xlsx_model.dax_measures)


def test_xlsx_size(xlsx_model):
    assert isinstance(xlsx_model.size, int)
    assert xlsx_model.size > 0


def test_xlsx_schema(xlsx_model):
    assert _is_nonempty_df(xlsx_model.schema)


def test_xlsx_relationships(xlsx_model):
    assert _is_df(xlsx_model.relationships)


# -------------------------------------------------------------------------
# Endpoints with no XLSX equivalent must still return an empty DataFrame
# (uniform surface with PBIX), never raise.
# -------------------------------------------------------------------------

@pytest.mark.parametrize(
    "endpoint",
    ["aggregations", "ols", "perspectives", "tmschema_column_permissions"],
)
def test_xlsx_pbix_only_endpoints_empty(xlsx_model, endpoint):
    df = getattr(xlsx_model, endpoint)
    assert _is_df(df) and df.empty


# -------------------------------------------------------------------------
# get_table data fidelity — verified against CSV fixtures captured from
# Excel's Power Pivot view. Compared as row-tuple multisets because
# VertiPaq stores rows in RLE-friendly order, not insertion order.
# -------------------------------------------------------------------------

@pytest.mark.parametrize(
    "table",
    ["Plant", "Category", "Material Type", "Defect Type", "Metrics"],
)
def test_xlsx_get_table_matches_fixture(xlsx_model, table):
    expected = _load_fixture(table)
    got = xlsx_model.get_table(table)
    assert len(got) == len(expected), (
        f"{table}: row count {len(got)} != fixture {len(expected)}"
    )
    assert _row_multiset_equal(got, expected), (
        f"{table}: row multiset does not match fixture"
    )


# -------------------------------------------------------------------------
# Data files are named <n>.<dimension_id>.<column>.<ext> (hierarchy files use
# <n>.H$<dimension_id>$<column>.<ext>), so the dimension id is a delimited
# token. Matching it as a bare substring handed one table's files to another
# whenever a dimension id also appeared inside some other table's column name.
# -------------------------------------------------------------------------

@pytest.mark.parametrize(
    "dimension_id, file_name, owned",
    [
        # Files the dimension really owns.
        ("Product", "0.Product.Product Key.0.idf", True),
        ("Product", "0.Product.Product.dictionary", True),
        ("Product", "3.H$Product$Product Key.hidx", True),
        ("Fact_fb28d60b", "17.Fact_fb28d60b.Product Key.dictionary", True),
        ("Fact_fb28d60b", "6.H$Fact_fb28d60b$Product Key.POS_TO_ID.0.idf", True),
        # The Customer Profitability collision: "Product"/"Scenario" occur
        # inside the fact table's column names, never as its dimension token.
        ("Product", "17.Fact_fb28d60b.Product Key.dictionary", False),
        ("Scenario", "17.Fact_fb28d60b.Scenario Key.dictionary", False),
        # An id that is only a prefix or a suffix of the real one.
        ("Fact", "17.Fact_fb28d60b.Product Key.dictionary", False),
        ("fb28d60b", "17.Fact_fb28d60b.Product Key.dictionary", False),
    ],
)
def test_dimension_file_pattern_matches_only_its_own_token(
    dimension_id, file_name, owned
):
    from pbixray.meta.xml_source import XmlMetadataSource

    pattern = XmlMetadataSource._dimension_file_pattern(dimension_id)
    assert bool(pattern.search(file_name)) is owned


# -------------------------------------------------------------------------
# Column file attribution.
#
# Files are named <n>.<dimension_id>.<column>.<ext>, or
# <n>.H$<dimension_id>$<column>.<ext> for hierarchy files. The dimension id is
# the *storage* id, which keeps the table's original name after a rename
# (Supplier Quality shows 'Category' stored as 'Sub Category_<guid>'), so file
# lookup has to key on it rather than on the display name. Storage ids carry a
# guid suffix, which is what makes them collide when tested as bare substrings:
# dimension 'Product' matched '17.Fact_<guid>.Product Key.dictionary' and took
# the fact table's dictionary for its own value-encoded column.
#
# The sweeps below run over every workbook available, including the two that
# have no PBIX counterpart to cross-validate against.
# -------------------------------------------------------------------------

SAMPLES_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "samples",
    "powerbi-desktop-samples", "powerbi-service-samples"))

_DATA_WORKBOOKS = ["Supplier Quality Analysis Sample-no-PV.xlsx", "null_data_id.xlsx"]


def _workbook_paths():
    paths = [os.path.join(os.path.dirname(__file__), "..", "data", n)
             for n in _DATA_WORKBOOKS]
    if os.path.isdir(SAMPLES_DIR):
        paths += sorted(glob.glob(os.path.join(SAMPLES_DIR, "*.xlsx")))
    return paths


@pytest.fixture(scope="module")
def workbook_source(request):
    return PBIXRay(request.param)._vertipaq_decoder._meta


_WORKBOOKS = pytest.mark.parametrize(
    "workbook_source", _workbook_paths(), ids=os.path.basename, indirect=True)


@pytest.mark.parametrize(
    "dimension_id, file_name, owned",
    [
        # Files the dimension really owns.
        ("Product", "0.Product.Product Key.0.idf", True),
        ("Product", "0.Product.Product.dictionary", True),
        ("Product", "3.H$Product$Product Key.hidx", True),
        ("Fact_fb28d60b", "17.Fact_fb28d60b.Product Key.dictionary", True),
        ("Fact_fb28d60b", "6.H$Fact_fb28d60b$Product Key.POS_TO_ID.0.idf", True),
        # The Customer Profitability collision: "Product"/"Scenario" occur
        # inside the fact table's column names, never as its dimension token.
        ("Product", "17.Fact_fb28d60b.Product Key.dictionary", False),
        ("Scenario", "17.Fact_fb28d60b.Scenario Key.dictionary", False),
        # A storage id truncated to the part before the guid, or to the guid.
        ("Fact", "17.Fact_fb28d60b.Product Key.dictionary", False),
        ("fb28d60b", "17.Fact_fb28d60b.Product Key.dictionary", False),
    ],
)
def test_dimension_file_pattern_matches_only_its_own_token(
    dimension_id, file_name, owned
):
    from pbixray.meta.xml_source import XmlMetadataSource

    pattern = XmlMetadataSource._dimension_file_pattern(dimension_id)
    assert bool(pattern.search(file_name)) is owned


@_WORKBOOKS
def test_column_files_belong_to_their_own_dimension(workbook_source):
    """No column may be handed a file owned by another dimension.

    Borrowing another table's dictionary is silent whenever the two id spaces
    happen to agree -- Scenario[Scenario Key] decoded correctly for exactly
    that reason -- so attribution is checked directly rather than by waiting
    for decoded values to disagree.
    """
    for _, column in workbook_source.schema_df.iterrows():
        pattern = workbook_source._dimension_file_pattern(column["DimensionID"])
        for key in ("Dictionary", "HIDX", "IDF"):
            file_name = column[key]
            if not (pd.notnull(file_name) and file_name):
                continue
            assert pattern.search(file_name), (
                f"{column['TableName']}[{column['ColumnName']}] {key} -> "
                f"{file_name} does not belong to dimension "
                f"{column['DimensionID']!r}"
            )


@_WORKBOOKS
def test_dimension_id_is_an_exact_storage_token(workbook_source):
    """Every dimension id must appear verbatim as a file-name token.

    Matching the id as a delimited token only resolves files while the id
    equals the token exactly. If a writer ever emits a truncated or otherwise
    divergent id, the lookup would return nothing and columns would decode as
    empty -- so pin the assumption here, where it fails loudly.
    """
    tokens = set()
    for file_entry in workbook_source.data_model.file_log:
        match = re.match(r'^\d+\.(?:H\$)?([^.$]+)[.$]', file_entry['FileName'])
        if match and file_entry['FileName'].endswith(('.dictionary', '.idf', '.hidx')):
            tokens.add(match.group(1))
    for dimension_id in workbook_source.schema_df['DimensionID'].unique():
        assert dimension_id in tokens, (
            f"dimension {dimension_id!r} has no exactly-matching file token; "
            f"closest: {[t for t in tokens if dimension_id in t or t in dimension_id]}"
        )


@_WORKBOOKS
def test_every_column_resolves_its_idf(workbook_source):
    """Anchoring the dimension match must not drop a file it used to find."""
    missing = [
        f"{c['TableName']}[{c['ColumnName']}]"
        for _, c in workbook_source.schema_df.iterrows()
        if not (pd.notnull(c["IDF"]) and c["IDF"])
    ]
    assert not missing, f"columns with no IDF: {missing}"


def test_xlsx_get_table_no_rownumber_column(xlsx_model):
    # RowNumber is VertiPaq's internal storage position; we hide it the
    # same way PBIX does, so get_table only exposes user-facing columns.
    for table in ["Plant", "Category", "Metrics"]:
        assert "RowNumber" not in xlsx_model.get_table(table).columns
