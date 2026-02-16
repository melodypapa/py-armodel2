"""EthernetPhysicalChannel AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "network_endpoints": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NetworkEndpoint,
        ),  # networkEndpoints
        "so_ad_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SoAdConfig,
        ),  # soAdConfig
        "vlan": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VlanConfig,
        ),  # vlan
    }

    def __init__(self) -> None:
        """Initialize EthernetPhysicalChannel."""
        super().__init__()
        self.network_endpoints: list[NetworkEndpoint] = []
        self.so_ad_config: Optional[SoAdConfig] = None
        self.vlan: Optional[VlanConfig] = None


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
