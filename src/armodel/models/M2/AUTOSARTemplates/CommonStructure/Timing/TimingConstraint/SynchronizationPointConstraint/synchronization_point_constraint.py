"""SynchronizationPointConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationPointConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)


class SynchronizationPointConstraint(TimingConstraint):
    """AUTOSAR SynchronizationPointConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    source_eec_refs: list[Any]
    source_event_refs: list[ARRef]
    target_eec_refs: list[Any]
    target_event_refs: list[ARRef]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse source_eec_refs (list from container "SOURCE-EEC-REFS")
        obj.source_eec_refs = []
        container = SerializationHelper.find_child_element(element, "SOURCE-EEC-REFS")
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
                    obj.source_eec_refs.append(child_value)

        # Parse source_event_refs (list from container "SOURCE-EVENT-REFS")
        obj.source_event_refs = []
        container = SerializationHelper.find_child_element(element, "SOURCE-EVENT-REFS")
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
                    obj.source_event_refs.append(child_value)

        # Parse target_eec_refs (list from container "TARGET-EEC-REFS")
        obj.target_eec_refs = []
        container = SerializationHelper.find_child_element(element, "TARGET-EEC-REFS")
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
                    obj.target_eec_refs.append(child_value)

        # Parse target_event_refs (list from container "TARGET-EVENT-REFS")
        obj.target_event_refs = []
        container = SerializationHelper.find_child_element(element, "TARGET-EVENT-REFS")
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
                    obj.target_event_refs.append(child_value)

        return obj



class SynchronizationPointConstraintBuilder:
    """Builder for SynchronizationPointConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SynchronizationPointConstraint = SynchronizationPointConstraint()


    def with_short_name(self, value: Identifier) -> "SynchronizationPointConstraintBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "SynchronizationPointConstraintBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "SynchronizationPointConstraintBuilder":
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

    def with_traces(self, items: list[Traceable]) -> "SynchronizationPointConstraintBuilder":
        """Set traces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.traces = list(items) if items else []
        return self

    def with_timing_condition(self, value: Optional[TimingCondition]) -> "SynchronizationPointConstraintBuilder":
        """Set timing_condition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_condition = value
        return self

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


    def add_short_name_fragment(self, item: ShortNameFragment) -> "SynchronizationPointConstraintBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "SynchronizationPointConstraintBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_trace(self, item: Traceable) -> "SynchronizationPointConstraintBuilder":
        """Add a single item to traces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.traces.append(item)
        return self

    def clear_traces(self) -> "SynchronizationPointConstraintBuilder":
        """Clear all items from traces list.

        Returns:
            self for method chaining
        """
        self._obj.traces = []
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


    def build(self) -> SynchronizationPointConstraint:
        """Build and return the SynchronizationPointConstraint instance with validation."""
        self._validate_instance()
        pass
        return self._obj