"""Common utility functions with no dependencies.

This module contains basic utility functions that can be safely imported
by other modules without causing circular import issues.
"""

import re


def to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case.

    Args:
        name: CamelCase string

    Returns:
        snake_case string
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def get_python_identifier(name: str) -> tuple[str, str]:
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
