"""ArbitraryEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.confidence_interval import (
    ConfidenceInterval,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ArbitraryEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    confidence_intervals: list[ConfidenceInterval]
    maximums: list[MultidimensionalTime]
    minimums: list[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize ArbitraryEventTriggering."""
        super().__init__()
        self.confidence_intervals: list[ConfidenceInterval] = []
        self.maximums: list[MultidimensionalTime] = []
        self.minimums: list[MultidimensionalTime] = []

    def serialize(self) -> ET.Element:
        """Serialize ArbitraryEventTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ArbitraryEventTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize confidence_intervals (list to container "CONFIDENCE-INTERVALS")
        if self.confidence_intervals:
            wrapper = ET.Element("CONFIDENCE-INTERVALS")
            for item in self.confidence_intervals:
                serialized = SerializationHelper.serialize_item(item, "ConfidenceInterval")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize maximums (list to container "MAXIMUMS")
        if self.maximums:
            wrapper = ET.Element("MAXIMUMS")
            for item in self.maximums:
                serialized = SerializationHelper.serialize_item(item, "MultidimensionalTime")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize minimums (list to container "MINIMUMS")
        if self.minimums:
            wrapper = ET.Element("MINIMUMS")
            for item in self.minimums:
                serialized = SerializationHelper.serialize_item(item, "MultidimensionalTime")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArbitraryEventTriggering":
        """Deserialize XML element to ArbitraryEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArbitraryEventTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ArbitraryEventTriggering, cls).deserialize(element)

        # Parse confidence_intervals (list from container "CONFIDENCE-INTERVALS")
        obj.confidence_intervals = []
        container = SerializationHelper.find_child_element(element, "CONFIDENCE-INTERVALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.confidence_intervals.append(child_value)

        # Parse maximums (list from container "MAXIMUMS")
        obj.maximums = []
        container = SerializationHelper.find_child_element(element, "MAXIMUMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.maximums.append(child_value)

        # Parse minimums (list from container "MINIMUMS")
        obj.minimums = []
        container = SerializationHelper.find_child_element(element, "MINIMUMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.minimums.append(child_value)

        return obj



class ArbitraryEventTriggeringBuilder:
    """Builder for ArbitraryEventTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: ArbitraryEventTriggering = ArbitraryEventTriggering()


    def with_short_name(self, value: Identifier) -> "ArbitraryEventTriggeringBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "ArbitraryEventTriggeringBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "ArbitraryEventTriggeringBuilder":
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

    def with_traces(self, items: list[Traceable]) -> "ArbitraryEventTriggeringBuilder":
        """Set traces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.traces = list(items) if items else []
        return self

    def with_timing_condition(self, value: Optional[TimingCondition]) -> "ArbitraryEventTriggeringBuilder":
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

    def with_event(self, value: Optional[TimingDescriptionEvent]) -> "ArbitraryEventTriggeringBuilder":
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

    def with_confidence_intervals(self, items: list[ConfidenceInterval]) -> "ArbitraryEventTriggeringBuilder":
        """Set confidence_intervals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.confidence_intervals = list(items) if items else []
        return self

    def with_maximums(self, items: list[MultidimensionalTime]) -> "ArbitraryEventTriggeringBuilder":
        """Set maximums list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.maximums = list(items) if items else []
        return self

    def with_minimums(self, items: list[MultidimensionalTime]) -> "ArbitraryEventTriggeringBuilder":
        """Set minimums list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.minimums = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "ArbitraryEventTriggeringBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "ArbitraryEventTriggeringBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_trace(self, item: Traceable) -> "ArbitraryEventTriggeringBuilder":
        """Add a single item to traces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.traces.append(item)
        return self

    def clear_traces(self) -> "ArbitraryEventTriggeringBuilder":
        """Clear all items from traces list.

        Returns:
            self for method chaining
        """
        self._obj.traces = []
        return self

    def add_confidence_interval(self, item: ConfidenceInterval) -> "ArbitraryEventTriggeringBuilder":
        """Add a single item to confidence_intervals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.confidence_intervals.append(item)
        return self

    def clear_confidence_intervals(self) -> "ArbitraryEventTriggeringBuilder":
        """Clear all items from confidence_intervals list.

        Returns:
            self for method chaining
        """
        self._obj.confidence_intervals = []
        return self

    def add_maximum(self, item: MultidimensionalTime) -> "ArbitraryEventTriggeringBuilder":
        """Add a single item to maximums list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.maximums.append(item)
        return self

    def clear_maximums(self) -> "ArbitraryEventTriggeringBuilder":
        """Clear all items from maximums list.

        Returns:
            self for method chaining
        """
        self._obj.maximums = []
        return self

    def add_minimum(self, item: MultidimensionalTime) -> "ArbitraryEventTriggeringBuilder":
        """Add a single item to minimums list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.minimums.append(item)
        return self

    def clear_minimums(self) -> "ArbitraryEventTriggeringBuilder":
        """Clear all items from minimums list.

        Returns:
            self for method chaining
        """
        self._obj.minimums = []
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


    def build(self) -> ArbitraryEventTriggering:
        """Build and return the ArbitraryEventTriggering instance with validation."""
        self._validate_instance()
        pass
        return self._obj