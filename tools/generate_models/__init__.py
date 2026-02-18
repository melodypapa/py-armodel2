"""Generate AUTOSAR model classes, enums, and primitives.

This package provides code generation tools for creating Python model classes
from AUTOSAR JSON schema definitions.
"""

from .main import generate_all_models
from .parsers import (
    load_all_package_data,
    load_skip_list,
    parse_enum_json,
    parse_hierarchy_json,
    parse_mapping_json,
    parse_primitive_json,
)
from .generators import (
    generate_builder_code,
    generate_class_code,
    generate_enum_code,
    generate_enumeration_type_base,
    generate_primitive_code,
    generate_primitive_type_base,
)
from .utils import (
    create_directory_structure,
    to_snake_case,
)
from ._common import get_python_identifier

__all__ = [
    # Main entry point
    "generate_all_models",
    # Parsers
    "load_all_package_data",
    "load_skip_list",
    "parse_enum_json",
    "parse_hierarchy_json",
    "parse_mapping_json",
    "parse_primitive_json",
    # Generators
    "generate_builder_code",
    "generate_class_code",
    "generate_enum_code",
    "generate_enumeration_type_base",
    "generate_primitive_code",
    "generate_primitive_type_base",
    # Utils
    "create_directory_structure",
    "to_snake_case",
    "get_python_identifier",
]
