"""DiagnosticDebouncingAlgorithm module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticDebouncingAlgorithm.diagnostic_debounce_algorithm_props import (
        DiagnosticDebounceAlgorithmProps,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticDebouncingAlgorithm.diagnostic_debounce_behavior_enum import (
    DiagnosticDebounceBehaviorEnum,
)

__all__ = [
    "DiagnosticDebounceAlgorithmProps",
    "DiagnosticDebounceBehaviorEnum",
]
