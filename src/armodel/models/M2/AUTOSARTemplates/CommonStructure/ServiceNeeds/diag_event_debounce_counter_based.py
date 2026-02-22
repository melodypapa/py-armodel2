"""DiagEventDebounceCounterBased AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 259)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 196)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 757)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


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



class DiagEventDebounceCounterBasedBuilder:
    """Builder for DiagEventDebounceCounterBased with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DiagEventDebounceCounterBased = DiagEventDebounceCounterBased()


    def with_short_name(self, value: Identifier) -> "DiagEventDebounceCounterBasedBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "DiagEventDebounceCounterBasedBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "DiagEventDebounceCounterBasedBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

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


    def add_short_name_fragment(self, item: ShortNameFragment) -> "DiagEventDebounceCounterBasedBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "DiagEventDebounceCounterBasedBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "DiagEventDebounceCounterBasedBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "DiagEventDebounceCounterBasedBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
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


    def build(self) -> DiagEventDebounceCounterBased:
        """Build and return the DiagEventDebounceCounterBased instance with validation."""
        self._validate_instance()
        pass
        return self._obj