"""RoutineControl module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.RoutineControl.diagnostic_routine_control import (
        DiagnosticRoutineControl,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.RoutineControl.diagnostic_routine_control_class import (
        DiagnosticRoutineControlClass,
    )

__all__ = [
    "DiagnosticRoutineControl",
    "DiagnosticRoutineControlClass",
]
