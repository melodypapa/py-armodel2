"""DiagnosticConditionGroup module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
        DiagnosticConditionGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_enable_condition_group import (
        DiagnosticEnableConditionGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_storage_condition_group import (
        DiagnosticStorageConditionGroup,
    )

__all__ = [
    "DiagnosticConditionGroup",
    "DiagnosticEnableConditionGroup",
    "DiagnosticStorageConditionGroup",
]
