"""ProvidedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 485)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_handler import (
    EventHandler,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)


class ProvidedServiceInstance(AbstractServiceInstance):
    """AUTOSAR ProvidedServiceInstance."""

    def __init__(self) -> None:
        """Initialize ProvidedServiceInstance."""
        super().__init__()
        self.allowed_services: list[NetworkEndpoint] = []
        self.auto_available: Optional[Boolean] = None
        self.event_handlers: list[EventHandler] = []
        self.instance: Optional[PositiveInteger] = None
        self.load_balancing: Optional[PositiveInteger] = None
        self.local_unicast: ApplicationEndpoint = None
        self.minor_version: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.remote_multicasts: list[ApplicationEndpoint] = []
        self.remote_unicasts: list[ApplicationEndpoint] = []
        self.sd_server_config: Optional[Any] = None
        self.sd_server_timer: Optional[Any] = None
        self.service_identifier: Optional[PositiveInteger] = None


class ProvidedServiceInstanceBuilder:
    """Builder for ProvidedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ProvidedServiceInstance = ProvidedServiceInstance()

    def build(self) -> ProvidedServiceInstance:
        """Build and return ProvidedServiceInstance object.

        Returns:
            ProvidedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
