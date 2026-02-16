"""BufferProperties AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


class BufferProperties(ARObject):
    """AUTOSAR BufferProperties."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("header_length", None, True, False, None),  # headerLength
        ("in_place", None, True, False, None),  # inPlace
    ]

    def __init__(self) -> None:
        """Initialize BufferProperties."""
        super().__init__()
        self.header_length: Optional[Integer] = None
        self.in_place: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BufferProperties to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BufferProperties":
        """Create BufferProperties from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BufferProperties instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BufferProperties since parent returns ARObject
        return cast("BufferProperties", obj)


class BufferPropertiesBuilder:
    """Builder for BufferProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BufferProperties = BufferProperties()

    def build(self) -> BufferProperties:
        """Build and return BufferProperties object.

        Returns:
            BufferProperties instance
        """
        # TODO: Add validation
        return self._obj
