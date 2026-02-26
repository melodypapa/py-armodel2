"""Mode_0x03_0x07_RequestEmission module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x03_0x07_RequestEmission.diagnostic_request_emission_related_dtc import (
        DiagnosticRequestEmissionRelatedDTC,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x03_0x07_RequestEmission.diagnostic_request_emission_related_dtc_class import (
        DiagnosticRequestEmissionRelatedDTCClass,
    )

__all__ = [
    "DiagnosticRequestEmissionRelatedDTC",
    "DiagnosticRequestEmissionRelatedDTCClass",
]
