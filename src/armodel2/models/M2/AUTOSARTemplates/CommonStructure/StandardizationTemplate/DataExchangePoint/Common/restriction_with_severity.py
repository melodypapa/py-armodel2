"""RestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint import (
    SeverityEnum,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RestrictionWithSeverity(ARObject, ABC):
    """AUTOSAR RestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    severity: SeverityEnum
    _DESERIALIZE_DISPATCH = {
        "SEVERITY": lambda obj, elem: setattr(obj, "severity", SeverityEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize RestrictionWithSeverity."""
        super().__init__()
        self.severity: SeverityEnum = None

    def serialize(self) -> ET.Element:
        """Serialize RestrictionWithSeverity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RestrictionWithSeverity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize severity
        if self.severity is not None:
            serialized = SerializationHelper.serialize_item(self.severity, "SeverityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEVERITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RestrictionWithSeverity":
        """Deserialize XML element to RestrictionWithSeverity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RestrictionWithSeverity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RestrictionWithSeverity, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SEVERITY":
                setattr(obj, "severity", SeverityEnum.deserialize(child))

        return obj



class RestrictionWithSeverityBuilder(BuilderBase, ABC):
    """Builder for RestrictionWithSeverity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RestrictionWithSeverity = RestrictionWithSeverity()


    def with_severity(self, value: SeverityEnum) -> "RestrictionWithSeverityBuilder":
        """Set severity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.severity = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "severity",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "severity", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'severity' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'severity' is None", UserWarning)


    @abstractmethod
    def build(self) -> RestrictionWithSeverity:
        """Build and return the RestrictionWithSeverity instance (abstract)."""
        raise NotImplementedError