"""EthernetPhysicalChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_ad_config import (
    SoAdConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_config import (
    VlanConfig,
)


class EthernetPhysicalChannel(PhysicalChannel):
    """AUTOSAR EthernetPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("network_endpoints", None, False, True, NetworkEndpoint),  # networkEndpoints
        ("so_ad_config", None, False, False, SoAdConfig),  # soAdConfig
        ("vlan", None, False, False, VlanConfig),  # vlan
    ]

    def __init__(self) -> None:
        """Initialize EthernetPhysicalChannel."""
        super().__init__()
        self.network_endpoints: list[NetworkEndpoint] = []
        self.so_ad_config: Optional[SoAdConfig] = None
        self.vlan: Optional[VlanConfig] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthernetPhysicalChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPhysicalChannel":
        """Create EthernetPhysicalChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthernetPhysicalChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthernetPhysicalChannel since parent returns ARObject
        return cast("EthernetPhysicalChannel", obj)


class EthernetPhysicalChannelBuilder:
    """Builder for EthernetPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetPhysicalChannel = EthernetPhysicalChannel()

    def build(self) -> EthernetPhysicalChannel:
        """Build and return EthernetPhysicalChannel object.

        Returns:
            EthernetPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
