"""ApplicationEndpoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_crypto_service_mapping import (
    TlsCryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)


class ApplicationEndpoint(Identifiable):
    """AUTOSAR ApplicationEndpoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consumed_services", None, False, True, any (ConsumedService)),  # consumedServices
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("network_endpoint_endpoint", None, False, False, NetworkEndpoint),  # networkEndpointEndpoint
        ("priority", None, True, False, None),  # priority
        ("provided_services", None, False, True, any (ProvidedService)),  # providedServices
        ("tls_crypto_service", None, False, False, TlsCryptoServiceMapping),  # tlsCryptoService
        ("tp_configuration_configuration", None, False, False, TransportProtocolConfiguration),  # tpConfigurationConfiguration
    ]

    def __init__(self) -> None:
        """Initialize ApplicationEndpoint."""
        super().__init__()
        self.consumed_services: list[Any] = []
        self.max_number_of: Optional[PositiveInteger] = None
        self.network_endpoint_endpoint: Optional[NetworkEndpoint] = None
        self.priority: Optional[PositiveInteger] = None
        self.provided_services: list[Any] = []
        self.tls_crypto_service: Optional[TlsCryptoServiceMapping] = None
        self.tp_configuration_configuration: Optional[TransportProtocolConfiguration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationEndpoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationEndpoint":
        """Create ApplicationEndpoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationEndpoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationEndpoint since parent returns ARObject
        return cast("ApplicationEndpoint", obj)


class ApplicationEndpointBuilder:
    """Builder for ApplicationEndpoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationEndpoint = ApplicationEndpoint()

    def build(self) -> ApplicationEndpoint:
        """Build and return ApplicationEndpoint object.

        Returns:
            ApplicationEndpoint instance
        """
        # TODO: Add validation
        return self._obj
