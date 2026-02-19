"""Unit tests for ARObject serialization."""

import pytest
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.limit import Limit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.interval_type_enum import (
    IntervalTypeEnum,
)
from armodel.serialization.decorators import xml_element_tag


class TestARObjectForSerialize(ARObject):
    """Test ARObject subclass for serialization tests."""

    def __init__(self):
        super().__init__()
        self.short_name: String = "test_name"
        self.category: str = "STANDARD"


class TestARObjectSerialize:
    """Unit tests for ARObject serialize functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.test_obj = TestARObjectForSerialize()

    def test_serialize_creates_element(self):
        """Test that serialize creates XML element with correct structure."""
        elem = self.test_obj.serialize()

        assert elem.tag == "TEST-A-R-OBJECT-FOR-SERIALIZE"
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
        from typing import Optional

        class TestObjectWithLimit(ARObject):
            def __init__(self):
                super().__init__()
                self.lower_limit: Optional[Limit] = None

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
        from typing import Optional

        class TestObjectWithLimit(ARObject):
            def __init__(self):
                super().__init__()
                self.lower_limit: Optional[Limit] = None

        obj = TestObjectWithLimit()
        obj.lower_limit = Limit(value="75")

        elem = obj.serialize()

        lower_limit_elem = elem.find("LOWER-LIMIT")
        assert lower_limit_elem is not None
        assert lower_limit_elem.text == "75"
        assert lower_limit_elem.get("INTERVAL-TYPE") is None


class TestARObjectPropertySerialization:
    """Test serialization of properties with custom XML tags."""

    def test_serialize_property_with_custom_tag(self):
        """Test that properties with @xml_element_tag decorator use custom tag."""
        class TestClass(ARObject):
            """Test class with custom tagged property."""

            def __init__(self) -> None:
                super().__init__()
                self._custom_value: Optional[str] = None

            @property
            @xml_element_tag("CUSTOM-TAG")
            def custom_value(self) -> Optional[str]:
                """Custom property with tag."""
                return self._custom_value

            @custom_value.setter
            def custom_value(self, value: Optional[str]) -> None:
                self._custom_value = value

        obj = TestClass()
        obj.custom_value = "test_value"

        elem = obj.serialize()

        # Should use CUSTOM-TAG, not CUSTOM-VALUE
        custom_elem = elem.find("CUSTOM-TAG")
        assert custom_elem is not None
        assert custom_elem.text == "test_value"
        # Should NOT have CUSTOM-VALUE
        assert elem.find("CUSTOM-VALUE") is None

    def test_serialize_property_with_none_value_skipped(self):
        """Test that properties with None values are skipped."""
        class TestClass(ARObject):
            """Test class with custom tagged property."""

            def __init__(self) -> None:
                super().__init__()
                self._custom_value: Optional[str] = None

            @property
            @xml_element_tag("CUSTOM-TAG")
            def custom_value(self) -> Optional[str]:
                """Custom property with tag."""
                return self._custom_value

            @custom_value.setter
            def custom_value(self, value: Optional[str]) -> None:
                self._custom_value = value

        obj = TestClass()
        # Don't set custom_value, it's None

        elem = obj.serialize()

        # Should not have CUSTOM-TAG element
        assert elem.find("CUSTOM-TAG") is None

    def test_serialize_property_with_serializable_object(self):
        """Test property with serializable ARObject value."""
        class InnerClass(ARObject):
            """Inner class."""

            def __init__(self) -> None:
                super().__init__()
                self.inner_value: str = "inner"

        class OuterClass(ARObject):
            """Outer class with property."""

            def __init__(self) -> None:
                super().__init__()
                self._inner: Optional[InnerClass] = None

            @property
            @xml_element_tag("INNER-OBJ")
            def inner(self) -> Optional[InnerClass]:
                """Inner object property."""
                return self._inner

            @inner.setter
            def inner(self, value: Optional[InnerClass]) -> None:
                self._inner = value

        obj = OuterClass()
        obj.inner = InnerClass()

        elem = obj.serialize()

        # Should have INNER-OBJ wrapper
        inner_elem = elem.find("INNER-OBJ")
        assert inner_elem is not None
        # Inner class should be serialized inside
        assert inner_elem.find("INNER-VALUE") is not None

    def test_serialize_property_with_primitive_value(self):
        """Test property with primitive (non-serializable) value."""
        class TestClass(ARObject):
            """Test class with property."""

            def __init__(self) -> None:
                super().__init__()
                self._value: int = 42

            @property
            @xml_element_tag("VALUE")
            def value(self) -> int:
                """Primitive property."""
                return self._value

            @value.setter
            def value(self, val: int) -> None:
                self._value = val

        obj = TestClass()

        elem = obj.serialize()

        # Should have VALUE element with text
        value_elem = elem.find("VALUE")
        assert value_elem is not None
        assert value_elem.text == "42"

    def test_serialize_property_with_attribute_error_continues(self):
        """Test that AttributeError on property getter is handled gracefully."""
        class TestClass(ARObject):
            """Test class with property that raises AttributeError."""

            @property
            @xml_element_tag("BROKEN-PROP")
            def broken_property(self) -> str:
                """Property that raises AttributeError."""
                raise AttributeError("Broken property")

        obj = TestClass()

        # Should not raise exception
        elem = obj.serialize()
        assert elem is not None
        assert elem.find("BROKEN-PROP") is None


class TestARObjectListSerialization:
    """Test list serialization with various item types."""

    def test_serialize_list_of_primitives(self):
        """Test serialization of list with primitive items."""
        class TestClass(ARObject):
            """Test class with list of primitives."""

            def __init__(self) -> None:
                super().__init__()
                self.items: list[str] = []

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

        obj = TestClass()

        elem = obj.serialize()

        items_elem = elem.find("ITEMS")
        assert items_elem is not None
        assert len(items_elem) == 0
