"""Nullable value-encoded (hidx) columns — AdventureWorksDW2017 ground truth.

Value-encoded columns carry no dictionary: a row's value is reconstructed
arithmetically as ``(data_id + BaseId) / Magnitude``. A segment that contains
nulls bases its bit-packed ids one below the column minimum and reserves that
slot for the null itself — the same convention the dictionary path handles
(PR #52), which the hidx path did not apply. Untreated, every value in such a
column is one granularity step too high and the null decodes as an ordinary
number.

Expectations come from the source these models were built from, not from
decoder output: ``data/adventure-works-dw/*.csv`` are the ``Product`` and
``Promotions`` sheets of ``AdventureWorksDW2017.xlsx`` (the
``samples/Expert-Data-Modeling-with-Power-BI`` submodule), projected to the
columns used here:

    SRC = ("samples/Expert-Data-Modeling-with-Power-BI/AdventureWorksDW2017(xlsx)/"
           "AdventureWorksDW2017.xlsx")
    pd.read_excel(SRC, sheet_name="Product")[[
        "ProductKey", "EnglishProductName",
        "StandardCost", "ListPrice", "DealerPrice", "Weight",
        "SafetyStockLevel", "ReorderPoint", "DaysToManufacture",
    ]].to_csv("data/adventure-works-dw/Product.csv", index=False)
    pd.read_excel(SRC, sheet_name="Promotions")[[
        "PromotionKey", "PromotionAlternateKey", "DiscountPct", "MinQty", "MaxQty",
    ]].to_csv("data/adventure-works-dw/Promotion.csv", index=False)

Two models read the same source tables, so both are checked:

  * ``Adventure Works Internet Sales Database.abf`` — ``Product`` stores
    Standard Cost / List Price / Dealer Price (Currency, Magnitude 1) and
    Weight (Float64, Magnitude 100) as value-encoded.
  * ``Adventure Works, Internet Sales.pbix`` — ``Product.List Price``
    (Float64, Magnitude 10000), ``Product.Weight`` (typed Int64 in that model,
    so the source is compared rounded) and ``Promotion.MaxQty``.

``Promotion`` is the tightest case: 16 rows in which ``MaxQty`` is nullable and
``MinQty`` / ``DiscountPct`` / ``PromotionAlternateKey`` are null-free — all
four value-encoded, so the null-free three pin the blast radius from inside the
same table.

Row order is storage order, so every comparison is keyed off the table's key
column rather than position.
"""
import os

import numpy as np
import pandas as pd
import pytest

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
SRC_CSV_DIR = os.path.join(DATA_DIR, "adventure-works-dw")

# Source null counts, straight out of the CSVs — the numbers each decode has to
# land on. Stated here so a decode that silently drops nulls is visible in the
# failure message rather than hidden inside a frame comparison.
PRODUCT_NULLS = {"StandardCost": 211, "ListPrice": 211, "DealerPrice": 211, "Weight": 324}
PROMOTION_MAXQTY_NULLS = 12
PRODUCT_ROWS = 606
PROMOTION_ROWS = 16


def _src(name):
    # Same convention as test_work_tables._csv: only a genuinely empty cell is
    # null (na_values=['']), and no string is coerced to NaN on pandas' default
    # sentinel list (keep_default_na=False). The blanks are the expectation
    # under test, so they must survive the read verbatim.
    return pd.read_csv(os.path.join(SRC_CSV_DIR, name), keep_default_na=False, na_values=[''])


@pytest.fixture(scope="module")
def src_product():
    df = _src("Product.csv").set_index("ProductKey")
    assert len(df) == PRODUCT_ROWS
    # Guard the fixture itself: if the CSV ever loses its blanks, the tests
    # below would pass against a decoder that never produces nulls.
    assert {c: int(df[c].isna().sum()) for c in PRODUCT_NULLS} == PRODUCT_NULLS
    return df


@pytest.fixture(scope="module")
def src_promotion():
    df = _src("Promotion.csv").set_index("PromotionKey")
    assert len(df) == PROMOTION_ROWS
    assert int(df["MaxQty"].isna().sum()) == PROMOTION_MAXQTY_NULLS
    assert int(df["MinQty"].isna().sum()) == 0
    return df


def _numeric(series):
    """Decoded column as float64, nulls preserved.

    Currency columns come back as ``Decimal`` in object dtype and integer ones
    as nullable ``Int64``; both compare cleanly once coerced.
    """
    return pd.to_numeric(series, errors="coerce").astype(float)


def _assert_column_matches(actual, expected, label):
    """Every row equal (or null on both sides) — values *and* null placement."""
    got = _numeric(actual)
    exp = expected.astype(float).reindex(got.index)
    assert not exp.isna().all(), f"{label}: expectation did not align on the key"
    both_null = got.isna() & exp.isna()
    close = (got - exp).abs() < 1e-6
    bad = ~(both_null | close)
    assert not bad.any(), (
        f"{label}: {int(bad.sum())} of {len(got)} rows differ from source; "
        f"first few:\n{pd.DataFrame({'decoded': got[bad], 'source': exp[bad]}).head(10)}"
    )
    # Null placement is asserted by the row-wise comparison above; restate the
    # count so a decode that produces no nulls at all fails loudly here.
    assert int(got.isna().sum()) == int(exp.isna().sum()), (
        f"{label}: decoded {int(got.isna().sum())} nulls, source has "
        f"{int(exp.isna().sum())}"
    )


# ---------------------------------------------------------------------------
# ABF — Product has four nullable value-encoded columns
# ---------------------------------------------------------------------------

ABF_PRODUCT_MAP = {
    "Standard Cost": "StandardCost",
    "List Price": "ListPrice",
    "Dealer Price": "DealerPrice",
    "Weight": "Weight",
}


@pytest.fixture(scope="module")
def abf_product(internet_sales_abf_model):
    return internet_sales_abf_model.get_table("Product").set_index("Product Id")


@pytest.mark.parametrize("decoded_col,source_col", sorted(ABF_PRODUCT_MAP.items()))
def test_abf_nullable_value_encoded_matches_source(
    abf_product, src_product, decoded_col, source_col
):
    assert len(abf_product) == PRODUCT_ROWS
    _assert_column_matches(
        abf_product[decoded_col], src_product[source_col], f"abf Product.{decoded_col}"
    )


def test_abf_nullable_value_encoded_null_counts(abf_product):
    """The nulls exist at all — the half of the bug that fabricated numbers."""
    counts = {
        decoded: int(_numeric(abf_product[decoded]).isna().sum())
        for decoded in ABF_PRODUCT_MAP
    }
    assert counts == {
        "Standard Cost": 211,
        "List Price": 211,
        "Dealer Price": 211,
        "Weight": 324,
    }


def test_abf_product_null_free_columns_match_source(abf_product, src_product):
    """Same table, columns the change must not touch."""
    for decoded_col, source_col in [
        ("Safety Stock Level", "SafetyStockLevel"),
        ("Reorder Point", "ReorderPoint"),
        ("Days To Manufacture", "DaysToManufacture"),
    ]:
        _assert_column_matches(
            abf_product[decoded_col], src_product[source_col],
            f"abf Product.{decoded_col}",
        )
        assert int(abf_product[decoded_col].isna().sum()) == 0
    names = abf_product["Product Name"].astype(str)
    expected_names = src_product["EnglishProductName"].astype(str).reindex(names.index)
    assert (names == expected_names).all()


def test_abf_multi_partition_null_free_value_encoded_stays_null_free(
    internet_sales_abf_model,
):
    """`Internet Sales.Margin` is value-encoded across 5 partitions with no
    nulls in any segment: the null branch must not fire for it."""
    margin = internet_sales_abf_model.get_table("Internet Sales", columns=["Margin"])
    assert len(margin) == 60_398
    assert int(margin["Margin"].isna().sum()) == 0


# ---------------------------------------------------------------------------
# Multi-segment control
#
# No sample model has a nullable value-encoded column spanning more than one
# segment, so that combination is not exercised here (see the PR notes).
# `Mix.A` is the closest available: value-encoded over 3 segments of one
# partition, null-free by construction, and it must stay that way.
# ---------------------------------------------------------------------------

MIX_ROWS = 2 * 2**20 + 1


def test_mix_multi_segment_null_free_value_encoded_unchanged(mix_model):
    """`Mix.A` is `{1..2097153}` per the M script in test_nullable_segments."""
    a = mix_model.get_table("Mix", columns=["A"])["A"]
    assert len(a) == MIX_ROWS
    assert int(a.isna().sum()) == 0
    assert np.array_equal(np.sort(a.astype("int64").to_numpy()), np.arange(1, MIX_ROWS + 1))


# ---------------------------------------------------------------------------
# PBIX — same source tables, different storage parameters
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def pbix_product(adventure_works_model):
    return adventure_works_model.get_table("Product").set_index("ProductKey")


def test_pbix_list_price_matches_source(pbix_product, src_product):
    """Float64 / Magnitude 10000 — the granularity-step half of the bug."""
    assert len(pbix_product) == PRODUCT_ROWS
    _assert_column_matches(
        pbix_product["List Price"], src_product["ListPrice"], "pbix Product.List Price"
    )


def test_pbix_weight_matches_rounded_source(pbix_product, src_product):
    """This model types Weight as a whole number, so the source rounds to it
    (half-to-even, as Power BI stored it); the nulls still have to line up."""
    expected = np.round(src_product["Weight"].astype(float))
    _assert_column_matches(pbix_product["Weight"], expected, "pbix Product.Weight")
    assert int(_numeric(pbix_product["Weight"]).isna().sum()) == PRODUCT_NULLS["Weight"]


# ---------------------------------------------------------------------------
# Promotion — nullable and null-free value-encoded columns side by side
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def pbix_promotion(adventure_works_model):
    return adventure_works_model.get_table("Promotion").set_index("PromotionKey")


def test_promotion_nullable_value_encoded_matches_source(pbix_promotion, src_promotion):
    assert len(pbix_promotion) == PROMOTION_ROWS
    _assert_column_matches(
        pbix_promotion["MaxQty"], src_promotion["MaxQty"], "pbix Promotion.MaxQty"
    )
    assert int(_numeric(pbix_promotion["MaxQty"]).isna().sum()) == PROMOTION_MAXQTY_NULLS


@pytest.mark.parametrize("column", ["MinQty", "DiscountPct", "PromotionAlternateKey"])
def test_promotion_null_free_value_encoded_matches_source(
    pbix_promotion, src_promotion, column
):
    """Value-encoded columns without nulls, in the table that has a nullable
    one — these must decode exactly as before, nulls included (there are none).
    """
    _assert_column_matches(
        pbix_promotion[column], src_promotion[column], f"pbix Promotion.{column}"
    )
    assert int(_numeric(pbix_promotion[column]).isna().sum()) == 0


def test_promotion_iter_table_agrees_with_get_table(adventure_works_model, src_promotion):
    """`iter_table` shares `_ColumnDecoder`, so it must see the same nulls."""
    chunks = list(
        adventure_works_model.iter_table("Promotion", columns=["PromotionKey", "MaxQty"])
    )
    streamed = pd.concat(chunks).set_index("PromotionKey")
    _assert_column_matches(
        streamed["MaxQty"], src_promotion["MaxQty"], "iter_table Promotion.MaxQty"
    )
