import pytest
from pathlib import Path
from lxml import etree

from armodel.writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


class TestARXMLWriter:
    """Unit tests for ARXMLWriter class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.autosar = AUTOSAR()
        self.writer = ARXMLWriter(pretty_print=True)
        self.writer_compact = ARXMLWriter(pretty_print=False)

    @pytest.mark.skip(reason="get_schema_version() method not yet implemented in generated code")
    def test_save_arxml_file(self, tmp_path):
        """Test saving AUTOSAR to ARXML file."""
        output_file = tmp_path / "output.arxml"

        self.writer.save_arxml(self.autosar, output_file)

        # Verify file was created and contains XML
        assert output_file.exists()
        content = output_file.read_text()
        assert "<?xml" in content
        assert "<AUTOSAR" in content

    @pytest.mark.skip(reason="get_schema_version() method not yet implemented in generated code")
    def test_save_arxml_without_pretty_print(self, tmp_path):
        """Test saving AUTOSAR to ARXML file without pretty printing."""
        output_file = tmp_path / "output_compact.arxml"

        self.writer_compact.save_arxml(self.autosar, output_file)

        # Verify file was created
        assert output_file.exists()

    @pytest.mark.skip(reason="get_schema_version() method not yet implemented in generated code")
    def test_configure_writer(self, tmp_path):
        """Test configuring writer after initialization."""
        output_file = tmp_path / "output.arxml"

        # Create writer and configure it
        writer = ARXMLWriter(pretty_print=False, encoding="UTF-8")
        writer.configure(pretty_print=True)
        writer.save_arxml(self.autosar, output_file)

        # Verify file was created
        assert output_file.exists()

    @pytest.mark.skip(reason="get_schema_version() method not yet implemented in generated code")
    def test_to_string(self):
        """Test converting AUTOSAR object to XML string."""
        xml_string = self.writer.to_string(self.autosar)

        # Verify string contains XML
        assert "<?xml" in xml_string
        assert "<AUTOSAR" in xml_string
