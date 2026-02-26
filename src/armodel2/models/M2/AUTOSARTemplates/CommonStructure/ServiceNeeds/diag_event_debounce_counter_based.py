"""DiagEventDebounceCounterBased AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 259)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 196)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 757)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import DiagEventDebounceAlgorithmBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceCounterBased."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    counter_based: Optional[Integer]
    counter: Optional[Integer]
    counter_failed: Optional[Integer]
    counter_jump: Optional[Integer]
    counter_jump_up: Optional[Integer]
    counter_passed: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DiagEventDebounceCounterBased."""
        super().__init__()
        self.counter_based: Optional[Integer] = None
        self.counter: Optional[Integer] = None
        self.counter_failed: Optional[Integer] = None
        self.counter_jump: Optional[Integer] = None
        self.counter_jump_up: Optional[Integer] = None
        self.counter_passed: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagEventDebounceCounterBased to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagEventDebounceCounterBased, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize counter_based
        if self.counter_based is not None:
            serialized = SerializationHelper.serialize_item(self.counter_based, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-BASED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter
        if self.counter is not None:
            serialized = SerializationHelper.serialize_item(self.counter, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_failed
        if self.counter_failed is not None:
            serialized = SerializationHelper.serialize_item(self.counter_failed, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_jump
        if self.counter_jump is not None:
            serialized = SerializationHelper.serialize_item(self.counter_jump, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-JUMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_jump_up
        if self.counter_jump_up is not None:
            serialized = SerializationHelper.serialize_item(self.counter_jump_up, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-JUMP-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_passed
        if self.counter_passed is not None:
            serialized = SerializationHelper.serialize_item(self.counter_passed, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-PASSED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceCounterBased":
        """Deserialize XML element to DiagEventDebounceCounterBased object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagEventDebounceCounterBased object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagEventDebounceCounterBased, cls).deserialize(element)

        # Parse counter_based
        child = SerializationHelper.find_child_element(element, "COUNTER-BASED")
        if child is not None:
            counter_based_value = child.text
            obj.counter_based = counter_based_value

        # Parse counter
        child = SerializationHelper.find_child_element(element, "COUNTER")
        if child is not None:
            counter_value = child.text
            obj.counter = counter_value

        # Parse counter_failed
        child = SerializationHelper.find_child_element(element, "COUNTER-FAILED")
        if child is not None:
            counter_failed_value = child.text
            obj.counter_failed = counter_failed_value

        # Parse counter_jump
        child = SerializationHelper.find_child_element(element, "COUNTER-JUMP")
        if child is not None:
            counter_jump_value = child.text
            obj.counter_jump = counter_jump_value

        # Parse counter_jump_up
        child = SerializationHelper.find_child_element(element, "COUNTER-JUMP-UP")
        if child is not None:
            counter_jump_up_value = child.text
            obj.counter_jump_up = counter_jump_up_value

        # Parse counter_passed
        child = SerializationHelper.find_child_element(element, "COUNTER-PASSED")
        if child is not None:
            counter_passed_value = child.text
            obj.counter_passed = counter_passed_value

        return obj



class DiagEventDebounceCounterBasedBuilder(DiagEventDebounceAlgorithmBuilder):
    """Builder for DiagEventDebounceCounterBased with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagEventDebounceCounterBased = DiagEventDebounceCounterBased()


    def with_counter_based(self, value: Optional[Integer]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set counter_based attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter_based = value
        return self

    def with_counter(self, value: Optional[Integer]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set counter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter = value
        return self

    def with_counter_failed(self, value: Optional[Integer]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set counter_failed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter_failed = value
        return self

    def with_counter_jump(self, value: Optional[Integer]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set counter_jump attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter_jump = value
        return self

    def with_counter_jump_up(self, value: Optional[Integer]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set counter_jump_up attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter_jump_up = value
        return self

    def with_counter_passed(self, value: Optional[Integer]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set counter_passed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.counter_passed = value
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


    def build(self) -> DiagEventDebounceCounterBased:
        """Build and return the DiagEventDebounceCounterBased instance with validation."""
        self._validate_instance()
        pass
        return self._obj