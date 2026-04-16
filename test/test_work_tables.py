"""
Translated from duckdb-pbix-extension/test/sql/work_*.test

Each test loads a table from work.pbix and verifies:
  1. Row count matches the CSV reference
  2. Data matches the CSV reference (zero mismatched rows)
"""
import os
import pandas as pd
import pytest

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
WORK_CSV_DIR = os.path.join(DATA_DIR, "work")


def _csv(name):
    # keep_default_na=False: don't auto-convert 'NA' strings to NaN (Power BI uses
    # 'NA' as a legitimate category label, e.g. Color='NA').
    # na_values=['']: only true empty cells become NaN (preserves numeric nulls).
    return pd.read_csv(os.path.join(WORK_CSV_DIR, name), keep_default_na=False, na_values=[''])


def _normalise(df):
    """
    Normalise extension types so assert_frame_equal handles NA consistently:
      - StringDtype <NA>  → "" (empty string, matches CSV empty cells)
      - Nullable integer  → float64 (<NA> becomes nan, comparable with CSV nan)
      - object with Decimal values → float64 (pbixray returns Decimal for some
        numeric columns; CSV has plain float64)
    """
    df = df.copy()
    for col in df.columns:
        if isinstance(df[col].dtype, pd.StringDtype):
            df[col] = df[col].fillna("").astype(str)
        elif hasattr(df[col].dtype, 'numpy_dtype'):
            # Catches pd.Int8Dtype, Int16Dtype, Int32Dtype, Int64Dtype, etc.
            df[col] = df[col].astype(float)
        elif df[col].dtype == object:
            # Convert Decimal objects to float (leave plain string columns unchanged)
            try:
                df[col] = pd.to_numeric(df[col])
            except (ValueError, TypeError):
                pass
    return df


def _assert_match(df_actual, df_expected, cols, key_col):
    """
    Mirror of the SQL EXCEPT pattern:
      - select only the specified columns
      - sort both by key_col
      - assert identical (ignoring dtypes, allowing float tolerance)
    """
    df_a = _normalise(df_actual[cols].sort_values(key_col).reset_index(drop=True))
    df_e = _normalise(df_expected[cols].sort_values(key_col).reset_index(drop=True))
    pd.testing.assert_frame_equal(df_a, df_e, check_dtype=False, check_exact=False, rtol=1e-4)


# ---------------------------------------------------------------------------
# Currency  (work_currency.test) — 105 rows
# ---------------------------------------------------------------------------

CURRENCY_COLS = ["CurrencyKey", "Code", "Currency", "Format String"]

def test_currency_row_count(work_model):
    table = work_model.get_table("Currency")
    csv = _csv("Currency.csv")
    assert len(table) == 105
    assert len(csv) == 105


def test_currency_data_matches_csv(work_model):
    table = work_model.get_table("Currency")
    csv = _csv("Currency.csv")
    _assert_match(table, csv, CURRENCY_COLS, "CurrencyKey")


# ---------------------------------------------------------------------------
# Customer  (work_customer.test) — 18,485 rows
# ---------------------------------------------------------------------------

CUSTOMER_COLS = [
    "CustomerKey", "Customer ID", "Customer", "City",
    "State-Province", "Country-Region", "Postal Code",
]

def test_customer_row_count(work_model):
    table = work_model.get_table("Customer")
    csv = _csv("Customer.csv")
    assert len(table) == 18_485
    assert len(csv) == 18_485


def test_customer_data_matches_csv(work_model):
    table = work_model.get_table("Customer")
    csv = _csv("Customer.csv")
    _assert_match(table, csv, CUSTOMER_COLS, "CustomerKey")


# ---------------------------------------------------------------------------
# Date  (work_date.test) — 1,461 rows
# ---------------------------------------------------------------------------

DATE_COLS = [
    "DateKey", "Date", "Fiscal Year", "Fiscal Quarter",
    "Month", "MonthKey", "Full Date", "Month Number Of Year",
]

def test_date_row_count(work_model):
    table = work_model.get_table("Date")
    csv = _csv("Date.csv")
    assert len(table) == 1_461
    assert len(csv) == 1_461


def test_date_data_matches_csv(work_model):
    table = work_model.get_table("Date")
    csv = _csv("Date.csv")

    # Normalise the Date column to string so timestamp formats don't differ
    table = table.copy()
    csv = csv.copy()
    table["Date"] = pd.to_datetime(table["Date"]).dt.strftime("%Y-%m-%d")
    csv["Date"] = pd.to_datetime(csv["Date"]).dt.strftime("%Y-%m-%d")

    _assert_match(table, csv, DATE_COLS, "DateKey")


# ---------------------------------------------------------------------------
# Product  (work_product.test) — 397 rows
# Note: List Price is excluded (commented out in the original SQL test).
#       Standard Cost is cast to int in both sides, matching the SQL cast.
# ---------------------------------------------------------------------------

PRODUCT_COLS = [
    "ProductKey", "Product", "Standard Cost", "Color", "Model",
    "Subcategory", "Category", "SKU", "Safety Stock Level", "Reorder Point", "Class",
]

def test_product_row_count(work_model):
    table = work_model.get_table("Product")
    csv = _csv("Product.csv")
    assert len(table) == 397
    assert len(csv) == 397


def test_product_data_matches_csv(work_model):
    table = work_model.get_table("Product")
    csv = _csv("Product.csv")

    # Mirror the SQL CAST("Standard Cost" AS INT)
    table = table.copy()
    csv = csv.copy()
    table["Standard Cost"] = table["Standard Cost"].astype(int)
    csv["Standard Cost"] = csv["Standard Cost"].astype(int)

    _assert_match(table, csv, PRODUCT_COLS, "ProductKey")


# ---------------------------------------------------------------------------
# Reseller  (work_reseller.test) — 702 rows
# ---------------------------------------------------------------------------

RESELLER_COLS = [
    "ResellerKey", "Business Type", "Reseller", "City",
    "State-Province", "Country-Region", "Postal Code",
]

def test_reseller_row_count(work_model):
    table = work_model.get_table("Reseller")
    csv = _csv("Reseller.csv")
    assert len(table) == 702
    assert len(csv) == 702


def test_reseller_data_matches_csv(work_model):
    table = work_model.get_table("Reseller")
    csv = _csv("Reseller.csv")
    _assert_match(table, csv, RESELLER_COLS, "ResellerKey")


# ---------------------------------------------------------------------------
# Sales  (work_sales.test) — 121,253 rows
# ---------------------------------------------------------------------------

SALES_COLS = [
    "SalesOrderLineKey", "ResellerKey", "CustomerKey", "ProductKey",
    "OrderDateKey", "DueDateKey", "ShipDateKey", "SalesTerritoryKey",
    "Order Quantity", "Unit Price", "Extended Amount",
    "Product Standard Cost", "Total Product Cost", "Sales Amount",
    "Unit Price Discount Pct", "CurrencyKey",
]

def test_sales_row_count(work_model):
    table = work_model.get_table("Sales")
    csv = _csv("Sales.csv")
    assert len(table) == 121_253
    assert len(csv) == 121_253


def test_sales_data_matches_csv(work_model):
    table = work_model.get_table("Sales")
    csv = _csv("Sales.csv")
    _assert_match(table, csv, SALES_COLS, "SalesOrderLineKey")


# ---------------------------------------------------------------------------
# Sales Order  (work_sales_order.test) — 121,253 rows
# ---------------------------------------------------------------------------

SALES_ORDER_COLS = [
    "SalesOrderLineKey", "Sales Order", "Sales Order Line", "Channel",
]

def test_sales_order_row_count(work_model):
    table = work_model.get_table("Sales Order")
    csv = _csv("Sales Order.csv")
    assert len(table) == 121_253
    assert len(csv) == 121_253


def test_sales_order_data_matches_csv(work_model):
    table = work_model.get_table("Sales Order")
    csv = _csv("Sales Order.csv")
    _assert_match(table, csv, SALES_ORDER_COLS, "SalesOrderLineKey")


# ---------------------------------------------------------------------------
# Sales Territory  (work_sales_territory.test) — 11 rows
# ---------------------------------------------------------------------------

SALES_TERRITORY_COLS = ["SalesTerritoryKey", "Region", "Country", "Group"]

def test_sales_territory_row_count(work_model):
    table = work_model.get_table("Sales Territory")
    csv = _csv("Sales Territory.csv")
    assert len(table) == 11
    assert len(csv) == 11


def test_sales_territory_data_matches_csv(work_model):
    table = work_model.get_table("Sales Territory")
    csv = _csv("Sales Territory.csv")
    _assert_match(table, csv, SALES_TERRITORY_COLS, "SalesTerritoryKey")
