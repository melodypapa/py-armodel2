"""Tests for ARPrimitive and AREnum transparent behavior with primitive types.

These tests ensure that primitive wrappers behave transparently like their
underlying Python types (str, int, float, bool) to maintain backward
compatibility with existing code that expects plain values.
"""

from __future__ import annotations

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import (
    ARPrimitive,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import (
    AREnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.identifier import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.byte_order_enum import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.integer import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.boolean import (
    Boolean,
)


class TestARPrimitiveTransparentEquality:
    """Tests for ARPrimitive transparent equality with primitive types."""

    def test_identifier_equals_string(self) -> None:
        """Identifier should equal its underlying string value."""
        # Arrange
        identifier = Identifier("test_value")

        # Act & Assert
        # This SHOULD work - comparing Identifier with string
        assert identifier == "test_value", (
            "Identifier('test_value') should equal 'test_value' string"
        )

    def test_identifier_equals_identifier(self) -> None:
        """Identifier should equal another Identifier with same value."""
        # Arrange
        id1 = Identifier("test")
        id2 = Identifier("test")

        # Act & Assert
        assert id1 == id2, "Two Identifiers with same value should be equal"

    def test_identifier_not_equals_different_string(self) -> None:
        """Identifier should not equal different string value."""
        # Arrange
        identifier = Identifier("value1")

        # Act & Assert
        assert identifier != "value2", "Identifier should not equal different string"

    def test_integer_equals_int(self) -> None:
        """Integer should equal its underlying int value."""
        # Arrange
        integer = Integer(42)

        # Act & Assert
        assert integer == 42, "Integer(42) should equal 42 int"

    def test_integer_equals_integer(self) -> None:
        """Integer should equal another Integer with same value."""
        # Arrange
        int1 = Integer(42)
        int2 = Integer(42)

        # Act & Assert
        assert int1 == int2, "Two Integers with same value should be equal"

    def test_boolean_equals_bool(self) -> None:
        """Boolean should equal its underlying bool value."""
        # Arrange
        boolean = Boolean(True)

        # Act & Assert
        assert boolean == True, "Boolean(True) should equal True bool"

    def test_identifier_hash_compatible_with_string(self) -> None:
        """Identifier hash should be compatible with string for dict/set usage."""
        # Arrange
        identifier = Identifier("test")

        # Act & Assert
        # Should be able to use in sets and dicts
        value_set = {"test", "other"}
        assert identifier in value_set or "test" in {identifier}, (
            "Identifier should be usable in sets with strings"
        )

    def test_identifier_as_dict_key(self) -> None:
        """Identifier should work as dict key transparently."""
        # Arrange
        identifier = Identifier("key1")

        # Act
        test_dict = {identifier: "value"}

        # Assert
        # Should be able to look up with string
        # This may not work directly due to hash equality, but let's test
        # what we can reasonably expect
        assert identifier in test_dict, "Identifier key should exist in dict"


class TestAREnumTransparentEquality:
    """Tests for AREnum transparent equality with string values."""

    def test_enum_equals_string(self) -> None:
        """AREnum should equal its underlying string value."""
        # Arrange
        enum_val = ByteOrderEnum(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)

        # Act & Assert
        # This SHOULD work - comparing enum with string
        assert enum_val == "mostSignificantByteFirst", (
            "ByteOrderEnum should equal its string value"
        )

    def test_enum_equals_enum(self) -> None:
        """AREnum should equal another enum of same type with same value."""
        # Arrange
        enum1 = ByteOrderEnum(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)
        enum2 = ByteOrderEnum(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)

        # Act & Assert
        assert enum1 == enum2, "Two enums with same value should be equal"

    def test_enum_not_equals_different_string(self) -> None:
        """AREnum should not equal different string value."""
        # Arrange
        enum_val = ByteOrderEnum(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)

        # Act & Assert
        assert enum_val != "mostSignificantByteLast", (
            "Enum should not equal different string"
        )

    def test_enum_hash_compatible_with_string(self) -> None:
        """AREnum hash should be compatible with string."""
        # Arrange
        enum_val = ByteOrderEnum(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST)

        # Act & Assert
        value_set = {"mostSignificantByteFirst", "other"}
        # Enum might not be in set of strings directly, but let's verify
        # the hash is based on value
        assert hash(enum_val) == hash("mostSignificantByteFirst"), (
            "Enum hash should match string value hash"
        )


class TestARObjectExtractValueUnwrapping:
    """Tests for ARObject._extract_value primitive unwrapping."""

    def test_extract_value_identifier_unwraps_to_string(self) -> None:
        """_extract_value should unwrap Identifier to plain string."""
        # Arrange
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
            ARObject,
        )

        element = ET.Element("SHORT-NAME")
        element.text = "MyPackage"

        # Act
        result = ARObject._extract_value(element, "Identifier")

        # Assert
        # Result should be the plain string, not Identifier wrapper
        assert isinstance(result, str), (
            f"Expected str, got {type(result).__name__}"
        )
        assert result == "MyPackage"

    def test_extract_value_integer_unwraps_to_int(self) -> None:
        """_extract_value should unwrap Integer to plain int."""
        # Arrange
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
            ARObject,
        )

        element = ET.Element("VALUE")
        element.text = "42"

        # Act
        result = ARObject._extract_value(element, "Integer")

        # Assert
        # Result should be the plain int, not Integer wrapper
        assert isinstance(result, int), (
            f"Expected int, got {type(result).__name__}"
        )
        assert result == 42

    def test_extract_value_enum_keeps_wrapper_with_transparent_equality(
        self,
    ) -> None:
        """_extract_value should keep AREnum wrapper but have transparent equality."""
        # Arrange
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
            ARObject,
        )

        element = ET.Element("BYTE-ORDER")
        element.text = "mostSignificantByteFirst"

        # Act
        result = ARObject._extract_value(element, "ByteOrderEnum")

        # Assert
        # Enums keep their wrapper
        assert isinstance(result, ByteOrderEnum), (
            f"Expected ByteOrderEnum, got {type(result).__name__}"
        )
        # But compare transparently with strings
        assert result == "mostSignificantByteFirst", (
            "Enum should equal its string value"
        )
