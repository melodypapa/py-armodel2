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
