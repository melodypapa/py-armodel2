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


def get_python_identifier_with_ref(
    name: str, is_ref: bool = False, multiplicity: str = "1", kind: str = "attribute"
) -> str:
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

    # Pluralize for multiplicity "*" or "0..*" (for non-reference attributes)
    if multiplicity in ("*", "0..*") and not is_ref:
        identifier = to_plural(identifier)

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


def to_singular(name: str) -> str:
    """Convert plural name to singular form.

    Rules applied in order:
    1. Special cases (e.g., 'values' -> 'value')
    2. 'ies' -> 'y' (entities -> entity)
    3. 'ses' -> 's' (buses -> bus)
    4. 'ves' -> 'f' (knives -> knife) or special (leaves -> leaf)
    5. 'es' ending with specific patterns
    6. 's' -> '' (elements -> element)

    Args:
        name: Plural name to convert

    Returns:
        Singular form of the name
    """
    # Special cases for common AUTOSAR and irregular plurals
    special_cases = {
        "values": "value",
        "axes": "axis",
        "indices": "index",
        "bases": "base",
        "classes": "class",
        "types": "type",
        "packages": "package",
        "variables": "variable",
        "libraries": "library",
        "entries": "entry",
        "bodies": "body",
        "leaves": "leaf",
        "knives": "knife",
        "lives": "life",
        "dies": "die",
    }
    if name in special_cases:
        return special_cases[name]

    # Handle 'ies' -> 'y'
    if name.endswith("ies"):
        return name[:-3] + "y"

    # Handle 'ves' -> 'f' or 'fe' (wives -> wife, calves -> calf)
    if name.endswith("ves"):
        return name[:-3] + "f"

    # Handle 'es' - check if removing 'es' leaves a valid ending
    if name.endswith("es"):
        without_s = name[:-1]   # Remove just 's'
        without_es = name[:-2]  # Remove 'es'

        # For words ending in 'ses': need to determine if we keep 'e' or not
        if name.endswith("ses"):
            # buses -> bus (remove 'es'), but houses -> house (remove 's')
            # Pattern check: what does without_es look like?
            # without_es for houses = hous, we need to add 'e' -> house
            # without_es for buses = bus, this is correct as-is
            # Check if without_es ends with vowel+'s' sound pattern that needs 'e'
            # hous -> house (need e), bus -> bus (correct)
            # The key: words where without_es ends with consonant+s and we need to add e
            # vs words where without_es is already complete
            if without_es.endswith(('ous', 'ase', 'ise', 'ose')):
                # houses -> house, cases -> case
                return without_s
            else:
                # buses -> bus, gases -> gas
                return without_es

        # For words ending in 'xes', 'zes', 'ches', 'shes' (box, size, church, bush)
        if name.endswith(("xes", "zes", "ches", "shes")):
            return without_es

        # Default for other 'es' endings: just remove 's'
        # This handles packages -> package, values -> value, ages -> age
        return without_s

    # Handle simple 's' -> ''
    if name.endswith("s"):
        return name[:-1]

    return name


def to_plural(name: str) -> str:
    """Convert singular name to plural form for Python variable names.

    Args:
        name: Singular name to convert

    Returns:
        Plural form of the name
    """
    # Irregular plurals - must match to_singular special cases
    special_cases = {
        "body": "bodies",
        "entity": "entities",
        "entry": "entries",
        "leaf": "leaves",
        "knife": "knives",
        "calf": "calves",
        "life": "lives",
        "die": "dies",
        "value": "values",
        "axis": "axes",
        "index": "indices",
        "base": "bases",
        "class": "classes",
        "type": "types",
        "package": "packages",
        "variable": "variables",
        "library": "libraries",
        # Common AUTOSAR abbreviations that should simply add 'S' for pluralization
        # These abbreviations should NOT follow the 'f' -> 'ves' rule
        "def": "defs",
        "ref": "refs",
        "conf": "confs",
        "calib": "calibs",
        "swc": "swcs",
        "bsw": "bsws",
        "hmi": "hmis",
        "spec": "specs",
        "cfg": "cfgs",
        "prof": "profs",
        "buf": "bufs",
        "brief": "briefs",
        "chef": "chefs",
    }
    if name in special_cases:
        return special_cases[name]

    # Check if the word ends with a known AUTOSAR abbreviation
    # This handles compound words like "vendor_specific_module_def" -> "vendor_specific_module_defs"
    # instead of applying the 'f' -> 'ves' rule which would produce "vendor_specific_module_deves"
    known_abbreviations = ["def", "ref", "conf", "calib", "swc", "bsw", "hmi", "spec", "cfg", "prof", "buf", "brief", "chef"]
    for abbr in known_abbreviations:
        if name.endswith(abbr):
            # Check if it's an exact match (already handled above) or a suffix
            if name != abbr:
                # It's a suffix, pluralize by adding 's'
                return name + "s"

    # Handle 'y' -> 'ies' (entity -> entities, body -> bodies)
    if name.endswith("y"):
        return name[:-1] + "ies"

    # Handle 'f' -> 'ves' (leaf -> leaves, knife -> knives, calf -> calves, life -> lives)
    if name.endswith("fe"):
        return name[:-2] + "ves"
    if name.endswith("f") and not name.endswith("ff"):
        return name[:-1] + "ves"

    # Handle 's', 'x', 'z', 'ch', 'sh' -> add 'es'
    if name.endswith(("s", "x", "z", "o")) or name.endswith("ch") or name.endswith("sh"):
        return name + "es"

    # Default: add 's'
    return name + "s"


def to_autosar_plural(name: str) -> str:
    """AUTOSAR XML pluralization: always add 'S'.

    AUTOSAR XML uses simple 'S' suffix for all plurals, not English grammar rules.
    For example:
    - memory -> MEMORYS (not MEMORIES)
    - access -> ACCESSS (not ACCESSES)
    - policy -> POLICYS (not POLICIES)
    - proxy -> PROXYS (not PROXIES)
    - dependency -> DEPENDENCYS (not DEPENDENCIES)

    Args:
        name: Singular name (in snake_case or UPPER-CASE-WITH-HYPHENS)

    Returns:
        Plural form with 's' or 'S' appended (matching the case of the last character)
    """
    # Match the case of the last character - uppercase gets 'S', lowercase gets 's'
    if name and name[-1].isupper():
        return name + "S"
    return name + "s"
