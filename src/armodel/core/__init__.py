"""Core utilities for AUTOSAR model handling.

This module contains non-model core functionality like version detection
and validation logic. Model classes are generated from mapping.json.
"""

from armodel.core.version import detect_schema_version, get_default_version

__all__ = ["detect_schema_version", "get_default_version"]
