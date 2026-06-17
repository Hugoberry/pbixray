"""
Tests for the Power Query ``DataMashup`` parser ([MS-QDEFF]).

The DirectQuery fixture keeps its queries and two parameters only in the
``DataMashup`` part (native-SQL partitions, empty AS ``Expression`` table), so it
exercises both the binary decoder and the ``Section1.m`` tokenizer end to end.
"""
import pandas as pd
import pytest

from pbixray import PBIXRay, DataMashupError
from pbixray.mashup.section_document import parse_section_document


# ---------------------------------------------------------------------------
# End-to-end via the public API
# ---------------------------------------------------------------------------

def test_mashup_queries_lists_parameters_and_queries(directquery_model):
    df = directquery_model.mashup_queries
    params = df[df["IsParameter"]]
    assert set(params["Name"]) == {"ServerName", "DatabaseName"}
    # Every table query is present as a non-parameter member.
    queries = set(df[~df["IsParameter"]]["Name"])
    assert {"DimDate", "DimProduct", "DimReseller", "FactResellerSales"} <= queries


def test_parameter_metadata_extracted(directquery_model):
    df = directquery_model.mashup_queries.set_index("Name")
    db = df.loc["DatabaseName"]
    assert db["Type"] == "Text"
    assert db["DefaultValue"] == "AdventureWorksDW2012"
    assert db["AllowedValues"] == ["AdventureWorksDW2012", "AdventureWorksDW2014"]


def test_data_mashup_object(directquery_model):
    mashup = directquery_model.data_mashup
    assert mashup is not None
    assert mashup.version == 0
    assert {p.name for p in mashup.parameters} == {"ServerName", "DatabaseName"}
    assert "section Section1" in mashup.section_m


def test_power_query_and_m_parameters_unchanged(directquery_model):
    # Mashup support is additive: the SQLite-backed views are untouched.
    assert isinstance(directquery_model.power_query, pd.DataFrame)
    assert isinstance(directquery_model.m_parameters, pd.DataFrame)


def test_model_without_mashup(sales_returns_model):
    assert sales_returns_model.data_mashup is None
    df = sales_returns_model.mashup_queries
    assert list(df.columns) == [
        "Name", "Kind", "IsParameter", "Expression",
        "Type", "DefaultValue", "AllowedValues",
    ]
    assert len(df) == 0


# ---------------------------------------------------------------------------
# Section1.m tokenizer unit tests
# ---------------------------------------------------------------------------

def test_tokenizer_basic_member():
    queries = parse_section_document("section Section1;\nshared Query1 = let Source = 1+1 in Source;")
    assert len(queries) == 1
    assert queries[0].name == "Query1"
    assert queries[0].expression == "let Source = 1+1 in Source"
    assert queries[0].is_parameter is False


def test_tokenizer_parameter_with_meta():
    doc = 'section Section1;\nshared P = "v" meta [IsParameterQuery=true, Type="Text", DefaultValue="d"];'
    q = parse_section_document(doc)[0]
    assert q.is_parameter
    assert q.param_type == "Text"
    assert q.default_value == "d"
    assert q.expression == '"v"'


def test_tokenizer_respects_strings_comments_and_inner_meta():
    doc = (
        "section Section1;\n"
        "// a comment with shared = fake;\n"
        'shared #"My Query" = let Source = "a;b;c", X = Source meta [Foo=1] in X;\n'
        "/* block ; [brackets] shared */\n"
        "shared Plain = 1+1;\n"
    )
    by_name = {q.name: q for q in parse_section_document(doc)}
    assert set(by_name) == {"My Query", "Plain"}
    # The inner `meta` operator must stay part of the expression.
    assert "meta [Foo=1] in X" in by_name["My Query"].expression
    assert by_name["My Query"].is_parameter is False


def test_tokenizer_handles_empty_input():
    assert parse_section_document("") == []
    assert parse_section_document(None) == []


def test_malformed_mashup_raises():
    with pytest.raises(DataMashupError):
        PBIXRay  # ensure import side-effect free
        from pbixray.mashup import parse_data_mashup
        parse_data_mashup(b"\x00\x01")  # too short / truncated
