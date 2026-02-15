import pytest
from pathlib import Path

def test_load_arxml_file(tmp_path):
    """Test loading ARXML file"""
    from armodel.reader.loader import load_arxml_file

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

    # Load file
    root = load_arxml_file(test_file)

    assert root is not None
    # Check local name (ignore namespace)
    assert root.tag.split("}")[-1] == "AUTOSAR"
