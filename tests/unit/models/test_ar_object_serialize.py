"""Unit tests for ARObject serialization."""

import pytest
import xml.etree.ElementTree as ET
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.limit import Limit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.interval_type_enum import (
    IntervalTypeEnum,
)
# Note: @xml_element_tag decorator has been removed from the framework


class MockARObjectForSerialize(ARObject):
    """Mock ARObject subclass for serialization tests."""

    def __init__(self):
        super().__init__()
        self.short_name: String = "test_name"
        self.category: str = "STANDARD"

    def serialize(self) -> ET.Element:
        """Serialize this test object."""
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Call parent's serialize to handle inherited attributes (checksum, timestamp)
        parent_elem = super().serialize()
        elem.attrib.update(parent_elem.attrib)
        for child in parent_elem:
            elem.append(child)

        # Serialize own attributes
        if self.short_name is not None:
            short_name_elem = ET.Element("SHORT-NAME")
            short_name_elem.text = str(self.short_name)
            elem.append(short_name_elem)

        if self.category is not None:
            category_elem = ET.Element("CATEGORY")
            category_elem.text = str(self.category)
            elem.append(category_elem)

        return elem


class TestARObjectSerialize:
    """Unit tests for ARObject serialize functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.test_obj = MockARObjectForSerialize()

    def test_serialize_creates_element(self):
        """Test that serialize creates XML element with correct structure."""
        elem = self.test_obj.serialize()

        assert elem.tag == "MOCK-A-R-OBJECT-FOR-SERIALIZE"
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("SHORT-NAME").text == "test_name"

    def test_serialize_converts_names(self):
        """Test that serialize converts snake_case to UPPER-CASE-WITH-HYPHENS."""
        elem = self.test_obj.serialize()

        # Verify snake_case → UPPER-CASE conversion
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("CATEGORY") is not None

    def test_serialize_with_arprimitive_wrapping(self) -> None:
        """Test that ARPrimitive types are wrapped with correct tag names."""

        class TestObjectWithLimit(ARObject):
            def __init__(self):
                super().__init__()
                self.lower_limit: Optional[Limit] = None

            def serialize(self) -> ET.Element:
                """Serialize this test object."""
                tag = SerializationHelper.get_xml_tag(self.__class__)
                elem = ET.Element(tag)

                # Call parent's serialize to handle inherited attributes (checksum, timestamp)
                parent_elem = super().serialize()
                elem.attrib.update(parent_elem.attrib)
                for child in parent_elem:
                    elem.append(child)

                # Serialize lower_limit
                if self.lower_limit is not None:
                    lower_limit_elem = ET.Element("LOWER-LIMIT")
                    if self.lower_limit.interval_type is not None:
                        lower_limit_elem.set("INTERVAL-TYPE", self.lower_limit.interval_type.value)
                    lower_limit_elem.text = str(self.lower_limit.value)
                    elem.append(lower_limit_elem)

                return elem

        obj = TestObjectWithLimit()
        obj.lower_limit = Limit(value="100", interval_type=IntervalTypeEnum.CLOSED)

        elem = obj.serialize()

        # Verify the Limit is wrapped with LOWER-LIMIT tag (not LIMIT)
        lower_limit_elem = elem.find("LOWER-LIMIT")
        assert lower_limit_elem is not None
        assert lower_limit_elem.tag == "LOWER-LIMIT"
        assert lower_limit_elem.text == "100"
        assert lower_limit_elem.get("INTERVAL-TYPE") == "CLOSED"

    def test_serialize_with_arprimitive_without_attributes(self) -> None:
        """Test that ARPrimitive without attributes is wrapped correctly."""

        class TestObjectWithLimit(ARObject):
            def __init__(self):
                super().__init__()
                self.lower_limit: Optional[Limit] = None

            def serialize(self) -> ET.Element:
                """Serialize this test object."""
                tag = SerializationHelper.get_xml_tag(self.__class__)
                elem = ET.Element(tag)

                # Call parent's serialize to handle inherited attributes (checksum, timestamp)
                parent_elem = super().serialize()
                elem.attrib.update(parent_elem.attrib)
                for child in parent_elem:
                    elem.append(child)

                # Serialize lower_limit
                if self.lower_limit is not None:
                    lower_limit_elem = ET.Element("LOWER-LIMIT")
                    if self.lower_limit.interval_type is not None:
                        lower_limit_elem.set("INTERVAL-TYPE", self.lower_limit.interval_type.value)
                    lower_limit_elem.text = str(self.lower_limit.value)
                    elem.append(lower_limit_elem)

                return elem

        obj = TestObjectWithLimit()
        obj.lower_limit = Limit(value="75")

        elem = obj.serialize()

        lower_limit_elem = elem.find("LOWER-LIMIT")
        assert lower_limit_elem is not None
        assert lower_limit_elem.text == "75"
        assert lower_limit_elem.get("INTERVAL-TYPE") is None


class TestARObjectListSerialization:
    """Test list serialization with various item types."""

    def test_serialize_list_of_primitives(self):
        """Test serialization of list with primitive items."""
        class TestClass(ARObject):
            """Test class with list of primitives."""

            def __init__(self) -> None:
                super().__init__()
                self.items: list[str] = []

            def serialize(self) -> ET.Element:
                """Serialize this test object."""
                tag = SerializationHelper.get_xml_tag(self.__class__)
                elem = ET.Element(tag)

                # Call parent's serialize to handle inherited attributes (checksum, timestamp)
                parent_elem = super().serialize()
                elem.attrib.update(parent_elem.attrib)
                for child in parent_elem:
                    elem.append(child)

                # Serialize items list
                if self.items:
                    items_elem = ET.Element("ITEMS")
                    for item in self.items:
                        item_elem = ET.Element("ITEM")
                        item_elem.text = str(item)
                        items_elem.append(item_elem)
                    elem.append(items_elem)

                return elem

        obj = TestClass()
        obj.items = ["item1", "item2", "item3"]

        elem = obj.serialize()

        items_elem = elem.find("ITEMS")
        assert items_elem is not None
        # List should create wrapper element
        assert len(items_elem) == 3
        # Each item should be a child element
        for child in items_elem:
            assert child.text in ["item1", "item2", "item3"]

    def test_serialize_list_of_integers(self):
        """Test serialization of list with integer items."""
        class TestClass(ARObject):
            """Test class with list of integers."""

            def __init__(self) -> None:
                super().__init__()
                self.numbers: list[int] = []

            def serialize(self) -> ET.Element:
                """Serialize this test object."""
                tag = SerializationHelper.get_xml_tag(self.__class__)
                elem = ET.Element(tag)

                # Call parent's serialize to handle inherited attributes (checksum, timestamp)
                parent_elem = super().serialize()
                elem.attrib.update(parent_elem.attrib)
                for child in parent_elem:
                    elem.append(child)

                # Serialize numbers list
                if self.numbers:
                    numbers_elem = ET.Element("NUMBERS")
                    for num in self.numbers:
                        num_elem = ET.Element("NUMBER")
                        num_elem.text = str(num)
                        numbers_elem.append(num_elem)
                    elem.append(numbers_elem)

                return elem

        obj = TestClass()
        obj.numbers = [1, 2, 3]

        elem = obj.serialize()

        numbers_elem = elem.find("NUMBERS")
        assert numbers_elem is not None
        assert len(numbers_elem) == 3
        assert numbers_elem[0].text == "1"
        assert numbers_elem[1].text == "2"
        assert numbers_elem[2].text == "3"

    def test_serialize_empty_list(self):
        """Test serialization of empty list."""
        class TestClass(ARObject):
            """Test class with empty list."""

            def __init__(self) -> None:
                super().__init__()
                self.items: list[str] = []

            def serialize(self) -> ET.Element:
                """Serialize this test object."""
                tag = SerializationHelper.get_xml_tag(self.__class__)
                elem = ET.Element(tag)

                # Call parent's serialize to handle inherited attributes (checksum, timestamp)
                parent_elem = super().serialize()
                elem.attrib.update(parent_elem.attrib)
                for child in parent_elem:
                    elem.append(child)

                # Serialize items list (empty, so no element created)
                if self.items:
                    items_elem = ET.Element("ITEMS")
                    for item in self.items:
                        item_elem = ET.Element("ITEM")
                        item_elem.text = str(item)
                        items_elem.append(item_elem)
                    elem.append(items_elem)

                return elem

        obj = TestClass()

        elem = obj.serialize()

        items_elem = elem.find("ITEMS")
        # Empty lists should not create an element
        assert items_elem is None
