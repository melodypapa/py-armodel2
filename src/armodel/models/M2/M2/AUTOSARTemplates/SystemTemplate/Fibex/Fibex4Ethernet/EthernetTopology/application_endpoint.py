"""ApplicationEndpoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "consumed_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # consumedServices
        "max_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNumberOf
        "network_endpoint_endpoint": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NetworkEndpoint,
        ),  # networkEndpointEndpoint
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "provided_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # providedServices
        "tls_crypto_service": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TlsCryptoServiceMapping,
        ),  # tlsCryptoService
        "tp_configuration_configuration": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TransportProtocolConfiguration,
        ),  # tpConfigurationConfiguration
    }

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
