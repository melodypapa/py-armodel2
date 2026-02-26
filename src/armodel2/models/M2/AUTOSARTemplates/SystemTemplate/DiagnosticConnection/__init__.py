"""DiagnosticConnection module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
        DiagnosticConnection,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
        TpConnectionIdent,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.do_ip_tp_connection import (
        DoIpTpConnection,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
        TpConnection,
    )

__all__ = [
    "DiagnosticConnection",
    "DoIpTpConnection",
    "TpConnection",
    "TpConnectionIdent",
]
