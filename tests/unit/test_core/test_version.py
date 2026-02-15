import pytest
from lxml import etree

def test_detect_schema_version_00046():
    """Test detection of AUTOSAR 00046 schema"""
    from armodel.core import SchemaVersionManager

    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Test</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    # Parse to get root
    root = etree.fromstring(xml_content.encode())
    manager = SchemaVersionManager()
    version = manager.detect_schema_version(root)
    assert version == "00046"

def test_detect_schema_version_unknown():
    """Test handling of unknown schema versions"""
    from armodel.core import SchemaVersionManager

    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<ROOT xmlns="http://unknown/schema">
</ROOT>'''

    root = etree.fromstring(xml_content.encode())
    manager = SchemaVersionManager()
    version = manager.detect_schema_version(root)
    assert version is None

def test_get_default_version():
    """Test getting default schema version"""
    from armodel.core import SchemaVersionManager

    manager = SchemaVersionManager()
    default = manager.get_default_version()
    assert default == "00046"

def test_get_config():
    """Test getting configuration for specific version"""
    from armodel.core import SchemaVersionManager

    manager = SchemaVersionManager()
    config = manager.get_config("00046")
    assert config is not None
    assert "namespace" in config
    assert config["namespace"] == "http://autosar.org/schema/r4.0"

def test_get_namespace():
    """Test getting namespace for specific version"""
    from armodel.core import SchemaVersionManager

    manager = SchemaVersionManager()
    namespace = manager.get_namespace("00046")
    assert namespace == "http://autosar.org/schema/r4.0"

def test_get_all_versions():
    """Test getting all available versions"""
    from armodel.core import SchemaVersionManager

    manager = SchemaVersionManager()
    versions = manager.get_all_versions()
    assert len(versions) == 3
    assert "00044" in versions
    assert "00046" in versions
    assert "00052" in versions

def test_singleton_pattern():
    """Test that SchemaVersionManager follows singleton pattern"""
    from armodel.core import SchemaVersionManager

    manager1 = SchemaVersionManager()
    manager2 = SchemaVersionManager()
    assert manager1 is manager2
