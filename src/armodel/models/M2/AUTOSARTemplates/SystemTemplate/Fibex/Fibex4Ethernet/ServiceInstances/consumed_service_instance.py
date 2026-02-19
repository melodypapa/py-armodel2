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
    def serialize(self) -> ET.Element:
        """Serialize ConsumedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsumedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_services (list to container "ALLOWED-SERVICES")
        if self.allowed_services:
            wrapper = ET.Element("ALLOWED-SERVICES")
            for item in self.allowed_services:
                serialized = ARObject._serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize auto_require
        if self.auto_require is not None:
            serialized = ARObject._serialize_item(self.auto_require, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-REQUIRE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize blocklisteds (list to container "BLOCKLISTEDS")
        if self.blocklisteds:
            wrapper = ET.Element("BLOCKLISTEDS")
            for item in self.blocklisteds:
                serialized = ARObject._serialize_item(item, "SomeipServiceVersion")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize consumed_event_group_refs (list to container "CONSUMED-EVENT-GROUPS")
        if self.consumed_event_group_refs:
            wrapper = ET.Element("CONSUMED-EVENT-GROUPS")
            for item in self.consumed_event_group_refs:
                serialized = ARObject._serialize_item(item, "ConsumedEventGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize event_multicast
        if self.event_multicast is not None:
            serialized = ARObject._serialize_item(self.event_multicast, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-MULTICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize instance
        if self.instance is not None:
            serialized = ARObject._serialize_item(self.instance, "AnyServiceInstanceId")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize local_unicast
        if self.local_unicast is not None:
            serialized = ARObject._serialize_item(self.local_unicast, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minor_version
        if self.minor_version is not None:
            serialized = ARObject._serialize_item(self.minor_version, "AnyVersionString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize provided_service
        if self.provided_service is not None:
            serialized = ARObject._serialize_item(self.provided_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_unicast
        if self.remote_unicast is not None:
            serialized = ARObject._serialize_item(self.remote_unicast, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMOTE-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd_client_config
        if self.sd_client_config is not None:
            serialized = ARObject._serialize_item(self.sd_client_config, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-CLIENT-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd_client_timer
        if self.sd_client_timer is not None:
            serialized = ARObject._serialize_item(self.sd_client_timer, "SomeipSdClientServiceInstanceConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-CLIENT-TIMER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_identifier
        if self.service_identifier is not None:
            serialized = ARObject._serialize_item(self.service_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize version_driven
        if self.version_driven is not None:
            serialized = ARObject._serialize_item(self.version_driven, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION-DRIVEN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedServiceInstance":
        """Deserialize XML element to ConsumedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsumedServiceInstance, cls).deserialize(element)

        # Parse allowed_services (list from container "ALLOWED-SERVICES")
        obj.allowed_services = []
        container = ARObject._find_child_element(element, "ALLOWED-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.allowed_services.append(child_value)

        # Parse auto_require
        child = ARObject._find_child_element(element, "AUTO-REQUIRE")
        if child is not None:
            auto_require_value = child.text
            obj.auto_require = auto_require_value

        # Parse blocklisteds (list from container "BLOCKLISTEDS")
        obj.blocklisteds = []
        container = ARObject._find_child_element(element, "BLOCKLISTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.blocklisteds.append(child_value)

        # Parse consumed_event_group_refs (list from container "CONSUMED-EVENT-GROUPS")
        obj.consumed_event_group_refs = []
        container = ARObject._find_child_element(element, "CONSUMED-EVENT-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.consumed_event_group_refs.append(child_value)

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
