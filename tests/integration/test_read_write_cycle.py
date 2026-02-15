import pytest
from pathlib import Path

def test_read_write_cycle(tmp_path):
    """Test reading and writing ARXML preserves structure"""
    from armodel.reader import ARXMLReader
    from armodel.writer import ARXMLWriter

    # Load fixture
    fixture = Path("tests/fixtures/arxml/AUTOSAR_00046_sample.arxml")
    reader = ARXMLReader()
    autosar = reader.load_arxml(fixture)

    # Write to temp file
    output = tmp_path / "output.arxml"
    writer = ARXMLWriter(pretty_print=True)
    writer.save_arxml(autosar, output)

    # Read back
    autosar2 = reader.load_arxml(output)

    # Verify both are AUTOSAR instances
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    assert isinstance(autosar, AUTOSAR)
    assert isinstance(autosar2, AUTOSAR)

    # TODO: Add deeper comparison when parsing is implemented
