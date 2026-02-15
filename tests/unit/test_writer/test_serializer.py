import pytest
from lxml import etree

def test_serialize_autosar_to_xml():
    """Test serializing AUTOSAR object to XML"""
    from armodel.writer import ARXMLWriter
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    writer = ARXMLWriter()
    root = writer._serialize_to_xml(autosar)

    assert root is not None
    assert root.tag.split("}")[-1] == "AUTOSAR"
