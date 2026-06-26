"""
Tests for the friendly ``aggregations`` endpoint (resolved view over AlternateOf).

The aggregations fixture is a Packt sample (submodule); the tests skip when the
submodule is not initialised. An aggregation-free model is exercised against the
rls fixture (conftest.py) to assert the empty shape.
"""
import os

import pandas as pd
import pytest

from pbixray import PBIXRay

SAMPLES_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'samples'))
_AGG_PBIX = os.path.join(
    SAMPLES_ROOT,
    'Expert-Data-Modeling-with-Power-BI', 'Chapter10',
    'Chapter 10, Aggregations on DirectQurey Data Sources.pbix',
)

_AGG_COLUMNS = [
    'AggregationTable', 'AggregationColumn', 'Summarization',
    'DetailTable', 'DetailColumn',
]


@pytest.fixture(scope="module")
def aggregations_model():
    if not os.path.exists(_AGG_PBIX):
        pytest.skip("Expert-Data-Modeling-with-Power-BI submodule not initialised")
    return PBIXRay(_AGG_PBIX)


def test_aggregations_shape(aggregations_model):
    df = aggregations_model.aggregations
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert list(df.columns) == _AGG_COLUMNS


def test_aggregations_sum_of_column(aggregations_model):
    df = aggregations_model.aggregations
    row = df[df['AggregationColumn'] == 'Sales_Sum'].iloc[0]
    assert row['Summarization'] == 'Sum'
    assert row['DetailTable'] == 'FactInternetSales'
    assert row['DetailColumn'] == 'SalesAmount'


def test_aggregations_count_rows(aggregations_model):
    df = aggregations_model.aggregations
    row = df[df['AggregationColumn'] == 'Sales_Count'].iloc[0]
    assert row['Summarization'] == 'Count'
    assert row['DetailTable'] == 'FactInternetSales'
    assert pd.isna(row['DetailColumn'])


def test_aggregations_groupby_resolves_own_detail_table(aggregations_model):
    # GroupBy keys must resolve to their own detail table (Date), not the
    # measures' table — verifies DetailTable comes from the base column's TableID.
    df = aggregations_model.aggregations
    row = df[df['AggregationColumn'] == 'CalendarYear'].iloc[0]
    assert row['Summarization'] == 'GroupBy'
    assert row['DetailTable'] == 'DimDate'
    assert row['DetailColumn'] == 'CalendarYear'


def test_aggregations_empty_model(rls_model):
    df = rls_model.aggregations
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert list(df.columns) == _AGG_COLUMNS
