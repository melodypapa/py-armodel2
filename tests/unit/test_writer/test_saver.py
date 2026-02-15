import pytest
from pathlib import Path
from lxml import etree

def test_save_arxml_file(tmp_path):
    """Test saving AUTOSAR to ARXML file"""
    from armodel.writer.saver import save_arxml_file
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    from armodel.writer.serializer import serialize_autosar_to_xml

    autosar = AUTOSAR()
    output_file = tmp_path / "output.arxml"

    # Serialize to XML
    from armodel.writer.serializer import serialize_autosar_to_xml
    root = serialize_autosar_to_xml(autosar)

    # Save to file
    save_arxml_file(root, output_file, pretty_print=True)

    # Verify file was created and contains XML
    assert output_file.exists()
    content = output_file.read_text()
    assert "<?xml" in content
    assert "<AUTOSAR" in content
