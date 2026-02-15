"""Schema version detection for ARXML files."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.cfg.schemas import load_schema_config


# Load schema configuration
_SCHEMA_CONFIG = load_schema_config()

# Build namespace to version mapping
_NAMESPACE_TO_VERSION = {}
for version, config in _SCHEMA_CONFIG["versions"].items():
    namespace = config.get("namespace", "")
    _NAMESPACE_TO_VERSION[namespace] = version

# Get default version
_DEFAULT_VERSION: str = cast(str, _SCHEMA_CONFIG.get("default", "00046"))


def detect_schema_version(root: ET.Element) -> Optional[str]:
    """Detect AUTOSAR schema version from XML element namespace.

    Args:
        root: Root XML element from ARXML file

    Returns:
        Schema version string (e.g., "00046") or None if unknown
    """
    # Extract namespace from tag (format: {namespace}tagname)
    namespace = ""
    if "}" in root.tag:
        # Namespace is embedded in tag: {namespace}tagname
        namespace = root.tag.split("}")[0].strip("{")
    elif "xmlns" in root.attrib:
        # Namespace in attribute (fallback)
        namespace = root.attrib.get("xmlns", "")

    # Map to version using configuration
    return _NAMESPACE_TO_VERSION.get(namespace)


def get_default_version() -> str:
    """Get default AUTOSAR schema version.

    Returns:
        Default version string from config
    """
    return _DEFAULT_VERSION
