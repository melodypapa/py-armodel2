"""HardwareConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HardwareConfiguration(ARObject):
    """AUTOSAR HardwareConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    additional: Optional[String]
    processor_mode: Optional[String]
    processor_speed: Optional[String]
    def __init__(self) -> None:
        """Initialize HardwareConfiguration."""
        super().__init__()
        self.additional: Optional[String] = None
        self.processor_mode: Optional[String] = None
        self.processor_speed: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize HardwareConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HardwareConfiguration, self).serialize()

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

        # Serialize processor_mode
        if self.processor_mode is not None:
            serialized = SerializationHelper.serialize_item(self.processor_mode, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSOR-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processor_speed
        if self.processor_speed is not None:
            serialized = SerializationHelper.serialize_item(self.processor_speed, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSOR-SPEED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HardwareConfiguration":
        """Deserialize XML element to HardwareConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HardwareConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HardwareConfiguration, cls).deserialize(element)

        # Parse additional
        child = SerializationHelper.find_child_element(element, "ADDITIONAL")
        if child is not None:
            additional_value = child.text
            obj.additional = additional_value

        # Parse processor_mode
        child = SerializationHelper.find_child_element(element, "PROCESSOR-MODE")
        if child is not None:
            processor_mode_value = child.text
            obj.processor_mode = processor_mode_value

        # Parse processor_speed
        child = SerializationHelper.find_child_element(element, "PROCESSOR-SPEED")
        if child is not None:
            processor_speed_value = child.text
            obj.processor_speed = processor_speed_value

        return obj



class HardwareConfigurationBuilder(BuilderBase):
    """Builder for HardwareConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HardwareConfiguration = HardwareConfiguration()


    def with_additional(self, value: Optional[String]) -> "HardwareConfigurationBuilder":
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

    def with_processor_mode(self, value: Optional[String]) -> "HardwareConfigurationBuilder":
        """Set processor_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.processor_mode = value
        return self

    def with_processor_speed(self, value: Optional[String]) -> "HardwareConfigurationBuilder":
        """Set processor_speed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.processor_speed = value
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


    def build(self) -> HardwareConfiguration:
        """Build and return the HardwareConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj