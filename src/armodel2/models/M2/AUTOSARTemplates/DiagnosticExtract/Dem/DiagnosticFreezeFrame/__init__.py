"""DiagnosticFreezeFrame module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame.diagnostic_freeze_frame import (
        DiagnosticFreezeFrame,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame.diagnostic_record_trigger_enum import (
    DiagnosticRecordTriggerEnum,
)

__all__ = [
    "DiagnosticFreezeFrame",
    "DiagnosticRecordTriggerEnum",
]
