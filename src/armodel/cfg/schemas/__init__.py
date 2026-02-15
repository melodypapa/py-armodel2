"""Schema configuration for AUTOSAR versions."""

import yaml
from pathlib import Path
from typing import Optional, Dict, Any, cast, List


class ConfigurationManager:
    """Manages configuration for ARXML processing.

    This class provides configuration loading, caching, and access
    with support for nested configuration keys.
    """

    def __init__(self, config_path: Optional[Path] = None):
        """Initialize configuration manager.

        Args:
            config_path: Path to config.yaml, defaults to package config
        """
        self._config_path = config_path or self._get_default_config_path()
        self._config = self._load_config()

    def _get_default_config_path(self) -> Path:
        """Get default configuration file path.

        Returns:
            Path to default config.yaml file
        """
        return Path(__file__).parent / "config.yaml"

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file.

        Returns:
            Configuration dictionary
        """
        with open(self._config_path, "r") as f:
            return cast(Dict[str, Any], yaml.safe_load(f))

    def reload(self) -> None:
        """Reload configuration from file.

        This method forces a reload of the configuration file,
        useful for testing or when configuration files change.
        """
        self._config = self._load_config()

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key.

        Args:
            key: Configuration key (supports dot notation for nested access)
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        keys = key.split(".")
        value = self._config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default

        return value

    def get_schema_config(self, version: str) -> Optional[Dict[str, Any]]:
        """Get schema configuration for specific version.

        Args:
            version: Schema version string (e.g., "00046")

        Returns:
            Schema configuration dictionary or None if version not found
        """
        return self.get(f"versions.{version}")

    def get_all_versions(self) -> List[str]:
        """Get list of all available schema versions.

        Returns:
            List of version strings
        """
        versions = self.get("versions", {})
        return list(versions.keys()) if versions else []

    def get_default_version(self) -> str:
        """Get default schema version.

        Returns:
            Default version string
        """
        return self.get("default", "00046")

    def get_namespace(self, version: str) -> Optional[str]:
        """Get namespace URI for specific schema version.

        Args:
            version: Schema version string (e.g., "00046")

        Returns:
            Namespace URI string or None if version not found
        """
        config = self.get_schema_config(version)
        return config.get("namespace") if config else None

    def get_xsd_path(self, version: str) -> Optional[str]:
        """Get XSD file path for specific schema version.

        Args:
            version: Schema version string (e.g., "00046")

        Returns:
            XSD file path or None if version not found
        """
        config = self.get_schema_config(version)
        return config.get("xsd_path") if config else None

    def get_features(self, version: str) -> Optional[Dict[str, Any]]:
        """Get features configuration for specific schema version.

        Args:
            version: Schema version string (e.g., "00046")

        Returns:
            Features dictionary or None if version not found
        """
        config = self.get_schema_config(version)
        return config.get("features") if config else None


__all__ = [
    "ConfigurationManager",
]
