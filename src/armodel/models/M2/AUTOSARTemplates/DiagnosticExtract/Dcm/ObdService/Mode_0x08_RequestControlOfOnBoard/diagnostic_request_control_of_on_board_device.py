"""DiagnosticRequestControlOfOnBoardDevice AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_test_routine_identifier import (
    DiagnosticTestRoutineIdentifier,
)


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDevice."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_control: Optional[Any]
    test_id_identifier: Optional[DiagnosticTestRoutineIdentifier]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDevice."""
        super().__init__()
        self.request_control: Optional[Any] = None
        self.test_id_identifier: Optional[DiagnosticTestRoutineIdentifier] = None


class DiagnosticRequestControlOfOnBoardDeviceBuilder:
    """Builder for DiagnosticRequestControlOfOnBoardDevice."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestControlOfOnBoardDevice = DiagnosticRequestControlOfOnBoardDevice()

    def build(self) -> DiagnosticRequestControlOfOnBoardDevice:
        """Build and return DiagnosticRequestControlOfOnBoardDevice object.

        Returns:
            DiagnosticRequestControlOfOnBoardDevice instance
        """
        # TODO: Add validation
        return self._obj
