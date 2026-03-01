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

    _XML_TAG = "CONSUMED-EVENT-GROUP"


    application_endpoint_ref: Optional[ARRef]
    auto_require: Optional[Boolean]
    event_group: Optional[PositiveInteger]
    event_multicast_refs: list[ARRef]
    pdu_activation_routings: list[PduActivationRoutingGroup]
    priority: Optional[PositiveInteger]
    routing_group_refs: list[ARRef]
    sd_client_config: Optional[Any]
    sd_client_timer_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "APPLICATION-ENDPOINT-REF": lambda obj, elem: setattr(obj, "application_endpoint_ref", ARRef.deserialize(elem)),
        "AUTO-REQUIRE": lambda obj, elem: setattr(obj, "auto_require", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "EVENT-GROUP": lambda obj, elem: setattr(obj, "event_group", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "EVENT-MULTICAST-REFS": lambda obj, elem: obj.event_multicast_refs.append(ARRef.deserialize(elem)),
        "PDU-ACTIVATION-ROUTINGS": lambda obj, elem: obj.pdu_activation_routings.append(SerializationHelper.deserialize_by_tag(elem, "PduActivationRoutingGroup")),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "ROUTING-GROUP-REFS": lambda obj, elem: obj.routing_group_refs.append(ARRef.deserialize(elem)),
        "SD-CLIENT-CONFIG": lambda obj, elem: setattr(obj, "sd_client_config", SerializationHelper.deserialize_by_tag(elem, "any (SdClientConfig)")),
        "SD-CLIENT-TIMER-REF": lambda obj, elem: setattr(obj, "sd_client_timer_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLICATION-ENDPOINT-REF":
                setattr(obj, "application_endpoint_ref", ARRef.deserialize(child))
            elif tag == "AUTO-REQUIRE":
                setattr(obj, "auto_require", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "EVENT-GROUP":
                setattr(obj, "event_group", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "EVENT-MULTICAST-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.event_multicast_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationEndpoint"))
            elif tag == "PDU-ACTIVATION-ROUTINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.pdu_activation_routings.append(SerializationHelper.deserialize_by_tag(item_elem, "PduActivationRoutingGroup"))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "ROUTING-GROUP-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.routing_group_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "SoAdRoutingGroup"))
            elif tag == "SD-CLIENT-CONFIG":
                setattr(obj, "sd_client_config", SerializationHelper.deserialize_by_tag(child, "any (SdClientConfig)"))
            elif tag == "SD-CLIENT-TIMER-REF":
                setattr(obj, "sd_client_timer_ref", ARRef.deserialize(child))

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