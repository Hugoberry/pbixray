# PBIXRay
[![Downloads](https://static.pepy.tech/badge/pbixray)](https://pepy.tech/project/pbixray)
## Overview

PBIXRay is a Python library designed to parse and analyze PBIX files, which are used with Microsoft Power BI. This library provides a straightforward way to extract valuable information from PBIX files, including tables, metadata, Power Query code, and more.

## Installation

Before using PBIXRay, ensure you have the following Python modules installed: `apsw`, `kaitaistruct`, and `pbixray`. You can install them using pip:

```bash
pip install pbixray
```

## Getting Started
To start using PBIXRay, import the module and initialize it with the path to your PBIX file:
```python
from pbixray import PBIXRay

model = PBIXRay('path/to/your/file.pbix')
```

## Features and Usage
### Tables
To list all tables in the model:
```python
tables = model.tables
print(tables)
```
### Metadata
To get metadata about the Power BI configuration used during model creation:
```python
metadata = model.metadata
print(metadata)
```
### Power Query
To display all M/Power Query code used for data transformation, in a dataframe with `TableName` and `Expression` columns:
```python
power_query = model.power_query
print(power_query)
```
### Model Size
To find out the model size in bytes:
```python
size = model.size
print(f"Model size: {size} bytes")
```
### DAX Calculated Tables
To view DAX calculated tables in a dataframe with `TableName` and `Expression` columns:
```python
dax_tables = model.dax_tables
print(dax_tables)
```
### DAX Measures
To access DAX measures in a dataframe with `TableName`, `Name`, `Expression`, `DisplayFolder`, and `Description` columns:
```python
dax_measures = model.dax_measures
print(dax_measures)
```
### Schema
To get details about the data model schema and column types in a dataframe with `TableName`, `ColumnName`, and `PandasDataType` columns:
```python
schema = model.schema
print(schema)
```
### Get Table Contents
To retrieve the contents of a specified table:
```python
table_name = 'YourTableName'
table_contents = model.get_table(table_name)
print(table_contents)
```
### Statistics
To get statistics about the model, including column cardinality and byte sizes of dictionary, hash index, and data components, in a dataframe with columns `TableName`, `ColumnName`, `Cardinality`, `Dictionary`, `HashIndex`, and `DataSize`:
```python
statistics = model.statistics
print(statistics)
```
