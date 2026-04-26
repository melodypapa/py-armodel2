"""Unit tests for SerializationHelper polymorphic methods."""

import pytest
import xml.etree.ElementTree as ET
from armodel2.serialization import SerializationHelper
from armodel2.serialization.decorators import polymorphic


class TestHasPolymorphic:
    """Test has_polymorphic method."""

    def test_has_polymorphic_with_decorator(self):
        """Test has_polymorphic returns True when decorator is present."""
        class TestClass:
            @polymorphic({"VALUE-SPEC": "ValueSpecification"})
            def test_attr(self):
                pass

        assert SerializationHelper.has_polymorphic(TestClass, "test_attr") is True

    def test_has_polymorphic_without_decorator(self):
        """Test has_polymorphic returns False when decorator is absent."""
        class TestClass:
            def test_attr(self):
                pass

        assert SerializationHelper.has_polymorphic(TestClass, "test_attr") is False

    def test_has_polymorphic_with_property(self):
        """Test has_polymorphic works with properties."""
        class TestClass:
            def __init__(self):
                self._value = None

            @property
            @polymorphic({"VALUE-SPEC": "ValueSpecification"})
            def test_prop(self):
                return self._value

        assert SerializationHelper.has_polymorphic(TestClass, "test_prop") is True

    def test_has_polymorphic_nonexistent_attribute(self):
        """Test has_polymorphic returns False for nonexistent attribute."""
        class TestClass:
            pass

        assert SerializationHelper.has_polymorphic(TestClass, "nonexistent") is False


class TestGetPolymorphicMapping:
    """Test get_polymorphic_mapping method."""

    def test_get_polymorphic_mapping_single(self):
        """Test get_polymorphic_mapping returns correct mapping for single entry."""
        class TestClass:
            @polymorphic({"VALUE-SPEC": "ValueSpecification"})
            def test_attr(self):
                pass

        mapping = SerializationHelper.get_polymorphic_mapping(TestClass, "test_attr")
        assert mapping == {"VALUE-SPEC": "ValueSpecification"}

    def test_get_polymorphic_mapping_multiple(self):
        """Test get_polymorphic_mapping returns correct mapping for multiple entries."""
        class TestClass:
            @polymorphic({
                "COMPU-INTERNAL-TO-PHYS": "CompuContent",
                "COMPU-PHYS-TO-INTERNAL": "CompuContent"
            })
            def test_attr(self):
                pass

        mapping = SerializationHelper.get_polymorphic_mapping(TestClass, "test_attr")
        assert mapping == {
            "COMPU-INTERNAL-TO-PHYS": "CompuContent",
            "COMPU-PHYS-TO-INTERNAL": "CompuContent"
        }

    def test_get_polymorphic_mapping_without_decorator(self):
        """Test get_polymorphic_mapping returns None when decorator is absent."""
        class TestClass:
            def test_attr(self):
                pass

        mapping = SerializationHelper.get_polymorphic_mapping(TestClass, "test_attr")
        assert mapping is None


class TestDeserializePolymorphic:
    """Test deserialize_polymorphic method."""

    def test_deserialize_polymorphic_with_empty_wrapper(self):
        """Test deserializing empty wrapper returns None."""
        wrapper = ET.Element("VALUE-SPEC")
        result = SerializationHelper.deserialize_polymorphic(wrapper, "ValueSpecification")
        assert result is None

    def test_deserialize_polymorphic_with_invalid_child(self):
        """Test deserializing wrapper with invalid concrete type raises ValueError."""
        wrapper = ET.Element("VALUE-SPEC")
        child = ET.SubElement(wrapper, "INVALID-TYPE")
        child.text = "test"

        # The ModelFactory raises ImportError for unknown types
        # which gets wrapped by deserialize_polymorphic's ValueError
        with pytest.raises((ValueError, ImportError)):
            SerializationHelper.deserialize_polymorphic(wrapper, "ValueSpecification")


class TestWrapAndAppend:
    """Test wrap_and_append method for generated serialize code."""

    def test_wrap_and_append_basic(self):
        """Test basic wrap_and_append functionality."""
        parent = ET.Element("PARENT")
        child = ET.Element("CHILD")
        child.text = "content"
        child.attrib["attr"] = "value"

        SerializationHelper.wrap_and_append(parent, child, "WRAPPER")

        # Parent should have one child
        assert len(parent) == 1
        # Wrapper should have correct tag
        wrapper = parent[0]
        assert wrapper.tag == "WRAPPER"
        # Wrapper should have child's text
        assert wrapper.text == "content"
        # Wrapper should have child's attributes
        assert wrapper.attrib.get("attr") == "value"

    def test_wrap_and_append_with_nested_children(self):
        """Test wrap_and_append with nested children."""
        parent = ET.Element("PARENT")
        child = ET.Element("CHILD")
        subchild = ET.Element("SUBCHILD")
        subchild.text = "nested"
        child.append(subchild)

        SerializationHelper.wrap_and_append(parent, child, "WRAPPER")

        wrapper = parent[0]
        assert len(wrapper) == 1
        assert wrapper[0].tag == "SUBCHILD"
        assert wrapper[0].text == "nested"

    def test_wrap_and_append_empty_child(self):
        """Test wrap_and_append with empty child."""
        parent = ET.Element("PARENT")
        child = ET.Element("CHILD")

        SerializationHelper.wrap_and_append(parent, child, "WRAPPER")

        wrapper = parent[0]
        assert wrapper.tag == "WRAPPER"
        assert wrapper.text is None
        assert len(wrapper.attrib) == 0

    def test_wrap_and_append_preserves_all_attributes(self):
        """Test wrap_and_append preserves multiple attributes."""
        parent = ET.Element("PARENT")
        child = ET.Element("CHILD")
        child.attrib["attr1"] = "value1"
        child.attrib["attr2"] = "value2"
        child.attrib["DEST"] = "SomeType"

        SerializationHelper.wrap_and_append(parent, child, "WRAPPER")

        wrapper = parent[0]
        assert wrapper.attrib.get("attr1") == "value1"
        assert wrapper.attrib.get("attr2") == "value2"
        assert wrapper.attrib.get("DEST") == "SomeType"
