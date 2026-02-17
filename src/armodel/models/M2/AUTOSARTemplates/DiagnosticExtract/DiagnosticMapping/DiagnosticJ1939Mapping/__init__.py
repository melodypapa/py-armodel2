"""DiagnosticJ1939Mapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.DiagnosticJ1939Mapping.diagnostic_j1939_spn_mapping import (
        DiagnosticJ1939SpnMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.DiagnosticJ1939Mapping.diagnostic_j1939_sw_mapping import (
        DiagnosticJ1939SwMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.DiagnosticJ1939Mapping.diagnostic_event_to_trouble_code_j1939_mapping import (
        DiagnosticEventToTroubleCodeJ1939Mapping,
    )

__all__ = [
    "DiagnosticEventToTroubleCodeJ1939Mapping",
    "DiagnosticJ1939SpnMapping",
    "DiagnosticJ1939SwMapping",
]
