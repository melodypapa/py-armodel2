import pytest
from pathlib import Path

from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR


class TestReaderWriterIntegration:
    """Integration tests for ARXML reader and writer functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.reader = ARXMLReader()
        self.writer = ARXMLWriter(pretty_print=True)
        self.test_arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    def test_read_arxml_integration(self, tmp_path):
        """Test full ARXML loading flow."""
        # Create test ARXML file
        test_file = tmp_path / "test.arxml"
        test_file.write_text(self.test_arxml_content)

        # Load file using ARXMLReader
        autosar = self.reader.load_arxml(test_file)

        # Verify
        assert isinstance(autosar, AUTOSAR)

    def test_save_arxml_integration(self, tmp_path):
        """Test full ARXML saving flow."""
        autosar = AUTOSAR()
        output_file = tmp_path / "output.arxml"

        # Save using ARXMLWriter
        self.writer.save_arxml(autosar, output_file)

        # Verify
        assert output_file.exists()
        content = output_file.read_text()
        assert "<?xml" in content
        assert "<AUTOSAR" in content

    def test_read_write_cycle(self, tmp_path):
        """Test reading and writing ARXML preserves structure."""
        # Load fixture
        fixture = Path("tests/fixtures/arxml/AUTOSAR_00046_sample.arxml")
        autosar = self.reader.load_arxml(fixture)

        # Write to temp file
        output = tmp_path / "output.arxml"
        self.writer.save_arxml(autosar, output)

        # Read back
        autosar2 = self.reader.load_arxml(output)

        # Verify both are AUTOSAR instances
        assert isinstance(autosar, AUTOSAR)
        assert isinstance(autosar2, AUTOSAR)

        # TODO: Add deeper comparison when parsing is implemented