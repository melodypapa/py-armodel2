"""EcuReset module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset.diagnostic_ecu_reset import (
        DiagnosticEcuReset,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset.diagnostic_ecu_reset_class import (
        DiagnosticEcuResetClass,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset.diagnostic_response_to_ecu_reset_enum import (
    DiagnosticResponseToEcuResetEnum,
)

__all__ = [
    "DiagnosticEcuReset",
    "DiagnosticEcuResetClass",
    "DiagnosticResponseToEcuResetEnum",
]
