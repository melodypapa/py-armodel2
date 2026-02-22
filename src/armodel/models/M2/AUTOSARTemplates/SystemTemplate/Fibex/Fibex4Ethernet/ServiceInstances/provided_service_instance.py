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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    allowed_service_refs: list[ARRef]
    auto_available: Optional[Boolean]
    event_handlers: list[EventHandler]
    instance: Optional[PositiveInteger]
    load_balancing: Optional[PositiveInteger]
    local_unicast: ApplicationEndpoint
    minor_version: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    remote_multicast_refs: list[ARRef]
    remote_unicast_refs: list[ARRef]
    sd_server_config: Optional[Any]
    sd_server_timer_ref: Optional[Any]
    service_identifier: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ProvidedServiceInstance."""
        super().__init__()
        self.allowed_service_refs: list[ARRef] = []
        self.auto_available: Optional[Boolean] = None
        self.event_handlers: list[EventHandler] = []
        self.instance: Optional[PositiveInteger] = None
        self.load_balancing: Optional[PositiveInteger] = None
        self.local_unicast: ApplicationEndpoint = None
        self.minor_version: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.remote_multicast_refs: list[ARRef] = []
        self.remote_unicast_refs: list[ARRef] = []
        self.sd_server_config: Optional[Any] = None
        self.sd_server_timer_ref: Optional[Any] = None
        self.service_identifier: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ProvidedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ProvidedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_service_refs (list to container "ALLOWED-SERVICE-REFS")
        if self.allowed_service_refs:
            wrapper = ET.Element("ALLOWED-SERVICE-REFS")
            for item in self.allowed_service_refs:
                serialized = SerializationHelper.serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("ALLOWED-SERVICE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize auto_available
        if self.auto_available is not None:
            serialized = SerializationHelper.serialize_item(self.auto_available, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-AVAILABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_handlers (list to container "EVENT-HANDLERS")
        if self.event_handlers:
            wrapper = ET.Element("EVENT-HANDLERS")
            for item in self.event_handlers:
                serialized = SerializationHelper.serialize_item(item, "EventHandler")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instance
        if self.instance is not None:
            serialized = SerializationHelper.serialize_item(self.instance, "PositiveInteger")
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

        # Serialize load_balancing
        if self.load_balancing is not None:
            serialized = SerializationHelper.serialize_item(self.load_balancing, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOAD-BALANCING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize local_unicast
        if self.local_unicast is not None:
            serialized = SerializationHelper.serialize_item(self.local_unicast, "ApplicationEndpoint")
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
            serialized = SerializationHelper.serialize_item(self.minor_version, "PositiveInteger")
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

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_multicast_refs (list to container "REMOTE-MULTICAST-REFS")
        if self.remote_multicast_refs:
            wrapper = ET.Element("REMOTE-MULTICAST-REFS")
            for item in self.remote_multicast_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("REMOTE-MULTICAST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize remote_unicast_refs (list to container "REMOTE-UNICAST-REFS")
        if self.remote_unicast_refs:
            wrapper = ET.Element("REMOTE-UNICAST-REFS")
            for item in self.remote_unicast_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("REMOTE-UNICAST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sd_server_config
        if self.sd_server_config is not None:
            serialized = SerializationHelper.serialize_item(self.sd_server_config, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-SERVER-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd_server_timer_ref
        if self.sd_server_timer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sd_server_timer_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-SERVER-TIMER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_identifier
        if self.service_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.service_identifier, "PositiveInteger")
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

        return elem

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

        # Parse allowed_service_refs (list from container "ALLOWED-SERVICE-REFS")
        obj.allowed_service_refs = []
        container = SerializationHelper.find_child_element(element, "ALLOWED-SERVICE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.allowed_service_refs.append(child_value)

        # Parse auto_available
        child = SerializationHelper.find_child_element(element, "AUTO-AVAILABLE")
        if child is not None:
            auto_available_value = child.text
            obj.auto_available = auto_available_value

        # Parse event_handlers (list from container "EVENT-HANDLERS")
        obj.event_handlers = []
        container = SerializationHelper.find_child_element(element, "EVENT-HANDLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.event_handlers.append(child_value)

        # Parse instance
        child = SerializationHelper.find_child_element(element, "INSTANCE")
        if child is not None:
            instance_value = child.text
            obj.instance = instance_value

        # Parse load_balancing
        child = SerializationHelper.find_child_element(element, "LOAD-BALANCING")
        if child is not None:
            load_balancing_value = child.text
            obj.load_balancing = load_balancing_value

        # Parse local_unicast
        child = SerializationHelper.find_child_element(element, "LOCAL-UNICAST")
        if child is not None:
            local_unicast_value = SerializationHelper.deserialize_by_tag(child, "ApplicationEndpoint")
            obj.local_unicast = local_unicast_value

        # Parse minor_version
        child = SerializationHelper.find_child_element(element, "MINOR-VERSION")
        if child is not None:
            minor_version_value = child.text
            obj.minor_version = minor_version_value

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse remote_multicast_refs (list from container "REMOTE-MULTICAST-REFS")
        obj.remote_multicast_refs = []
        container = SerializationHelper.find_child_element(element, "REMOTE-MULTICAST-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_multicast_refs.append(child_value)

        # Parse remote_unicast_refs (list from container "REMOTE-UNICAST-REFS")
        obj.remote_unicast_refs = []
        container = SerializationHelper.find_child_element(element, "REMOTE-UNICAST-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.remote_unicast_refs.append(child_value)

        # Parse sd_server_config
        child = SerializationHelper.find_child_element(element, "SD-SERVER-CONFIG")
        if child is not None:
            sd_server_config_value = child.text
            obj.sd_server_config = sd_server_config_value

        # Parse sd_server_timer_ref
        child = SerializationHelper.find_child_element(element, "SD-SERVER-TIMER-REF")
        if child is not None:
            sd_server_timer_ref_value = ARRef.deserialize(child)
            obj.sd_server_timer_ref = sd_server_timer_ref_value

        # Parse service_identifier
        child = SerializationHelper.find_child_element(element, "SERVICE-IDENTIFIER")
        if child is not None:
            service_identifier_value = child.text
            obj.service_identifier = service_identifier_value

        return obj



class ProvidedServiceInstanceBuilder:
    """Builder for ProvidedServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: ProvidedServiceInstance = ProvidedServiceInstance()


    def with_short_name(self, value: Identifier) -> "ProvidedServiceInstanceBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "ProvidedServiceInstanceBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "ProvidedServiceInstanceBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "ProvidedServiceInstanceBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "ProvidedServiceInstanceBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "ProvidedServiceInstanceBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "ProvidedServiceInstanceBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "ProvidedServiceInstanceBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "ProvidedServiceInstanceBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_capabilities(self, items: list[TagWithOptionalValue]) -> "ProvidedServiceInstanceBuilder":
        """Set capabilities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.capabilities = list(items) if items else []
        return self

    def with_major_version(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set major_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.major_version = value
        return self

    def with_method(self, value: Optional[PduActivationRoutingGroup]) -> "ProvidedServiceInstanceBuilder":
        """Set method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.method = value
        return self

    def with_routing_groups(self, items: list[SoAdRoutingGroup]) -> "ProvidedServiceInstanceBuilder":
        """Set routing_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = list(items) if items else []
        return self

    def with_allowed_services(self, items: list[NetworkEndpoint]) -> "ProvidedServiceInstanceBuilder":
        """Set allowed_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = list(items) if items else []
        return self

    def with_auto_available(self, value: Optional[Boolean]) -> "ProvidedServiceInstanceBuilder":
        """Set auto_available attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auto_available = value
        return self

    def with_event_handlers(self, items: list[EventHandler]) -> "ProvidedServiceInstanceBuilder":
        """Set event_handlers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.event_handlers = list(items) if items else []
        return self

    def with_instance(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.instance = value
        return self

    def with_load_balancing(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set load_balancing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.load_balancing = value
        return self

    def with_local_unicast(self, value: ApplicationEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Set local_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.local_unicast = value
        return self

    def with_minor_version(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set minor_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minor_version = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_remote_multicasts(self, items: list[ApplicationEndpoint]) -> "ProvidedServiceInstanceBuilder":
        """Set remote_multicasts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.remote_multicasts = list(items) if items else []
        return self

    def with_remote_unicasts(self, items: list[ApplicationEndpoint]) -> "ProvidedServiceInstanceBuilder":
        """Set remote_unicasts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.remote_unicasts = list(items) if items else []
        return self

    def with_sd_server_config(self, value: Optional[any (SdServerConfig)]) -> "ProvidedServiceInstanceBuilder":
        """Set sd_server_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_server_config = value
        return self

    def with_sd_server_timer(self, value: Optional[any (SomeipSdServer)]) -> "ProvidedServiceInstanceBuilder":
        """Set sd_server_timer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_server_timer = value
        return self

    def with_service_identifier(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set service_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_identifier = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_capabilitie(self, item: TagWithOptionalValue) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to capabilities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.capabilities.append(item)
        return self

    def clear_capabilities(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from capabilities list.

        Returns:
            self for method chaining
        """
        self._obj.capabilities = []
        return self

    def add_routing_group(self, item: SoAdRoutingGroup) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to routing_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.routing_groups.append(item)
        return self

    def clear_routing_groups(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from routing_groups list.

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = []
        return self

    def add_allowed_service(self, item: NetworkEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to allowed_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.allowed_services.append(item)
        return self

    def clear_allowed_services(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from allowed_services list.

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = []
        return self

    def add_event_handler(self, item: EventHandler) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to event_handlers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.event_handlers.append(item)
        return self

    def clear_event_handlers(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from event_handlers list.

        Returns:
            self for method chaining
        """
        self._obj.event_handlers = []
        return self

    def add_remote_multicast(self, item: ApplicationEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to remote_multicasts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.remote_multicasts.append(item)
        return self

    def clear_remote_multicasts(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from remote_multicasts list.

        Returns:
            self for method chaining
        """
        self._obj.remote_multicasts = []
        return self

    def add_remote_unicast(self, item: ApplicationEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to remote_unicasts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.remote_unicasts.append(item)
        return self

    def clear_remote_unicasts(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from remote_unicasts list.

        Returns:
            self for method chaining
        """
        self._obj.remote_unicasts = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> ProvidedServiceInstance:
        """Build and return the ProvidedServiceInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj