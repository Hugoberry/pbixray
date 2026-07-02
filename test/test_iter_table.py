import os
from collections import Counter

import pandas as pd
import pytest

from pbixray import PBIXRay
import pbixray.vertipaq_decoder as vpd

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


def _as_object(series):
    """Normalizes a Series to object dtype with None for missing values."""
    s = series.astype(object)
    return s.where(s.notna(), None).reset_index(drop=True)


def _concat_chunks(chunks):
    out = pd.concat(chunks)
    out.index = pd.RangeIndex(len(out))
    return out


def assert_chunks_match_table(model, table_name, expected=None, **iter_kwargs):
    expected = model.get_table(table_name) if expected is None else expected
    chunks = list(model.iter_table(table_name, **iter_kwargs))
    if not chunks:
        assert len(expected) == 0
        return
    actual = _concat_chunks(chunks)
    assert list(actual.columns) == list(expected.columns)
    for col in expected.columns:
        pd.testing.assert_series_equal(
            _as_object(actual[col]), _as_object(expected[col]),
            check_dtype=False, check_names=False,
        )


# ---------- multi-segment table (5M.pbix / 2Mrow has 3 segments) ----------

def test_segment_chunks_concat_equals_get_table(five_m_model):
    expected = five_m_model.get_table("2Mrow")
    chunks = list(five_m_model.iter_table("2Mrow", strings_as_categorical=False))
    assert len(chunks) == 3  # one chunk per VertiPaq segment
    pd.testing.assert_frame_equal(_concat_chunks(chunks), expected)


def test_categorical_default_values_match(five_m_model):
    assert_chunks_match_table(five_m_model, "2Mrow")


def test_chunk_size_respects_segment_boundaries(five_m_model):
    seg_lengths = [1048576, 1048576, 1]
    chunks = list(five_m_model.iter_table("2Mrow", chunk_size=300_000))
    expected_lengths = []
    for seg_len in seg_lengths:
        for lo in range(0, seg_len, 300_000):
            expected_lengths.append(min(300_000, seg_len - lo))
    assert [len(c) for c in chunks] == expected_lengths


def test_chunk_size_larger_than_segments(five_m_model):
    chunks = list(five_m_model.iter_table("2Mrow", chunk_size=5_000_000))
    assert [len(c) for c in chunks] == [1048576, 1048576, 1]


def test_chunk_size_values_match(five_m_model):
    assert_chunks_match_table(five_m_model, "2Mrow", chunk_size=300_000)


def test_chunk_index_is_global_row_range(five_m_model):
    offset = 0
    for chunk in five_m_model.iter_table("2Mrow", chunk_size=400_000):
        assert chunk.index[0] == offset
        assert chunk.index[-1] == offset + len(chunk) - 1
        offset += len(chunk)
    assert offset == 2 * 1048576 + 1


# ---------- multi-partition table (raw .abf, 5 partitions 2010..2014) ----------

def test_multi_partition_chunk_lengths(internet_sales_abf_model):
    """Partitions flatten to one chunk per segment, covering all 60,398 rows."""
    chunks = list(internet_sales_abf_model.iter_table("Internet Sales"))
    assert len(chunks) == 5  # each partition is small enough for one segment
    assert Counter(len(c) for c in chunks) == Counter([14, 2216, 3397, 52801, 1970])


def test_multi_partition_chunks_match_get_table(internet_sales_abf_model):
    assert_chunks_match_table(
        internet_sales_abf_model, "Internet Sales", strings_as_categorical=False
    )
    assert_chunks_match_table(internet_sales_abf_model, "Internet Sales")


# ---------- all dtypes / all tables ----------

@pytest.mark.parametrize("fixture_name", ["work_model", "xlsx_model"])
def test_all_tables_chunks_match_get_table(fixture_name, request):
    model = request.getfixturevalue(fixture_name)
    for table_name in model.tables:
        assert_chunks_match_table(model, table_name, strings_as_categorical=False)
        assert_chunks_match_table(model, table_name)  # categorical default


def test_small_chunk_size(work_model):
    table_name = work_model.tables[0]
    assert_chunks_match_table(work_model, table_name, chunk_size=7)


# ---------- strings_as_categorical on get_table ----------

def test_get_table_categorical_flag(adventure_works_dw_model):
    default = adventure_works_dw_model.get_table("Product")
    cat = adventure_works_dw_model.get_table("Product", strings_as_categorical=True)
    cat_cols = [c for c in cat.columns if isinstance(cat[c].dtype, pd.CategoricalDtype)]
    assert cat_cols  # Product has string columns
    for col in default.columns:
        pd.testing.assert_series_equal(
            _as_object(cat[col]), _as_object(default[col]),
            check_dtype=False, check_names=False,
        )
    # non-string columns keep their regular dtype
    non_string = [c for c in default.columns if c not in cat_cols]
    for col in non_string:
        assert cat[col].dtype == default[col].dtype


def test_iter_table_categorical_shares_categories(five_m_model):
    chunks = list(five_m_model.iter_table("2Mrow", chunk_size=400_000))
    cat_cols = [
        c for c in chunks[0].columns
        if isinstance(chunks[0][c].dtype, pd.CategoricalDtype)
    ]
    for col in cat_cols:
        dtypes = {chunk[col].dtype for chunk in chunks}
        assert len(dtypes) == 1  # same categories across every chunk


# ---------- projection & errors ----------

def test_projection(five_m_model):
    table_cols = five_m_model.schema[five_m_model.schema["TableName"] == "2Mrow"]["ColumnName"]
    wanted = [table_cols.iloc[0]]
    chunks = list(five_m_model.iter_table("2Mrow", columns=wanted))
    assert all(list(c.columns) == wanted for c in chunks)


def test_unknown_column_raises(five_m_model):
    with pytest.raises(ValueError, match="not found in table"):
        next(iter(five_m_model.iter_table("2Mrow", columns=["nope"])))


def test_unknown_table_yields_nothing(five_m_model):
    assert list(five_m_model.iter_table("no_such_table")) == []


def test_bad_chunk_size_raises(five_m_model):
    with pytest.raises(ValueError, match="chunk_size"):
        next(iter(five_m_model.iter_table("2Mrow", chunk_size=0)))


# ---------- alignment guardrail ----------

def test_misaligned_segments_raise(work_model, monkeypatch):
    table_name = next(
        t for t in work_model.tables
        if (work_model.schema["TableName"] == t).sum() >= 2
    )
    original = vpd._ColumnDecoder.segment_lengths
    state = {"calls": 0}

    def mismatched(self):
        state["calls"] += 1
        lengths = original(self)
        if state["calls"] > 1:
            return [length + 1 for length in lengths]
        return lengths

    monkeypatch.setattr(vpd._ColumnDecoder, "segment_lengths", mismatched)
    with pytest.raises(ValueError, match="not row-aligned"):
        list(work_model.iter_table(table_name))


# ---------- duplicate dictionary values ----------

def test_duplicate_dictionary_values_dedupe():
    lookup = vpd._DictionaryLookup({10: "a", 11: "b", 12: "a", 13: "c"})
    dtype, inverse = lookup.categorical_dtype_and_inverse()
    assert list(dtype.categories) == ["a", "b", "c"]
    assert list(inverse) == [0, 1, 0, 2]
    import numpy as np
    codes = vpd.VertiPaqDecoder._ids_to_codes(np.array([12, 9, 10, 13]), lookup)
    series = vpd.VertiPaqDecoder._codes_to_series(codes, lookup, as_categorical=True)
    assert list(series.astype(object).where(series.notna(), None)) == ["a", None, "a", "c"]


# ---------- on_disk parity (also exercises the streaming loader) ----------

def test_on_disk_chunks_match_in_memory(five_m_model):
    expected = list(five_m_model.iter_table("2Mrow", chunk_size=500_000))
    with PBIXRay(os.path.join(DATA_DIR, "5M.pbix"), on_disk=True) as on_disk_model:
        actual = list(on_disk_model.iter_table("2Mrow", chunk_size=500_000))
        assert len(actual) == len(expected)
        for left, right in zip(actual, expected):
            pd.testing.assert_frame_equal(left, right)
