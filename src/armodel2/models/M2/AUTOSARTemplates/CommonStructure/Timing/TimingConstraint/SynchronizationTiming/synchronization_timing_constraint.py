"""SynchronizationTimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 92)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationTiming.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import TimingConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
    EventOccurrenceKindEnum,
    SynchronizationTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SynchronizationTimingConstraint(TimingConstraint):
    """AUTOSAR SynchronizationTimingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SYNCHRONIZATION-TIMING-CONSTRAINT"


    event: Optional[EventOccurrenceKindEnum]
    scope_refs: list[ARRef]
    scope_event_refs: list[ARRef]
    synchronization: Optional[SynchronizationTypeEnum]
    tolerance: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "EVENT": lambda obj, elem: setattr(obj, "event", EventOccurrenceKindEnum.deserialize(elem)),
        "SCOPES": ("_POLYMORPHIC_LIST", "scope_refs", ["TDEventBsw", "TDEventBswInternalBehavior", "TDEventCom", "TDEventComplex", "TDEventSLLET", "TDEventSwc", "TDEventVfb"]),
        "SCOPE-EVENTS": ("_POLYMORPHIC_LIST", "scope_event_refs", ["TDEventBsw", "TDEventBswInternalBehavior", "TDEventCom", "TDEventComplex", "TDEventSLLET", "TDEventSwc", "TDEventVfb"]),
        "SYNCHRONIZATION": lambda obj, elem: setattr(obj, "synchronization", SynchronizationTypeEnum.deserialize(elem)),
        "TOLERANCE": lambda obj, elem: setattr(obj, "tolerance", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize SynchronizationTimingConstraint."""
        super().__init__()
        self.event: Optional[EventOccurrenceKindEnum] = None
        self.scope_refs: list[ARRef] = []
        self.scope_event_refs: list[ARRef] = []
        self.synchronization: Optional[SynchronizationTypeEnum] = None
        self.tolerance: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize SynchronizationTimingConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SynchronizationTimingConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event
        if self.event is not None:
            serialized = SerializationHelper.serialize_item(self.event, "EventOccurrenceKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scope_refs (list to container "SCOPE-REFS")
        if self.scope_refs:
            wrapper = ET.Element("SCOPE-REFS")
            for item in self.scope_refs:
                serialized = SerializationHelper.serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    child_elem = ET.Element("SCOPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scope_event_refs (list to container "SCOPE-EVENT-REFS")
        if self.scope_event_refs:
            wrapper = ET.Element("SCOPE-EVENT-REFS")
            for item in self.scope_event_refs:
                serialized = SerializationHelper.serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    child_elem = ET.Element("SCOPE-EVENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize synchronization
        if self.synchronization is not None:
            serialized = SerializationHelper.serialize_item(self.synchronization, "SynchronizationTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNCHRONIZATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tolerance
        if self.tolerance is not None:
            serialized = SerializationHelper.serialize_item(self.tolerance, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOLERANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronizationTimingConstraint":
        """Deserialize XML element to SynchronizationTimingConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SynchronizationTimingConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SynchronizationTimingConstraint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EVENT":
                setattr(obj, "event", EventOccurrenceKindEnum.deserialize(child))
            elif tag == "SCOPES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "T-D-EVENT-BSW":
                        obj.scope_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventBsw"))
                    elif concrete_tag == "T-D-EVENT-BSW-INTERNAL-BEHAVIOR":
                        obj.scope_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventBswInternalBehavior"))
                    elif concrete_tag == "T-D-EVENT-COM":
                        obj.scope_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventCom"))
                    elif concrete_tag == "T-D-EVENT-COMPLEX":
                        obj.scope_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventComplex"))
                    elif concrete_tag == "T-D-EVENT-S-L-L-E-T":
                        obj.scope_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventSLLET"))
                    elif concrete_tag == "T-D-EVENT-SWC":
                        obj.scope_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventSwc"))
                    elif concrete_tag == "T-D-EVENT-VFB":
                        obj.scope_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventVfb"))
            elif tag == "SCOPE-EVENTS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "T-D-EVENT-BSW":
                        obj.scope_event_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventBsw"))
                    elif concrete_tag == "T-D-EVENT-BSW-INTERNAL-BEHAVIOR":
                        obj.scope_event_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventBswInternalBehavior"))
                    elif concrete_tag == "T-D-EVENT-COM":
                        obj.scope_event_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventCom"))
                    elif concrete_tag == "T-D-EVENT-COMPLEX":
                        obj.scope_event_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventComplex"))
                    elif concrete_tag == "T-D-EVENT-S-L-L-E-T":
                        obj.scope_event_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventSLLET"))
                    elif concrete_tag == "T-D-EVENT-SWC":
                        obj.scope_event_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventSwc"))
                    elif concrete_tag == "T-D-EVENT-VFB":
                        obj.scope_event_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventVfb"))
            elif tag == "SYNCHRONIZATION":
                setattr(obj, "synchronization", SynchronizationTypeEnum.deserialize(child))
            elif tag == "TOLERANCE":
                setattr(obj, "tolerance", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class SynchronizationTimingConstraintBuilder(TimingConstraintBuilder):
    """Builder for SynchronizationTimingConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SynchronizationTimingConstraint = SynchronizationTimingConstraint()


    def with_event(self, value: Optional[EventOccurrenceKindEnum]) -> "SynchronizationTimingConstraintBuilder":
        """Set event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event = value
        return self

    def with_scopes(self, items: list[TimingDescriptionEvent]) -> "SynchronizationTimingConstraintBuilder":
        """Set scopes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.scopes = list(items) if items else []
        return self

    def with_scope_events(self, items: list[TimingDescriptionEvent]) -> "SynchronizationTimingConstraintBuilder":
        """Set scope_events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.scope_events = list(items) if items else []
        return self

    def with_synchronization(self, value: Optional[SynchronizationTypeEnum]) -> "SynchronizationTimingConstraintBuilder":
        """Set synchronization attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.synchronization = value
        return self

    def with_tolerance(self, value: Optional[MultidimensionalTime]) -> "SynchronizationTimingConstraintBuilder":
        """Set tolerance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tolerance = value
        return self


    def add_scope(self, item: TimingDescriptionEvent) -> "SynchronizationTimingConstraintBuilder":
        """Add a single item to scopes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.scopes.append(item)
        return self

    def clear_scopes(self) -> "SynchronizationTimingConstraintBuilder":
        """Clear all items from scopes list.

        Returns:
            self for method chaining
        """
        self._obj.scopes = []
        return self

    def add_scope_event(self, item: TimingDescriptionEvent) -> "SynchronizationTimingConstraintBuilder":
        """Add a single item to scope_events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.scope_events.append(item)
        return self

    def clear_scope_events(self) -> "SynchronizationTimingConstraintBuilder":
        """Clear all items from scope_events list.

        Returns:
            self for method chaining
        """
        self._obj.scope_events = []
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


    def build(self) -> SynchronizationTimingConstraint:
        """Build and return the SynchronizationTimingConstraint instance with validation."""
        self._validate_instance()
        pass
        return self._obj