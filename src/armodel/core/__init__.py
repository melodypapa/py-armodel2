"""Core utilities for AUTOSAR model handling.

This module contains non-model core functionality like version detection
and validation logic. Model classes are generated from mapping.json.
"""

from .version import SchemaVersionManager

__all__ = [
    "SchemaVersionManager",
]
