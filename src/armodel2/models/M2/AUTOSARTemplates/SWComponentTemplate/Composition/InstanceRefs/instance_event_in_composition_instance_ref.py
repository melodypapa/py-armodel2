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
        "CONTEXT-PROTOTYPE-REFS": lambda obj, elem: [obj.context_prototype_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
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
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-PROTOTYPE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_prototype_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TARGET-EVENT-REF":
                setattr(obj, "target_event_ref", ARRef.deserialize(child))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "base",
        "contextPrototype",
        "targetEvent",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> InstanceEventInCompositionInstanceRef:
        """Build and return the InstanceEventInCompositionInstanceRef instance with validation."""
        self._validate_instance()
        return self._obj