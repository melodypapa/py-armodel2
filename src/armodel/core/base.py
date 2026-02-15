"""Base AUTOSAR object classes."""

from typing import Any
from lxml import etree


class ARObject:
    """Base class for all AUTOSAR objects.

    All generated AUTOSAR classes inherit from this base class.
    """

    def __init__(self):
        """Initialize ARObject."""
        self._attributes: dict[str, Any] = {}

    def serialize(self) -> etree.Element:
        """Convert object to XML element.

        Raises:
            NotImplementedError: Subclasses must implement this method
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement serialize() method"
        )

    @classmethod
    def deserialize(cls, element: etree.Element) -> "ARObject":
        """Create object from XML element.

        Args:
            element: XML element to deserialize from

        Raises:
            NotImplementedError: Subclasses must implement this method
        """
        raise NotImplementedError(
            f"{cls.__name__} must implement deserialize() classmethod"
        )
