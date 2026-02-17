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


class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEnvironmentalCondition."""

    formula: Optional[Any]
    mode_elements: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvironmentalCondition."""
        super().__init__()
        self.formula: Optional[Any] = None
        self.mode_elements: list[Any] = []


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
