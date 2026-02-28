"""BurstPatternEventTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import (
    EventTriggeringConstraint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint.event_triggering_constraint import EventTriggeringConstraintBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BurstPatternEventTriggering(EventTriggeringConstraint):
    """AUTOSAR BurstPatternEventTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BURST-PATTERN-EVENT-TRIGGERING"


    max_number_of: Optional[PositiveInteger]
    minimum_inter: Optional[MultidimensionalTime]
    min_number_of: Optional[PositiveInteger]
    pattern_jitter: Optional[MultidimensionalTime]
    pattern_length: Optional[MultidimensionalTime]
    pattern_period: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "MAX-NUMBER-OF": lambda obj, elem: setattr(obj, "max_number_of", elem.text),
        "MINIMUM-INTER": lambda obj, elem: setattr(obj, "minimum_inter", MultidimensionalTime.deserialize(elem)),
        "MIN-NUMBER-OF": lambda obj, elem: setattr(obj, "min_number_of", elem.text),
        "PATTERN-JITTER": lambda obj, elem: setattr(obj, "pattern_jitter", MultidimensionalTime.deserialize(elem)),
        "PATTERN-LENGTH": lambda obj, elem: setattr(obj, "pattern_length", MultidimensionalTime.deserialize(elem)),
        "PATTERN-PERIOD": lambda obj, elem: setattr(obj, "pattern_period", MultidimensionalTime.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BurstPatternEventTriggering."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.minimum_inter: Optional[MultidimensionalTime] = None
        self.min_number_of: Optional[PositiveInteger] = None
        self.pattern_jitter: Optional[MultidimensionalTime] = None
        self.pattern_length: Optional[MultidimensionalTime] = None
        self.pattern_period: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize BurstPatternEventTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BurstPatternEventTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_inter
        if self.minimum_inter is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_inter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-INTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_number_of
        if self.min_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.min_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_jitter
        if self.pattern_jitter is not None:
            serialized = SerializationHelper.serialize_item(self.pattern_jitter, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-JITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_length
        if self.pattern_length is not None:
            serialized = SerializationHelper.serialize_item(self.pattern_length, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern_period
        if self.pattern_period is not None:
            serialized = SerializationHelper.serialize_item(self.pattern_period, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BurstPatternEventTriggering":
        """Deserialize XML element to BurstPatternEventTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BurstPatternEventTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BurstPatternEventTriggering, cls).deserialize(element)

        # Parse max_number_of
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse minimum_inter
        child = SerializationHelper.find_child_element(element, "MINIMUM-INTER")
        if child is not None:
            minimum_inter_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum_inter = minimum_inter_value

        # Parse min_number_of
        child = SerializationHelper.find_child_element(element, "MIN-NUMBER-OF")
        if child is not None:
            min_number_of_value = child.text
            obj.min_number_of = min_number_of_value

        # Parse pattern_jitter
        child = SerializationHelper.find_child_element(element, "PATTERN-JITTER")
        if child is not None:
            pattern_jitter_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_jitter = pattern_jitter_value

        # Parse pattern_length
        child = SerializationHelper.find_child_element(element, "PATTERN-LENGTH")
        if child is not None:
            pattern_length_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_length = pattern_length_value

        # Parse pattern_period
        child = SerializationHelper.find_child_element(element, "PATTERN-PERIOD")
        if child is not None:
            pattern_period_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.pattern_period = pattern_period_value

        return obj



class BurstPatternEventTriggeringBuilder(EventTriggeringConstraintBuilder):
    """Builder for BurstPatternEventTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BurstPatternEventTriggering = BurstPatternEventTriggering()


    def with_max_number_of(self, value: Optional[PositiveInteger]) -> "BurstPatternEventTriggeringBuilder":
        """Set max_number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number_of = value
        return self

    def with_minimum_inter(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggeringBuilder":
        """Set minimum_inter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_inter = value
        return self

    def with_min_number_of(self, value: Optional[PositiveInteger]) -> "BurstPatternEventTriggeringBuilder":
        """Set min_number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_number_of = value
        return self

    def with_pattern_jitter(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggeringBuilder":
        """Set pattern_jitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pattern_jitter = value
        return self

    def with_pattern_length(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggeringBuilder":
        """Set pattern_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pattern_length = value
        return self

    def with_pattern_period(self, value: Optional[MultidimensionalTime]) -> "BurstPatternEventTriggeringBuilder":
        """Set pattern_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pattern_period = value
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


    def build(self) -> BurstPatternEventTriggering:
        """Build and return the BurstPatternEventTriggering instance with validation."""
        self._validate_instance()
        pass
        return self._obj