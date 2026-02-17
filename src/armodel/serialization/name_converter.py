"""Name conversion utility for Python ↔ AUTOSAR XML naming conventions."""


class NameConverter:
    """Convert between Python snake_case and AUTOSAR UPPER-CASE-WITH-HYPHENS naming."""

    @staticmethod
    def to_xml_tag(name: str) -> str:
        """Convert Python attribute name to XML tag name.

        Args:
            name: Python attribute name (snake_case)

        Returns:
            XML tag name (UPPER-CASE-WITH-HYPHENS)

        Examples:
            short_name → SHORT-NAME
            sw_data_def_props → SW-DATA-DEF-PROPS
        """
        # Remove private prefix
        if name.startswith('_'):
            name = name[1:]
        # Convert to uppercase and replace underscores with hyphens
        return name.upper().replace('_', '-')

    @staticmethod
    def to_python_name(tag: str) -> str:
        """Convert XML tag name to Python attribute name.

        Args:
            tag: XML tag name (UPPER-CASE-WITH-HYPHENS)

        Returns:
            Python attribute name (snake_case)

        Examples:
            SHORT-NAME → short_name
            SW-DATA-DEF-PROPS → sw_data_def_props
        """
        return tag.lower().replace('-', '_')
