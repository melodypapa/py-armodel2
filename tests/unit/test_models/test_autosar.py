import pytest

def test_autosar_singleton():
    """Test that AUTOSAR is a singleton"""
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    obj1 = AUTOSAR()
    obj2 = AUTOSAR()
    assert obj1 is obj2

def test_autosar_get_splitable_elements():
    """Test getting splitable elements"""
    from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR

    autosar = AUTOSAR()
    splitable = autosar.get_splitable_elements()
    assert isinstance(splitable, list)
