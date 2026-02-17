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


class DiagnosticEnvModeCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvModeCondition."""

    mode_element: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvModeCondition."""
        super().__init__()
        self.mode_element: Optional[Any] = None


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
