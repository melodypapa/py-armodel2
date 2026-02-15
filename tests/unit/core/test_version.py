import pytest
from lxml import etree

from armodel.core import SchemaVersionManager


class TestSchemaVersionManager:
    """Unit tests for SchemaVersionManager class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.manager = SchemaVersionManager()
        self.xml_00046 = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Test</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''
        self.xml_unknown = '''<?xml version="1.0" encoding="UTF-8"?>
<ROOT xmlns="http://unknown/schema">
</ROOT>'''

    def test_detect_schema_version_00046(self):
        """Test detection of AUTOSAR 00046 schema."""
        root = etree.fromstring(self.xml_00046.encode())
        version = self.manager.detect_schema_version(root)
        assert version == "00046"

    def test_detect_schema_version_unknown(self):
        """Test handling of unknown schema versions."""
        root = etree.fromstring(self.xml_unknown.encode())
        version = self.manager.detect_schema_version(root)
        assert version is None

    def test_get_default_version(self):
        """Test getting default schema version."""
        default = self.manager.get_default_version()
        assert default == "00046"

    def test_get_config(self):
        """Test getting configuration for specific version."""
        config = self.manager.get_config("00046")
        assert config is not None
        assert "namespace" in config
        assert config["namespace"] == "http://autosar.org/schema/r4.0"

    def test_get_namespace(self):
        """Test getting namespace for specific version."""
        namespace = self.manager.get_namespace("00046")
        assert namespace == "http://autosar.org/schema/r4.0"

    def test_get_all_versions(self):
        """Test getting all available versions."""
        versions = self.manager.get_all_versions()
        assert len(versions) == 3
        assert "00044" in versions
        assert "00046" in versions
        assert "00052" in versions

    def test_singleton_pattern(self):
        """Test that SchemaVersionManager follows singleton pattern."""
        manager1 = SchemaVersionManager()
        manager2 = SchemaVersionManager()
        assert manager1 is manager2
