"""AREnum base class for all AUTOSAR enumeration types."""

from __future__ import annotations
import xml.etree.ElementTree as ET
from enum import Enum

class AREnum(Enum):
    """Base class for all AUTOSAR enumeration types.

    All enumeration types inherit from this class.
    Provides common functionality for enum value serialization.
    """

    def __init__(self) -> None:
        """Initialize AREnum."""
        super().__init__()

    def serialize(self, namespace: str = "") -> ET.Element:
        """Serialize the enum to an XML element.

        Args:
            namespace: XML namespace URI (optional)

        Returns:
            xml.etree.ElementTree.Element representing this enum value
        """
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        if namespace:
            elem.set("xmlns", namespace)

        # Get the value from the enum and convert to uppercase
        if hasattr(self, 'value'):
            elem.text = str(self.value).upper()
        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AREnum":
        """Deserialize an XML element to an AREnum instance.

        This method automatically matches the XML text content against
        enum members (case-insensitive). If no match is found, creates
        a custom instance with the text value.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AREnum instance

        Raises:
            ValueError: If element is empty
        """
        if element.text:
            text = element.text.strip()

            # Try to find matching enum value (case-insensitive)
            # Iterate through class attributes to find matching enum members
            for attr_name in dir(cls):
                if attr_name.isupper() and not attr_name.startswith('_'):
                    attr_value = getattr(cls, attr_name)
                    # Handle both string values and enum instances
                    if isinstance(attr_value, str):
                        if attr_value.lower() == text.lower():
                            # Create instance with the matching value
                            return cls(attr_value)
                    elif hasattr(attr_value, 'value') and isinstance(attr_value.value, str):
                        if attr_value.value.lower() == text.lower():
                            # Return the enum instance directly
                            return attr_value

            # Fallback: create a custom instance if no match found
            return cls(text)

        raise ValueError(f"Cannot deserialize {cls.__name__} from empty element")

    def __str__(self) -> str:
        """Return string representation of the enum value."""
        return str(self.value) if hasattr(self, 'value') else ""

    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"{self.__class__.__name__}.{self.name if hasattr(self, 'name') else self.value}"

    def __eq__(self, other: object) -> bool:
        """Check equality based on value.

        Provides transparent comparison with string values.

        Args:
            other: Object to compare with

        Returns:
            True if values are equal (both same class or string), False otherwise
        """
        # Compare with same class (existing behavior)
        if isinstance(other, self.__class__):
            if hasattr(self, 'value') and hasattr(other, 'value'):
                return self.value == other.value
            return True  # Both have no value attribute
        # Compare with string (transparent behavior)
        if isinstance(other, str):
            return self.value == other
        return NotImplemented

    def __hash__(self) -> int:
        """Return hash based on value.

        Returns:
            Hash of the value, or hash of empty string if no value
        """
        value = self.value if hasattr(self, 'value') else ""
        return hash(value)
