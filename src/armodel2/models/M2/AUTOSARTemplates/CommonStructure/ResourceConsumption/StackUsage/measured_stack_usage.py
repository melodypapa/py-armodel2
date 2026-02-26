"""MeasuredStackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import StackUsageBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MeasuredStackUsage(StackUsage):
    """AUTOSAR MeasuredStackUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    average_memory_consumption: Optional[PositiveInteger]
    maximum_memory_consumption: Optional[PositiveInteger]
    minimum_memory_consumption: Optional[PositiveInteger]
    test_pattern: Optional[String]
    def __init__(self) -> None:
        """Initialize MeasuredStackUsage."""
        super().__init__()
        self.average_memory_consumption: Optional[PositiveInteger] = None
        self.maximum_memory_consumption: Optional[PositiveInteger] = None
        self.minimum_memory_consumption: Optional[PositiveInteger] = None
        self.test_pattern: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize MeasuredStackUsage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MeasuredStackUsage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize average_memory_consumption
        if self.average_memory_consumption is not None:
            serialized = SerializationHelper.serialize_item(self.average_memory_consumption, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AVERAGE-MEMORY-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum_memory_consumption
        if self.maximum_memory_consumption is not None:
            serialized = SerializationHelper.serialize_item(self.maximum_memory_consumption, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-MEMORY-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_memory_consumption
        if self.minimum_memory_consumption is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_memory_consumption, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-MEMORY-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize test_pattern
        if self.test_pattern is not None:
            serialized = SerializationHelper.serialize_item(self.test_pattern, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEST-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredStackUsage":
        """Deserialize XML element to MeasuredStackUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MeasuredStackUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MeasuredStackUsage, cls).deserialize(element)

        # Parse average_memory_consumption
        child = SerializationHelper.find_child_element(element, "AVERAGE-MEMORY-CONSUMPTION")
        if child is not None:
            average_memory_consumption_value = child.text
            obj.average_memory_consumption = average_memory_consumption_value

        # Parse maximum_memory_consumption
        child = SerializationHelper.find_child_element(element, "MAXIMUM-MEMORY-CONSUMPTION")
        if child is not None:
            maximum_memory_consumption_value = child.text
            obj.maximum_memory_consumption = maximum_memory_consumption_value

        # Parse minimum_memory_consumption
        child = SerializationHelper.find_child_element(element, "MINIMUM-MEMORY-CONSUMPTION")
        if child is not None:
            minimum_memory_consumption_value = child.text
            obj.minimum_memory_consumption = minimum_memory_consumption_value

        # Parse test_pattern
        child = SerializationHelper.find_child_element(element, "TEST-PATTERN")
        if child is not None:
            test_pattern_value = child.text
            obj.test_pattern = test_pattern_value

        return obj



class MeasuredStackUsageBuilder(StackUsageBuilder):
    """Builder for MeasuredStackUsage with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MeasuredStackUsage = MeasuredStackUsage()


    def with_average_memory_consumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsageBuilder":
        """Set average_memory_consumption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.average_memory_consumption = value
        return self

    def with_maximum_memory_consumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsageBuilder":
        """Set maximum_memory_consumption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum_memory_consumption = value
        return self

    def with_minimum_memory_consumption(self, value: Optional[PositiveInteger]) -> "MeasuredStackUsageBuilder":
        """Set minimum_memory_consumption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_memory_consumption = value
        return self

    def with_test_pattern(self, value: Optional[String]) -> "MeasuredStackUsageBuilder":
        """Set test_pattern attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.test_pattern = value
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


    def build(self) -> MeasuredStackUsage:
        """Build and return the MeasuredStackUsage instance with validation."""
        self._validate_instance()
        pass
        return self._obj