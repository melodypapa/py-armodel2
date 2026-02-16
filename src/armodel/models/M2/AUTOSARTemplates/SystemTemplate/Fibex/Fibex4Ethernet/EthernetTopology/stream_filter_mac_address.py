"""StreamFilterMACAddress AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)


class StreamFilterMACAddress(ARObject):
    """AUTOSAR StreamFilterMACAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mac_address_string", None, True, False, None),  # macAddressString
    ]

    def __init__(self) -> None:
        """Initialize StreamFilterMACAddress."""
        super().__init__()
        self.mac_address_string: Optional[MacAddressString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StreamFilterMACAddress to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterMACAddress":
        """Create StreamFilterMACAddress from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StreamFilterMACAddress instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StreamFilterMACAddress since parent returns ARObject
        return cast("StreamFilterMACAddress", obj)


class StreamFilterMACAddressBuilder:
    """Builder for StreamFilterMACAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterMACAddress = StreamFilterMACAddress()

    def build(self) -> StreamFilterMACAddress:
        """Build and return StreamFilterMACAddress object.

        Returns:
            StreamFilterMACAddress instance
        """
        # TODO: Add validation
        return self._obj
