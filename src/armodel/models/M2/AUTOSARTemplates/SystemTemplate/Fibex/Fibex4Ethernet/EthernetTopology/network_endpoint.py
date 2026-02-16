"""NetworkEndpoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)


class NetworkEndpoint(Identifiable):
    """AUTOSAR NetworkEndpoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("fully_qualified", None, True, False, None),  # fullyQualified
        ("infrastructure_services", None, False, False, InfrastructureServices),  # infrastructureServices
        ("ip_sec_config", None, False, False, IPSecConfig),  # ipSecConfig
        ("network_endpoints", None, False, True, NetworkEndpoint),  # networkEndpoints
        ("priority", None, True, False, None),  # priority
    ]

    def __init__(self) -> None:
        """Initialize NetworkEndpoint."""
        super().__init__()
        self.fully_qualified: Optional[String] = None
        self.infrastructure_services: Optional[InfrastructureServices] = None
        self.ip_sec_config: Optional[IPSecConfig] = None
        self.network_endpoints: list[NetworkEndpoint] = []
        self.priority: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NetworkEndpoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NetworkEndpoint":
        """Create NetworkEndpoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NetworkEndpoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NetworkEndpoint since parent returns ARObject
        return cast("NetworkEndpoint", obj)


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
