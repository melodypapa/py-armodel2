"""HwDescriptionEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 15)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 990)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_value import (
    HwAttributeValue,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_category import (
    HwCategory,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_type import (
        HwType,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HwDescriptionEntity(Identifiable, ABC):
    """AUTOSAR HwDescriptionEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    hw_attribute_values: list[HwAttributeValue]
    hw_category_refs: list[ARRef]
    hw_type_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HW-ATTRIBUTE-VALUES": lambda obj, elem: obj.hw_attribute_values.append(SerializationHelper.deserialize_by_tag(elem, "HwAttributeValue")),
        "HW-CATEGORY-REFS": lambda obj, elem: [obj.hw_category_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "HW-TYPE-REF": lambda obj, elem: setattr(obj, "hw_type_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize HwDescriptionEntity."""
        super().__init__()
        self.hw_attribute_values: list[HwAttributeValue] = []
        self.hw_category_refs: list[ARRef] = []
        self.hw_type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize HwDescriptionEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwDescriptionEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_attribute_values (list to container "HW-ATTRIBUTE-VALUES")
        if self.hw_attribute_values:
            wrapper = ET.Element("HW-ATTRIBUTE-VALUES")
            for item in self.hw_attribute_values:
                serialized = SerializationHelper.serialize_item(item, "HwAttributeValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_category_refs (list to container "HW-CATEGORY-REFS")
        if self.hw_category_refs:
            wrapper = ET.Element("HW-CATEGORY-REFS")
            for item in self.hw_category_refs:
                serialized = SerializationHelper.serialize_item(item, "HwCategory")
                if serialized is not None:
                    child_elem = ET.Element("HW-CATEGORY-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_type_ref
        if self.hw_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_type_ref, "HwType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwDescriptionEntity":
        """Deserialize XML element to HwDescriptionEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwDescriptionEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwDescriptionEntity, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HW-ATTRIBUTE-VALUES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.hw_attribute_values.append(SerializationHelper.deserialize_by_tag(item_elem, "HwAttributeValue"))
            elif tag == "HW-CATEGORY-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.hw_category_refs.append(ARRef.deserialize(item_elem))
            elif tag == "HW-TYPE-REF":
                setattr(obj, "hw_type_ref", ARRef.deserialize(child))

        return obj



class HwDescriptionEntityBuilder(ReferrableBuilder):
    """Builder for HwDescriptionEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwDescriptionEntity = HwDescriptionEntity()


    def with_hw_attribute_values(self, items: list[HwAttributeValue]) -> "HwDescriptionEntityBuilder":
        """Set hw_attribute_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_attribute_values = list(items) if items else []
        return self

    def with_hw_categories(self, items: list[HwCategory]) -> "HwDescriptionEntityBuilder":
        """Set hw_categories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_categories = list(items) if items else []
        return self

    def with_hw_type(self, value: Optional[HwType]) -> "HwDescriptionEntityBuilder":
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


    def add_hw_attribute_value(self, item: HwAttributeValue) -> "HwDescriptionEntityBuilder":
        """Add a single item to hw_attribute_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_attribute_values.append(item)
        return self

    def clear_hw_attribute_values(self) -> "HwDescriptionEntityBuilder":
        """Clear all items from hw_attribute_values list.

        Returns:
            self for method chaining
        """
        self._obj.hw_attribute_values = []
        return self

    def add_hw_category(self, item: HwCategory) -> "HwDescriptionEntityBuilder":
        """Add a single item to hw_categories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_categories.append(item)
        return self

    def clear_hw_categories(self) -> "HwDescriptionEntityBuilder":
        """Clear all items from hw_categories list.

        Returns:
            self for method chaining
        """
        self._obj.hw_categories = []
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


    @abstractmethod
    def build(self) -> HwDescriptionEntity:
        """Build and return the HwDescriptionEntity instance (abstract)."""
        raise NotImplementedError