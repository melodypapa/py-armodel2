"""NetworkEndpoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 463)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.infrastructure_services import (
    InfrastructureServices,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config import (
        IPSecConfig,
    )



class NetworkEndpoint(Identifiable):
    """AUTOSAR NetworkEndpoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fully_qualified: Optional[String]
    infrastructure_services: Optional[InfrastructureServices]
    ip_sec_config: Optional[IPSecConfig]
    network_endpoints: list[NetworkEndpoint]
    priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NetworkEndpoint."""
        super().__init__()
        self.fully_qualified: Optional[String] = None
        self.infrastructure_services: Optional[InfrastructureServices] = None
        self.ip_sec_config: Optional[IPSecConfig] = None
        self.network_endpoints: list[NetworkEndpoint] = []
        self.priority: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NetworkEndpoint":
        """Deserialize XML element to NetworkEndpoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NetworkEndpoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse fully_qualified
        child = ARObject._find_child_element(element, "FULLY-QUALIFIED")
        if child is not None:
            fully_qualified_value = child.text
            obj.fully_qualified = fully_qualified_value

        # Parse infrastructure_services
        child = ARObject._find_child_element(element, "INFRASTRUCTURE-SERVICES")
        if child is not None:
            infrastructure_services_value = ARObject._deserialize_by_tag(child, "InfrastructureServices")
            obj.infrastructure_services = infrastructure_services_value

        # Parse ip_sec_config
        child = ARObject._find_child_element(element, "IP-SEC-CONFIG")
        if child is not None:
            ip_sec_config_value = ARObject._deserialize_by_tag(child, "IPSecConfig")
            obj.ip_sec_config = ip_sec_config_value

        # Parse network_endpoints (list)
        obj.network_endpoints = []
        for child in ARObject._find_all_child_elements(element, "NETWORK-ENDPOINTS"):
            network_endpoints_value = ARObject._deserialize_by_tag(child, "NetworkEndpoint")
            obj.network_endpoints.append(network_endpoints_value)

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        return obj



class NetworkEndpointBuilder:
    """Builder for NetworkEndpoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NetworkEndpoint = NetworkEndpoint()

    def build(self) -> NetworkEndpoint:
        """Build and return NetworkEndpoint object.

        Returns:
            NetworkEndpoint instance
        """
        # TODO: Add validation
        return self._obj
