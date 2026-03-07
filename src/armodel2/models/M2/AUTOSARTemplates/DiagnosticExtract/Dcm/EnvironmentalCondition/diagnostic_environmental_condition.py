"""DiagnosticEnvironmentalCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEnvironmentalCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-ENVIRONMENTAL-CONDITION"


    formula: Optional[Any]
    mode_elements: list[Any]
    _DESERIALIZE_DISPATCH = {
        "FORMULA": lambda obj, elem: setattr(obj, "formula", SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticEnvCondition)")),
        "MODE-ELEMENTS": lambda obj, elem: obj.mode_elements.append(SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticEnvMode)")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticEnvironmentalCondition."""
        super().__init__()
        self.formula: Optional[Any] = None
        self.mode_elements: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvironmentalCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvironmentalCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize formula
        if self.formula is not None:
            serialized = SerializationHelper.serialize_item(self.formula, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_elements (list to container "MODE-ELEMENTS")
        if self.mode_elements:
            wrapper = ET.Element("MODE-ELEMENTS")
            for item in self.mode_elements:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvironmentalCondition":
        """Deserialize XML element to DiagnosticEnvironmentalCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvironmentalCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvironmentalCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FORMULA":
                setattr(obj, "formula", SerializationHelper.deserialize_by_tag(child, "any (DiagnosticEnvCondition)"))
            elif tag == "MODE-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "any (DiagnosticEnvMode)"))

        return obj



class DiagnosticEnvironmentalConditionBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticEnvironmentalCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEnvironmentalCondition = DiagnosticEnvironmentalCondition()


    def with_formula(self, value: Optional[Any]) -> "DiagnosticEnvironmentalConditionBuilder":
        """Set formula attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'formula' is required and cannot be None")
        self._obj.formula = value
        return self

    def with_mode_elements(self, items: list[Any]) -> "DiagnosticEnvironmentalConditionBuilder":
        """Set mode_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_elements = list(items) if items else []
        return self


    def add_mode_element(self, item: Any) -> "DiagnosticEnvironmentalConditionBuilder":
        """Add a single item to mode_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_elements.append(item)
        return self

    def clear_mode_elements(self) -> "DiagnosticEnvironmentalConditionBuilder":
        """Clear all items from mode_elements list.

        Returns:
            self for method chaining
        """
        self._obj.mode_elements = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "formula",
        "modeElement",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticEnvironmentalCondition:
        """Build and return the DiagnosticEnvironmentalCondition instance with validation."""
        self._validate_instance()
        return self._obj