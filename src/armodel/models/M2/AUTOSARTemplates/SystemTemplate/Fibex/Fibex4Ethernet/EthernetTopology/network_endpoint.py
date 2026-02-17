"""NetworkEndpoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config import (
    IPSecConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.infrastructure_services import (
    InfrastructureServices,
)


class NetworkEndpoint(Identifiable):
    """AUTOSAR NetworkEndpoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "fully_qualified": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # fullyQualified
        "infrastructure_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=InfrastructureServices,
        ),  # infrastructureServices
        "ip_sec_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IPSecConfig,
        ),  # ipSecConfig
        "network_endpoints": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NetworkEndpoint,
        ),  # networkEndpoints
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
    }

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
