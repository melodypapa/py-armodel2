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
from armodel.serialization import SerializationHelper
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

    allowed_service_refs: list[ARRef]
    auto_require: Optional[Boolean]
    blocklisteds: list[SomeipServiceVersion]
    consumed_event_group_refs: list[ARRef]
    event_multicast_ref: Optional[ARRef]
    instance: Optional[AnyServiceInstanceId]
    local_unicast: ApplicationEndpoint
    minor_version: Optional[AnyVersionString]
    provided_service_ref: Optional[Any]
    remote_unicast: ApplicationEndpoint
    sd_client_config: Optional[Any]
    sd_client_timer_ref: Optional[ARRef]
    service_identifier: Optional[PositiveInteger]
    version_driven: Optional[Any]
    def __init__(self) -> None:
        """Initialize ConsumedServiceInstance."""
        super().__init__()
        self.allowed_service_refs: list[ARRef] = []
        self.auto_require: Optional[Boolean] = None
        self.blocklisteds: list[SomeipServiceVersion] = []
        self.consumed_event_group_refs: list[ARRef] = []
        self.event_multicast_ref: Optional[ARRef] = None
        self.instance: Optional[AnyServiceInstanceId] = None
        self.local_unicast: ApplicationEndpoint = None
        self.minor_version: Optional[AnyVersionString] = None
        self.provided_service_ref: Optional[Any] = None
        self.remote_unicast: ApplicationEndpoint = None
        self.sd_client_config: Optional[Any] = None
        self.sd_client_timer_ref: Optional[ARRef] = None
        self.service_identifier: Optional[PositiveInteger] = None
        self.version_driven: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ConsumedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsumedServiceInstance, self).serialize()

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

        # Serialize auto_require
        if self.auto_require is not None:
            serialized = SerializationHelper.serialize_item(self.auto_require, "Boolean")
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
                serialized = SerializationHelper.serialize_item(item, "SomeipServiceVersion")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize consumed_event_group_refs (list to container "CONSUMED-EVENT-GROUP-REFS")
        if self.consumed_event_group_refs:
            wrapper = ET.Element("CONSUMED-EVENT-GROUP-REFS")
            for item in self.consumed_event_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedEventGroup")
                if serialized is not None:
                    child_elem = ET.Element("CONSUMED-EVENT-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize event_multicast_ref
        if self.event_multicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_multicast_ref, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-MULTICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize instance
        if self.instance is not None:
            serialized = SerializationHelper.serialize_item(self.instance, "AnyServiceInstanceId")
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
            serialized = SerializationHelper.serialize_item(self.minor_version, "AnyVersionString")
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

        # Serialize provided_service_ref
        if self.provided_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provided_service_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_unicast
        if self.remote_unicast is not None:
            serialized = SerializationHelper.serialize_item(self.remote_unicast, "ApplicationEndpoint")
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
            serialized = SerializationHelper.serialize_item(self.sd_client_config, "Any")
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

        # Serialize sd_client_timer_ref
        if self.sd_client_timer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sd_client_timer_ref, "SomeipSdClientServiceInstanceConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-CLIENT-TIMER-REF")
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

        # Serialize version_driven
        if self.version_driven is not None:
            serialized = SerializationHelper.serialize_item(self.version_driven, "Any")
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

        # Parse auto_require
        child = SerializationHelper.find_child_element(element, "AUTO-REQUIRE")
        if child is not None:
            auto_require_value = child.text
            obj.auto_require = auto_require_value

        # Parse blocklisteds (list from container "BLOCKLISTEDS")
        obj.blocklisteds = []
        container = SerializationHelper.find_child_element(element, "BLOCKLISTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.blocklisteds.append(child_value)

        # Parse consumed_event_group_refs (list from container "CONSUMED-EVENT-GROUP-REFS")
        obj.consumed_event_group_refs = []
        container = SerializationHelper.find_child_element(element, "CONSUMED-EVENT-GROUP-REFS")
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
                    obj.consumed_event_group_refs.append(child_value)

        # Parse event_multicast_ref
        child = SerializationHelper.find_child_element(element, "EVENT-MULTICAST-REF")
        if child is not None:
            event_multicast_ref_value = ARRef.deserialize(child)
            obj.event_multicast_ref = event_multicast_ref_value

        # Parse instance
        child = SerializationHelper.find_child_element(element, "INSTANCE")
        if child is not None:
            instance_value = child.text
            obj.instance = instance_value

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

        # Parse provided_service_ref
        child = SerializationHelper.find_child_element(element, "PROVIDED-SERVICE-REF")
        if child is not None:
            provided_service_ref_value = ARRef.deserialize(child)
            obj.provided_service_ref = provided_service_ref_value

        # Parse remote_unicast
        child = SerializationHelper.find_child_element(element, "REMOTE-UNICAST")
        if child is not None:
            remote_unicast_value = SerializationHelper.deserialize_by_tag(child, "ApplicationEndpoint")
            obj.remote_unicast = remote_unicast_value

        # Parse sd_client_config
        child = SerializationHelper.find_child_element(element, "SD-CLIENT-CONFIG")
        if child is not None:
            sd_client_config_value = child.text
            obj.sd_client_config = sd_client_config_value

        # Parse sd_client_timer_ref
        child = SerializationHelper.find_child_element(element, "SD-CLIENT-TIMER-REF")
        if child is not None:
            sd_client_timer_ref_value = ARRef.deserialize(child)
            obj.sd_client_timer_ref = sd_client_timer_ref_value

        # Parse service_identifier
        child = SerializationHelper.find_child_element(element, "SERVICE-IDENTIFIER")
        if child is not None:
            service_identifier_value = child.text
            obj.service_identifier = service_identifier_value

        # Parse version_driven
        child = SerializationHelper.find_child_element(element, "VERSION-DRIVEN")
        if child is not None:
            version_driven_value = child.text
            obj.version_driven = version_driven_value

        return obj



class ConsumedServiceInstanceBuilder:
    """Builder for ConsumedServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: ConsumedServiceInstance = ConsumedServiceInstance()


    def with_short_name(self, value: Identifier) -> "ConsumedServiceInstanceBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "ConsumedServiceInstanceBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "ConsumedServiceInstanceBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "ConsumedServiceInstanceBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "ConsumedServiceInstanceBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "ConsumedServiceInstanceBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "ConsumedServiceInstanceBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "ConsumedServiceInstanceBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "ConsumedServiceInstanceBuilder":
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

    def with_capabilities(self, items: list[TagWithOptionalValue]) -> "ConsumedServiceInstanceBuilder":
        """Set capabilities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.capabilities = list(items) if items else []
        return self

    def with_major_version(self, value: Optional[PositiveInteger]) -> "ConsumedServiceInstanceBuilder":
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

    def with_method(self, value: Optional[PduActivationRoutingGroup]) -> "ConsumedServiceInstanceBuilder":
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

    def with_routing_groups(self, items: list[SoAdRoutingGroup]) -> "ConsumedServiceInstanceBuilder":
        """Set routing_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = list(items) if items else []
        return self

    def with_allowed_services(self, items: list[NetworkEndpoint]) -> "ConsumedServiceInstanceBuilder":
        """Set allowed_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = list(items) if items else []
        return self

    def with_auto_require(self, value: Optional[Boolean]) -> "ConsumedServiceInstanceBuilder":
        """Set auto_require attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auto_require = value
        return self

    def with_blocklisteds(self, items: list[SomeipServiceVersion]) -> "ConsumedServiceInstanceBuilder":
        """Set blocklisteds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.blocklisteds = list(items) if items else []
        return self

    def with_consumed_event_groups(self, items: list[ConsumedEventGroup]) -> "ConsumedServiceInstanceBuilder":
        """Set consumed_event_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups = list(items) if items else []
        return self

    def with_event_multicast(self, value: Optional[ApplicationEndpoint]) -> "ConsumedServiceInstanceBuilder":
        """Set event_multicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_multicast = value
        return self

    def with_instance(self, value: Optional[AnyServiceInstanceId]) -> "ConsumedServiceInstanceBuilder":
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

    def with_local_unicast(self, value: ApplicationEndpoint) -> "ConsumedServiceInstanceBuilder":
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

    def with_minor_version(self, value: Optional[AnyVersionString]) -> "ConsumedServiceInstanceBuilder":
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

    def with_provided_service(self, value: Optional[any (ProvidedService)]) -> "ConsumedServiceInstanceBuilder":
        """Set provided_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provided_service = value
        return self

    def with_remote_unicast(self, value: ApplicationEndpoint) -> "ConsumedServiceInstanceBuilder":
        """Set remote_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remote_unicast = value
        return self

    def with_sd_client_config(self, value: Optional[any (SdClientConfig)]) -> "ConsumedServiceInstanceBuilder":
        """Set sd_client_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_client_config = value
        return self

    def with_sd_client_timer(self, value: Optional[SomeipSdClientServiceInstanceConfig]) -> "ConsumedServiceInstanceBuilder":
        """Set sd_client_timer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_client_timer = value
        return self

    def with_service_identifier(self, value: Optional[PositiveInteger]) -> "ConsumedServiceInstanceBuilder":
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

    def with_version_driven(self, value: Optional[any (ServiceVersion)]) -> "ConsumedServiceInstanceBuilder":
        """Set version_driven attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.version_driven = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_capabilitie(self, item: TagWithOptionalValue) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to capabilities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.capabilities.append(item)
        return self

    def clear_capabilities(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from capabilities list.

        Returns:
            self for method chaining
        """
        self._obj.capabilities = []
        return self

    def add_routing_group(self, item: SoAdRoutingGroup) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to routing_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.routing_groups.append(item)
        return self

    def clear_routing_groups(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from routing_groups list.

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = []
        return self

    def add_allowed_service(self, item: NetworkEndpoint) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to allowed_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.allowed_services.append(item)
        return self

    def clear_allowed_services(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from allowed_services list.

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = []
        return self

    def add_blocklisted(self, item: SomeipServiceVersion) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to blocklisteds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.blocklisteds.append(item)
        return self

    def clear_blocklisteds(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from blocklisteds list.

        Returns:
            self for method chaining
        """
        self._obj.blocklisteds = []
        return self

    def add_consumed_event_group(self, item: ConsumedEventGroup) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to consumed_event_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups.append(item)
        return self

    def clear_consumed_event_groups(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from consumed_event_groups list.

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups = []
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


    def build(self) -> ConsumedServiceInstance:
        """Build and return the ConsumedServiceInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj