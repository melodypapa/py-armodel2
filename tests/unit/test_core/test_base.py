import pytest

def test_ar_object_creation():
    """Test that ARObject can be instantiated"""
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject

    obj = ARObject()
    assert obj is not None

def test_ar_object_serialization_not_implemented():
    """Test that serialize raises NotImplementedError by default"""
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject

    obj = ARObject()
    with pytest.raises(NotImplementedError):
        obj.serialize()
