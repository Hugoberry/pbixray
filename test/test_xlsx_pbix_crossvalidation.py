"""Cross-validation of the XLSX decode against the equivalent PBIX.

Microsoft ships several samples twice: as a Power Pivot workbook under
``samples/powerbi-desktop-samples/powerbi-service-samples/*-no-PV.xlsx`` and as
a Power BI model in ``data/old-*-Sample-PBIX.pbix``. The two are produced by
different tools and read through different metadata sources
(``xml_source`` vs ``sqlite_source``), so agreement between them is real ground
truth for the decoder -- not an expectation written to match its output.

That matters for the dictionary base. A column's dictionary always starts at
data id 3, but the base used to be derived from the first segment's declared
minimum, which is the null id (2) for a nullable column on the XLSX path
(``CompressionInfo.Min`` is the null-inclusive bit-pack base). Ten columns in
these workbooks hit that case and decoded with every id shifted by one entry:
``Employee.isNewHire`` came back with 1,247,139 values where the PBIX has
nulls, and blank for the 43,120 rows that hold its only real value.

Comparisons are on row / null / distinct counts rather than values, because the
two formats legitimately differ in representation: dates arrive as serial
numbers from the workbook and as Timestamps from the PBIX, and currency columns
are scaled differently. String columns are compared by value as well.

Requires the powerbi-desktop-samples submodule; skipped without it.
"""
import os

import pandas as pd
import pytest

from pbixray import PBIXRay

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
SAMPLES_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'samples',
    'powerbi-desktop-samples', 'powerbi-service-samples'))

# (workbook, equivalent PBIX) -- every pair shares its full table set.
PAIRS = [
    ("Customer Profitability Sample-no-PV.xlsx", "old-Customer-Profitability-Sample-PBIX.pbix"),
    ("Human Resources Sample-no-PV.xlsx", "old-Human-Resources-Sample-PBIX.pbix"),
    ("Procurement Analysis Sample-no-PV.xlsx", "old-Procurement-Analysis-Sample-PBIX.pbix"),
    ("Retail Analysis Sample-no-PV.xlsx", "old-Retail-Analysis-Sample-PBIX.pbix"),
    ("Sales and Marketing Sample-no-PV.xlsx", "old-Sales-and-Marketing-Sample-PBIX.pbix"),
    ("Supplier Quality Analysis Sample-no-PV.xlsx", "old-Supplier-Quality-Analysis-Sample-PBIX.pbix"),
]

# Dictionary columns whose first segment declares min_data_id == 2 (the null id)
# instead of 3, i.e. the columns a derived dictionary base decodes wrongly.
# Asserted to be exactly this set by test_shifted_base_columns_are_known, so a
# workbook that gains one cannot slip past unnoticed.
SHIFTED_BASE_COLUMNS = {
    "Human Resources Sample-no-PV.xlsx": [
        ("Employee", "TermDate"), ("Employee", "isNewHire"), ("Employee", "TermReason"),
    ],
    "Procurement Analysis Sample-no-PV.xlsx": [
        ("Invoice Line Item", "ExchangeRate"), ("Invoice Line Item", "Invoice Amount"),
    ],
    "Sales and Marketing Sample-no-PV.xlsx": [
        ("SalesFact", "Revenue"), ("Date", "Running Year"), ("Date", "Running Months"),
        ("Date", "Rolling Period"), ("Date", "Rolling Period Sort"),
    ],
}

# Columns that differ for a reason unrelated to the dictionary base, tracked so
# they surface when fixed rather than being silently tolerated.
#
# Product[Product Key] is value-encoded -- its ids are 3/13/23/33/73/75 and
# id + BaseId(7) gives 10/20/30/40/80/82, exactly the PBIX values -- but the
# XLSX schema also names a Dictionary file for it, so _ColumnDecoder takes the
# dictionary branch, builds a six-entry lookup keyed 3..8, and every id except
# the first misses it and becomes NaN. Separate bug, separate fix.
KNOWN_DIFFERENCES = {
    ("Customer Profitability Sample-no-PV.xlsx", "Product", "Product Key"),
}

pytestmark = pytest.mark.skipif(
    not os.path.isdir(SAMPLES_DIR),
    reason="powerbi-desktop-samples submodule not initialised",
)


def _pair_id(pair):
    return pair[0].replace(" Sample-no-PV.xlsx", "")


def _profile(series):
    """Representation-independent shape of a column."""
    return {
        "rows": int(len(series)),
        "nulls": int(pd.isna(series).sum()),
        "distinct": int(series.nunique(dropna=True)),
    }


def _string_values(series):
    """Sorted non-null values, or None when the column is not string-like."""
    if not (pd.api.types.is_object_dtype(series) or pd.api.types.is_string_dtype(series)):
        return None
    present = series[~pd.isna(series)]
    if not all(isinstance(v, str) for v in present.head(50)):
        return None
    return sorted(str(v) for v in present)


@pytest.fixture(scope="module")
def models(request):
    xlsx_name, pbix_name = request.param
    xlsx_path = os.path.join(SAMPLES_DIR, xlsx_name)
    if not os.path.isfile(xlsx_path):
        pytest.skip(f"{xlsx_name} not present in the submodule checkout")
    return xlsx_name, PBIXRay(xlsx_path), PBIXRay(os.path.join(DATA_DIR, pbix_name))


@pytest.mark.parametrize("models", PAIRS, ids=_pair_id, indirect=True)
def test_shifted_base_columns_are_known(models):
    """Pin which columns declare the null id as their first segment minimum.

    The decoder must not derive the dictionary base from that value; this test
    records where the distinction actually bites, so the fixtures below keep
    covering a real case rather than a hypothetical one.
    """
    xlsx_name, xlsx_model, _ = models
    meta = xlsx_model._vertipaq_decoder._meta
    found = []
    for _, column in meta.schema_df.iterrows():
        if not (pd.notnull(column["Dictionary"]) and column["Dictionary"]):
            continue
        if not (pd.notnull(column["IDF"]) and column["IDF"]):
            continue
        segments = meta.get_segment_meta(column)
        if segments and segments[0]["min_data_id"] != 3:
            found.append((column["TableName"], column["ColumnName"]))
    assert sorted(found) == sorted(SHIFTED_BASE_COLUMNS.get(xlsx_name, []))


@pytest.mark.parametrize("models", PAIRS, ids=_pair_id, indirect=True)
def test_shifted_base_columns_match_pbix(models):
    """The columns above must decode to the same shape as the PBIX."""
    xlsx_name, xlsx_model, pbix_model = models
    for table, column in SHIFTED_BASE_COLUMNS.get(xlsx_name, []):
        from_xlsx = xlsx_model.get_table(table, columns=[column])[column]
        from_pbix = pbix_model.get_table(table, columns=[column])[column]
        assert _profile(from_xlsx) == _profile(from_pbix), f"{table}[{column}]"
        values = _string_values(from_pbix)
        if values is not None:
            assert _string_values(from_xlsx) == values, f"{table}[{column}]"


@pytest.mark.slow
@pytest.mark.parametrize("models", PAIRS, ids=_pair_id, indirect=True)
def test_every_common_column_matches_pbix(models):
    """Whole-model sweep: every shared column agrees on rows, nulls, distincts.

    Slower than the targeted test above (these models run to ~1.3M rows) but it
    is the part that would catch a base or null regression in a column nobody
    thought to list.
    """
    xlsx_name, xlsx_model, pbix_model = models
    shared_tables = sorted(set(xlsx_model.tables) & set(pbix_model.tables))
    assert shared_tables, "no tables in common"

    mismatched = set()
    detail = []
    for table in shared_tables:
        xlsx_table = xlsx_model.get_table(table)
        pbix_table = pbix_model.get_table(table)
        assert len(xlsx_table) == len(pbix_table), table
        for column in sorted(set(xlsx_table.columns) & set(pbix_table.columns)):
            from_xlsx = _profile(xlsx_table[column])
            from_pbix = _profile(pbix_table[column])
            if from_xlsx != from_pbix:
                mismatched.add((xlsx_name, table, column))
                detail.append(f"{table}[{column}]: xlsx={from_xlsx} pbix={from_pbix}")

    # Compared as a set so a new regression and a fixed known difference are
    # both failures -- the latter meaning the KNOWN_DIFFERENCES entry is stale.
    expected = {d for d in KNOWN_DIFFERENCES if d[0] == xlsx_name}
    assert mismatched == expected, "\n".join(detail) or "a known difference no longer differs"
