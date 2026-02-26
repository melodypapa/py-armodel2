"""Mode_0x08_RequestControlOfOnBoard module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_request_control_of_on_board_device import (
        DiagnosticRequestControlOfOnBoardDevice,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_request_control_of_on_board_device_class import (
        DiagnosticRequestControlOfOnBoardDeviceClass,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_test_routine_identifier import (
        DiagnosticTestRoutineIdentifier,
    )

__all__ = [
    "DiagnosticRequestControlOfOnBoardDevice",
    "DiagnosticRequestControlOfOnBoardDeviceClass",
    "DiagnosticTestRoutineIdentifier",
]
