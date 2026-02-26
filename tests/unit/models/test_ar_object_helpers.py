"""Unit tests for ARObject helper methods."""

import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
# Note: @xml_element_tag decorator has been removed from the framework


class TestARObjectHelperMethods:
    """Test helper static methods."""

    def test_strip_namespace_with_namespace(self):
        """Test stripping namespace from tag."""
        tag = "{http://autosar.org/schema/r4.0}ELEMENT"
        result = SerializationHelper.strip_namespace(tag)
        assert result == "ELEMENT"

    def test_strip_namespace_without_namespace(self):
        """Test tag without namespace."""
        tag = "ELEMENT"
        result = SerializationHelper.strip_namespace(tag)
        assert result == "ELEMENT"

    def test_get_element_tag_auto_generated(self):
        """Test auto-generating element tag from attribute name."""
        tag = SerializationHelper.get_element_tag("my_attribute")
        assert tag == "MY-ATTRIBUTE"

    def test_add_text_element_with_value(self):
        """Test adding text element with value."""
        parent = ET.Element("PARENT")
        SerializationHelper.add_text_element(parent, "CHILD", "value")

        child = parent.find("CHILD")
        assert child is not None
        assert child.text == "value"

    def test_add_text_element_with_none(self):
        """Test adding text element with None value does nothing."""
        parent = ET.Element("PARENT")
        SerializationHelper.add_text_element(parent, "CHILD", None)

        assert len(parent) == 0

    def test_extract_text_from_element(self):
        """Test extracting text from element."""
        elem = ET.Element("TEST")
        elem.text = "hello"

        result = SerializationHelper.extract_text(elem)
        assert result == "hello"

    def test_extract_text_from_element_with_whitespace(self):
        """Test extracting text with whitespace."""
        elem = ET.Element("TEST")
        elem.text = "  hello  "

        result = SerializationHelper.extract_text(elem)
        assert result == "hello"

    def test_extract_text_from_empty_element(self):
        """Test extracting text from empty element."""
        elem = ET.Element("TEST")
        elem.text = ""

        result = SerializationHelper.extract_text(elem)
        assert result is None

    def test_extract_text_from_none_element(self):
        """Test extracting text from None element."""
        result = SerializationHelper.extract_text(None)
        assert result is None

    def test_extract_text_with_tag(self):
        """Test extracting text with tag search."""
        parent = ET.Element("PARENT")
        child = ET.Element("CHILD")
        child.text = "value"
        parent.append(child)

        result = SerializationHelper.extract_text(parent, "CHILD")
        assert result == "value"

    def test_extract_text_with_tag_not_found(self):
        """Test extracting text with tag not found."""
        parent = ET.Element("PARENT")

        result = SerializationHelper.extract_text(parent, "MISSING")
        assert result is None

    def test_import_class_by_name_existing(self):
        """Test importing existing class by name."""
        cls = SerializationHelper.import_class_by_name("ARPackage")
        assert cls is not None
        assert cls.__name__ == "ARPackage"

    def test_import_class_by_name_nonexistent(self):
        """Test importing non-existent class returns None."""
        cls = SerializationHelper.import_class_by_name("NonExistentClass")
        assert cls is None

    def test_is_xml_attribute_static_with_property(self):
        """Test checking if attribute is XML attribute via property."""
        class TestClass(ARObject):
            """Test class."""

            @property
            def test_prop(self) -> str:
                """Test property."""
                return "value"

        # Without decorator, should be False
        result = SerializationHelper.is_xml_attribute_static(TestClass, "test_prop")
        assert result is False

    def test_is_xml_attribute_static_with_attribute(self):
        """Test checking if attribute is XML attribute via attribute."""
        class TestClass(ARObject):
            """Test class."""

            test_attr = "value"

        result = SerializationHelper.is_xml_attribute_static(TestClass, "test_attr")
        assert result is False

    def test_is_xml_attribute_static_nonexistent(self):
        """Test checking non-existent attribute."""
        class TestClass(ARObject):
            """Test class."""

        result = SerializationHelper.is_xml_attribute_static(TestClass, "nonexistent")
        assert result is False