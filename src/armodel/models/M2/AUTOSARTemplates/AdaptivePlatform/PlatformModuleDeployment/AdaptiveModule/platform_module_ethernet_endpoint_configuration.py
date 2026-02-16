"""PlatformModuleEthernetEndpointConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
)


class PlatformModuleEthernetEndpointConfiguration(ARElement):
    """AUTOSAR PlatformModuleEthernetEndpointConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication", None, False, False, any (EthernetCommunication)),  # communication
        ("ipv4_multicast_ip", None, True, False, None),  # ipv4MulticastIp
        ("ipv6_multicast_ip", None, True, False, None),  # ipv6MulticastIp
    ]

    def __init__(self) -> None:
        """Initialize PlatformModuleEthernetEndpointConfiguration."""
        super().__init__()
        self.communication: Optional[Any] = None
        self.ipv4_multicast_ip: Optional[Ip4AddressString] = None
        self.ipv6_multicast_ip: Optional[Ip6AddressString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PlatformModuleEthernetEndpointConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PlatformModuleEthernetEndpointConfiguration":
        """Create PlatformModuleEthernetEndpointConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PlatformModuleEthernetEndpointConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PlatformModuleEthernetEndpointConfiguration since parent returns ARObject
        return cast("PlatformModuleEthernetEndpointConfiguration", obj)


class PlatformModuleEthernetEndpointConfigurationBuilder:
    """Builder for PlatformModuleEthernetEndpointConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PlatformModuleEthernetEndpointConfiguration = PlatformModuleEthernetEndpointConfiguration()

    def build(self) -> PlatformModuleEthernetEndpointConfiguration:
        """Build and return PlatformModuleEthernetEndpointConfiguration object.

        Returns:
            PlatformModuleEthernetEndpointConfiguration instance
        """
        # TODO: Add validation
        return self._obj
