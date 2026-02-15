import pytest
from lxml import etree

def test_detect_schema_version_00046():
    """Test detection of AUTOSAR 00046 schema"""
    from armodel.core.version import detect_schema_version

    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Test</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    # Parse to get root
    root = etree.fromstring(xml_content.encode())
    version = detect_schema_version(root)
    assert version == "00046"

def test_detect_schema_version_unknown():
    """Test handling of unknown schema versions"""
    from armodel.core.version import detect_schema_version

    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<ROOT xmlns="http://unknown/schema">
</ROOT>'''

    root = etree.fromstring(xml_content.encode())
    version = detect_schema_version(root)
    assert version is None
