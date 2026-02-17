# tests/integration/test_roundtrip.py
import tempfile
from pathlib import Path
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter

def test_roundtrip_serialization():
    """Test read → serialize → write produces valid XML."""
    # Read original file
    reader = ARXMLReader()
    autosar = reader.load_arxml('demos/arxml/AUTOSAR_Datatypes.arxml')

    # Write to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
        temp_path = f.name

    try:
        writer = ARXMLWriter(pretty_print=True)
        writer.save_arxml(autosar, temp_path)

        # Read back
        autosar2 = reader.load_arxml(temp_path)

        # Basic verification
        assert autosar2 is not None
        assert len(autosar2.ar_packages) == len(autosar.ar_packages)

        # Verify structure is preserved
        for pkg1, pkg2 in zip(autosar.ar_packages, autosar2.ar_packages):
            assert pkg1.short_name == pkg2.short_name
            if hasattr(pkg1, 'ar_packages') and hasattr(pkg2, 'ar_packages'):
                assert len(pkg1.ar_packages) == len(pkg2.ar_packages)

    finally:
        # Cleanup
        Path(temp_path).unlink()
