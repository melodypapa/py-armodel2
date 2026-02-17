"""Mode_0x0A_RequestEmissionRelated module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x0A_RequestEmissionRelated.diagnostic_request_emission_related_dtc_permanent_status import (
        DiagnosticRequestEmissionRelatedDTCPermanentStatus,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x0A_RequestEmissionRelated.diagnostic_request_emission_related_dtc_permanent_status_class import (
        DiagnosticRequestEmissionRelatedDTCPermanentStatusClass,
    )

__all__ = [
    "DiagnosticRequestEmissionRelatedDTCPermanentStatus",
    "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass",
]
