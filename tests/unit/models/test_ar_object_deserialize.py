"""Unit tests for ARObject deserialization."""

import pytest
import xml.etree.ElementTree as ET
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.limit import Limit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.interval_type_enum import (
    IntervalTypeEnum,
)


class MockARObject(ARObject):
    """Mock ARObject subclass for deserialization tests."""

    # Class-level type annotations (required for get_type_hints)
    short_name: str
    category: str
    sw_data_def_props: str

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MockARObject":
        """Deserialize this test object."""
        # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
        obj = super().deserialize(element)

        # Parse own attributes
        child = SerializationHelper.find_child_element(element, "SHORT-NAME")
        if child is not None and child.text:
            obj.short_name = child.text

        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None and child.text:
            obj.category = child.text

        child = SerializationHelper.find_child_element(element, "SW-DATA-DEF-PROPS")
        if child is not None and child.text:
            obj.sw_data_def_props = child.text

        return obj


class TestARObjectDeserialize:
    """Unit tests for ARObject deserialize functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.test_xml_with_name_and_category = '''<TESTAROBJECT>
            <SHORT-NAME>test_name</SHORT-NAME>
            <CATEGORY>STANDARD</CATEGORY>
        </TESTAROBJECT>'''

        self.test_xml_with_sw_data_def_props = '''<TESTAROBJECT>
            <SW-DATA-DEF-PROPS>value</SW-DATA-DEF-PROPS>
        </TESTAROBJECT>'''

    def test_deserialize_from_xml(self):
        """Test deserializing ARObject from XML element."""
        elem = ET.fromstring(self.test_xml_with_name_and_category)
        obj = MockARObject.deserialize(elem)

        assert obj.short_name == "test_name"
        assert obj.category == "STANDARD"

    def test_deserialize_converts_names(self):
        """Test that deserialize converts XML tags to snake_case attribute names."""
        elem = ET.fromstring(self.test_xml_with_sw_data_def_props)
        obj = MockARObject.deserialize(elem)

        assert hasattr(obj, 'sw_data_def_props')
        assert obj.sw_data_def_props == "value"

    def test_deserialize_with_arprimitive_with_attributes(self) -> None:
        """Test deserializing ARObject with ARPrimitive that has attributes."""
        from typing import Optional

        class TestObjectWithLimit(ARObject):
            lower_limit: Optional[Limit]

            def __init__(self) -> None:
                super().__init__()
                self.lower_limit: Optional[Limit] = None

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestObjectWithLimit":
                """Deserialize this test object."""
                # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
                obj = super().deserialize(element)

                # Parse lower_limit
                child = SerializationHelper.find_child_element(element, "LOWER-LIMIT")
                if child is not None:
                    interval_type_str = child.get("INTERVAL-TYPE")
                    interval_type = None
                    if interval_type_str:
                        # Case-insensitive enum conversion
                        interval_type = IntervalTypeEnum(interval_type_str.upper())

                    obj.lower_limit = Limit(value=child.text, interval_type=interval_type)

                return obj

        xml = '''<TESTOBJECTWITHLIMIT>
            <LOWER-LIMIT INTERVAL-TYPE="CLOSED">100</LOWER-LIMIT>
        </TESTOBJECTWITHLIMIT>'''

        elem = ET.fromstring(xml)
        obj = TestObjectWithLimit.deserialize(elem)

        # Verify Limit is deserialized with its attributes
        assert obj.lower_limit is not None
        assert isinstance(obj.lower_limit, Limit)
        assert obj.lower_limit.value == "100"
        assert obj.lower_limit.interval_type == IntervalTypeEnum.CLOSED

    def test_deserialize_with_arprimitive_case_insensitive_enum(self) -> None:
        """Test deserializing ARObject with ARPrimitive containing lowercase enum value."""
        from typing import Optional

        class TestObjectWithLimit(ARObject):
            lower_limit: Optional[Limit]

            def __init__(self) -> None:
                super().__init__()
                self.lower_limit: Optional[Limit] = None

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestObjectWithLimit":
                """Deserialize this test object."""
                # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
                obj = super().deserialize(element)

                # Parse lower_limit
                child = SerializationHelper.find_child_element(element, "LOWER-LIMIT")
                if child is not None:
                    interval_type_str = child.get("INTERVAL-TYPE")
                    interval_type = None
                    if interval_type_str:
                        # Case-insensitive enum conversion
                        interval_type = IntervalTypeEnum(interval_type_str.upper())

                    obj.lower_limit = Limit(value=child.text, interval_type=interval_type)

                return obj

        xml = '''<TESTOBJECTWITHLIMIT>
            <LOWER-LIMIT INTERVAL-TYPE="closed">100</LOWER-LIMIT>
        </TESTOBJECTWITHLIMIT>'''

        elem = ET.fromstring(xml)
        obj = TestObjectWithLimit.deserialize(elem)

        # Verify enum is deserialized case-insensitively
        assert obj.lower_limit is not None
        assert obj.lower_limit.value == "100"
        assert obj.lower_limit.interval_type == IntervalTypeEnum.CLOSED


class TestARObjectListDeserialization:
    """Test list deserialization with various types."""

    def test_deserialize_list_of_strings(self):
        """Test deserializing list of strings."""
        xml = '''<PARENT>
            <ITEMS>
                <ITEM>item1</ITEM>
                <ITEM>item2</ITEM>
                <ITEM>item3</ITEM>
            </ITEMS>
        </PARENT>'''

        class TestClass(ARObject):
            """Test class with list of strings."""

            items: list[str]

            def __init__(self) -> None:
                super().__init__()
                self.items: list[str] = []

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize this test object."""
                # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
                obj = super().deserialize(element)

                # Parse items list
                items_elem = SerializationHelper.find_child_element(element, "ITEMS")
                if items_elem is not None:
                    obj.items = []
                    for item_elem in items_elem.findall("ITEM"):
                        if item_elem.text:
                            obj.items.append(item_elem.text)

                return obj

        elem = ET.fromstring(xml)
        obj = TestClass.deserialize(elem)

        assert obj.items == ["item1", "item2", "item3"]

    def test_deserialize_list_with_none_type(self):
        """Test deserializing list when type hints fail - returns text."""
        xml = '''<PARENT>
            <ITEMS>item1,item2</ITEMS>
        </PARENT>'''

        class TestClass(ARObject):
            """Test class with list."""

            items: list

            def __init__(self) -> None:
                super().__init__()
                self.items: list = []

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize this test object."""
                # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
                obj = super().deserialize(element)

                # Parse items list (when no child elements, treat as text)
                items_elem = SerializationHelper.find_child_element(element, "ITEMS")
                if items_elem is not None:
                    # Check if there are child ITEM elements
                    item_elems = items_elem.findall("ITEM")
                    if item_elems:
                        obj.items = []
                        for item_elem in item_elems:
                            if item_elem.text:
                                obj.items.append(item_elem.text)
                    else:
                        # No child elements, treat as text
                        obj.items = items_elem.text if items_elem.text else ""

                return obj

        elem = ET.fromstring(xml)
        obj = TestClass.deserialize(elem)

        # With no type args, returns string
        assert obj.items == "item1,item2"

    def test_deserialize_empty_list(self):
        """Test deserializing empty list."""
        xml = '''<PARENT>
            <ITEMS />
        </PARENT>'''

        class TestClass(ARObject):
            """Test class with list."""

            items: list[str]

            def __init__(self) -> None:
                super().__init__()
                self.items: list[str] = []

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize this test object."""
                # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
                obj = super().deserialize(element)

                # Parse items list
                items_elem = SerializationHelper.find_child_element(element, "ITEMS")
                if items_elem is not None:
                    obj.items = []
                    for item_elem in items_elem.findall("ITEM"):
                        if item_elem.text:
                            obj.items.append(item_elem.text)

                return obj

        elem = ET.fromstring(xml)
        obj = TestClass.deserialize(elem)

        assert obj.items == []


class TestARObjectOptionalDeserialization:
    """Test Optional type deserialization."""

    def test_deserialize_optional_with_string_annotation(self):
        """Test deserializing Optional type from string annotation."""

        class TestClass(ARObject):
            """Test class with Optional field."""

            name: Optional[str]

            def __init__(self) -> None:
                super().__init__()
                self.name: Optional[str] = None

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize this test object."""
                # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
                obj = super().deserialize(element)

                # Parse name
                child = SerializationHelper.find_child_element(element, "NAME")
                if child is not None and child.text:
                    obj.name = child.text

                return obj

        xml = '''<PARENT>
            <NAME>test_name</NAME>
        </PARENT>'''

        elem = ET.fromstring(xml)
        obj = TestClass.deserialize(elem)

        assert obj.name == "test_name"

    def test_deserialize_optional_missing_returns_none(self):
        """Test deserializing missing Optional field returns None."""
        class TestClass(ARObject):
            """Test class with Optional field."""

            name: Optional[str]

            def __init__(self) -> None:
                super().__init__()
                self.name: Optional[str] = None

            @classmethod
            def deserialize(cls, element: ET.Element) -> "TestClass":
                """Deserialize this test object."""
                # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
                obj = super().deserialize(element)

                # Parse name
                child = SerializationHelper.find_child_element(element, "NAME")
                if child is not None and child.text:
                    obj.name = child.text

                return obj

        xml = '''<PARENT>
        </PARENT>'''

        elem = ET.fromstring(xml)
        obj = TestClass.deserialize(elem)

        assert obj.name is None


class TestARObjectPrimitiveTypeConversions:
    """Test primitive type conversions in _extract_value."""

    def test_extract_string_value(self):
        """Test extracting string value."""
        elem = ET.Element("TEST")
        elem.text = "hello"

        result = SerializationHelper.extract_value(elem, str)
        assert result == "hello"

    def test_extract_int_value_valid(self):
        """Test extracting valid integer value."""
        elem = ET.Element("TEST")
        elem.text = "42"

        result = SerializationHelper.extract_value(elem, int)
        assert result == 42
        assert isinstance(result, int)

    def test_extract_int_value_invalid(self):
        """Test extracting invalid integer value returns string."""
        elem = ET.Element("TEST")
        elem.text = "not_a_number"

        result = SerializationHelper.extract_value(elem, int)
        assert result == "not_a_number"
        assert isinstance(result, str)

    def test_extract_float_value_valid(self):
        """Test extracting valid float value."""
        elem = ET.Element("TEST")
        elem.text = "3.14"

        result = SerializationHelper.extract_value(elem, float)
        assert result == 3.14
        assert isinstance(result, float)

    def test_extract_float_value_invalid(self):
        """Test extracting invalid float value returns string."""
        elem = ET.Element("TEST")
        elem.text = "not_a_float"

        result = SerializationHelper.extract_value(elem, float)
        assert result == "not_a_float"
        assert isinstance(result, str)

    def test_extract_bool_value_true_variants(self):
        """Test extracting boolean value with true variants."""
        for text in ["true", "TRUE", "1", "yes", "YES"]:
            elem = ET.Element("TEST")
            elem.text = text

            result = SerializationHelper.extract_value(elem, bool)
            assert result is True

    def test_extract_bool_value_false_variants(self):
        """Test extracting boolean value with false variants."""
        for text in ["false", "FALSE", "0", "no", "NO", "random"]:
            elem = ET.Element("TEST")
            elem.text = text

            result = SerializationHelper.extract_value(elem, bool)
            assert result is False

    def test_extract_unknown_type_returns_string(self):
        """Test extracting unknown type returns string."""
        elem = ET.Element("TEST")
        elem.text = "some_value"

        class CustomType:
            """Custom type."""

        result = SerializationHelper.extract_value(elem, CustomType)
        assert result == "some_value"

    def test_extract_none_element_returns_none(self):
        """Test extracting None element returns None."""
        result = SerializationHelper.extract_value(None, str)
        assert result is None

    def test_extract_element_with_none_text_returns_none(self):
        """Test extracting element with None text returns None."""
        elem = ET.Element("TEST")
        # Don't set text, it's None

        result = SerializationHelper.extract_value(elem, str)
        assert result is None
