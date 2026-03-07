"""DiagnosticParameterSupportInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 149)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticParameterSupportInfo(ARObject):
    """AUTOSAR DiagnosticParameterSupportInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-PARAMETER-SUPPORT-INFO"


    support_info_bit: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "SUPPORT-INFO-BIT": lambda obj, elem: setattr(obj, "support_info_bit", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticParameterSupportInfo."""
        super().__init__()
        self.support_info_bit: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameterSupportInfo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticParameterSupportInfo, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize support_info_bit
        if self.support_info_bit is not None:
            serialized = SerializationHelper.serialize_item(self.support_info_bit, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-INFO-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterSupportInfo":
        """Deserialize XML element to DiagnosticParameterSupportInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterSupportInfo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameterSupportInfo, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SUPPORT-INFO-BIT":
                setattr(obj, "support_info_bit", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticParameterSupportInfoBuilder(BuilderBase):
    """Builder for DiagnosticParameterSupportInfo with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticParameterSupportInfo = DiagnosticParameterSupportInfo()


    def with_support_info_bit(self, value: Optional[PositiveInteger]) -> "DiagnosticParameterSupportInfoBuilder":
        """Set support_info_bit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'support_info_bit' is required and cannot be None")
        self._obj.support_info_bit = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "supportInfoBit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticParameterSupportInfo:
        """Build and return the DiagnosticParameterSupportInfo instance with validation."""
        self._validate_instance()
        return self._obj