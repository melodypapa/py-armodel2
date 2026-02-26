"""CommunicationControl module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
        DiagnosticComControl,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control_specific_channel import (
        DiagnosticComControlSpecificChannel,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control_class import (
        DiagnosticComControlClass,
    )
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control_sub_node_channel import (
        DiagnosticComControlSubNodeChannel,
    )

__all__ = [
    "DiagnosticComControl",
    "DiagnosticComControlClass",
    "DiagnosticComControlSpecificChannel",
    "DiagnosticComControlSubNodeChannel",
]
