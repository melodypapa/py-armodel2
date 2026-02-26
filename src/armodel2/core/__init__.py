"""Core utilities for AUTOSAR model handling.

This module contains non-model core functionality like version detection
and validation logic. Model classes are generated from mapping.json.
"""

from armodel2.core.global_settings import GlobalSettingsManager, BuilderValidationMode
from armodel2.core.version import SchemaVersionManager

__all__ = [
    "GlobalSettingsManager",
    "BuilderValidationMode",
    "SchemaVersionManager",
]
