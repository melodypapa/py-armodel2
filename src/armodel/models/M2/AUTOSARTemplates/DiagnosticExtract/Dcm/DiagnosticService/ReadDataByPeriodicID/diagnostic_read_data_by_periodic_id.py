"""DiagnosticReadDataByPeriodicID AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDataByPeriodicID."""

    read_data_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicID."""
        super().__init__()
        self.read_data_class: Optional[Any] = None


class DiagnosticReadDataByPeriodicIDBuilder:
    """Builder for DiagnosticReadDataByPeriodicID."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicID = DiagnosticReadDataByPeriodicID()

    def build(self) -> DiagnosticReadDataByPeriodicID:
        """Build and return DiagnosticReadDataByPeriodicID object.

        Returns:
            DiagnosticReadDataByPeriodicID instance
        """
        # TODO: Add validation
        return self._obj
