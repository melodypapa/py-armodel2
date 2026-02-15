import pytest
from pathlib import Path
from lxml import etree

def test_save_arxml_file(tmp_path):
    """Test saving AUTOSAR to ARXML file"""
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    output_file = tmp_path / "output.arxml"

    # Save to file using ARXMLWriter
    writer = ARXMLWriter(pretty_print=True)
    writer.save_arxml(autosar, output_file)

    # Verify file was created and contains XML
    assert output_file.exists()
    content = output_file.read_text()
    assert "<?xml" in content
    assert "<AUTOSAR" in content

def test_save_arxml_without_pretty_print(tmp_path):
    """Test saving AUTOSAR to ARXML file without pretty printing"""
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    output_file = tmp_path / "output_compact.arxml"

    # Save to file without pretty printing
    writer = ARXMLWriter(pretty_print=False)
    writer.save_arxml(autosar, output_file)

    # Verify file was created
    assert output_file.exists()

def test_configure_writer(tmp_path):
    """Test configuring writer after initialization"""
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    output_file = tmp_path / "output.arxml"

    # Create writer and configure it
    writer = ARXMLWriter(pretty_print=False, encoding="UTF-8")
    writer.configure(pretty_print=True)
    writer.save_arxml(autosar, output_file)

    # Verify file was created
    assert output_file.exists()

def test_to_string(tmp_path):
    """Test converting AUTOSAR object to XML string"""
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()

    # Convert to string
    writer = ARXMLWriter(pretty_print=True)
    xml_string = writer.to_string(autosar)

    # Verify string contains XML
    assert "<?xml" in xml_string
    assert "<AUTOSAR" in xml_string
