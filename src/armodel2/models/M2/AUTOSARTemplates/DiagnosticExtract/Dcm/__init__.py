"""Dcm module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
        DiagnosticAccessPermission,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
        DiagnosticSession,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
        DiagnosticSecurityLevel,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role_proxy import (
        DiagnosticAuthRoleProxy,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
        DiagnosticAuthRole,
    )

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_jump_to_boot_loader_enum import (
    DiagnosticJumpToBootLoaderEnum,
)

__all__ = [
    "DiagnosticAccessPermission",
    "DiagnosticAuthRole",
    "DiagnosticAuthRoleProxy",
    "DiagnosticJumpToBootLoaderEnum",
    "DiagnosticSecurityLevel",
    "DiagnosticSession",
]
