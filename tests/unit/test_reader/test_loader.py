import pytest
from pathlib import Path

def test_load_arxml_file(tmp_path):
    """Test loading ARXML file"""
    from armodel.reader import ARXMLReader

    # Create test ARXML file
    arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    test_file = tmp_path / "test.arxml"
    test_file.write_text(arxml_content)

    # Load file using ARXMLReader
    reader = ARXMLReader()
    autosar = reader.load_arxml(test_file)

    assert autosar is not None

def test_get_schema_version(tmp_path):
    """Test getting schema version from ARXML file"""
    from armodel.reader import ARXMLReader

    # Create test ARXML file
    arxml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>'''

    test_file = tmp_path / "test.arxml"
    test_file.write_text(arxml_content)

    # Get schema version
    reader = ARXMLReader()
    version = reader.get_schema_version(test_file)

    assert version == "00046"


