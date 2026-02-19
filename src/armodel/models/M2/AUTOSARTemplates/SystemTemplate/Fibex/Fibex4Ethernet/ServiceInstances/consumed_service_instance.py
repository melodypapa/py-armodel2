"""ConsumedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 980)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 500)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_services: list[NetworkEndpoint]
    auto_require: Optional[Boolean]
    blocklisteds: list[SomeipServiceVersion]
    consumed_event_group_refs: list[ARRef]
    event_multicast: Optional[ApplicationEndpoint]
    instance: Optional[AnyServiceInstanceId]
    local_unicast: ApplicationEndpoint
    minor_version: Optional[AnyVersionString]
    provided_service: Optional[Any]
    remote_unicast: ApplicationEndpoint
    sd_client_config: Optional[Any]
    sd_client_timer: Optional[SomeipSdClientServiceInstanceConfig]
    service_identifier: Optional[PositiveInteger]
    version_driven: Optional[Any]
    def __init__(self) -> None:
        """Initialize ConsumedServiceInstance."""
        super().__init__()
        self.allowed_services: list[NetworkEndpoint] = []
        self.auto_require: Optional[Boolean] = None
        self.blocklisteds: list[SomeipServiceVersion] = []
        self.consumed_event_group_refs: list[ARRef] = []
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedServiceInstance":
        """Deserialize XML element to ConsumedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedServiceInstance object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse allowed_services (list)
        obj.allowed_services = []
        for child in ARObject._find_all_child_elements(element, "ALLOWED-SERVICES"):
            allowed_services_value = ARObject._deserialize_by_tag(child, "NetworkEndpoint")
            obj.allowed_services.append(allowed_services_value)

        # Parse auto_require
        child = ARObject._find_child_element(element, "AUTO-REQUIRE")
        if child is not None:
            auto_require_value = child.text
            obj.auto_require = auto_require_value

        # Parse blocklisteds (list)
        obj.blocklisteds = []
        for child in ARObject._find_all_child_elements(element, "BLOCKLISTEDS"):
            blocklisteds_value = ARObject._deserialize_by_tag(child, "SomeipServiceVersion")
            obj.blocklisteds.append(blocklisteds_value)

        # Parse consumed_event_group_refs (list)
        obj.consumed_event_group_refs = []
        for child in ARObject._find_all_child_elements(element, "CONSUMED-EVENT-GROUPS"):
            consumed_event_group_refs_value = ARObject._deserialize_by_tag(child, "ConsumedEventGroup")
            obj.consumed_event_group_refs.append(consumed_event_group_refs_value)

        # Parse event_multicast
        child = ARObject._find_child_element(element, "EVENT-MULTICAST")
        if child is not None:
            event_multicast_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.event_multicast = event_multicast_value

        # Parse instance
        child = ARObject._find_child_element(element, "INSTANCE")
        if child is not None:
            instance_value = child.text
            obj.instance = instance_value

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

        # Parse provided_service
        child = ARObject._find_child_element(element, "PROVIDED-SERVICE")
        if child is not None:
            provided_service_value = child.text
            obj.provided_service = provided_service_value

        # Parse remote_unicast
        child = ARObject._find_child_element(element, "REMOTE-UNICAST")
        if child is not None:
            remote_unicast_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.remote_unicast = remote_unicast_value

        # Parse sd_client_config
        child = ARObject._find_child_element(element, "SD-CLIENT-CONFIG")
        if child is not None:
            sd_client_config_value = child.text
            obj.sd_client_config = sd_client_config_value

        # Parse sd_client_timer
        child = ARObject._find_child_element(element, "SD-CLIENT-TIMER")
        if child is not None:
            sd_client_timer_value = ARObject._deserialize_by_tag(child, "SomeipSdClientServiceInstanceConfig")
            obj.sd_client_timer = sd_client_timer_value

        # Parse service_identifier
        child = ARObject._find_child_element(element, "SERVICE-IDENTIFIER")
        if child is not None:
            service_identifier_value = child.text
            obj.service_identifier = service_identifier_value

        # Parse version_driven
        child = ARObject._find_child_element(element, "VERSION-DRIVEN")
        if child is not None:
            version_driven_value = child.text
            obj.version_driven = version_driven_value

        return obj



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
