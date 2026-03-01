"""ArbitraryEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import EventTriggeringConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.confidence_interval import (
    ConfidenceInterval,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ArbitraryEventTriggering(EventTriggeringConstraint):
    """AUTOSAR ArbitraryEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ARBITRARY-EVENT-TRIGGERING"


    confidence_intervals: list[ConfidenceInterval]
    maximums: list[MultidimensionalTime]
    minimums: list[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "CONFIDENCE-INTERVALS": lambda obj, elem: obj.confidence_intervals.append(SerializationHelper.deserialize_by_tag(elem, "ConfidenceInterval")),
        "MAXIMUMS": lambda obj, elem: obj.maximums.append(SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
        "MINIMUMS": lambda obj, elem: obj.minimums.append(SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CONFIDENCE-INTERVALS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.confidence_intervals.append(SerializationHelper.deserialize_by_tag(item_elem, "ConfidenceInterval"))
            elif tag == "MAXIMUMS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.maximums.append(SerializationHelper.deserialize_by_tag(item_elem, "MultidimensionalTime"))
            elif tag == "MINIMUMS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.minimums.append(SerializationHelper.deserialize_by_tag(item_elem, "MultidimensionalTime"))

        return obj



class ArbitraryEventTriggeringBuilder(EventTriggeringConstraintBuilder):
    """Builder for ArbitraryEventTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ArbitraryEventTriggering = ArbitraryEventTriggering()


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


    def build(self) -> ArbitraryEventTriggering:
        """Build and return the ArbitraryEventTriggering instance with validation."""
        self._validate_instance()
        pass
        return self._obj