"""ProvidedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 485)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "allowed_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NetworkEndpoint,
        ),  # allowedServices
        "auto_available": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # autoAvailable
        "event_handlers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EventHandler,
        ),  # eventHandlers
        "instance": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # instance
        "load_balancing": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # loadBalancing
        "local_unicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ApplicationEndpoint,
        ),  # localUnicast
        "minor_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minorVersion
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "remote_multicasts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationEndpoint,
        ),  # remoteMulticasts
        "remote_unicasts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationEndpoint,
        ),  # remoteUnicasts
        "sd_server_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # sdServerConfig
        "sd_server_timer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # sdServerTimer
        "service_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # serviceIdentifier
    }

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
