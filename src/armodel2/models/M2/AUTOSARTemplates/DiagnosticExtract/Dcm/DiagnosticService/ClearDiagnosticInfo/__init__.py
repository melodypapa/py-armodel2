"""ClearDiagnosticInfo module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ClearDiagnosticInfo.diagnostic_clear_diagnostic_information import (
        DiagnosticClearDiagnosticInformation,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ClearDiagnosticInfo.diagnostic_clear_diagnostic_information_class import (
        DiagnosticClearDiagnosticInformationClass,
    )

__all__ = [
    "DiagnosticClearDiagnosticInformation",
    "DiagnosticClearDiagnosticInformationClass",
]
