# tests/unit/serialization/test_decorators.py
from armodel.serialization.decorators import xml_attribute, xml_tag

def test_xml_attribute_decorator():
    @xml_attribute
    def category():
        return "STANDARD"

    assert hasattr(category, '_is_xml_attribute')
    assert category._is_xml_attribute == True

def test_xml_tag_decorator():
    @xml_tag("CUSTOM-TAG")
    class MyElement:
        pass

    assert hasattr(MyElement, '_xml_tag')
    assert MyElement._xml_tag == "CUSTOM-TAG"

def test_decorator_chain():
    @xml_attribute
    @property
    def schema_version(self):
        return self._schema_version

    assert hasattr(schema_version.fget, '_is_xml_attribute')
    assert schema_version.fget._is_xml_attribute == True
