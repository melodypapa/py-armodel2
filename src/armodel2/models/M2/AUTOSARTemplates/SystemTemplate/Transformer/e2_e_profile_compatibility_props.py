"""E2EProfileCompatibilityProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class E2EProfileCompatibilityProps(ARElement):
    """AUTOSAR E2EProfileCompatibilityProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "E2-E-PROFILE-COMPATIBILITY-PROPS"


    transit_to_invalid: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "TRANSIT-TO-INVALID": lambda obj, elem: setattr(obj, "transit_to_invalid", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize E2EProfileCompatibilityProps."""
        super().__init__()
        self.transit_to_invalid: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize E2EProfileCompatibilityProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(E2EProfileCompatibilityProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize transit_to_invalid
        if self.transit_to_invalid is not None:
            serialized = SerializationHelper.serialize_item(self.transit_to_invalid, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSIT-TO-INVALID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "E2EProfileCompatibilityProps":
        """Deserialize XML element to E2EProfileCompatibilityProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized E2EProfileCompatibilityProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(E2EProfileCompatibilityProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TRANSIT-TO-INVALID":
                setattr(obj, "transit_to_invalid", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class E2EProfileCompatibilityPropsBuilder(ARElementBuilder):
    """Builder for E2EProfileCompatibilityProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: E2EProfileCompatibilityProps = E2EProfileCompatibilityProps()


    def with_transit_to_invalid(self, value: Optional[Boolean]) -> "E2EProfileCompatibilityPropsBuilder":
        """Set transit_to_invalid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transit_to_invalid = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "transitToInvalid",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> E2EProfileCompatibilityProps:
        """Build and return the E2EProfileCompatibilityProps instance with validation."""
        self._validate_instance()
        return self._obj