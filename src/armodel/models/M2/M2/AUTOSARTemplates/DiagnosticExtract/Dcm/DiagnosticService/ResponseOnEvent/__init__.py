"""ResponseOnEvent module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_response_on_event import (
        DiagnosticResponseOnEvent,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_response_on_event_class import (
        DiagnosticResponseOnEventClass,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_event_window import (
        DiagnosticEventWindow,
    )

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_event_window_time_enum import (
    DiagnosticEventWindowTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_response_on_event_action_enum import (
    DiagnosticResponseOnEventActionEnum,
)

__all__ = [
    "DiagnosticEventWindow",
    "DiagnosticEventWindowTimeEnum",
    "DiagnosticResponseOnEvent",
    "DiagnosticResponseOnEventActionEnum",
    "DiagnosticResponseOnEventClass",
]
