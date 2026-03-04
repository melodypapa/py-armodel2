"""SecurityEventThresholdFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import AbstractSecurityEventFilterBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventThresholdFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURITY-EVENT-THRESHOLD-FILTER"


    interval_length: Optional[TimeValue]
    threshold: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "INTERVAL-LENGTH": lambda obj, elem: setattr(obj, "interval_length", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "THRESHOLD": lambda obj, elem: setattr(obj, "threshold", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTERVAL-LENGTH":
                setattr(obj, "interval_length", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "THRESHOLD":
                setattr(obj, "threshold", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "intervalLength",
        "threshold",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecurityEventThresholdFilter:
        """Build and return the SecurityEventThresholdFilter instance with validation."""
        self._validate_instance()
        return self._obj