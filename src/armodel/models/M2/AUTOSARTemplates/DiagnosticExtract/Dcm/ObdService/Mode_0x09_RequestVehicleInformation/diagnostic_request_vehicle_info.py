"""DiagnosticRequestVehicleInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x09_RequestVehicleInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_info_type import (
    DiagnosticInfoType,
)


class DiagnosticRequestVehicleInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestVehicleInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    info_type: Optional[DiagnosticInfoType]
    request_vehicle: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestVehicleInfo."""
        super().__init__()
        self.info_type: Optional[DiagnosticInfoType] = None
        self.request_vehicle: Optional[Any] = None


class DiagnosticRequestVehicleInfoBuilder:
    """Builder for DiagnosticRequestVehicleInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestVehicleInfo = DiagnosticRequestVehicleInfo()

    def build(self) -> DiagnosticRequestVehicleInfo:
        """Build and return DiagnosticRequestVehicleInfo object.

        Returns:
            DiagnosticRequestVehicleInfo instance
        """
        # TODO: Add validation
        return self._obj
