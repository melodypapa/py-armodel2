"""DiagnosticEnvironmentalCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEnvironmentalCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    formula: Optional[Any]
    mode_elements: list[Any]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvironmentalCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize formula
        if self.formula is not None:
            serialized = ARObject._serialize_item(self.formula, "Any")
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
                serialized = ARObject._serialize_item(item, "Any")
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

        # Parse formula
        child = ARObject._find_child_element(element, "FORMULA")
        if child is not None:
            formula_value = child.text
            obj.formula = formula_value

        # Parse mode_elements (list from container "MODE-ELEMENTS")
        obj.mode_elements = []
        container = ARObject._find_child_element(element, "MODE-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_elements.append(child_value)

        return obj



class DiagnosticEnvironmentalConditionBuilder:
    """Builder for DiagnosticEnvironmentalCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvironmentalCondition = DiagnosticEnvironmentalCondition()

    def build(self) -> DiagnosticEnvironmentalCondition:
        """Build and return DiagnosticEnvironmentalCondition object.

        Returns:
            DiagnosticEnvironmentalCondition instance
        """
        # TODO: Add validation
        return self._obj
