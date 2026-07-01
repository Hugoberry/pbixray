"""
Tests for the two friendly security/metadata roll-ups:

  * ``ols`` (+ raw ``tmschema_column_permissions``) — object-level security,
    exercised against ``ols-sample-report.pbix``.
  * ``perspectives`` — consolidated perspective membership, exercised against
    the AdventureWorks Internet Sales ``.abf`` (its sole perspective covers
    6 tables / 82 columns / 19 measures).

Fixtures live in conftest.py.
"""
import pandas as pd

_OLS_COLUMNS = ['RoleName', 'TableName', 'ColumnName', 'Scope', 'Permission']
_PERSPECTIVES_COLUMNS = [
    'PerspectiveName', 'ObjectType', 'TableName', 'ObjectName', 'IncludeAll',
]


# ---------------------------------------------------------------------------
# Object-level security
# ---------------------------------------------------------------------------

def test_ols_resolved(ols_model):
    df = ols_model.ols
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == _OLS_COLUMNS
    assert not df.empty

    # Column-level OLS: three Customers columns hidden (MetadataPermission=None).
    cols = df[df["Scope"] == "Column"]
    hidden = set(cols.loc[cols["TableName"] == "Customers", "ColumnName"])
    assert {"Address", "ContactInformation", "PreferredContactMethod"} <= hidden
    assert (cols["Permission"] == "None").all()
    assert cols["ColumnName"].notna().all()

    # Table-level OLS: the Reviews table is hidden, with no column attached.
    tables = df[df["Scope"] == "Table"]
    assert (tables["TableName"] == "Reviews").any()
    assert tables["ColumnName"].isna().all()


def test_ols_excludes_plain_rls(ols_model):
    # Roles that only carry a row filter (MetadataPermission=Default) must not
    # appear as OLS rows — they belong to `rls`. The Customers table is filtered
    # for several roles but only surfaces here via its hidden columns, never as a
    # Scope='Table' row.
    df = ols_model.ols
    customer_tables = df[(df["Scope"] == "Table") & (df["TableName"] == "Customers")]
    assert customer_tables.empty


def test_ols_empty_shape(rls_model):
    # A model with row-level security but no object-level security returns an
    # empty frame with the canonical columns (not a column-less frame).
    df = rls_model.ols
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert list(df.columns) == _OLS_COLUMNS


def test_tmschema_column_permissions(ols_model):
    df = ols_model.tmschema_column_permissions
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert {"RoleName", "TableName", "ColumnName", "MetadataPermission"} <= set(df.columns)


def test_tmschema_column_permissions_empty(rls_model):
    df = rls_model.tmschema_column_permissions
    assert isinstance(df, pd.DataFrame)
    assert df.empty


# ---------------------------------------------------------------------------
# Perspectives (consolidated membership)
# ---------------------------------------------------------------------------

def test_perspectives_membership(internet_sales_abf_model):
    df = internet_sales_abf_model.perspectives
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == _PERSPECTIVES_COLUMNS
    assert not df.empty

    counts = df.groupby("ObjectType").size().to_dict()
    assert counts.get("Table") == 6
    assert counts.get("Column") == 82
    assert counts.get("Measure") == 19

    # IncludeAll is populated only for Table rows.
    assert df.loc[df["ObjectType"] == "Table", "IncludeAll"].notna().all()
    assert df.loc[df["ObjectType"] != "Table", "IncludeAll"].isna().all()

    # For Table rows, ObjectName mirrors TableName.
    tables = df[df["ObjectType"] == "Table"]
    assert (tables["TableName"] == tables["ObjectName"]).all()


def test_perspectives_empty_shape(abc_model):
    # A model with no perspectives returns an empty frame with canonical columns.
    df = abc_model.perspectives
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert list(df.columns) == _PERSPECTIVES_COLUMNS
