"""Schema version detection for ARXML files."""

from typing import Optional, Dict, Any, cast
import xml.etree.ElementTree as ET
from armodel.cfg.schemas import ConfigurationManager


class SchemaVersionManager:
    """Manages AUTOSAR schema version detection and configuration.

    This class provides a singleton instance for managing schema version
    detection, namespace mapping, and configuration access.
    """

    _instance: Optional["SchemaVersionManager"] = None
    _initialized: bool = False

    def __new__(cls) -> "SchemaVersionManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        """Initialize version manager (singleton pattern)."""
        if self._initialized:
            return

        self._config_manager = ConfigurationManager()
        self._config = self._config_manager._config
        self._namespace_to_version = self._build_namespace_mapping()
        self._default_version = self._config.get("default", "00046")
        self._initialized = True

    def _build_namespace_mapping(self) -> Dict[str, str]:
        """Build namespace to version mapping from config.

        Returns:
            Dictionary mapping namespace URIs to version strings
        """
        mapping = {}
        for version, config in self._config.get("versions", {}).items():
            namespace = config.get("namespace", "")
            if namespace:
                mapping[namespace] = version
        return mapping

    def detect_schema_version(self, root: ET.Element) -> Optional[str]:
        """Detect AUTOSAR schema version from XML element namespace.

        Args:
            root: Root XML element from ARXML file

        Returns:
            Schema version string (e.g., "00046") or None if unknown
        """
        namespace = self._extract_namespace(root)
        return self._namespace_to_version.get(namespace)

    def _extract_namespace(self, root: ET.Element) -> str:
        """Extract namespace from XML element.

        Args:
            root: XML element

        Returns:
            Namespace URI string
        """
        if "}" in root.tag:
            # Namespace is embedded in tag: {namespace}tagname
            return root.tag.split("}")[0].strip("{")
        elif "xmlns" in root.attrib:
            # Namespace in attribute (fallback)
            return root.attrib.get("xmlns", "")
        return ""

    def get_default_version(self) -> str:
        """Get default AUTOSAR schema version.

        Returns:
            Default version string from config
        """
        return cast(str, self._default_version)

    def get_config(self, version: str) -> Optional[Dict[str, Any]]:
        """Get configuration for specific schema version.

        Args:
            version: Schema version string (e.g., "00046")

        Returns:
            Configuration dictionary or None if version not found
        """
        config = self._config.get("versions", {}).get(version)
        return cast(Optional[Dict[str, Any]], config)

    def get_namespace(self, version: str) -> Optional[str]:
        """Get namespace URI for specific schema version.

        Args:
            version: Schema version string (e.g., "00046")

        Returns:
            Namespace URI string or None if version not found
        """
        config = self.get_config(version)
        return config.get("namespace") if config else None

    def get_xsd_path(self, version: str) -> Optional[str]:
        """Get XSD file path for specific schema version.

        Args:
            version: Schema version string (e.g., "00046")

        Returns:
            XSD file path or None if version not found
        """
        config = self.get_config(version)
        xsd_file = config.get("xsd_file") if config else None
        if xsd_file:
            from pathlib import Path

            return str(Path("demos/xsd/AUTOSAR_") / version / xsd_file)
        return None

    def get_all_versions(self) -> list[str]:
        """Get list of all available schema versions.

        Returns:
            List of version strings
        """
        return list(self._config.get("versions", {}).keys())

    def reload(self) -> None:
        """Reload configuration from file.

        This method resets the singleton state and reloads configuration,
        useful for testing or when configuration files change.
        """
        self._config_manager.reload()
        self._config = self._config_manager._config
        self._namespace_to_version = self._build_namespace_mapping()
        self._default_version = self._config.get("default", "00046")
