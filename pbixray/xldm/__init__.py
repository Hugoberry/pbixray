"""
XLDM ( eXceL Data Model) package for parsing Microsoft Analysis Services objects.

This package provides classes for parsing and working with various Analysis Services
XML definitions including databases, cubes, data sources, dimensions, and more.

The package has been refactored to eliminate duplicate class definitions and provide
a common base for shared functionality.
"""

# Common base classes and utilities
from .common import (
    Annotation,
    Source, 
    MajorObject,
    ProcessableObject,
    XmlLoadMixin,
    parse_int_or_default,
    parse_bool_from_text,
    find_text_with_namespace
)

# Namespace utilities
from .namespaces import (
    STANDARD_NAMESPACES,
    SIMPLE_NAMESPACES,
    XmlDefinitionBase,
    ParentObject,
    ObjectDefinitionBase,
    get_namespaced_element_text,
    parse_storage_mode_with_namespace,
    create_definition_loader
)

# Specific object definitions
from .cube import Cube, CubXmlLoad
from .data_source import DataSource, RelationalDataSource, OlapDataSource, PushedDataSource, DataSourceDefinition
from .data_source_view import DataSourceView, DataSourceViewDefinition
from .database import Database, DatabaseXmlLoad

# Import other XLDM classes that may be used
try:
    from .dimension import *
except ImportError:
    pass

try:
    from .measure_group import *
except ImportError:
    pass

try:
    from .partition import *
except ImportError:
    pass

try:
    from .mdx_script import *
except ImportError:
    pass

try:
    from .xmobject import *
except ImportError:
    pass

__all__ = [
    # Common classes
    'Annotation',
    'Source', 
    'MajorObject',
    'ProcessableObject',
    'XmlLoadMixin',
    
    # Namespace utilities
    'STANDARD_NAMESPACES',
    'SIMPLE_NAMESPACES',
    'XmlDefinitionBase',
    'ParentObject',
    'ObjectDefinitionBase',
    
    # Specific objects
    'Cube',
    'CubXmlLoad',
    'DataSource',
    'RelationalDataSource', 
    'OlapDataSource',
    'PushedDataSource',
    'DataSourceDefinition',
    'DataSourceView',
    'DataSourceViewDefinition',
    'Database',
    'DatabaseXmlLoad',
    
    # Utility functions
    'parse_int_or_default',
    'parse_bool_from_text',
    'find_text_with_namespace',
    'get_namespaced_element_text',
    'parse_storage_mode_with_namespace',
    'create_definition_loader'
]