"""DiagnosticCondition module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticCondition.diagnostic_condition import (
        DiagnosticCondition,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticCondition.diagnostic_enable_condition import (
        DiagnosticEnableCondition,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticCondition.diagnostic_storage_condition import (
        DiagnosticStorageCondition,
    )

__all__ = [
    "DiagnosticCondition",
    "DiagnosticEnableCondition",
    "DiagnosticStorageCondition",
]
