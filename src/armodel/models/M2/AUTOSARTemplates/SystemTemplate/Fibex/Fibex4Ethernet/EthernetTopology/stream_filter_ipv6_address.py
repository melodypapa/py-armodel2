"""StreamFilterIpv6Address AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip6AddressString,
)


class StreamFilterIpv6Address(ARObject):
    """AUTOSAR StreamFilterIpv6Address."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ipv6_address", None, True, False, None),  # ipv6Address
    ]

    def __init__(self) -> None:
        """Initialize StreamFilterIpv6Address."""
        super().__init__()
        self.ipv6_address: Optional[Ip6AddressString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StreamFilterIpv6Address to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterIpv6Address":
        """Create StreamFilterIpv6Address from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StreamFilterIpv6Address instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StreamFilterIpv6Address since parent returns ARObject
        return cast("StreamFilterIpv6Address", obj)


class StreamFilterIpv6AddressBuilder:
    """Builder for StreamFilterIpv6Address."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterIpv6Address = StreamFilterIpv6Address()

    def build(self) -> StreamFilterIpv6Address:
        """Build and return StreamFilterIpv6Address object.

        Returns:
            StreamFilterIpv6Address instance
        """
        # TODO: Add validation
        return self._obj
