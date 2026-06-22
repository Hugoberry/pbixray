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


@pytest.fixture(scope="module")
def five_m_model():
    return PBIXRay(os.path.join(DATA_DIR, "5M.pbix"))


@pytest.fixture(scope="module")
def legacy_schema17_model():
    # SCHEMAVERSION 17 PowerPivot-era model whose `Column` table has no `Type`
    # column (role lives in `BindingType`). Regression guard for that schema.
    return PBIXRay(os.path.join(DATA_DIR, "old-schema17-DataTable.pbix"))


@pytest.fixture(scope="module")
def empty_schema_model():
    # Model with only calculated tables / measures, so the schema query matches
    # no rows. Regression guard: the model must still open with an empty schema.
    return PBIXRay(os.path.join(DATA_DIR, "empty-schema-calc-only.pbix"))


@pytest.fixture(scope="module")
def internet_sales_abf_model():
    # AdventureWorks Internet Sales tabular backup, loaded natively as a raw .abf
    # (no zip envelope). Its `Internet Sales` table has 5 partitions
    # (2010..2014) — the canonical multi-partition decode fixture.
    return PBIXRay(os.path.join(DATA_DIR, "Adventure Works Internet Sales Database.abf"))


@pytest.fixture(scope="module")
def directquery_model():
    # DirectQuery model whose queries and parameters live only in the DataMashup
    # part (native-SQL partitions, empty AS Expression table).
    return PBIXRay(os.path.join(DATA_DIR, "directquery-parameters.pbix"))
