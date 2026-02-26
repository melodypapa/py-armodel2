"""GlobalTimeCorrectionProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 862)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeCorrectionProps(ARObject):
    """AUTOSAR GlobalTimeCorrectionProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    offset_correction: Optional[TimeValue]
    rate_correction: Optional[TimeValue]
    rate_corrections: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize GlobalTimeCorrectionProps."""
        super().__init__()
        self.offset_correction: Optional[TimeValue] = None
        self.rate_correction: Optional[TimeValue] = None
        self.rate_corrections: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeCorrectionProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeCorrectionProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize offset_correction
        if self.offset_correction is not None:
            serialized = SerializationHelper.serialize_item(self.offset_correction, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_correction
        if self.rate_correction is not None:
            serialized = SerializationHelper.serialize_item(self.rate_correction, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_corrections
        if self.rate_corrections is not None:
            serialized = SerializationHelper.serialize_item(self.rate_corrections, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-CORRECTIONS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCorrectionProps":
        """Deserialize XML element to GlobalTimeCorrectionProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCorrectionProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeCorrectionProps, cls).deserialize(element)

        # Parse offset_correction
        child = SerializationHelper.find_child_element(element, "OFFSET-CORRECTION")
        if child is not None:
            offset_correction_value = child.text
            obj.offset_correction = offset_correction_value

        # Parse rate_correction
        child = SerializationHelper.find_child_element(element, "RATE-CORRECTION")
        if child is not None:
            rate_correction_value = child.text
            obj.rate_correction = rate_correction_value

        # Parse rate_corrections
        child = SerializationHelper.find_child_element(element, "RATE-CORRECTIONS")
        if child is not None:
            rate_corrections_value = child.text
            obj.rate_corrections = rate_corrections_value

        return obj



class GlobalTimeCorrectionPropsBuilder(BuilderBase):
    """Builder for GlobalTimeCorrectionProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeCorrectionProps = GlobalTimeCorrectionProps()


    def with_offset_correction(self, value: Optional[TimeValue]) -> "GlobalTimeCorrectionPropsBuilder":
        """Set offset_correction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.offset_correction = value
        return self

    def with_rate_correction(self, value: Optional[TimeValue]) -> "GlobalTimeCorrectionPropsBuilder":
        """Set rate_correction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rate_correction = value
        return self

    def with_rate_corrections(self, value: Optional[PositiveInteger]) -> "GlobalTimeCorrectionPropsBuilder":
        """Set rate_corrections attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rate_corrections = value
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


    def build(self) -> GlobalTimeCorrectionProps:
        """Build and return the GlobalTimeCorrectionProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj