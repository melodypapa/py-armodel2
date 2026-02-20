"""Unit tests for ARObject serialization."""

import pytest
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.limit import Limit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.interval_type_enum import (
    IntervalTypeEnum,
)
# Note: @xml_element_tag decorator has been removed from the framework


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
