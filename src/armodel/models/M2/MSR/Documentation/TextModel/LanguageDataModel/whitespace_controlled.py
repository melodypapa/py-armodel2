"""WhitespaceControlled AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class WhitespaceControlled(ARObject):
    """AUTOSAR WhitespaceControlled."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("xml_space", None, False, False, None),  # xmlSpace
    ]

    def __init__(self) -> None:
        """Initialize WhitespaceControlled."""
        super().__init__()
        self.xml_space: Any = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert WhitespaceControlled to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "WhitespaceControlled":
        """Create WhitespaceControlled from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            WhitespaceControlled instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to WhitespaceControlled since parent returns ARObject
        return cast("WhitespaceControlled", obj)


class WhitespaceControlledBuilder:
    """Builder for WhitespaceControlled."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WhitespaceControlled = WhitespaceControlled()

    def build(self) -> WhitespaceControlled:
        """Build and return WhitespaceControlled object.

        Returns:
            WhitespaceControlled instance
        """
        # TODO: Add validation
        return self._obj
