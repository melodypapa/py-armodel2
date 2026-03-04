"""SecurityEventContextMappingApplication AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 42)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import SecurityEventContextMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventContextMappingApplication(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingApplication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURITY-EVENT-CONTEXT-MAPPING-APPLICATION"


    affected: String
    _DESERIALIZE_DISPATCH = {
        "AFFECTED": lambda obj, elem: setattr(obj, "affected", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingApplication."""
        super().__init__()
        self.affected: String = None

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextMappingApplication to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextMappingApplication, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize affected
        if self.affected is not None:
            serialized = SerializationHelper.serialize_item(self.affected, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AFFECTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingApplication":
        """Deserialize XML element to SecurityEventContextMappingApplication object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextMappingApplication object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextMappingApplication, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AFFECTED":
                setattr(obj, "affected", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class SecurityEventContextMappingApplicationBuilder(SecurityEventContextMappingBuilder):
    """Builder for SecurityEventContextMappingApplication with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventContextMappingApplication = SecurityEventContextMappingApplication()


    def with_affected(self, value: String) -> "SecurityEventContextMappingApplicationBuilder":
        """Set affected attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.affected = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "affected",
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
        if getattr(self._obj, "affected", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'affected' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'affected' is None", UserWarning)


    def build(self) -> SecurityEventContextMappingApplication:
        """Build and return the SecurityEventContextMappingApplication instance with validation."""
        self._validate_instance()
        return self._obj