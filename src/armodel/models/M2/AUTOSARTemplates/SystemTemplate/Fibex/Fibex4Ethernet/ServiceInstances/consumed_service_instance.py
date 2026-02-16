"""ConsumedServiceInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyServiceInstanceId,
    AnyVersionString,
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_client_service_instance_config import (
    SomeipSdClientServiceInstanceConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_service_version import (
    SomeipServiceVersion,
)


class ConsumedServiceInstance(AbstractServiceInstance):
    """AUTOSAR ConsumedServiceInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("allowed_services", None, False, True, NetworkEndpoint),  # allowedServices
        ("auto_require", None, True, False, None),  # autoRequire
        ("blocklisteds", None, False, True, SomeipServiceVersion),  # blocklisteds
        ("consumed_event_groups", None, False, True, ConsumedEventGroup),  # consumedEventGroups
        ("event_multicast", None, False, False, ApplicationEndpoint),  # eventMulticast
        ("instance", None, True, False, None),  # instance
        ("local_unicast", None, False, False, ApplicationEndpoint),  # localUnicast
        ("minor_version", None, True, False, None),  # minorVersion
        ("provided_service", None, False, False, any (ProvidedService)),  # providedService
        ("remote_unicast", None, False, False, ApplicationEndpoint),  # remoteUnicast
        ("sd_client_config", None, False, False, any (SdClientConfig)),  # sdClientConfig
        ("sd_client_timer", None, False, False, SomeipSdClientServiceInstanceConfig),  # sdClientTimer
        ("service_identifier", None, True, False, None),  # serviceIdentifier
        ("version_driven", None, False, False, any (ServiceVersion)),  # versionDriven
    ]

    def __init__(self) -> None:
        """Initialize ConsumedServiceInstance."""
        super().__init__()
        self.allowed_services: list[NetworkEndpoint] = []
        self.auto_require: Optional[Boolean] = None
        self.blocklisteds: list[SomeipServiceVersion] = []
        self.consumed_event_groups: list[ConsumedEventGroup] = []
        self.event_multicast: Optional[ApplicationEndpoint] = None
        self.instance: Optional[AnyServiceInstanceId] = None
        self.local_unicast: ApplicationEndpoint = None
        self.minor_version: Optional[AnyVersionString] = None
        self.provided_service: Optional[Any] = None
        self.remote_unicast: ApplicationEndpoint = None
        self.sd_client_config: Optional[Any] = None
        self.sd_client_timer: Optional[SomeipSdClientServiceInstanceConfig] = None
        self.service_identifier: Optional[PositiveInteger] = None
        self.version_driven: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConsumedServiceInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedServiceInstance":
        """Create ConsumedServiceInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConsumedServiceInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConsumedServiceInstance since parent returns ARObject
        return cast("ConsumedServiceInstance", obj)


class ConsumedServiceInstanceBuilder:
    """Builder for ConsumedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedServiceInstance = ConsumedServiceInstance()

    def build(self) -> ConsumedServiceInstance:
        """Build and return ConsumedServiceInstance object.

        Returns:
            ConsumedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
