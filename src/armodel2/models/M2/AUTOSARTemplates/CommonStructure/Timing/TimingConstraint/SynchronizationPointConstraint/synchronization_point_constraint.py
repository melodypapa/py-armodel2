"""SynchronizationPointConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationPointConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import TimingConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SynchronizationPointConstraint(TimingConstraint):
    """AUTOSAR SynchronizationPointConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SYNCHRONIZATION-POINT-CONSTRAINT"


    source_eec_refs: list[Any]
    source_event_refs: list[ARRef]
    target_eec_refs: list[Any]
    target_event_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SOURCE-EEC-REFS": lambda obj, elem: [obj.source_eec_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SOURCE-EVENT-REFS": ("_POLYMORPHIC_LIST", "source_event_refs", ["BswEvent", "RTEEvent"]),
        "TARGET-EEC-REFS": lambda obj, elem: [obj.target_eec_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "TARGET-EVENT-REFS": ("_POLYMORPHIC_LIST", "target_event_refs", ["BswEvent", "RTEEvent"]),
    }


    def __init__(self) -> None:
        """Initialize SynchronizationPointConstraint."""
        super().__init__()
        self.source_eec_refs: list[Any] = []
        self.source_event_refs: list[ARRef] = []
        self.target_eec_refs: list[Any] = []
        self.target_event_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SynchronizationPointConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SynchronizationPointConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize source_eec_refs (list to container "SOURCE-EEC-REFS")
        if self.source_eec_refs:
            wrapper = ET.Element("SOURCE-EEC-REFS")
            for item in self.source_eec_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("SOURCE-EEC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_event_refs (list to container "SOURCE-EVENT-REFS")
        if self.source_event_refs:
            wrapper = ET.Element("SOURCE-EVENT-REFS")
            for item in self.source_event_refs:
                serialized = SerializationHelper.serialize_item(item, "AbstractEvent")
                if serialized is not None:
                    child_elem = ET.Element("SOURCE-EVENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_eec_refs (list to container "TARGET-EEC-REFS")
        if self.target_eec_refs:
            wrapper = ET.Element("TARGET-EEC-REFS")
            for item in self.target_eec_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("TARGET-EEC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_event_refs (list to container "TARGET-EVENT-REFS")
        if self.target_event_refs:
            wrapper = ET.Element("TARGET-EVENT-REFS")
            for item in self.target_event_refs:
                serialized = SerializationHelper.serialize_item(item, "AbstractEvent")
                if serialized is not None:
                    child_elem = ET.Element("TARGET-EVENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronizationPointConstraint":
        """Deserialize XML element to SynchronizationPointConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SynchronizationPointConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SynchronizationPointConstraint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SOURCE-EEC-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.source_eec_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SOURCE-EVENT-REFS":
                for item_elem in child:
                    obj.source_event_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TARGET-EEC-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.target_eec_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TARGET-EVENT-REFS":
                for item_elem in child:
                    obj.target_event_refs.append(ARRef.deserialize(item_elem))

        return obj



class SynchronizationPointConstraintBuilder(TimingConstraintBuilder):
    """Builder for SynchronizationPointConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SynchronizationPointConstraint = SynchronizationPointConstraint()


    def with_source_eecs(self, items: list[any (EOCExecutableEntity)]) -> "SynchronizationPointConstraintBuilder":
        """Set source_eecs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.source_eecs = list(items) if items else []
        return self

    def with_source_events(self, items: list[AbstractEvent]) -> "SynchronizationPointConstraintBuilder":
        """Set source_events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.source_events = list(items) if items else []
        return self

    def with_target_eecs(self, items: list[any (EOCExecutableEntity)]) -> "SynchronizationPointConstraintBuilder":
        """Set target_eecs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.target_eecs = list(items) if items else []
        return self

    def with_target_events(self, items: list[AbstractEvent]) -> "SynchronizationPointConstraintBuilder":
        """Set target_events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.target_events = list(items) if items else []
        return self


    def add_source_eec(self, item: any (EOCExecutableEntity)) -> "SynchronizationPointConstraintBuilder":
        """Add a single item to source_eecs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.source_eecs.append(item)
        return self

    def clear_source_eecs(self) -> "SynchronizationPointConstraintBuilder":
        """Clear all items from source_eecs list.

        Returns:
            self for method chaining
        """
        self._obj.source_eecs = []
        return self

    def add_source_event(self, item: AbstractEvent) -> "SynchronizationPointConstraintBuilder":
        """Add a single item to source_events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.source_events.append(item)
        return self

    def clear_source_events(self) -> "SynchronizationPointConstraintBuilder":
        """Clear all items from source_events list.

        Returns:
            self for method chaining
        """
        self._obj.source_events = []
        return self

    def add_target_eec(self, item: any (EOCExecutableEntity)) -> "SynchronizationPointConstraintBuilder":
        """Add a single item to target_eecs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.target_eecs.append(item)
        return self

    def clear_target_eecs(self) -> "SynchronizationPointConstraintBuilder":
        """Clear all items from target_eecs list.

        Returns:
            self for method chaining
        """
        self._obj.target_eecs = []
        return self

    def add_target_event(self, item: AbstractEvent) -> "SynchronizationPointConstraintBuilder":
        """Add a single item to target_events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.target_events.append(item)
        return self

    def clear_target_events(self) -> "SynchronizationPointConstraintBuilder":
        """Clear all items from target_events list.

        Returns:
            self for method chaining
        """
        self._obj.target_events = []
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


    def build(self) -> SynchronizationPointConstraint:
        """Build and return the SynchronizationPointConstraint instance with validation."""
        self._validate_instance()
        pass
        return self._obj