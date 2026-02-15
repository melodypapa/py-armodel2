import pytest
from lxml import etree

def test_map_xml_to_autosar():
    """Test mapping XML to AUTOSAR object"""
    from armodel.reader.mapper import map_xml_to_autosar

    xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    root = etree.fromstring(xml_string.encode())
    autosar = map_xml_to_autosar(root)

    assert autosar is not None
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    assert isinstance(autosar, AUTOSAR)
