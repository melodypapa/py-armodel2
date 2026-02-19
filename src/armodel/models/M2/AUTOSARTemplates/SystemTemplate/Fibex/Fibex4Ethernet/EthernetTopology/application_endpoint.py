"""ApplicationEndpoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consumed_services: list[Any]
    max_number_of: Optional[PositiveInteger]
    network_endpoint_endpoint: Optional[NetworkEndpoint]
    priority: Optional[PositiveInteger]
    provided_services: list[Any]
    tls_crypto_service: Optional[TlsCryptoServiceMapping]
    tp_configuration_configuration: Optional[TransportProtocolConfiguration]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationEndpoint":
        """Deserialize XML element to ApplicationEndpoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationEndpoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse consumed_services (list)
        obj.consumed_services = []
        for child in ARObject._find_all_child_elements(element, "CONSUMED-SERVICES"):
            consumed_services_value = child.text
            obj.consumed_services.append(consumed_services_value)

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse network_endpoint_endpoint
        child = ARObject._find_child_element(element, "NETWORK-ENDPOINT-ENDPOINT")
        if child is not None:
            network_endpoint_endpoint_value = ARObject._deserialize_by_tag(child, "NetworkEndpoint")
            obj.network_endpoint_endpoint = network_endpoint_endpoint_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse provided_services (list)
        obj.provided_services = []
        for child in ARObject._find_all_child_elements(element, "PROVIDED-SERVICES"):
            provided_services_value = child.text
            obj.provided_services.append(provided_services_value)

        # Parse tls_crypto_service
        child = ARObject._find_child_element(element, "TLS-CRYPTO-SERVICE")
        if child is not None:
            tls_crypto_service_value = ARObject._deserialize_by_tag(child, "TlsCryptoServiceMapping")
            obj.tls_crypto_service = tls_crypto_service_value

        # Parse tp_configuration_configuration
        child = ARObject._find_child_element(element, "TP-CONFIGURATION-CONFIGURATION")
        if child is not None:
            tp_configuration_configuration_value = ARObject._deserialize_by_tag(child, "TransportProtocolConfiguration")
            obj.tp_configuration_configuration = tp_configuration_configuration_value

        return obj



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
