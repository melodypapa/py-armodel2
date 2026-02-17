"""J1939 module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
        DiagnosticJ1939Spn,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_freeze_frame import (
        DiagnosticJ1939FreezeFrame,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_expanded_freeze_frame import (
        DiagnosticJ1939ExpandedFreezeFrame,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
        DiagnosticJ1939Node,
    )

__all__ = [
    "DiagnosticJ1939ExpandedFreezeFrame",
    "DiagnosticJ1939FreezeFrame",
    "DiagnosticJ1939Node",
    "DiagnosticJ1939Spn",
]
