"""DiagnosticCommonProps module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticCommonProps.diagnostic_common_props import (
        DiagnosticCommonProps,
    )

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticCommonProps.diagnostic_occurrence_counter_processing_enum import (
    DiagnosticOccurrenceCounterProcessingEnum,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticCommonProps.diagnostic_event_combination_behavior_enum import (
    DiagnosticEventCombinationBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticCommonProps.diagnostic_event_combination_reporting_behavior_enum import (
    DiagnosticEventCombinationReportingBehaviorEnum,
)

__all__ = [
    "DiagnosticCommonProps",
    "DiagnosticEventCombinationBehaviorEnum",
    "DiagnosticEventCombinationReportingBehaviorEnum",
    "DiagnosticOccurrenceCounterProcessingEnum",
]
