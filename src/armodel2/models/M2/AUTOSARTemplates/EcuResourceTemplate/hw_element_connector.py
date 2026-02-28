"""HwElementConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 21)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_connector import (
    HwPinGroupConnector,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
        HwElement,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class HwElementConnector(Describable):
    """AUTOSAR HwElementConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "HW-ELEMENT-CONNECTOR"


    hw_element_refs: list[ARRef]
    hw_pins: list[HwPinConnector]
    hw_pin_group_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HW-ELEMENTS": lambda obj, elem: obj.hw_element_refs.append(ARRef.deserialize(elem)),
        "HW-PINS": lambda obj, elem: obj.hw_pins.append(HwPinConnector.deserialize(elem)),
        "HW-PIN-GROUPS": lambda obj, elem: obj.hw_pin_group_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize HwElementConnector."""
        super().__init__()
        self.hw_element_refs: list[ARRef] = []
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize HwElementConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwElementConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_element_refs (list to container "HW-ELEMENT-REFS")
        if self.hw_element_refs:
            wrapper = ET.Element("HW-ELEMENT-REFS")
            for item in self.hw_element_refs:
                serialized = SerializationHelper.serialize_item(item, "HwElement")
                if serialized is not None:
                    child_elem = ET.Element("HW-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pins (list to container "HW-PINS")
        if self.hw_pins:
            wrapper = ET.Element("HW-PINS")
            for item in self.hw_pins:
                serialized = SerializationHelper.serialize_item(item, "HwPinConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pin_group_refs (list to container "HW-PIN-GROUP-REFS")
        if self.hw_pin_group_refs:
            wrapper = ET.Element("HW-PIN-GROUP-REFS")
            for item in self.hw_pin_group_refs:
                serialized = SerializationHelper.serialize_item(item, "HwPinGroupConnector")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElementConnector":
        """Deserialize XML element to HwElementConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwElementConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwElementConnector, cls).deserialize(element)

        # Parse hw_element_refs (list from container "HW-ELEMENT-REFS")
        obj.hw_element_refs = []
        container = SerializationHelper.find_child_element(element, "HW-ELEMENT-REFS")
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
                    obj.hw_element_refs.append(child_value)

        # Parse hw_pins (list from container "HW-PINS")
        obj.hw_pins = []
        container = SerializationHelper.find_child_element(element, "HW-PINS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_pins.append(child_value)

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

        return obj



class HwElementConnectorBuilder(DescribableBuilder):
    """Builder for HwElementConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwElementConnector = HwElementConnector()


    def with_hw_elements(self, items: list[HwElement]) -> "HwElementConnectorBuilder":
        """Set hw_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = list(items) if items else []
        return self

    def with_hw_pins(self, items: list[HwPinConnector]) -> "HwElementConnectorBuilder":
        """Set hw_pins list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_pins = list(items) if items else []
        return self

    def with_hw_pin_groups(self, items: list[HwPinGroupConnector]) -> "HwElementConnectorBuilder":
        """Set hw_pin_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups = list(items) if items else []
        return self


    def add_hw_element(self, item: HwElement) -> "HwElementConnectorBuilder":
        """Add a single item to hw_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_elements.append(item)
        return self

    def clear_hw_elements(self) -> "HwElementConnectorBuilder":
        """Clear all items from hw_elements list.

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = []
        return self

    def add_hw_pin(self, item: HwPinConnector) -> "HwElementConnectorBuilder":
        """Add a single item to hw_pins list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_pins.append(item)
        return self

    def clear_hw_pins(self) -> "HwElementConnectorBuilder":
        """Clear all items from hw_pins list.

        Returns:
            self for method chaining
        """
        self._obj.hw_pins = []
        return self

    def add_hw_pin_group(self, item: HwPinGroupConnector) -> "HwElementConnectorBuilder":
        """Add a single item to hw_pin_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups.append(item)
        return self

    def clear_hw_pin_groups(self) -> "HwElementConnectorBuilder":
        """Clear all items from hw_pin_groups list.

        Returns:
            self for method chaining
        """
        self._obj.hw_pin_groups = []
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


    def build(self) -> HwElementConnector:
        """Build and return the HwElementConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj