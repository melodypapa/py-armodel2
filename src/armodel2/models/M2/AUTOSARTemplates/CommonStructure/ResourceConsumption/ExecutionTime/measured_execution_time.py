"""MeasuredExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import ExecutionTimeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MeasuredExecutionTime(ExecutionTime):
    """AUTOSAR MeasuredExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    maximum_execution_time: Optional[MultidimensionalTime]
    minimum_execution_time: Optional[MultidimensionalTime]
    nominal_execution_time: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize MeasuredExecutionTime."""
        super().__init__()
        self.maximum_execution_time: Optional[MultidimensionalTime] = None
        self.minimum_execution_time: Optional[MultidimensionalTime] = None
        self.nominal_execution_time: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize MeasuredExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MeasuredExecutionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize maximum_execution_time
        if self.maximum_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.maximum_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_execution_time
        if self.minimum_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nominal_execution_time
        if self.nominal_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.nominal_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOMINAL-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredExecutionTime":
        """Deserialize XML element to MeasuredExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MeasuredExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MeasuredExecutionTime, cls).deserialize(element)

        # Parse maximum_execution_time
        child = SerializationHelper.find_child_element(element, "MAXIMUM-EXECUTION-TIME")
        if child is not None:
            maximum_execution_time_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum_execution_time = maximum_execution_time_value

        # Parse minimum_execution_time
        child = SerializationHelper.find_child_element(element, "MINIMUM-EXECUTION-TIME")
        if child is not None:
            minimum_execution_time_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum_execution_time = minimum_execution_time_value

        # Parse nominal_execution_time
        child = SerializationHelper.find_child_element(element, "NOMINAL-EXECUTION-TIME")
        if child is not None:
            nominal_execution_time_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.nominal_execution_time = nominal_execution_time_value

        return obj



class MeasuredExecutionTimeBuilder(ExecutionTimeBuilder):
    """Builder for MeasuredExecutionTime with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MeasuredExecutionTime = MeasuredExecutionTime()


    def with_maximum_execution_time(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTimeBuilder":
        """Set maximum_execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum_execution_time = value
        return self

    def with_minimum_execution_time(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTimeBuilder":
        """Set minimum_execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_execution_time = value
        return self

    def with_nominal_execution_time(self, value: Optional[MultidimensionalTime]) -> "MeasuredExecutionTimeBuilder":
        """Set nominal_execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nominal_execution_time = value
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


    def build(self) -> MeasuredExecutionTime:
        """Build and return the MeasuredExecutionTime instance with validation."""
        self._validate_instance()
        pass
        return self._obj