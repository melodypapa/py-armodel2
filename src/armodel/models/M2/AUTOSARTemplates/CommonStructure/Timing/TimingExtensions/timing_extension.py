"""TimingExtension AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 254)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock_sync_accuracy import (
    TimingClockSyncAccuracy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TimingExtension(ARElement, ABC):
    """AUTOSAR TimingExtension."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    timing_clocks: list[TimingClock]
    timing_clock_syncs: list[TimingClockSyncAccuracy]
    timing_conditions: list[TimingCondition]
    timings: list[TimingConstraint]
    timing_resource: Optional[TimingExtension]
    def __init__(self) -> None:
        """Initialize TimingExtension."""
        super().__init__()
        self.timing_clocks: list[TimingClock] = []
        self.timing_clock_syncs: list[TimingClockSyncAccuracy] = []
        self.timing_conditions: list[TimingCondition] = []
        self.timings: list[TimingConstraint] = []
        self.timing_resource: Optional[TimingExtension] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingExtension to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingExtension, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timing_clocks (list to container "TIMING-CLOCKS")
        if self.timing_clocks:
            wrapper = ET.Element("TIMING-CLOCKS")
            for item in self.timing_clocks:
                serialized = SerializationHelper.serialize_item(item, "TimingClock")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_clock_syncs (list to container "TIMING-CLOCK-SYNCS")
        if self.timing_clock_syncs:
            wrapper = ET.Element("TIMING-CLOCK-SYNCS")
            for item in self.timing_clock_syncs:
                serialized = SerializationHelper.serialize_item(item, "TimingClockSyncAccuracy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_conditions (list to container "TIMING-CONDITIONS")
        if self.timing_conditions:
            wrapper = ET.Element("TIMING-CONDITIONS")
            for item in self.timing_conditions:
                serialized = SerializationHelper.serialize_item(item, "TimingCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timings (list to container "TIMINGS")
        if self.timings:
            wrapper = ET.Element("TIMINGS")
            for item in self.timings:
                serialized = SerializationHelper.serialize_item(item, "TimingConstraint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_resource
        if self.timing_resource is not None:
            serialized = SerializationHelper.serialize_item(self.timing_resource, "TimingExtension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtension":
        """Deserialize XML element to TimingExtension object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingExtension object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingExtension, cls).deserialize(element)

        # Parse timing_clocks (list from container "TIMING-CLOCKS")
        obj.timing_clocks = []
        container = SerializationHelper.find_child_element(element, "TIMING-CLOCKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_clocks.append(child_value)

        # Parse timing_clock_syncs (list from container "TIMING-CLOCK-SYNCS")
        obj.timing_clock_syncs = []
        container = SerializationHelper.find_child_element(element, "TIMING-CLOCK-SYNCS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_clock_syncs.append(child_value)

        # Parse timing_conditions (list from container "TIMING-CONDITIONS")
        obj.timing_conditions = []
        container = SerializationHelper.find_child_element(element, "TIMING-CONDITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_conditions.append(child_value)

        # Parse timings (list from container "TIMINGS")
        obj.timings = []
        container = SerializationHelper.find_child_element(element, "TIMINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timings.append(child_value)

        # Parse timing_resource
        child = SerializationHelper.find_child_element(element, "TIMING-RESOURCE")
        if child is not None:
            timing_resource_value = SerializationHelper.deserialize_by_tag(child, "TimingExtension")
            obj.timing_resource = timing_resource_value

        return obj



class TimingExtensionBuilder(ARElementBuilder):
    """Builder for TimingExtension with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimingExtension = TimingExtension()


    def with_timing_clocks(self, items: list[TimingClock]) -> "TimingExtensionBuilder":
        """Set timing_clocks list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.timing_clocks = list(items) if items else []
        return self

    def with_timing_clock_syncs(self, items: list[TimingClockSyncAccuracy]) -> "TimingExtensionBuilder":
        """Set timing_clock_syncs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.timing_clock_syncs = list(items) if items else []
        return self

    def with_timing_conditions(self, items: list[TimingCondition]) -> "TimingExtensionBuilder":
        """Set timing_conditions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.timing_conditions = list(items) if items else []
        return self

    def with_timings(self, items: list[TimingConstraint]) -> "TimingExtensionBuilder":
        """Set timings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.timings = list(items) if items else []
        return self

    def with_timing_resource(self, value: Optional[TimingExtension]) -> "TimingExtensionBuilder":
        """Set timing_resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_resource = value
        return self


    def add_timing_clock(self, item: TimingClock) -> "TimingExtensionBuilder":
        """Add a single item to timing_clocks list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.timing_clocks.append(item)
        return self

    def clear_timing_clocks(self) -> "TimingExtensionBuilder":
        """Clear all items from timing_clocks list.

        Returns:
            self for method chaining
        """
        self._obj.timing_clocks = []
        return self

    def add_timing_clock_sync(self, item: TimingClockSyncAccuracy) -> "TimingExtensionBuilder":
        """Add a single item to timing_clock_syncs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.timing_clock_syncs.append(item)
        return self

    def clear_timing_clock_syncs(self) -> "TimingExtensionBuilder":
        """Clear all items from timing_clock_syncs list.

        Returns:
            self for method chaining
        """
        self._obj.timing_clock_syncs = []
        return self

    def add_timing_condition(self, item: TimingCondition) -> "TimingExtensionBuilder":
        """Add a single item to timing_conditions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.timing_conditions.append(item)
        return self

    def clear_timing_conditions(self) -> "TimingExtensionBuilder":
        """Clear all items from timing_conditions list.

        Returns:
            self for method chaining
        """
        self._obj.timing_conditions = []
        return self

    def add_timing(self, item: TimingConstraint) -> "TimingExtensionBuilder":
        """Add a single item to timings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.timings.append(item)
        return self

    def clear_timings(self) -> "TimingExtensionBuilder":
        """Clear all items from timings list.

        Returns:
            self for method chaining
        """
        self._obj.timings = []
        return self



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


    @abstractmethod
    def build(self) -> TimingExtension:
        """Build and return the TimingExtension instance (abstract)."""
        raise NotImplementedError