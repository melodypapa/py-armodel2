"""ReadDTCInformation module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDTCInformation.diagnostic_read_dtc_information import (
        DiagnosticReadDTCInformation,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDTCInformation.diagnostic_read_dtc_information_class import (
        DiagnosticReadDTCInformationClass,
    )

__all__ = [
    "DiagnosticReadDTCInformation",
    "DiagnosticReadDTCInformationClass",
]
