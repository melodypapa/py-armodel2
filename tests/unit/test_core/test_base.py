import pytest

def test_ar_object_creation():
    """Test that ARObject can be instantiated"""
    from armodel.core.base import ARObject

    obj = ARObject()
    assert obj is not None

def test_ar_object_serialization_not_implemented():
    """Test that serialize raises NotImplementedError by default"""
    from armodel.core.base import ARObject

    obj = ARObject()
    with pytest.raises(NotImplementedError):
        obj.serialize()
