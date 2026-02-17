# tests/unit/models/test_ar_object_serialize.py
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

class TestARObject(ARObject):
    def __init__(self):
        super().__init__()
        self.short_name: String = "test_name"
        self.category: str = "STANDARD"

def test_serialize_creates_element():
    obj = TestARObject()
    elem = obj.serialize()

    assert elem.tag == "TEST-A-R-OBJECT"
    assert elem.find("SHORT-NAME") is not None
    assert elem.find("SHORT-NAME").text == "test_name"

def test_serialize_converts_names():
    obj = TestARObject()
    elem = obj.serialize()

    # Verify snake_case → UPPER-CASE conversion
    assert elem.find("SHORT-NAME") is not None
    assert elem.find("CATEGORY") is not None
