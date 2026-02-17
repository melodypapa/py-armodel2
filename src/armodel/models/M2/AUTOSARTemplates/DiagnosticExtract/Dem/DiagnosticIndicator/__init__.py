"""DiagnosticIndicator module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator.diagnostic_indicator import (
        DiagnosticIndicator,
    )

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator.diagnostic_indicator_type_enum import (
    DiagnosticIndicatorTypeEnum,
)

__all__ = [
    "DiagnosticIndicator",
    "DiagnosticIndicatorTypeEnum",
]
