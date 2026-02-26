"""Unit tests for SwBaseType class."""

import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import SwBaseType


class TestSwBaseType:
    """Unit tests for SwBaseType class."""

    def test_deserialize_flat_format(self):
        """Test deserializing flat XML format without BASE-TYPE-DEFINITION wrapper."""
        xml = """<SW-BASE-TYPE>
              <SHORT-NAME>float32</SHORT-NAME>
              <CATEGORY>FIXED_LENGTH</CATEGORY>
              <BASE-TYPE-SIZE>32</BASE-TYPE-SIZE>
              <BASE-TYPE-ENCODING>IEEE754</BASE-TYPE-ENCODING>
              <MEM-ALIGNMENT>32</MEM-ALIGNMENT>
              <NATIVE-DECLARATION>float</NATIVE-DECLARATION>
            </SW-BASE-TYPE>"""
        element = ET.fromstring(xml)
        obj = SwBaseType.deserialize(element)

        assert obj is not None
        # short_name is now unwrapped to plain string
        assert obj.short_name == "float32"
        assert str(obj.category) == "FIXED_LENGTH"
        assert obj.base_type_definition is not None
        assert obj.base_type_definition.base_type_size == "32"
        assert obj.base_type_definition.base_type_encoding == "IEEE754"
        assert obj.base_type_definition.mem_alignment == "32"
        assert obj.base_type_definition.native == "float"

    def test_deserialize_nested_format(self):
        """Test deserializing standard nested XML format with BASE-TYPE-DEFINITION wrapper."""
        xml = """<SW-BASE-TYPE>
              <SHORT-NAME>float32</SHORT-NAME>
              <BASE-TYPE-DEFINITION>
                <BASE-TYPE-SIZE>32</BASE-TYPE-SIZE>
                <BASE-TYPE-ENCODING>IEEE754</BASE-TYPE-ENCODING>
              </BASE-TYPE-DEFINITION>
            </SW-BASE-TYPE>"""
        element = ET.fromstring(xml)
        obj = SwBaseType.deserialize(element)

        assert obj is not None
        assert str(obj.short_name) == "float32"
        # Nested format is handled by standard reflection-based deserializer
        # Just verify base_type_definition is created (polymorphic deserialization)
        assert obj.base_type_definition is not None

    def test_deserialize_with_optional_fields_missing(self):
        """Test deserializing flat format with optional fields (BYTE-ORDER, NATIVE-DECLARATION) missing."""
        xml = """<SW-BASE-TYPE>
              <SHORT-NAME>uint8</SHORT-NAME>
              <CATEGORY>FIXED_LENGTH</CATEGORY>
              <BASE-TYPE-SIZE>8</BASE-TYPE-SIZE>
              <BASE-TYPE-ENCODING>2C</BASE-TYPE-ENCODING>
              <MEM-ALIGNMENT>8</MEM-ALIGNMENT>
            </SW-BASE-TYPE>"""
        element = ET.fromstring(xml)
        obj = SwBaseType.deserialize(element)

        assert obj is not None
        assert obj.base_type_definition is not None
        assert obj.base_type_definition.base_type_size == "8"
        assert obj.base_type_definition.base_type_encoding == "2C"
        assert obj.base_type_definition.mem_alignment == "8"
        assert obj.base_type_definition.byte_order is None
        assert obj.base_type_definition.native is None

    def test_deserialize_minimal_flat_format(self):
        """Test deserializing flat format with only required fields."""
        xml = """<SW-BASE-TYPE>
              <SHORT-NAME>void</SHORT-NAME>
              <CATEGORY>VOID</CATEGORY>
            </SW-BASE-TYPE>"""
        element = ET.fromstring(xml)
        obj = SwBaseType.deserialize(element)

        assert obj is not None
        assert str(obj.short_name) == "void"
        assert str(obj.category) == "VOID"
        assert obj.base_type_definition is not None
        assert obj.base_type_definition.base_type_size is None
        assert obj.base_type_definition.base_type_encoding is None