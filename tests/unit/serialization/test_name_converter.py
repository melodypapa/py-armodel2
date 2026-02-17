"""Unit tests for NameConverter."""

import pytest
from armodel.serialization.name_converter import NameConverter


class TestNameConverter:
    """Unit tests for NameConverter."""

    def test_to_xml_tag_snake_case(self) -> None:
        """Test converting snake_case to XML tag."""
        assert NameConverter.to_xml_tag("short_name") == "SHORT-NAME"
        assert NameConverter.to_xml_tag("sw_data_def_props") == "SW-DATA-DEF-PROPS"

    def test_to_xml_tag_pascal_case(self) -> None:
        """Test converting PascalCase to XML tag."""
        assert NameConverter.to_xml_tag("SwBaseType") == "SW-BASE-TYPE"
        assert NameConverter.to_xml_tag("ImplementationDataType") == "IMPLEMENTATION-DATA-TYPE"

    def test_to_xml_tag_ar_prefix(self) -> None:
        """Test converting AR prefix class names."""
        assert NameConverter.to_xml_tag("ARPackage") == "AR-PACKAGE"
        assert NameConverter.to_xml_tag("ARObject") == "AR-OBJECT"

    def test_to_xml_tag_all_caps(self) -> None:
        """Test converting all caps class names."""
        assert NameConverter.to_xml_tag("AUTOSAR") == "AUTOSAR"

    def test_to_python_name(self) -> None:
        """Test converting XML tag to snake_case."""
        assert NameConverter.to_python_name("SHORT-NAME") == "short_name"
        assert NameConverter.to_python_name("SW-DATA-DEF-PROPS") == "sw_data_def_props"

    def test_to_singular(self) -> None:
        """Test converting plural tags to singular."""
        assert NameConverter.to_singular("AR-PACKAGES") == "AR-PACKAGE"
        assert NameConverter.to_singular("ELEMENTS") == "ELEMENT"
        assert NameConverter.to_singular("PACKAGES") == "PACKAGE"

    def test_tag_to_class_name_simple(self) -> None:
        """Test converting XML tag to class name."""
        assert NameConverter.tag_to_class_name("SW-BASE-TYPE") == "SwBaseType"
        assert NameConverter.tag_to_class_name("IMPLEMENTATION-DATA-TYPE") == "ImplementationDataType"

    def test_tag_to_class_name_ar_prefix(self) -> None:
        """Test converting XML tag with AR prefix to class name."""
        assert NameConverter.tag_to_class_name("AR-PACKAGE") == "ARPackage"
        assert NameConverter.tag_to_class_name("AR-OBJECT") == "ARObject"

    def test_tag_to_class_name_all_caps(self) -> None:
        """Test converting all caps XML tag to class name."""
        assert NameConverter.tag_to_class_name("AUTOSAR") == "AUTOSAR"

    def test_tag_to_class_name_simple_word(self) -> None:
        """Test converting simple XML tag to class name."""
        assert NameConverter.tag_to_class_name("SHORT-NAME") == "ShortName"
        assert NameConverter.tag_to_class_name("CATEGORY") == "Category"

    def test_round_trip_pascal_case(self) -> None:
        """Test round-trip conversion: PascalCase → XML tag → PascalCase."""
        original = "SwBaseType"
        xml_tag = NameConverter.to_xml_tag(original)
        result = NameConverter.tag_to_class_name(xml_tag)
        assert result == original

    def test_round_trip_snake_case(self) -> None:
        """Test round-trip conversion: snake_case → XML tag → snake_case."""
        original = "short_name"
        xml_tag = NameConverter.to_xml_tag(original)
        result = NameConverter.to_python_name(xml_tag)
        assert result == original