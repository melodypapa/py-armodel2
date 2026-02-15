import pytest
from pathlib import Path

def test_load_arxml_integration(tmp_path):
    """Test full ARXML loading flow"""
    from armodel.reader import load_arxml

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
    autosar = load_arxml(test_file)

    # Verify
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR
    assert isinstance(autosar, AUTOSAR)
