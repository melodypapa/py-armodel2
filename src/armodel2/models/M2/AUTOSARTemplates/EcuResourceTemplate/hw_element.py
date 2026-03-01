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

from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import HwDescriptionEntityBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element_connector import (
        HwElementConnector,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class HwElement(HwDescriptionEntity):
    """AUTOSAR HwElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "HW-ELEMENT"


    hw_element_connections: list[HwElementConnector]
    hw_pin_groups: list[HwPinGroup]
    nested_element_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HW-ELEMENT-CONNECTIONS": lambda obj, elem: obj.hw_element_connections.append(SerializationHelper.deserialize_by_tag(elem, "HwElementConnector")),
        "HW-PIN-GROUPS": lambda obj, elem: obj.hw_pin_groups.append(SerializationHelper.deserialize_by_tag(elem, "HwPinGroup")),
        "NESTED-ELEMENTS": lambda obj, elem: obj.nested_element_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize HwElement."""
        super().__init__()
        self.hw_element_connections: list[HwElementConnector] = []
        self.hw_pin_groups: list[HwPinGroup] = []
        self.nested_element_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize HwElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize hw_element_connections (list to container "HW-ELEMENT-CONNECTIONS")
        if self.hw_element_connections:
            wrapper = ET.Element("HW-ELEMENT-CONNECTIONS")
            for item in self.hw_element_connections:
                serialized = SerializationHelper.serialize_item(item, "HwElementConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pin_groups (list to container "HW-PIN-GROUPS")
        if self.hw_pin_groups:
            wrapper = ET.Element("HW-PIN-GROUPS")
            for item in self.hw_pin_groups:
                serialized = SerializationHelper.serialize_item(item, "HwPinGroup")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "HW-ELEMENT-CONNECTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.hw_element_connections.append(SerializationHelper.deserialize_by_tag(item_elem, "HwElementConnector"))
            elif tag == "HW-PIN-GROUPS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.hw_pin_groups.append(SerializationHelper.deserialize_by_tag(item_elem, "HwPinGroup"))
            elif tag == "NESTED-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.nested_element_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "HwElement"))

        return obj



class HwElementBuilder(HwDescriptionEntityBuilder):
    """Builder for HwElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwElement = HwElement()


    def with_hw_element_connections(self, items: list[HwElementConnector]) -> "HwElementBuilder":
        """Set hw_element_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_element_connections = list(items) if items else []
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


    def add_hw_element_connection(self, item: HwElementConnector) -> "HwElementBuilder":
        """Add a single item to hw_element_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_element_connections.append(item)
        return self

    def clear_hw_element_connections(self) -> "HwElementBuilder":
        """Clear all items from hw_element_connections list.

        Returns:
            self for method chaining
        """
        self._obj.hw_element_connections = []
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


    def build(self) -> HwElement:
        """Build and return the HwElement instance with validation."""
        self._validate_instance()
        pass
        return self._obj