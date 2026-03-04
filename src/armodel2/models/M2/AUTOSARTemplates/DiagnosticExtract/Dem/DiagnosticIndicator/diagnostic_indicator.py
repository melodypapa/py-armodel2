"""DiagnosticIndicator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 203)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticIndicator.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator import (
    DiagnosticIndicatorTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticIndicator(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIndicator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-INDICATOR"


    type: Optional[DiagnosticIndicatorTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "TYPE": lambda obj, elem: setattr(obj, "type", DiagnosticIndicatorTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticIndicator."""
        super().__init__()
        self.type: Optional[DiagnosticIndicatorTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIndicator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIndicator, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type
        if self.type is not None:
            serialized = SerializationHelper.serialize_item(self.type, "DiagnosticIndicatorTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIndicator":
        """Deserialize XML element to DiagnosticIndicator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIndicator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIndicator, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TYPE":
                setattr(obj, "type", DiagnosticIndicatorTypeEnum.deserialize(child))

        return obj



class DiagnosticIndicatorBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticIndicator with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticIndicator = DiagnosticIndicator()


    def with_type(self, value: Optional[DiagnosticIndicatorTypeEnum]) -> "DiagnosticIndicatorBuilder":
        """Set type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "type",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticIndicator:
        """Build and return the DiagnosticIndicator instance with validation."""
        self._validate_instance()
        return self._obj