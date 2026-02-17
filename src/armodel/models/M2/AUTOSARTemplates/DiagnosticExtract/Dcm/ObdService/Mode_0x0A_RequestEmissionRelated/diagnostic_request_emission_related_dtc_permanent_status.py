"""DiagnosticRequestEmissionRelatedDTCPermanentStatus AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x0A_RequestEmissionRelated.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestEmissionRelatedDTCPermanentStatus(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    request: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTCPermanentStatus."""
        super().__init__()
        self.request: Optional[Any] = None


class DiagnosticRequestEmissionRelatedDTCPermanentStatusBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTCPermanentStatus = DiagnosticRequestEmissionRelatedDTCPermanentStatus()

    def build(self) -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
        """Build and return DiagnosticRequestEmissionRelatedDTCPermanentStatus object.

        Returns:
            DiagnosticRequestEmissionRelatedDTCPermanentStatus instance
        """
        # TODO: Add validation
        return self._obj
