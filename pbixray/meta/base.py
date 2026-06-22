from typing import Protocol

import pandas as pd


class MetadataSource(Protocol):
    """Uniform view over a container's metadata, regardless of whether it
    originated from a SQLite database (pbix) or a set of XML documents (xlsx).

    Implementations must normalize ``schema_df`` so callers never need to know
    the source format. Required columns:

    * ``TableName``, ``ColumnName`` — identification
    * ``Cardinality`` — distinct value count
    * ``Dictionary``, ``HIDX``, ``IDF`` — storage file refs (may be None);
      ``IDF`` is the first partition's data file
    * ``IDFs`` — ordered list of per-partition IDF data files (one entry for
      single-partition columns); the decoder concatenates them in this order
    * ``ModifiedTime``, ``StructureModifiedTime``
    * ``PandasDataType`` — pandas dtype string ready for ``astype`` (e.g.
      ``"Int64"``, ``"string"``, ``"datetime64[ns]"``)
    * ``SemanticType`` — one of ``"Date"``, ``"Currency"``, ``"Other"``; used
      by the decoder for special-case post-processing
    """

    schema_df: pd.DataFrame
    dax_tables_df: pd.DataFrame
    dax_measures_df: pd.DataFrame
    dax_columns_df: pd.DataFrame
    relationships_df: pd.DataFrame
    m_df: pd.DataFrame
    m_parameters_df: pd.DataFrame
    rls_df: pd.DataFrame
    metadata_df: pd.DataFrame
