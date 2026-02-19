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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_services: list[NetworkEndpoint]
    auto_available: Optional[Boolean]
    event_handlers: list[EventHandler]
    instance: Optional[PositiveInteger]
    load_balancing: Optional[PositiveInteger]
    local_unicast: ApplicationEndpoint
    minor_version: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    remote_multicasts: list[ApplicationEndpoint]
    remote_unicasts: list[ApplicationEndpoint]
    sd_server_config: Optional[Any]
    sd_server_timer: Optional[Any]
    service_identifier: Optional[PositiveInteger]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ProvidedServiceInstance":
        """Deserialize XML element to ProvidedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ProvidedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ProvidedServiceInstance, cls).deserialize(element)

        # Parse allowed_services (list from container "ALLOWED-SERVICES")
        obj.allowed_services = []
        container = ARObject._find_child_element(element, "ALLOWED-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.allowed_services.append(child_value)

        # Parse auto_available
        child = ARObject._find_child_element(element, "AUTO-AVAILABLE")
        if child is not None:
            auto_available_value = child.text
            obj.auto_available = auto_available_value

        # Parse event_handlers (list from container "EVENT-HANDLERS")
        obj.event_handlers = []
        container = ARObject._find_child_element(element, "EVENT-HANDLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.event_handlers.append(child_value)

        # Parse instance
        child = ARObject._find_child_element(element, "INSTANCE")
        if child is not None:
            instance_value = child.text
            obj.instance = instance_value

        # Parse load_balancing
        child = ARObject._find_child_element(element, "LOAD-BALANCING")
        if child is not None:
            load_balancing_value = child.text
            obj.load_balancing = load_balancing_value

        # Parse local_unicast
        child = ARObject._find_child_element(element, "LOCAL-UNICAST")
        if child is not None:
            local_unicast_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.local_unicast = local_unicast_value

        # Parse minor_version
        child = ARObject._find_child_element(element, "MINOR-VERSION")
        if child is not None:
            minor_version_value = child.text
            obj.minor_version = minor_version_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse remote_multicasts (list from container "REMOTE-MULTICASTS")
        obj.remote_multicasts = []
        container = ARObject._find_child_element(element, "REMOTE-MULTICASTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_multicasts.append(child_value)

        # Parse remote_unicasts (list from container "REMOTE-UNICASTS")
        obj.remote_unicasts = []
        container = ARObject._find_child_element(element, "REMOTE-UNICASTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_unicasts.append(child_value)

        # Parse sd_server_config
        child = ARObject._find_child_element(element, "SD-SERVER-CONFIG")
        if child is not None:
            sd_server_config_value = child.text
            obj.sd_server_config = sd_server_config_value

        # Parse sd_server_timer
        child = ARObject._find_child_element(element, "SD-SERVER-TIMER")
        if child is not None:
            sd_server_timer_value = child.text
            obj.sd_server_timer = sd_server_timer_value

        # Parse service_identifier
        child = ARObject._find_child_element(element, "SERVICE-IDENTIFIER")
        if child is not None:
            service_identifier_value = child.text
            obj.service_identifier = service_identifier_value

        return obj



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
