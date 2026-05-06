EXPECTED_ROWS = 2 * 2**20 + 1


def test_multi_segment_row_count(five_m_model):
    """5M.pbix table '2Mrow' has 3 segments totalling 2*2^20+1 rows."""
    table = five_m_model.get_table("2Mrow")
    assert len(table) == EXPECTED_ROWS


def test_multi_segment_values(five_m_model):
    """Column A should contain consecutive integers 1 ... 2*2^20+1."""
    table = five_m_model.get_table("2Mrow")
    col = table["A"].astype(int)
    assert int(col.iloc[0]) == 1
    assert int(col.iloc[-1]) == EXPECTED_ROWS
    assert int(col.max()) == EXPECTED_ROWS
