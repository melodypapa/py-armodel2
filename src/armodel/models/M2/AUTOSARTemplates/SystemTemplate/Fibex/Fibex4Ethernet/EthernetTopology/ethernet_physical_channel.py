"""EthernetPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    network_endpoints: list[NetworkEndpoint]
    so_ad_config: Optional[SoAdConfig]
    vlan: Optional[VlanConfig]
    def __init__(self) -> None:
        """Initialize EthernetPhysicalChannel."""
        super().__init__()
        self.network_endpoints: list[NetworkEndpoint] = []
        self.so_ad_config: Optional[SoAdConfig] = None
        self.vlan: Optional[VlanConfig] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPhysicalChannel":
        """Deserialize XML element to EthernetPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetPhysicalChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse network_endpoints (list)
        obj.network_endpoints = []
        for child in ARObject._find_all_child_elements(element, "NETWORK-ENDPOINTS"):
            network_endpoints_value = ARObject._deserialize_by_tag(child, "NetworkEndpoint")
            obj.network_endpoints.append(network_endpoints_value)

        # Parse so_ad_config
        child = ARObject._find_child_element(element, "SO-AD-CONFIG")
        if child is not None:
            so_ad_config_value = ARObject._deserialize_by_tag(child, "SoAdConfig")
            obj.so_ad_config = so_ad_config_value

        # Parse vlan
        child = ARObject._find_child_element(element, "VLAN")
        if child is not None:
            vlan_value = ARObject._deserialize_by_tag(child, "VlanConfig")
            obj.vlan = vlan_value

        return obj



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
