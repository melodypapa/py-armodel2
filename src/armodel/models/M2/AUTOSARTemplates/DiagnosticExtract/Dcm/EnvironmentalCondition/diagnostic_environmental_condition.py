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
