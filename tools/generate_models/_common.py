"""Common utility functions with no dependencies.

This module contains basic utility functions that can be safely imported
by other modules without causing circular import issues.
"""

import re
from typing import Optional, Tuple


def to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case.

    Args:
        name: CamelCase string

    Returns:
        snake_case string
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def get_python_identifier(name: str) -> Tuple[str, Optional[str]]:
    """Convert a name to a valid Python identifier, handling keywords.

    Args:
        name: Name to convert (e.g., AUTOSAR attribute name)

    Returns:
        Tuple of (python_identifier, xml_tag_name)
        - python_identifier: Valid Python identifier (with underscore appended if keyword)
        - xml_tag_name: XML tag name to use (None if same as identifier, otherwise uppercase form)

    Examples:
        "shortName" -> ("short_name", None)
        "class" -> ("class_", "CLASS")
        "from" -> ("from_", "FROM")
    """
    # Python keywords that cannot be used as attribute names
    python_keywords = {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    }

    snake_name = to_snake_case(name)

    # Check if the name is a Python keyword
    if snake_name in python_keywords:
        # Append underscore and use uppercase original as XML tag
        return f"{snake_name}_", name.upper()
    else:
        # Not a keyword, use as-is
        return snake_name, None


def get_python_identifier_with_ref(name: str, is_ref: bool = False, multiplicity: str = "1") -> str:
    """Convert AUTOSAR identifier to Python identifier, handling reference suffix.

    Args:
        name: AUTOSAR identifier (e.g., "SHORT-NAME" or "SW-ADDR-METHOD")
        is_ref: Whether this is a reference type (adds '_ref' suffix if not present)
        multiplicity: Multiplicity of the attribute (e.g., "*", "0..1", "1")

    Returns:
        Python identifier (e.g., "short_name" or "sw_addr_method_ref")

    Examples:
        >>> get_python_identifier_with_ref("SHORT-NAME", False)
        "short_name"
        >>> get_python_identifier_with_ref("SW-ADDR-METHOD", True)
        "sw_addr_method_ref"
        >>> get_python_identifier_with_ref("indications", True, "*")
        "indication_refs"  # Singularize, then add plural s and _ref
    """
    # Convert to snake_case first
    identifier = to_snake_case(name)

    # If it's a reference, handle the suffix
    if is_ref:
        if not identifier.endswith("_ref"):
            # For list types (multiplicity "*"), singularize first
            # This ensures "indications" becomes "indication" before adding "s" + "_ref"
            if multiplicity in ["*", "0..*"]:
                # Remove trailing 's' to singularize (simple heuristic)
                if identifier.endswith("s"):
                    identifier = identifier[:-1]
                # Add plural 's' and '_ref' suffix (combined as '_refs')
                identifier = f"{identifier}_refs"
            else:
                # For single items, just add '_ref'
                identifier = f"{identifier}_ref"

    # Check if the resulting identifier is a Python keyword
    python_keywords = {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    }

    # If it's a keyword, append underscore
    if identifier in python_keywords:
        identifier = f"{identifier}_"

    return identifier
