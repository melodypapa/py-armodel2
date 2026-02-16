"""ProvidedServiceInstance AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("allowed_services", None, False, True, NetworkEndpoint),  # allowedServices
        ("auto_available", None, True, False, None),  # autoAvailable
        ("event_handlers", None, False, True, EventHandler),  # eventHandlers
        ("instance", None, True, False, None),  # instance
        ("load_balancing", None, True, False, None),  # loadBalancing
        ("local_unicast", None, False, False, ApplicationEndpoint),  # localUnicast
        ("minor_version", None, True, False, None),  # minorVersion
        ("priority", None, True, False, None),  # priority
        ("remote_multicasts", None, False, True, ApplicationEndpoint),  # remoteMulticasts
        ("remote_unicasts", None, False, True, ApplicationEndpoint),  # remoteUnicasts
        ("sd_server_config", None, False, False, any (SdServerConfig)),  # sdServerConfig
        ("sd_server_timer", None, False, False, any (SomeipSdServer)),  # sdServerTimer
        ("service_identifier", None, True, False, None),  # serviceIdentifier
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ProvidedServiceInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ProvidedServiceInstance":
        """Create ProvidedServiceInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ProvidedServiceInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ProvidedServiceInstance since parent returns ARObject
        return cast("ProvidedServiceInstance", obj)


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
