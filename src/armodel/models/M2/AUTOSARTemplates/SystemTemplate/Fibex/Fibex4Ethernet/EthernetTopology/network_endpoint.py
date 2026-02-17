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
