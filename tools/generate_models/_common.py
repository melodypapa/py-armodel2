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


def get_python_identifier_with_ref(name: str, is_ref: bool = False, multiplicity: str = "1", kind: str = "attribute") -> str:
    """Convert AUTOSAR identifier to Python identifier, handling reference suffix.

    Args:
        name: AUTOSAR identifier (e.g., "SHORT-NAME" or "SW-ADDR-METHOD")
        is_ref: Whether this is a reference type (adds suffix if not present)
        multiplicity: Multiplicity of the attribute (e.g., "*", "0..1", "1")
        kind: Kind of attribute (e.g., "attribute", "ref", "tref", "iref")

    Returns:
        Python identifier (e.g., "short_name" or "sw_addr_method_ref" or "inner_port_iref")

    Examples:
        >>> get_python_identifier_with_ref("SHORT-NAME", False)
        "short_name"
        >>> get_python_identifier_with_ref("SW-ADDR-METHOD", True)
        "sw_addr_method_ref"
        >>> get_python_identifier_with_ref("indications", True, "*")
        "indication_refs"  # Singularize, then add plural s and _ref
        >>> get_python_identifier_with_ref("innerPort", True, "0..1", "iref")
        "inner_port_iref"
    """
    # Convert to snake_case first
    identifier = to_snake_case(name)

    # If it's a reference, handle the suffix
    if is_ref:
        # Determine the suffix based on kind
        # iref kind uses _iref suffix, other reference kinds use _ref suffix
        suffix = "_iref" if kind == "iref" else "_ref"
        
        if not identifier.endswith(suffix):
            # For list types (multiplicity "*"), singularize then add plural suffix
            if multiplicity in ["*", "0..*"]:
                # Remove trailing 's' to singularize (simple heuristic)
                if identifier.endswith("s"):
                    identifier = identifier[:-1]
                # Add plural suffix (e.g., _refs or _irefs)
                # For ref kind: singular + _refs (not singular + s + _ref)
                # For iref kind: singular + _irefs
                identifier = f"{identifier}{suffix}s"
            else:
                # For single items, just add the suffix
                identifier = f"{identifier}{suffix}"

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


def to_autosar_xml_format(name: str) -> str:
    """Convert camelCase name to AUTOSAR XML format (UPPER-CASE-WITH-HYPHENS).

    This function converts camelCase enum literal names to the AUTOSAR XML format
    which uses uppercase letters with hyphens between words.

    Args:
        name: camelCase string (e.g., "readOnly", "notAccessible", "readWrite")

    Returns:
        UPPER-CASE-WITH-HYPHENS string (e.g., "READ-ONLY", "NOT-ACCESSIBLE", "READ-WRITE")

    Examples:
        >>> to_autosar_xml_format("readOnly")
        "READ-ONLY"
        >>> to_autosar_xml_format("notAccessible")
        "NOT-ACCESSIBLE"
        >>> to_autosar_xml_format("readWrite")
        "READ-WRITE"
        >>> to_autosar_xml_format("presentationContinuous")
        "PRESENTATION-CONTINUOUS"
    """
    # Insert hyphens before uppercase letters and convert to uppercase
    result = ""
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result += "-"
        result += char.upper()
    return result
