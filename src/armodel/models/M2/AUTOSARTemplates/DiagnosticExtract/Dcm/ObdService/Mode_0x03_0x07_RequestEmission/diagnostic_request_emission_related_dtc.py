"""DiagnosticRequestEmissionRelatedDTC AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x03_0x07_RequestEmission.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestEmissionRelatedDTC(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTC."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTC."""
        super().__init__()
        self.request: Optional[Any] = None


class DiagnosticRequestEmissionRelatedDTCBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTC."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTC = DiagnosticRequestEmissionRelatedDTC()

    def build(self) -> DiagnosticRequestEmissionRelatedDTC:
        """Build and return DiagnosticRequestEmissionRelatedDTC object.

        Returns:
            DiagnosticRequestEmissionRelatedDTC instance
        """
        # TODO: Add validation
        return self._obj
