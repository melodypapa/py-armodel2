"""EventControlledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 397)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EventControlledTiming(Describable):
    """AUTOSAR EventControlledTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EVENT-CONTROLLED-TIMING"


    number_of_repetitions: Optional[Integer]
    repetition_period: Optional[TimeRangeType]
    _DESERIALIZE_DISPATCH = {
        "NUMBER-OF-REPETITIONS": lambda obj, elem: setattr(obj, "number_of_repetitions", elem.text),
        "REPETITION-PERIOD": lambda obj, elem: setattr(obj, "repetition_period", TimeRangeType.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EventControlledTiming."""
        super().__init__()
        self.number_of_repetitions: Optional[Integer] = None
        self.repetition_period: Optional[TimeRangeType] = None

    def serialize(self) -> ET.Element:
        """Serialize EventControlledTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EventControlledTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize number_of_repetitions
        if self.number_of_repetitions is not None:
            serialized = SerializationHelper.serialize_item(self.number_of_repetitions, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMBER-OF-REPETITIONS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize repetition_period
        if self.repetition_period is not None:
            serialized = SerializationHelper.serialize_item(self.repetition_period, "TimeRangeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REPETITION-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventControlledTiming":
        """Deserialize XML element to EventControlledTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EventControlledTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EventControlledTiming, cls).deserialize(element)

        # Parse number_of_repetitions
        child = SerializationHelper.find_child_element(element, "NUMBER-OF-REPETITIONS")
        if child is not None:
            number_of_repetitions_value = child.text
            obj.number_of_repetitions = number_of_repetitions_value

        # Parse repetition_period
        child = SerializationHelper.find_child_element(element, "REPETITION-PERIOD")
        if child is not None:
            repetition_period_value = SerializationHelper.deserialize_by_tag(child, "TimeRangeType")
            obj.repetition_period = repetition_period_value

        return obj



class EventControlledTimingBuilder(DescribableBuilder):
    """Builder for EventControlledTiming with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EventControlledTiming = EventControlledTiming()


    def with_number_of_repetitions(self, value: Optional[Integer]) -> "EventControlledTimingBuilder":
        """Set number_of_repetitions attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.number_of_repetitions = value
        return self

    def with_repetition_period(self, value: Optional[TimeRangeType]) -> "EventControlledTimingBuilder":
        """Set repetition_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.repetition_period = value
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


    def build(self) -> EventControlledTiming:
        """Build and return the EventControlledTiming instance with validation."""
        self._validate_instance()
        pass
        return self._obj