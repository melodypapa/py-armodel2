import pytest
import xml.etree.cElementTree as ET

from armodel2.core import SchemaVersionManager


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
        """Test detection of AUTOSAR schema with r4.0 namespace."""
        root = ET.fromstring(self.xml_00046.encode())
        version = self.manager.detect_schema_version(root)
        # Multiple versions use this namespace (00046-00051), so it may return any of them
        assert version in ["00046", "00047", "00048", "00049", "00050", "00051"]

    def test_detect_schema_version_unknown(self):
        """Test handling of unknown schema versions."""
        root = ET.fromstring(self.xml_unknown.encode())
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
        assert len(versions) == 14
        # Check legacy versions
        assert "00042" in versions
        assert "00043" in versions
        assert "00044" in versions
        assert "00045" in versions
        assert "00046" in versions
        assert "00047" in versions
        # Check unified versions
        assert "00048" in versions
        assert "00049" in versions
        assert "00050" in versions
        assert "00051" in versions
        assert "00052" in versions
        assert "00053" in versions
        assert "00054" in versions
        # Check legacy version
        assert "3_2_3" in versions

    def test_singleton_pattern(self):
        """Test that SchemaVersionManager follows singleton pattern."""
        manager1 = SchemaVersionManager()
        manager2 = SchemaVersionManager()
        assert manager1 is manager2

    def test_namespace_collision(self):
        """Test that multiple versions can share the same namespace."""
        # Versions 00046-00051 all use the same namespace
        ns_r40 = self.manager.get_namespace("00046")
        assert ns_r40 == "http://autosar.org/schema/r4.0"

        for version in ["00047", "00048", "00049", "00050", "00051"]:
            assert self.manager.get_namespace(version) == ns_r40

        # Versions 00042-00045 all use the same namespace
        ns_304 = self.manager.get_namespace("00044")
        assert ns_304 == "http://autosar.org/3.0.4"

        for version in ["00042", "00043", "00045"]:
            assert self.manager.get_namespace(version) == ns_304

        # Versions 00052-00054 all use the same namespace
        ns_r50 = self.manager.get_namespace("00052")
        assert ns_r50 == "http://autosar.org/schema/r5.0"

        for version in ["00053", "00054"]:
            assert self.manager.get_namespace(version) == ns_r50
