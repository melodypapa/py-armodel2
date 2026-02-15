import pytest
from pathlib import Path

def test_save_arxml_integration(tmp_path):
    """Test full ARXML saving flow"""
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    output_file = tmp_path / "output.arxml"

    # Save using ARXMLWriter
    writer = ARXMLWriter(pretty_print=True)
    writer.save_arxml(autosar, output_file)

    # Verify
    assert output_file.exists()
    content = output_file.read_text()
    assert "<?xml" in content
    assert "<AUTOSAR" in content
