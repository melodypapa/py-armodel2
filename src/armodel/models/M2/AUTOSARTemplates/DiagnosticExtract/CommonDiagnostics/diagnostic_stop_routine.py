"""DiagnosticStopRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

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


class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticStopRoutine."""

    requests: list[DiagnosticParameter]
    responses: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticStopRoutine."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []


class DiagnosticStopRoutineBuilder:
    """Builder for DiagnosticStopRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStopRoutine = DiagnosticStopRoutine()

    def build(self) -> DiagnosticStopRoutine:
        """Build and return DiagnosticStopRoutine object.

        Returns:
            DiagnosticStopRoutine instance
        """
        # TODO: Add validation
        return self._obj
