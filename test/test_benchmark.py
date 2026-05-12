import pytest
import time
import os

from pbixray import PBIXRay

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


@pytest.fixture(scope="module")
def five_m_path():
    return os.path.join(DATA_DIR, "5M.pbix")


def test_benchmark_load(five_m_path):
    """Benchmark: full model load."""
    start = time.perf_counter()
    model = PBIXRay(five_m_path)
    elapsed = time.perf_counter() - start
    print(f"\nModel load: {elapsed:.3f}s")


def test_benchmark_decode(five_m_path):
    """Benchmark: decode 2M+ row table."""
    model = PBIXRay(five_m_path)

    times = []
    for _ in range(3):
        start = time.perf_counter()
        table = model.get_table("2Mrow")
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    median = sorted(times)[1]
    print(f"\nTable decode (2M rows): median {median:.3f}s over 3 runs")
    print(f"  Rows: {len(table)}, Columns: {len(table.columns)}")
    assert len(table) == 2 * 2**20 + 1
