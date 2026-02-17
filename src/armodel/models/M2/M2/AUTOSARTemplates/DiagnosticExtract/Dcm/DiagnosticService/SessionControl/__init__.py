"""SessionControl module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.SessionControl.diagnostic_session_control import (
        DiagnosticSessionControl,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.SessionControl.diagnostic_session_control_class import (
        DiagnosticSessionControlClass,
    )

__all__ = [
    "DiagnosticSessionControl",
    "DiagnosticSessionControlClass",
]
