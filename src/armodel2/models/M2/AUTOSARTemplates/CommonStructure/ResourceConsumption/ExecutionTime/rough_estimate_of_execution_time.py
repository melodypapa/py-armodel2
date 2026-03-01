"""RoughEstimateOfExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 167)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import ExecutionTimeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RoughEstimateOfExecutionTime(ExecutionTime):
    """AUTOSAR RoughEstimateOfExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ROUGH-ESTIMATE-OF-EXECUTION-TIME"


    additional: Optional[String]
    estimated_execution_time: Optional[MultidimensionalTime]
    _DESERIALIZE_DISPATCH = {
        "ADDITIONAL": lambda obj, elem: setattr(obj, "additional", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ESTIMATED-EXECUTION-TIME": lambda obj, elem: setattr(obj, "estimated_execution_time", SerializationHelper.deserialize_by_tag(elem, "MultidimensionalTime")),
    }


    def __init__(self) -> None:
        """Initialize RoughEstimateOfExecutionTime."""
        super().__init__()
        self.additional: Optional[String] = None
        self.estimated_execution_time: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize RoughEstimateOfExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RoughEstimateOfExecutionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize additional
        if self.additional is not None:
            serialized = SerializationHelper.serialize_item(self.additional, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDITIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize estimated_execution_time
        if self.estimated_execution_time is not None:
            serialized = SerializationHelper.serialize_item(self.estimated_execution_time, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ESTIMATED-EXECUTION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoughEstimateOfExecutionTime":
        """Deserialize XML element to RoughEstimateOfExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoughEstimateOfExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RoughEstimateOfExecutionTime, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ADDITIONAL":
                setattr(obj, "additional", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ESTIMATED-EXECUTION-TIME":
                setattr(obj, "estimated_execution_time", SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime"))

        return obj



class RoughEstimateOfExecutionTimeBuilder(ExecutionTimeBuilder):
    """Builder for RoughEstimateOfExecutionTime with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RoughEstimateOfExecutionTime = RoughEstimateOfExecutionTime()


    def with_additional(self, value: Optional[String]) -> "RoughEstimateOfExecutionTimeBuilder":
        """Set additional attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.additional = value
        return self

    def with_estimated_execution_time(self, value: Optional[MultidimensionalTime]) -> "RoughEstimateOfExecutionTimeBuilder":
        """Set estimated_execution_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.estimated_execution_time = value
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


    def build(self) -> RoughEstimateOfExecutionTime:
        """Build and return the RoughEstimateOfExecutionTime instance with validation."""
        self._validate_instance()
        pass
        return self._obj