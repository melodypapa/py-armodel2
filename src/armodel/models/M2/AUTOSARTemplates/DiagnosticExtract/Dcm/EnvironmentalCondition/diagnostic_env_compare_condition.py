"""DiagnosticEnvCompareCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import (
    DiagnosticEnvConditionFormulaPart,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition import (
    DiagnosticCompareTypeEnum,
)


class DiagnosticEnvCompareCondition(DiagnosticEnvConditionFormulaPart):
    """AUTOSAR DiagnosticEnvCompareCondition."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DiagnosticEnvCompareCondition."""
        super().__init__()
        self.compare_type: Optional[DiagnosticCompareTypeEnum] = None


class DiagnosticEnvCompareConditionBuilder:
    """Builder for DiagnosticEnvCompareCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvCompareCondition = DiagnosticEnvCompareCondition()

    def build(self) -> DiagnosticEnvCompareCondition:
        """Build and return DiagnosticEnvCompareCondition object.

        Returns:
            DiagnosticEnvCompareCondition instance
        """
        # TODO: Add validation
        return self._obj
