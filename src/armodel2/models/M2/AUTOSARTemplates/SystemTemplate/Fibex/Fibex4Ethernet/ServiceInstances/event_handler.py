"""EventHandler AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 492)

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
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_server_event_group_timing_config import (
    SomeipSdServerEventGroupTimingConfig,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EventHandler(Identifiable):
    """AUTOSAR EventHandler."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EVENT-HANDLER"


    consumed_event_group_refs: list[ARRef]
    event_group: Optional[PositiveInteger]
    event_multicast_ref: Optional[ARRef]
    multicast: Optional[PositiveInteger]
    pdu_activation_routings: list[PduActivationRoutingGroup]
    routing_group_refs: list[ARRef]
    sd_server_config: Optional[Any]
    sd_server_eg_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONSUMED-EVENT-GROUP-REFS": lambda obj, elem: [obj.consumed_event_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "EVENT-GROUP": lambda obj, elem: setattr(obj, "event_group", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "EVENT-MULTICAST-REF": lambda obj, elem: setattr(obj, "event_multicast_ref", ARRef.deserialize(elem)),
        "MULTICAST": lambda obj, elem: setattr(obj, "multicast", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PDU-ACTIVATION-ROUTINGS": lambda obj, elem: obj.pdu_activation_routings.append(SerializationHelper.deserialize_by_tag(elem, "PduActivationRoutingGroup")),
        "ROUTING-GROUP-REFS": lambda obj, elem: [obj.routing_group_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SD-SERVER-CONFIG": lambda obj, elem: setattr(obj, "sd_server_config", SerializationHelper.deserialize_by_tag(elem, "any (SdServerConfig)")),
        "SD-SERVER-EG-REF": lambda obj, elem: setattr(obj, "sd_server_eg_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EventHandler."""
        super().__init__()
        self.consumed_event_group_refs: list[ARRef] = []
        self.event_group: Optional[PositiveInteger] = None
        self.event_multicast_ref: Optional[ARRef] = None
        self.multicast: Optional[PositiveInteger] = None
        self.pdu_activation_routings: list[PduActivationRoutingGroup] = []
        self.routing_group_refs: list[ARRef] = []
        self.sd_server_config: Optional[Any] = None
        self.sd_server_eg_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EventHandler to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EventHandler, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize multicast
        if self.multicast is not None:
            serialized = SerializationHelper.serialize_item(self.multicast, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_activation_routings (list to container "PDU-ACTIVATION-ROUTINGS")
        if self.pdu_activation_routings:
            wrapper = ET.Element("PDU-ACTIVATION-ROUTINGS")
            for item in self.pdu_activation_routings:
                serialized = SerializationHelper.serialize_item(item, "PduActivationRoutingGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize sd_server_eg_ref
        if self.sd_server_eg_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sd_server_eg_ref, "SomeipSdServerEventGroupTimingConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-SERVER-EG-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventHandler":
        """Deserialize XML element to EventHandler object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EventHandler object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EventHandler, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSUMED-EVENT-GROUP-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.consumed_event_group_refs.append(ARRef.deserialize(item_elem))
            elif tag == "EVENT-GROUP":
                setattr(obj, "event_group", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "EVENT-MULTICAST-REF":
                setattr(obj, "event_multicast_ref", ARRef.deserialize(child))
            elif tag == "MULTICAST":
                setattr(obj, "multicast", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PDU-ACTIVATION-ROUTINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.pdu_activation_routings.append(SerializationHelper.deserialize_by_tag(item_elem, "PduActivationRoutingGroup"))
            elif tag == "ROUTING-GROUP-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.routing_group_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SD-SERVER-CONFIG":
                setattr(obj, "sd_server_config", SerializationHelper.deserialize_by_tag(child, "any (SdServerConfig)"))
            elif tag == "SD-SERVER-EG-REF":
                setattr(obj, "sd_server_eg_ref", ARRef.deserialize(child))

        return obj



class EventHandlerBuilder(IdentifiableBuilder):
    """Builder for EventHandler with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EventHandler = EventHandler()


    def with_consumed_event_groups(self, items: list[ConsumedEventGroup]) -> "EventHandlerBuilder":
        """Set consumed_event_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups = list(items) if items else []
        return self

    def with_event_group(self, value: Optional[PositiveInteger]) -> "EventHandlerBuilder":
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

    def with_event_multicast(self, value: Optional[ApplicationEndpoint]) -> "EventHandlerBuilder":
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

    def with_multicast(self, value: Optional[PositiveInteger]) -> "EventHandlerBuilder":
        """Set multicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.multicast = value
        return self

    def with_pdu_activation_routings(self, items: list[PduActivationRoutingGroup]) -> "EventHandlerBuilder":
        """Set pdu_activation_routings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_activation_routings = list(items) if items else []
        return self

    def with_routing_groups(self, items: list[SoAdRoutingGroup]) -> "EventHandlerBuilder":
        """Set routing_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = list(items) if items else []
        return self

    def with_sd_server_config(self, value: Optional[any (SdServerConfig)]) -> "EventHandlerBuilder":
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

    def with_sd_server_eg(self, value: Optional[SomeipSdServerEventGroupTimingConfig]) -> "EventHandlerBuilder":
        """Set sd_server_eg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_server_eg = value
        return self


    def add_consumed_event_group(self, item: ConsumedEventGroup) -> "EventHandlerBuilder":
        """Add a single item to consumed_event_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups.append(item)
        return self

    def clear_consumed_event_groups(self) -> "EventHandlerBuilder":
        """Clear all items from consumed_event_groups list.

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups = []
        return self

    def add_pdu_activation_routing(self, item: PduActivationRoutingGroup) -> "EventHandlerBuilder":
        """Add a single item to pdu_activation_routings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_activation_routings.append(item)
        return self

    def clear_pdu_activation_routings(self) -> "EventHandlerBuilder":
        """Clear all items from pdu_activation_routings list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_activation_routings = []
        return self

    def add_routing_group(self, item: SoAdRoutingGroup) -> "EventHandlerBuilder":
        """Add a single item to routing_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.routing_groups.append(item)
        return self

    def clear_routing_groups(self) -> "EventHandlerBuilder":
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


    def build(self) -> EventHandler:
        """Build and return the EventHandler instance with validation."""
        self._validate_instance()
        pass
        return self._obj