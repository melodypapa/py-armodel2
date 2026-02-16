"""MacMulticastConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


class MacMulticastConfiguration(NetworkEndpointAddress):
    """AUTOSAR MacMulticastConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mac_multicast_group_group", None, False, False, MacMulticastGroup),  # macMulticastGroupGroup
    ]

    def __init__(self) -> None:
        """Initialize MacMulticastConfiguration."""
        super().__init__()
        self.mac_multicast_group_group: Optional[MacMulticastGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacMulticastConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacMulticastConfiguration":
        """Create MacMulticastConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacMulticastConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacMulticastConfiguration since parent returns ARObject
        return cast("MacMulticastConfiguration", obj)


class MacMulticastConfigurationBuilder:
    """Builder for MacMulticastConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacMulticastConfiguration = MacMulticastConfiguration()

    def build(self) -> MacMulticastConfiguration:
        """Build and return MacMulticastConfiguration object.

        Returns:
            MacMulticastConfiguration instance
        """
        # TODO: Add validation
        return self._obj
