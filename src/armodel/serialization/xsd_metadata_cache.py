"""
XSD Metadata Cache Manager

Provides fast access to XSD metadata from pre-generated YAML files.

Usage:
    from armodel.serialization.xsd_metadata_cache import XSDBasedSchemaManager

    # Get singleton instance
    manager = XSDBasedSchemaManager()

    # Load metadata for a version
    metadata = manager.get_metadata("00046")

    # Get type information
    type_info = manager.get_type_info("SW-BASE-TYPE", "00046")

    # Get all elements for a type
    elements = manager.get_elements_for_type("SW-BASE-TYPE", "00046")
"""

from pathlib import Path
from typing import Optional, Dict, List, Any, cast
import yaml


class XSDBasedSchemaManager:
    """Singleton manager for XSD metadata cache."""

    _instance: Optional["XSDBasedSchemaManager"] = None
    _initialized: bool = False

    def __new__(cls) -> "XSDBasedSchemaManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize the schema manager."""
        if not self._initialized:
            self._metadata_dir = Path(__file__).parent.parent / "cfg" / "xsd_metadata"
            self._cache: Dict[str, Dict[str, Any]] = {}
            self._initialized = True

    def get_metadata(self, version: str) -> Dict[str, Any]:
        """
        Get metadata for a specific schema version.

        Args:
            version: Schema version (e.g., "00046")

        Returns:
            Dictionary containing all metadata for the version

        Raises:
            FileNotFoundError: If YAML file doesn't exist
        """
        # Check cache first
        if version in self._cache:
            return self._cache[version]

        # Load from file
        yaml_path = self._metadata_dir / f"schema_{version}.yaml"

        if not yaml_path.exists():
            raise FileNotFoundError(
                f"XSD metadata file not found: {yaml_path}\n"
                f"Run: python tools/generate_xsd_metadata.py --version {version}"
            )

        with open(yaml_path, "r") as f:
            metadata = cast(Dict[str, Any], yaml.safe_load(f))

        # Cache it
        self._cache[version] = metadata

        return metadata

    def get_type_info(self, type_name: str, version: str) -> Optional[Dict[str, Any]]:
        """
        Get type information for a complex type.

        Args:
            type_name: Name of the complex type (e.g., "SW-BASE-TYPE")
            version: Schema version

        Returns:
            Dictionary with type information or None if not found
        """
        metadata = self.get_metadata(version)
        complex_types = metadata.get("complex_types", {})
        if not isinstance(complex_types, dict):
            return None
        return cast(Optional[Dict[str, Any]], complex_types.get(type_name))

    def get_simple_type_info(self, type_name: str, version: str) -> Optional[Dict[str, Any]]:
        """
        Get simple type information (enums, patterns).

        Args:
            type_name: Name of the simple type
            version: Schema version

        Returns:
            Dictionary with simple type information or None if not found
        """
        metadata = self.get_metadata(version)
        simple_types = metadata.get("simple_types", {})
        if not isinstance(simple_types, dict):
            return None
        return cast(Optional[Dict[str, Any]], simple_types.get(type_name))

    def get_elements_for_type(self, type_name: str, version: str) -> List[Dict[str, Any]]:
        """
        Get all elements for a type (including inherited elements).

        Args:
            type_name: Name of the complex type
            version: Schema version

        Returns:
            List of element dictionaries
        """
        metadata = self.get_metadata(version)
        indexes = metadata.get("indexes", {})
        if not isinstance(indexes, dict):
            return []
        type_to_elements = indexes.get("type_to_elements", {})
        if not isinstance(type_to_elements, dict):
            return []
        result = type_to_elements.get(type_name, [])
        if not isinstance(result, list):
            return []
        return cast(List[Dict[str, Any]], result)

    def get_attributes_for_type(self, type_name: str, version: str) -> List[Dict[str, Any]]:
        """
        Get all attributes for a type.

        Args:
            type_name: Name of the complex type
            version: Schema version

        Returns:
            List of attribute dictionaries
        """
        type_info = self.get_type_info(type_name, version)
        if type_info:
            attrs = type_info.get("attributes", [])
            if not isinstance(attrs, list):
                return []
            return cast(List[Dict[str, Any]], attrs)
        return []

    def get_element_types(self, element_name: str, version: str) -> List[str]:
        """
        Get all types that can contain a specific element.

        Args:
            element_name: Name of the element (e.g., "SHORT-NAME")
            version: Schema version

        Returns:
            List of type names that contain this element
        """
        metadata = self.get_metadata(version)
        indexes = metadata.get("indexes", {})
        if not isinstance(indexes, dict):
            return []
        element_to_types = indexes.get("element_to_types", {})
        if not isinstance(element_to_types, dict):
            return []
        result = element_to_types.get(element_name, [])
        if not isinstance(result, list):
            return []
        return cast(List[str], result)

    def get_inheritance_chain(self, type_name: str, version: str) -> List[str]:
        """
        Get the inheritance chain for a type.

        Args:
            type_name: Name of the complex type
            version: Schema version

        Returns:
            List of type names from base to derived
        """
        chain = []
        current_type: Optional[str] = type_name

        while current_type:
            chain.append(current_type)
            type_info = self.get_type_info(current_type, version)
            if not type_info:
                break
            base_type = type_info.get("base_type")
            if isinstance(base_type, str):
                current_type = base_type
            else:
                break

        return chain

    def validate_value(self, value: Any, type_name: str, version: str) -> bool:
        """
        Validate a value against a simple type's constraints.

        Args:
            value: Value to validate
            type_name: Name of the simple type
            version: Schema version

        Returns:
            True if valid, False otherwise
        """
        simple_type = self.get_simple_type_info(type_name, version)
        if not simple_type:
            return True  # No constraints to validate

        # Check enum values
        enum_values = simple_type.get("enum_values")
        if enum_values and value not in enum_values:
            return False

        # Check pattern
        pattern = simple_type.get("pattern")
        if pattern and isinstance(value, str):
            import re

            if not re.match(pattern, value):
                return False

        # Check length constraints
        if isinstance(value, str):
            min_length = simple_type.get("min_length")
            max_length = simple_type.get("max_length")
            if min_length and len(value) < min_length:
                return False
            if max_length and len(value) > max_length:
                return False

        return True

    def clear_cache(self) -> None:
        """Clear the metadata cache."""
        self._cache.clear()

    def is_loaded(self, version: str) -> bool:
        """
        Check if metadata for a version is loaded in cache.

        Args:
            version: Schema version

        Returns:
            True if loaded, False otherwise
        """
        return version in self._cache
