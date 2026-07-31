"""Null data id handling across segments (3segment.pbix).

VertiPaq reserves data id 2 for NULL and rebases every column so its first real
data id is 3. Both are absolute constants, but the decoder used to derive them
from a segment's declared ``min_data_id``, which is only equal to them for a
column whose first segment holds the column minimum and contains no nulls.

The `TheTable` table was built in Power BI Desktop from:

    let
        seg = 1048576,
        n   = 2 * seg + 1,                    // 3 segments: 1048576 / 1048576 / 1
        Rows = List.Transform({1..n}, each
            let
                k = _,
                s = Number.IntegerDivide(k - 1, seg)
            in
            {
                if s = 1 and Number.Mod(k, 7) = 0 then null else k,      // N1
                if s = 0 then null else k * 2,                           // N2
                if s = 0 then null else "x" & Text.From(Number.Mod(k, 1000))  // S1
            }),
        Source = #table(
            type table [N1 = Int64.Type, N2 = Int64.Type, S1 = Text.Type],
            Rows)
    in
        Source

Each column pins one way of getting the constants wrong:

N1  value-encoded, nulls in segment 1 only. That segment's own min_data_id is
    1048579 while the column's is 3, so basing it at ``min_data_id - 1``
    decodes every one of its rows 1048576 too high.
N2  value-encoded, all-null segment 0. That segment reports the sentinel
    min == max == 2, so ``min_data_id - 1`` yields a null slot of 1 that never
    matches the id 2 actually stored, and the nulls decode as numbers.
S1  dictionary-encoded, all-null segment 0. Deriving the dictionary base from
    that segment's min_data_id yields 2 instead of 3, shifting every id by one
    so each row returns a neighbouring dictionary entry.

Row order is storage order and rows are reordered within a segment, so
expectations are keyed off N1, whose value is its own source row number.
Segments concatenate in order, so a row's segment follows from its position.

The same constants apply to the XLSX (Power Pivot) metadata path, which reaches
them through different fields: per-segment stats live in ColumnSegmentStats
rather than an .idfmeta SS record, and `min_data_id` is read from
CompressionInfo.Min -- the bit-pack base, already null-inclusive -- rather than
from the null-excluding minimum. `null_data_id.xlsx` is the only sample of that
format containing nulls at all, built in Excel (Get & Transform -> Data Model):

    let
        n = 500,
        Rows = List.Transform({1..n}, each {
            _,
            if Number.Mod(_, 7)  = 0 then null else _ * 3,
            if Number.Mod(_, 5)  = 0 then null else _ / 100,
            if Number.Mod(_, 11) = 0 then null else "s" & Text.From(Number.Mod(_, 40)),
            _ * 2
        }),
        Source = #table(
            type table [A = Int64.Type, N = Int64.Type, C = Currency.Type,
                        S = Text.Type, K = Int64.Type],
            Rows)
    in
        Source
"""
import numpy as np
import pandas as pd
import pytest

# Stated here rather than imported from the decoder: these are properties of the
# VertiPaq format, so the test must fail if the decoder's own idea of them drifts.
XM_DATA_ID_NULL = 2
XM_FIRST_DATA_ID = 3

SEG = 2 ** 20
N = 2 * SEG + 1

# nulls in N1: segment 1 rows divisible by 7; in N2/S1: all of segment 0.
N1_NULLS = 2 * SEG // 7 - SEG // 7
SEG0_ROWS = SEG


@pytest.fixture(scope="module")
def table(three_segment_model):
    return three_segment_model.get_table("TheTable")


@pytest.fixture(scope="module")
def source_row(table):
    """Source row number k per decoded row, and the rows it is known for.

    N1 carries its own source row number, so it keys the other columns; the
    rows where N1 itself is null (segment 1, k % 7 == 0) are excluded.
    """
    k = table["N1"].to_numpy(dtype="float64")
    known = ~np.isnan(k)
    return k, known


@pytest.fixture(scope="module")
def segment_of(table):
    """Segment index per decoded row (segments concatenate in storage order)."""
    return np.arange(len(table)) // SEG


def test_row_count(table):
    assert len(table) == N


def test_segment_layout(three_segment_model):
    """The layout the rest of this module depends on.

    Asserted explicitly because a Desktop version that packed these columns
    differently would leave the tests passing while testing nothing.
    """
    meta = three_segment_model._vertipaq_decoder._meta
    schema = meta.schema_df
    layout = {}
    for _, column in schema[schema["TableName"] == "TheTable"].iterrows():
        segments = meta.get_segment_meta(column)
        layout[column["ColumnName"]] = [
            (s["min_data_id"], bool(s.get("has_nulls"))) for s in segments
        ]

    # N1: nulls confined to segment 1, whose own minimum is far above the
    # column's -- this is what separates the constant from min_data_id - 1.
    mins, nulls = zip(*layout["N1"])
    assert nulls == (False, True, False)
    assert mins[0] == XM_FIRST_DATA_ID
    assert mins[1] > XM_FIRST_DATA_ID + SEG // 2

    # N2 and S1: all-null first segment carrying the sentinel.
    for name in ("N2", "S1"):
        mins, nulls = zip(*layout[name])
        assert nulls == (True, False, False), name
        assert mins[0] == XM_DATA_ID_NULL, name


def test_value_encoded_nulls_in_a_later_segment(table, source_row, segment_of):
    """N1: nulls in a segment whose own minimum is ~1M above the column's."""
    k, known = source_row
    expected_null = (segment_of == 1) & ~known
    # every row of segment 1 divisible by 7 is null, and nothing else is
    assert int(table["N1"].isna().sum()) == N1_NULLS
    assert expected_null.sum() == N1_NULLS
    # non-null rows decode to their own source row number, in every segment
    assert np.array_equal(k[known], k[known].astype("int64").astype("float64"))
    assert np.array_equal(np.sort(k[known & (segment_of == 0)]),
                          np.arange(1, SEG + 1, dtype="float64"))
    tail = np.sort(k[known & (segment_of == 1)])
    assert tail[0] == SEG + 1 and tail[-1] == 2 * SEG
    assert not np.any(tail % 7 == 0)


def test_value_encoded_all_null_first_segment(table, source_row, segment_of):
    """N2: the sentinel segment must decode as nulls, not as numbers."""
    k, known = source_row
    n2 = table["N2"].to_numpy(dtype="float64")
    assert int(table["N2"].isna().sum()) == SEG0_ROWS
    assert np.isnan(n2[segment_of == 0]).all()
    rest = known & (segment_of > 0)
    assert np.array_equal(n2[rest], k[rest] * 2)


def test_dictionary_all_null_first_segment(table, source_row, segment_of):
    """S1: dictionary base must not come from the sentinel segment."""
    k, known = source_row
    s1 = table["S1"].to_numpy()
    assert int(table["S1"].isna().sum()) == SEG0_ROWS
    assert table["S1"][segment_of == 0].isna().all()
    rest = known & (segment_of > 0)
    expected = np.char.add("x", (k[rest] % 1000).astype("int64").astype(str))
    assert np.array_equal(s1[rest].astype(str), expected)


def test_iter_table_matches_get_table(three_segment_model, table):
    """iter_table shares _ColumnDecoder, so it must agree row for row."""
    chunks = list(
        three_segment_model.iter_table(
            "TheTable", chunk_size=250_000, strings_as_categorical=False
        )
    )
    assert sum(len(c) for c in chunks) == N
    for column in ("N1", "N2", "S1"):
        streamed = pd.concat([c[column] for c in chunks], ignore_index=True)
        whole = table[column].reset_index(drop=True)
        assert streamed.isna().equals(whole.isna()), column
        present = ~whole.isna()
        assert (streamed[present].to_numpy() == whole[present].to_numpy()).all(), column


# --------------------------------------------------------------------------
# XLSX (Power Pivot) metadata path -- null_data_id.xlsx, 500 rows, 1 segment
# --------------------------------------------------------------------------

XLSX_ROWS = 500
XLSX_NULLS = {"N": XLSX_ROWS // 7, "C": XLSX_ROWS // 5, "S": XLSX_ROWS // 11,
              "A": 0, "K": 0}


@pytest.fixture(scope="module")
def xlsx_table(null_data_id_xlsx_model):
    return null_data_id_xlsx_model.get_table("TheTable")


@pytest.fixture(scope="module")
def xlsx_source_row(xlsx_table):
    """Source row number k per decoded row, from the null-free key column A."""
    k = xlsx_table["A"].to_numpy(dtype="int64")
    assert sorted(k) == list(range(1, XLSX_ROWS + 1))
    return k


def test_xlsx_segment_stats_reach_the_decoder(null_data_id_xlsx_model):
    """has_nulls must survive the XLSX metadata path, per segment.

    Without it the decoder cannot know a segment carries a null slot, and the
    reserved id decodes as an ordinary value.
    """
    meta = null_data_id_xlsx_model._vertipaq_decoder._meta
    schema = meta.schema_df
    for _, column in schema[schema["TableName"] == "TheTable"].iterrows():
        name = column["ColumnName"]
        if name not in XLSX_NULLS:
            continue
        segments = meta.get_segment_meta(column)
        assert len(segments) == 1, name
        segment = segments[0]
        assert 'has_nulls' in segment, name
        assert bool(segment['has_nulls']) is (XLSX_NULLS[name] > 0), name
        # min_data_id here is CompressionInfo.Min, i.e. the bit-pack base: the
        # null id for a segment with nulls, the segment's own minimum otherwise.
        expected = XM_DATA_ID_NULL if XLSX_NULLS[name] else XM_FIRST_DATA_ID
        assert segment['min_data_id'] == expected, name


def test_xlsx_null_counts(xlsx_table):
    for column, expected in XLSX_NULLS.items():
        assert int(xlsx_table[column].isna().sum()) == expected, column


def test_xlsx_value_encoded_values(xlsx_table, xlsx_source_row):
    """N (integer) and C (currency) are value-encoded and nullable."""
    k = xlsx_source_row
    n = xlsx_table["N"].to_numpy(dtype="float64")
    expected_n = np.where(k % 7 == 0, np.nan, k * 3.0)
    assert ((np.isnan(n) & np.isnan(expected_n)) | (n == expected_n)).all()

    c = xlsx_table["C"].to_numpy(dtype="float64")
    expected_c = np.where(k % 5 == 0, np.nan, k / 100)
    assert ((np.isnan(c) & np.isnan(expected_c)) | (np.abs(c - expected_c) < 1e-9)).all()

    # the null-free control keeps its integer dtype -- only segments that
    # declare nulls widen
    assert np.array_equal(xlsx_table["K"].to_numpy(dtype="int64"), k * 2)


def test_xlsx_dictionary_values(xlsx_table, xlsx_source_row):
    """S is dictionary-encoded: a base of CompressionInfo.Min would shift it.

    Ids are assigned in insertion order, so an off-by-one base does not map to
    the numerically adjacent string -- each row returns an arbitrary other row's
    value, which is why equality here is checked row by row.
    """
    k = xlsx_source_row
    s = xlsx_table["S"]
    present = ~s.isna().to_numpy()
    expected = np.char.add("s", (k[present] % 40).astype(str))
    assert np.array_equal(s.to_numpy()[present].astype(str), expected)
    assert (k[~present] % 11 == 0).all()
