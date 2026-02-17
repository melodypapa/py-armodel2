# tests/unit/serialization/test_name_converter.py
from armodel.serialization.name_converter import NameConverter

def test_short_name_to_xml_tag():
    result = NameConverter.to_xml_tag("short_name")
    assert result == "SHORT-NAME"

def test_xml_tag_to_python_name():
    result = NameConverter.to_python_name("SHORT-NAME")
    assert result == "short_name"

def test_complex_conversion():
    result = NameConverter.to_xml_tag("sw_data_def_props")
    assert result == "SW-DATA-DEF-PROPS"

def test_private_attribute_stripped():
    result = NameConverter.to_xml_tag("_private_attr")
    assert result == "PRIVATE-ATTR"
