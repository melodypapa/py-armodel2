"""HwPin AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HwPin(Identifiable):
    """AUTOSAR HwPin."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function_names: list[String]
    packaging_pin: Optional[String]
    pin_number: Optional[Integer]
    def __init__(self) -> None:
        """Initialize HwPin."""
        super().__init__()
        self.function_names: list[String] = []
        self.packaging_pin: Optional[String] = None
        self.pin_number: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize HwPin to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPin, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function_names (list to container "FUNCTION-NAMES")
        if self.function_names:
            wrapper = ET.Element("FUNCTION-NAMES")
            for item in self.function_names:
                serialized = SerializationHelper.serialize_item(item, "String")
                if serialized is not None:
                    child_elem = ET.Element("FUNCTION-NAME")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize packaging_pin
        if self.packaging_pin is not None:
            serialized = SerializationHelper.serialize_item(self.packaging_pin, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKAGING-PIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pin_number
        if self.pin_number is not None:
            serialized = SerializationHelper.serialize_item(self.pin_number, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PIN-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPin":
        """Deserialize XML element to HwPin object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPin object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPin, cls).deserialize(element)

        # Parse function_names (list from container "FUNCTION-NAMES")
        obj.function_names = []
        container = SerializationHelper.find_child_element(element, "FUNCTION-NAMES")
        if container is not None:
            for child in container:
                # Extract primitive value (String) as text
                child_value = child.text
                if child_value is not None:
                    obj.function_names.append(child_value)

        # Parse packaging_pin
        child = SerializationHelper.find_child_element(element, "PACKAGING-PIN")
        if child is not None:
            packaging_pin_value = child.text
            obj.packaging_pin = packaging_pin_value

        # Parse pin_number
        child = SerializationHelper.find_child_element(element, "PIN-NUMBER")
        if child is not None:
            pin_number_value = child.text
            obj.pin_number = pin_number_value

        return obj



class HwPinBuilder(IdentifiableBuilder):
    """Builder for HwPin with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwPin = HwPin()


    def with_function_names(self, items: list[String]) -> "HwPinBuilder":
        """Set function_names list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.function_names = list(items) if items else []
        return self

    def with_packaging_pin(self, value: Optional[String]) -> "HwPinBuilder":
        """Set packaging_pin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.packaging_pin = value
        return self

    def with_pin_number(self, value: Optional[Integer]) -> "HwPinBuilder":
        """Set pin_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pin_number = value
        return self


    def add_function_name(self, item: String) -> "HwPinBuilder":
        """Add a single item to function_names list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.function_names.append(item)
        return self

    def clear_function_names(self) -> "HwPinBuilder":
        """Clear all items from function_names list.

        Returns:
            self for method chaining
        """
        self._obj.function_names = []
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


    def build(self) -> HwPin:
        """Build and return the HwPin instance with validation."""
        self._validate_instance()
        pass
        return self._obj