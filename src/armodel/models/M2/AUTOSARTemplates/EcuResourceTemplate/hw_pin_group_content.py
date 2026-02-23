"""HwPinGroupContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
        HwPinGroup,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class HwPinGroupContent(ARObject):
    """AUTOSAR HwPinGroupContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pin: Optional[HwPin]
    hw_pin_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize HwPinGroupContent."""
        super().__init__()
        self.hw_pin: Optional[HwPin] = None
        self.hw_pin_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize HwPinGroupContent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPinGroupContent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_pin
        if self.hw_pin is not None:
            serialized = SerializationHelper.serialize_item(self.hw_pin, "HwPin")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-PIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_pin_group_ref
        if self.hw_pin_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_pin_group_ref, "HwPinGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-PIN-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroupContent":
        """Deserialize XML element to HwPinGroupContent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinGroupContent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPinGroupContent, cls).deserialize(element)

        # Parse hw_pin
        child = SerializationHelper.find_child_element(element, "HW-PIN")
        if child is not None:
            hw_pin_value = SerializationHelper.deserialize_by_tag(child, "HwPin")
            obj.hw_pin = hw_pin_value

        # Parse hw_pin_group_ref
        child = SerializationHelper.find_child_element(element, "HW-PIN-GROUP-REF")
        if child is not None:
            hw_pin_group_ref_value = ARRef.deserialize(child)
            obj.hw_pin_group_ref = hw_pin_group_ref_value

        return obj



class HwPinGroupContentBuilder(BuilderBase):
    """Builder for HwPinGroupContent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwPinGroupContent = HwPinGroupContent()


    def with_hw_pin(self, value: Optional[HwPin]) -> "HwPinGroupContentBuilder":
        """Set hw_pin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hw_pin = value
        return self

    def with_hw_pin_group(self, value: Optional[HwPinGroup]) -> "HwPinGroupContentBuilder":
        """Set hw_pin_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hw_pin_group = value
        return self




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


    def build(self) -> HwPinGroupContent:
        """Build and return the HwPinGroupContent instance with validation."""
        self._validate_instance()
        pass
        return self._obj