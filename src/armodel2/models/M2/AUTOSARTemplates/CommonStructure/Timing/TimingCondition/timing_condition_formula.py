"""TimingConditionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_condition import (
    TimingCondition,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimingConditionFormula(ARObject):
    """AUTOSAR TimingConditionFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timing_argument_argument_instance_ref: Optional[ARRef]
    timing_condition_ref: Optional[ARRef]
    timing_event_ref: Optional[ARRef]
    timing_mode_ref: Optional[ARRef]
    timing_variable_instance_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize TimingConditionFormula."""
        super().__init__()
        self.timing_argument_argument_instance_ref: Optional[ARRef] = None
        self.timing_condition_ref: Optional[ARRef] = None
        self.timing_event_ref: Optional[ARRef] = None
        self.timing_mode_ref: Optional[ARRef] = None
        self.timing_variable_instance_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingConditionFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingConditionFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timing_argument_argument_instance_ref
        if self.timing_argument_argument_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_argument_argument_instance_ref, "AutosarOperationArgumentInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-ARGUMENT-ARGUMENT-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_condition_ref
        if self.timing_condition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_condition_ref, "TimingCondition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-CONDITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_event_ref
        if self.timing_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_event_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_mode_ref
        if self.timing_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_mode_ref, "TimingModeInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_variable_instance_ref
        if self.timing_variable_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_variable_instance_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-VARIABLE-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingConditionFormula":
        """Deserialize XML element to TimingConditionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingConditionFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingConditionFormula, cls).deserialize(element)

        # Parse timing_argument_argument_instance_ref
        child = SerializationHelper.find_child_element(element, "TIMING-ARGUMENT-ARGUMENT-INSTANCE-REF")
        if child is not None:
            timing_argument_argument_instance_ref_value = ARRef.deserialize(child)
            obj.timing_argument_argument_instance_ref = timing_argument_argument_instance_ref_value

        # Parse timing_condition_ref
        child = SerializationHelper.find_child_element(element, "TIMING-CONDITION-REF")
        if child is not None:
            timing_condition_ref_value = ARRef.deserialize(child)
            obj.timing_condition_ref = timing_condition_ref_value

        # Parse timing_event_ref
        child = SerializationHelper.find_child_element(element, "TIMING-EVENT-REF")
        if child is not None:
            timing_event_ref_value = ARRef.deserialize(child)
            obj.timing_event_ref = timing_event_ref_value

        # Parse timing_mode_ref
        child = SerializationHelper.find_child_element(element, "TIMING-MODE-REF")
        if child is not None:
            timing_mode_ref_value = ARRef.deserialize(child)
            obj.timing_mode_ref = timing_mode_ref_value

        # Parse timing_variable_instance_ref
        child = SerializationHelper.find_child_element(element, "TIMING-VARIABLE-INSTANCE-REF")
        if child is not None:
            timing_variable_instance_ref_value = ARRef.deserialize(child)
            obj.timing_variable_instance_ref = timing_variable_instance_ref_value

        return obj



class TimingConditionFormulaBuilder(BuilderBase):
    """Builder for TimingConditionFormula with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimingConditionFormula = TimingConditionFormula()


    def with_timing_argument_argument_instance(self, value: Optional[AutosarOperationArgumentInstance]) -> "TimingConditionFormulaBuilder":
        """Set timing_argument_argument_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_argument_argument_instance = value
        return self

    def with_timing_condition(self, value: Optional[TimingCondition]) -> "TimingConditionFormulaBuilder":
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

    def with_timing_event(self, value: Optional[TimingDescriptionEvent]) -> "TimingConditionFormulaBuilder":
        """Set timing_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_event = value
        return self

    def with_timing_mode(self, value: Optional[TimingModeInstance]) -> "TimingConditionFormulaBuilder":
        """Set timing_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_mode = value
        return self

    def with_timing_variable_instance(self, value: Optional[any (AutosarVariable)]) -> "TimingConditionFormulaBuilder":
        """Set timing_variable_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_variable_instance = value
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


    def build(self) -> TimingConditionFormula:
        """Build and return the TimingConditionFormula instance with validation."""
        self._validate_instance()
        pass
        return self._obj