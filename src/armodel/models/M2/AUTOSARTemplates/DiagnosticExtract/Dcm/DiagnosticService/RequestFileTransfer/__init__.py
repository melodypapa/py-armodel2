"""RequestFileTransfer module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.RequestFileTransfer.diagnostic_request_file_transfer import (
        DiagnosticRequestFileTransfer,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.RequestFileTransfer.diagnostic_request_file_transfer_class import (
        DiagnosticRequestFileTransferClass,
    )

__all__ = [
    "DiagnosticRequestFileTransfer",
    "DiagnosticRequestFileTransferClass",
]
