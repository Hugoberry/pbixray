"""Nullable dictionary columns split across VertiPaq segments (Mix.pbix).

The `Mix` table was built in Power BI Desktop from:

    let
        n = 2097153,          // 2*2^20 + 1  -> 3 segments of 2^20, 2^20, 1 rows
        seg = 1048576,
        rows = List.Transform({1..n}, each {
            _,                                                             // A
            if _ > seg and _ <= 2*seg and Number.Mod(_, 7) = 0
                then null else "S" & Text.From(Number.Mod(_, 997)),        // B
            if _ <= seg and Number.Mod(_, 5) = 0
                then null else Number.From(_) / 3,                         // C
            if _ <= seg then "low" & Text.From(Number.Mod(_, 50))
            else if Number.Mod(_, 7) = 0 then null
            else "high" & Text.From(Number.Mod(_, 50))                     // D
        }),
        Source = #table(
            type table [A = Int64.Type, B = Text.Type, C = Number.Type, D = Text.Type],
            rows)
    in
        Source

Per column, SS.has_nulls by segment: B [no, yes, no], C [yes, no, no],
D [no, yes, no] (D's null segment introduces new dictionary entries).
The null adjustment to a segment's bit-pack base is a per-segment
property; applying it per-column (IsNullable) shifted every null-free
segment of B and C to the adjacent dictionary entry and turned some real
values into nulls.

Row order is storage order, so expectations are keyed off A (unique 1..n)
rather than position.
"""
import numpy as np
import pytest

N = 2 * 2**20 + 1
SEG = 2**20


@pytest.fixture(scope="module")
def mix_table(mix_model):
    return mix_model.get_table("Mix")


@pytest.fixture(scope="module")
def source_row(mix_table):
    """Source row number k per decoded row, from the key column A."""
    a = mix_table["A"].astype("int64").to_numpy()
    assert a.min() == 1 and a.max() == N and len(np.unique(a)) == N
    return a


def test_row_count(mix_table):
    assert len(mix_table) == N


def test_null_counts_exact(mix_table):
    # From the M script: nulls in B iff seg < k <= 2*seg and k % 7 == 0,
    # in C iff k <= seg and k % 5 == 0, in D iff k > seg and k % 7 == 0.
    assert int(mix_table["B"].isna().sum()) == 2 * SEG // 7 - SEG // 7
    assert int(mix_table["C"].isna().sum()) == SEG // 5
    assert int(mix_table["D"].isna().sum()) == N // 7 - SEG // 7


def test_string_column_nulls_only_in_middle_segment(mix_table, source_row):
    k = source_row
    b = mix_table["B"].to_numpy()
    expected = np.where(
        (k > SEG) & (k <= 2 * SEG) & (k % 7 == 0),
        None,
        np.char.add("S", (k % 997).astype(str)),
    )
    actual = np.where(mix_table["B"].isna().to_numpy(), None, b)
    assert (actual == expected).all()


def test_float_column_nulls_only_in_first_segment(mix_table, source_row):
    k = source_row
    c = mix_table["C"].to_numpy().astype(float)
    expected = np.where((k <= SEG) & (k % 5 == 0), np.nan, k / 3)
    both_null = np.isnan(c) & np.isnan(expected)
    assert (both_null | (np.abs(c - expected) < 1e-9)).all()


def test_null_segment_with_new_dictionary_entries(mix_table, source_row):
    k = source_row
    d = mix_table["D"].to_numpy()
    expected = np.where(
        (k > SEG) & (k % 7 == 0),
        None,
        np.where(
            k <= SEG,
            np.char.add("low", (k % 50).astype(str)),
            np.char.add("high", (k % 50).astype(str)),
        ),
    )
    actual = np.where(mix_table["D"].isna().to_numpy(), None, d)
    assert (actual == expected).all()
