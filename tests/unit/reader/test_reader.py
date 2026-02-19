import pytest

from armodel.reader import ARXMLReader


class TestARXMLReader:
    """Unit tests for ARXMLReader class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.reader = ARXMLReader()
        self.test_arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    def test_get_schema_version(self, tmp_path):
        """Test getting schema version from ARXML file."""
        test_file = tmp_path / "test.arxml"
        test_file.write_text(self.test_arxml_content)

        version = self.reader.get_schema_version(test_file)

        # Multiple versions use the r4.0 namespace (00046-00051)
        # The system may return any of these versions
        assert version in ["00046", "00047", "00048", "00049", "00050", "00051"]


