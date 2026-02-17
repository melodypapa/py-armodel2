"""SecurityAccess module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.SecurityAccess.diagnostic_security_access import (
        DiagnosticSecurityAccess,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.SecurityAccess.diagnostic_security_access_class import (
        DiagnosticSecurityAccessClass,
    )

__all__ = [
    "DiagnosticSecurityAccess",
    "DiagnosticSecurityAccessClass",
]
