"""DiagnosticEnvModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticEnvModeCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvModeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_element: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvModeCondition."""
        super().__init__()
        self.mode_element: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvModeCondition":
        """Deserialize XML element to DiagnosticEnvModeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvModeCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvModeCondition, cls).deserialize(element)

        # Parse mode_element
        child = ARObject._find_child_element(element, "MODE-ELEMENT")
        if child is not None:
            mode_element_value = child.text
            obj.mode_element = mode_element_value

        return obj



class DiagnosticEnvModeConditionBuilder:
    """Builder for DiagnosticEnvModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvModeCondition = DiagnosticEnvModeCondition()

    def build(self) -> DiagnosticEnvModeCondition:
        """Build and return DiagnosticEnvModeCondition object.

        Returns:
            DiagnosticEnvModeCondition instance
        """
        # TODO: Add validation
        return self._obj
