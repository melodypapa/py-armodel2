"""ConsumedEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 504)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_client_event_group_timing_config import (
    SomeipSdClientEventGroupTimingConfig,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConsumedEventGroup(Identifiable):
    """AUTOSAR ConsumedEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_endpoint_ref: Optional[ARRef]
    auto_require: Optional[Boolean]
    event_group: Optional[PositiveInteger]
    event_multicast_refs: list[ARRef]
    pdu_activation_routings: list[PduActivationRoutingGroup]
    priority: Optional[PositiveInteger]
    routing_group_refs: list[ARRef]
    sd_client_config: Optional[Any]
    sd_client_timer_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ConsumedEventGroup."""
        super().__init__()
        self.application_endpoint_ref: Optional[ARRef] = None
        self.auto_require: Optional[Boolean] = None
        self.event_group: Optional[PositiveInteger] = None
        self.event_multicast_refs: list[ARRef] = []
        self.pdu_activation_routings: list[PduActivationRoutingGroup] = []
        self.priority: Optional[PositiveInteger] = None
        self.routing_group_refs: list[ARRef] = []
        self.sd_client_config: Optional[Any] = None
        self.sd_client_timer_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ConsumedEventGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsumedEventGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_endpoint_ref
        if self.application_endpoint_ref is not None:
            serialized = SerializationHelper.serialize_item(self.application_endpoint_ref, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-ENDPOINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize event_group
        if self.event_group is not None:
            serialized = SerializationHelper.serialize_item(self.event_group, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_multicast_refs (list to container "EVENT-MULTICAST-REFS")
        if self.event_multicast_refs:
            wrapper = ET.Element("EVENT-MULTICAST-REFS")
            for item in self.event_multicast_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("EVENT-MULTICAST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_activation_routings (list to container "PDU-ACTIVATION-ROUTINGS")
        if self.pdu_activation_routings:
            wrapper = ET.Element("PDU-ACTIVATION-ROUTINGS")
            for item in self.pdu_activation_routings:
                serialized = SerializationHelper.serialize_item(item, "PduActivationRoutingGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize routing_group_refs (list to container "ROUTING-GROUP-REFS")
        if self.routing_group_refs:
            wrapper = ET.Element("ROUTING-GROUP-REFS")
            for item in self.routing_group_refs:
                serialized = SerializationHelper.serialize_item(item, "SoAdRoutingGroup")
                if serialized is not None:
                    child_elem = ET.Element("ROUTING-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
            serialized = SerializationHelper.serialize_item(self.sd_client_timer_ref, "SomeipSdClientEventGroupTimingConfig")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedEventGroup":
        """Deserialize XML element to ConsumedEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedEventGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsumedEventGroup, cls).deserialize(element)

        # Parse application_endpoint_ref
        child = SerializationHelper.find_child_element(element, "APPLICATION-ENDPOINT-REF")
        if child is not None:
            application_endpoint_ref_value = ARRef.deserialize(child)
            obj.application_endpoint_ref = application_endpoint_ref_value

        # Parse auto_require
        child = SerializationHelper.find_child_element(element, "AUTO-REQUIRE")
        if child is not None:
            auto_require_value = child.text
            obj.auto_require = auto_require_value

        # Parse event_group
        child = SerializationHelper.find_child_element(element, "EVENT-GROUP")
        if child is not None:
            event_group_value = child.text
            obj.event_group = event_group_value

        # Parse event_multicast_refs (list from container "EVENT-MULTICAST-REFS")
        obj.event_multicast_refs = []
        container = SerializationHelper.find_child_element(element, "EVENT-MULTICAST-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.event_multicast_refs.append(child_value)

        # Parse pdu_activation_routings (list from container "PDU-ACTIVATION-ROUTINGS")
        obj.pdu_activation_routings = []
        container = SerializationHelper.find_child_element(element, "PDU-ACTIVATION-ROUTINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdu_activation_routings.append(child_value)

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse routing_group_refs (list from container "ROUTING-GROUP-REFS")
        obj.routing_group_refs = []
        container = SerializationHelper.find_child_element(element, "ROUTING-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.routing_group_refs.append(child_value)

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

        return obj



class ConsumedEventGroupBuilder(IdentifiableBuilder):
    """Builder for ConsumedEventGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConsumedEventGroup = ConsumedEventGroup()


    def with_application_endpoint(self, value: Optional[ApplicationEndpoint]) -> "ConsumedEventGroupBuilder":
        """Set application_endpoint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.application_endpoint = value
        return self

    def with_auto_require(self, value: Optional[Boolean]) -> "ConsumedEventGroupBuilder":
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

    def with_event_group(self, value: Optional[PositiveInteger]) -> "ConsumedEventGroupBuilder":
        """Set event_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_group = value
        return self

    def with_event_multicasts(self, items: list[ApplicationEndpoint]) -> "ConsumedEventGroupBuilder":
        """Set event_multicasts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.event_multicasts = list(items) if items else []
        return self

    def with_pdu_activation_routings(self, items: list[PduActivationRoutingGroup]) -> "ConsumedEventGroupBuilder":
        """Set pdu_activation_routings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_activation_routings = list(items) if items else []
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "ConsumedEventGroupBuilder":
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

    def with_routing_groups(self, items: list[SoAdRoutingGroup]) -> "ConsumedEventGroupBuilder":
        """Set routing_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = list(items) if items else []
        return self

    def with_sd_client_config(self, value: Optional[any (SdClientConfig)]) -> "ConsumedEventGroupBuilder":
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

    def with_sd_client_timer(self, value: Optional[SomeipSdClientEventGroupTimingConfig]) -> "ConsumedEventGroupBuilder":
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


    def add_event_multicast(self, item: ApplicationEndpoint) -> "ConsumedEventGroupBuilder":
        """Add a single item to event_multicasts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.event_multicasts.append(item)
        return self

    def clear_event_multicasts(self) -> "ConsumedEventGroupBuilder":
        """Clear all items from event_multicasts list.

        Returns:
            self for method chaining
        """
        self._obj.event_multicasts = []
        return self

    def add_pdu_activation_routing(self, item: PduActivationRoutingGroup) -> "ConsumedEventGroupBuilder":
        """Add a single item to pdu_activation_routings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_activation_routings.append(item)
        return self

    def clear_pdu_activation_routings(self) -> "ConsumedEventGroupBuilder":
        """Clear all items from pdu_activation_routings list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_activation_routings = []
        return self

    def add_routing_group(self, item: SoAdRoutingGroup) -> "ConsumedEventGroupBuilder":
        """Add a single item to routing_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.routing_groups.append(item)
        return self

    def clear_routing_groups(self) -> "ConsumedEventGroupBuilder":
        """Clear all items from routing_groups list.

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> ConsumedEventGroup:
        """Build and return the ConsumedEventGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj