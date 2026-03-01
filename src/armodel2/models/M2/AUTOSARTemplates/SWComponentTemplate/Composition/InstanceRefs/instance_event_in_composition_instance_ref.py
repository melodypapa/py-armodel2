"""InstanceEventInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 959)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InstanceEventInCompositionInstanceRef(ARObject):
    """AUTOSAR InstanceEventInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INSTANCE-EVENT-IN-COMPOSITION-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_prototype_refs: list[Any]
    target_event_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": lambda obj, elem: setattr(obj, "base_ref", ARRef.deserialize(elem)),
        "CONTEXT-PROTOTYPES": lambda obj, elem: obj.context_prototype_refs.append(ARRef.deserialize(elem)),
        "TARGET-EVENT-REF": ("_POLYMORPHIC", "target_event_ref", ["AsynchronousServerCallReturnsEvent", "BackgroundEvent", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "ExternalTriggerOccurredEvent", "InitEvent", "InternalTriggerOccurredEvent", "ModeSwitchedAckEvent", "OperationInvokedEvent", "OsTaskExecutionEvent", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "TimingEvent", "TransformerHardErrorEvent"]),
    }


    def __init__(self) -> None:
        """Initialize InstanceEventInCompositionInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_prototype_refs: list[Any] = []
        self.target_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize InstanceEventInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InstanceEventInCompositionInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_prototype_refs (list to container "CONTEXT-PROTOTYPE-REFS")
        if self.context_prototype_refs:
            wrapper = ET.Element("CONTEXT-PROTOTYPE-REFS")
            for item in self.context_prototype_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-PROTOTYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_event_ref
        if self.target_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_event_ref, "RTEEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstanceEventInCompositionInstanceRef":
        """Deserialize XML element to InstanceEventInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InstanceEventInCompositionInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InstanceEventInCompositionInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-PROTOTYPES":
                obj.context_prototype_refs.append(ARRef.deserialize(child))
            elif tag == "TARGET-EVENT-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "BackgroundEvent"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "DataWriteCompletedEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "INIT-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchedAckEvent"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "OsTaskExecutionEvent"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcModeSwitchEvent"))
                    elif concrete_tag == "TIMING-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        setattr(obj, "target_event_ref", SerializationHelper.deserialize_by_tag(child[0], "TransformerHardErrorEvent"))

        return obj



class InstanceEventInCompositionInstanceRefBuilder(BuilderBase):
    """Builder for InstanceEventInCompositionInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InstanceEventInCompositionInstanceRef = InstanceEventInCompositionInstanceRef()


    def with_base(self, value: Optional[CompositionSwComponentType]) -> "InstanceEventInCompositionInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base = value
        return self

    def with_context_prototypes(self, items: list[any (SwComponent)]) -> "InstanceEventInCompositionInstanceRefBuilder":
        """Set context_prototypes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_prototypes = list(items) if items else []
        return self

    def with_target_event(self, value: Optional[RTEEvent]) -> "InstanceEventInCompositionInstanceRefBuilder":
        """Set target_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_event = value
        return self


    def add_context_prototype(self, item: any (SwComponent)) -> "InstanceEventInCompositionInstanceRefBuilder":
        """Add a single item to context_prototypes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_prototypes.append(item)
        return self

    def clear_context_prototypes(self) -> "InstanceEventInCompositionInstanceRefBuilder":
        """Clear all items from context_prototypes list.

        Returns:
            self for method chaining
        """
        self._obj.context_prototypes = []
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


    def build(self) -> InstanceEventInCompositionInstanceRef:
        """Build and return the InstanceEventInCompositionInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj