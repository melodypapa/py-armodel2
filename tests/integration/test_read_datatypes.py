# tests/integration/test_read_datatypes.py
from armodel.reader import ARXMLReader

def test_read_autosar_datatypes():
    """Test reading AUTOSAR_Datatypes.arxml file."""
    reader = ARXMLReader()
    autosar = reader.load_arxml('demos/arxml/AUTOSAR_Datatypes.arxml')

    # Verify root element
    assert autosar is not None
    assert hasattr(autosar, 'ar_packages')

    # Verify structure
    assert len(autosar.ar_packages) > 0

    # Find AUTOSAR_Platform package
    platform_pkg = None
    for pkg in autosar.ar_packages:
        if pkg.short_name == 'AUTOSAR_Platform':
            platform_pkg = pkg
            break

    assert platform_pkg is not None, "AUTOSAR_Platform package not found"

    # Verify BaseTypes subpackage
    base_types = None
    for pkg in platform_pkg.ar_packages:
        if pkg.short_name == 'BaseTypes':
            base_types = pkg
            break

    assert base_types is not None, "BaseTypes package not found"

    # Verify we have SwBaseType elements
    assert hasattr(base_types, 'elements')
    assert len(base_types.elements) > 0

    # Verify first SwBaseType
    first_type = base_types.elements[0]
    assert first_type.short_name == 'float32'
