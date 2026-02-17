"""DiagnosticStartRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import (
    DiagnosticRoutineSubfunction,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticStartRoutine(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticStartRoutine."""

    def __init__(self) -> None:
        """Initialize DiagnosticStartRoutine."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []


class DiagnosticStartRoutineBuilder:
    """Builder for DiagnosticStartRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStartRoutine = DiagnosticStartRoutine()

    def build(self) -> DiagnosticStartRoutine:
        """Build and return DiagnosticStartRoutine object.

        Returns:
            DiagnosticStartRoutine instance
        """
        # TODO: Add validation
        return self._obj
