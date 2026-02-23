"""HwElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 296)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 18)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 991)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element_connector import (
        HwElementConnector,
    )



class HwElement(HwDescriptionEntity):
    """AUTOSAR HwElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_elements: list[HwElementConnector]
    hw_pin_group_refs: list[ARRef]
    nested_element_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize HwElement."""
        super().__init__()
        self.hw_elements: list[HwElementConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []
        self.nested_element_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize HwElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_elements (list to container "HW-ELEMENTS")
        if self.hw_elements:
            wrapper = ET.Element("HW-ELEMENTS")
            for item in self.hw_elements:
                serialized = SerializationHelper.serialize_item(item, "HwElementConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pin_group_refs (list to container "HW-PIN-GROUP-REFS")
        if self.hw_pin_group_refs:
            wrapper = ET.Element("HW-PIN-GROUP-REFS")
            for item in self.hw_pin_group_refs:
                serialized = SerializationHelper.serialize_item(item, "HwPinGroup")
                if serialized is not None:
                    child_elem = ET.Element("HW-PIN-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nested_element_refs (list to container "NESTED-ELEMENT-REFS")
        if self.nested_element_refs:
            wrapper = ET.Element("NESTED-ELEMENT-REFS")
            for item in self.nested_element_refs:
                serialized = SerializationHelper.serialize_item(item, "HwElement")
                if serialized is not None:
                    child_elem = ET.Element("NESTED-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElement":
        """Deserialize XML element to HwElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwElement, cls).deserialize(element)

        # Parse hw_elements (list from container "HW-ELEMENTS")
        obj.hw_elements = []
        container = SerializationHelper.find_child_element(element, "HW-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_elements.append(child_value)

        # Parse hw_pin_group_refs (list from container "HW-PIN-GROUP-REFS")
        obj.hw_pin_group_refs = []
        container = SerializationHelper.find_child_element(element, "HW-PIN-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_pin_group_refs.append(child_value)

        # Parse nested_element_refs (list from container "NESTED-ELEMENT-REFS")
        obj.nested_element_refs = []
        container = SerializationHelper.find_child_element(element, "NESTED-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nested_element_refs.append(child_value)

        return obj



class HwElementBuilder:
    """Builder for HwElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: HwElement = HwElement()


    def with_short_name(self, value: Identifier) -> "HwElementBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "HwElementBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_hw_attributes(self, items: list[HwAttributeValue]) -> "HwElementBuilder":
        """Set hw_attributes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_attributes = list(items) if items else []
        return self

    def with_hw_categories(self, items: list[HwCategory]) -> "HwElementBuilder":
        """Set hw_categories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_categories = list(items) if items else []
        return self

    def with_hw_type(self, value: Optional[HwType]) -> "HwElementBuilder":
        """Set hw_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hw_type = value
        return self

    def with_hw_elements(self, items: list[HwElementConnector]) -> "HwElementBuilder":
        """Set hw_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = list(items) if items else []
        return self

    def with_hw_pin_groups(self, items: list[HwPinGroup]) -> "HwElementBuilder":
        """Set hw_pin_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups = list(items) if items else []
        return self

    def with_nested_elements(self, items: list[HwElement]) -> "HwElementBuilder":
        """Set nested_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nested_elements = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "HwElementBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "HwElementBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_hw_attribute(self, item: HwAttributeValue) -> "HwElementBuilder":
        """Add a single item to hw_attributes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_attributes.append(item)
        return self

    def clear_hw_attributes(self) -> "HwElementBuilder":
        """Clear all items from hw_attributes list.

        Returns:
            self for method chaining
        """
        self._obj.hw_attributes = []
        return self

    def add_hw_categorie(self, item: HwCategory) -> "HwElementBuilder":
        """Add a single item to hw_categories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_categories.append(item)
        return self

    def clear_hw_categories(self) -> "HwElementBuilder":
        """Clear all items from hw_categories list.

        Returns:
            self for method chaining
        """
        self._obj.hw_categories = []
        return self

    def add_hw_element(self, item: HwElementConnector) -> "HwElementBuilder":
        """Add a single item to hw_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_elements.append(item)
        return self

    def clear_hw_elements(self) -> "HwElementBuilder":
        """Clear all items from hw_elements list.

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = []
        return self

    def add_hw_pin_group(self, item: HwPinGroup) -> "HwElementBuilder":
        """Add a single item to hw_pin_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups.append(item)
        return self

    def clear_hw_pin_groups(self) -> "HwElementBuilder":
        """Clear all items from hw_pin_groups list.

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups = []
        return self

    def add_nested_element(self, item: HwElement) -> "HwElementBuilder":
        """Add a single item to nested_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nested_elements.append(item)
        return self

    def clear_nested_elements(self) -> "HwElementBuilder":
        """Clear all items from nested_elements list.

        Returns:
            self for method chaining
        """
        self._obj.nested_elements = []
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


    def build(self) -> HwElement:
        """Build and return the HwElement instance with validation."""
        self._validate_instance()
        pass
        return self._obj