# tests/unit/models/test_ar_object_deserialize.py
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

class TestARObject(ARObject):
    # Class-level type annotations (required for get_type_hints)
    short_name: str
    category: str
    sw_data_def_props: str

def test_deserialize_from_xml():
    xml = '''<TESTAROBJECT>
        <SHORT-NAME>test_name</SHORT-NAME>
        <CATEGORY>STANDARD</CATEGORY>
    </TESTAROBJECT>'''

    elem = ET.fromstring(xml)
    obj = TestARObject.deserialize(elem)

    assert obj.short_name == "test_name"
    assert obj.category == "STANDARD"

def test_deserialize_converts_names():
    xml = '''<TESTAROBJECT>
        <SW-DATA-DEF-PROPS>value</SW-DATA-DEF-PROPS>
    </TESTAROBJECT>'''

    elem = ET.fromstring(xml)
    obj = TestARObject.deserialize(elem)

    assert hasattr(obj, 'sw_data_def_props')
    assert obj.sw_data_def_props == "value"
