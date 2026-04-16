import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pbix')))

from pbixray import PBIXRay

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


@pytest.fixture(scope="module")
def work_model():
    return PBIXRay(os.path.join(DATA_DIR, "work.pbix"))


@pytest.fixture(scope="module")
def abc_model():
    return PBIXRay(os.path.join(DATA_DIR, "abc.pbix"))


@pytest.fixture(scope="module")
def sales_returns_model():
    return PBIXRay(os.path.join(DATA_DIR, "Sales & Returns Sample v201912.pbix"))


@pytest.fixture(scope="module")
def adventure_works_model():
    return PBIXRay(os.path.join(DATA_DIR, "Adventure Works, Internet Sales.pbix"))


@pytest.fixture(scope="module")
def supplier_quality_model():
    return PBIXRay(os.path.join(DATA_DIR, "old-Supplier-Quality-Analysis-Sample-PBIX.pbix"))


@pytest.fixture(scope="module")
def rls_model():
    return PBIXRay(os.path.join(DATA_DIR, "rls-sample-report.pbix"))


@pytest.fixture(scope="module")
def excalidraw_model():
    return PBIXRay(os.path.join(DATA_DIR, "Excalidraw.pbix"))


@pytest.fixture(scope="module")
def adventure_works_dw_model():
    return PBIXRay(os.path.join(DATA_DIR, "Adventure Works DW 2020.pbix"))


@pytest.fixture(scope="module")
def blog_demo_model():
    return PBIXRay(os.path.join(DATA_DIR, "2020SU11 Blog Demo - November.pbix"))


@pytest.fixture(scope="module")
def xlsx_model():
    return PBIXRay(os.path.join(DATA_DIR, "Supplier Quality Analysis Sample-no-PV.xlsx"))
