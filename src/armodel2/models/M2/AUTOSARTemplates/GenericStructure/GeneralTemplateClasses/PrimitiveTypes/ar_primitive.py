"""ARPrimitive base class for all AUTOSAR primitive types."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.serialization.serialization_helper import SerializationHelper

class ARPrimitive:
    """Base class for all AUTOSAR primitive types.

    All primitive types (String, Integer, Float, etc.) inherit from this class.
    Provides common functionality for value wrapping and serialization.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[Any] = None, _original_text: Optional[str] = None) -> None:
        """Initialize ARPrimitive.

        Args:
            value: The primitive value
            _original_text: Original XML text representation (for preserving format)
        """
        self.value: Optional[Any] = value
        self._original_text: Optional[str] = _original_text  # Preserve original XML text format

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the primitive to an XML element.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this primitive
        """
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        if namespace:
            elem.set("xmlns", namespace)

        if self.value is not None:
            # Preserve original format for binary-exact round-trip serialization
            if self._original_text is not None:
                # Use original text format for floats and booleans
                if isinstance(self.value, (float, bool)):
                    elem.text = self._original_text
                else:
                    elem.text = str(self.value)
            else:
                elem.text = str(self.value)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPrimitive":
        """Deserialize an XML element to an ARPrimitive instance.

        Automatically converts the text content to the appropriate Python type
        based on the python_type class attribute.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARPrimitive instance
        """
        obj = cls()
        if element.text:
            # Preserve original format for binary-exact serialization
            original_text = element.text

            # Convert to the appropriate Python type based on python_type
            if cls.python_type is str:
                obj.value = original_text
            elif cls.python_type is int:
                try:
                    obj.value = int(original_text)
                except ValueError:
                    obj.value = original_text  # Keep as string if conversion fails
            elif cls.python_type is float:
                try:
                    obj.value = float(original_text)
                except ValueError:
                    obj.value = original_text
            elif cls.python_type is bool:
                obj.value = original_text.lower() in ('true', '1', 'yes')
            else:
                obj.value = original_text

            # Store original text for format preservation during serialization
            obj._original_text = original_text
        return obj

    def __str__(self) -> str:
        """Return string representation of the primitive value."""
        return str(self.value) if self.value is not None else ""

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}({self.value!r})"

    def __eq__(self, other: object) -> bool:
        """Check equality based on value.

        Provides transparent comparison with primitive Python types (str, int, float, bool).

        Args:
            other: Object to compare with

        Returns:
            True if values are equal (both same class or primitive type), False otherwise
        """
        # Compare with same class (existing behavior)
        if isinstance(other, self.__class__):
            return self.value == other.value
        # Compare with primitive Python type (transparent behavior)
        if isinstance(other, self.python_type):
            return self.value == other
        return NotImplemented

    def __hash__(self) -> int:
        """Return hash based on value.

        Returns:
            Hash of the value, or hash of None if value is None
        """
        return hash(self.value) if self.value is not None else hash(None)
