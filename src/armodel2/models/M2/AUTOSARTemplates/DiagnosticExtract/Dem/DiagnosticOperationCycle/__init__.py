"""DiagnosticOperationCycle module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticOperationCycle.diagnostic_operation_cycle import (
        DiagnosticOperationCycle,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticOperationCycle.diagnostic_operation_cycle_type_enum import (
    DiagnosticOperationCycleTypeEnum,
)

__all__ = [
    "DiagnosticOperationCycle",
    "DiagnosticOperationCycleTypeEnum",
]
