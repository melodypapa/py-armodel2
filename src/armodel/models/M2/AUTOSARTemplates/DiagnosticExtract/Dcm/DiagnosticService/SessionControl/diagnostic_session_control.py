"""DiagnosticSessionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SessionControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)


class DiagnosticSessionControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSessionControl."""

    def __init__(self) -> None:
        """Initialize DiagnosticSessionControl."""
        super().__init__()
        self.diagnostic_session_session: Optional[DiagnosticSession] = None
        self.session_control: Optional[DiagnosticSession] = None


class DiagnosticSessionControlBuilder:
    """Builder for DiagnosticSessionControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControl = DiagnosticSessionControl()

    def build(self) -> DiagnosticSessionControl:
        """Build and return DiagnosticSessionControl object.

        Returns:
            DiagnosticSessionControl instance
        """
        # TODO: Add validation
        return self._obj
