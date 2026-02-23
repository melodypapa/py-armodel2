"""SecurityEventThresholdFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import AbstractSecurityEventFilterBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventThresholdFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interval_length: Optional[TimeValue]
    threshold: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecurityEventThresholdFilter."""
        super().__init__()
        self.interval_length: Optional[TimeValue] = None
        self.threshold: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventThresholdFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventThresholdFilter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interval_length
        if self.interval_length is not None:
            serialized = SerializationHelper.serialize_item(self.interval_length, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERVAL-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize threshold
        if self.threshold is not None:
            serialized = SerializationHelper.serialize_item(self.threshold, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("THRESHOLD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventThresholdFilter":
        """Deserialize XML element to SecurityEventThresholdFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventThresholdFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventThresholdFilter, cls).deserialize(element)

        # Parse interval_length
        child = SerializationHelper.find_child_element(element, "INTERVAL-LENGTH")
        if child is not None:
            interval_length_value = child.text
            obj.interval_length = interval_length_value

        # Parse threshold
        child = SerializationHelper.find_child_element(element, "THRESHOLD")
        if child is not None:
            threshold_value = child.text
            obj.threshold = threshold_value

        return obj



class SecurityEventThresholdFilterBuilder(AbstractSecurityEventFilterBuilder):
    """Builder for SecurityEventThresholdFilter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventThresholdFilter = SecurityEventThresholdFilter()


    def with_interval_length(self, value: Optional[TimeValue]) -> "SecurityEventThresholdFilterBuilder":
        """Set interval_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.interval_length = value
        return self

    def with_threshold(self, value: Optional[PositiveInteger]) -> "SecurityEventThresholdFilterBuilder":
        """Set threshold attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.threshold = value
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


    def build(self) -> SecurityEventThresholdFilter:
        """Build and return the SecurityEventThresholdFilter instance with validation."""
        self._validate_instance()
        pass
        return self._obj