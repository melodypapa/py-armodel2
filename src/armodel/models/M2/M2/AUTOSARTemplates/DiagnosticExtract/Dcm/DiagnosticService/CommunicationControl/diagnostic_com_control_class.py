"""DiagnosticComControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
    DiagnosticComControl,
)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticComControlClass."""

    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channelses: list[CommunicationCluster] = []
        self.all_physicals: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []


class DiagnosticComControlClassBuilder:
    """Builder for DiagnosticComControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlClass = DiagnosticComControlClass()

    def build(self) -> DiagnosticComControlClass:
        """Build and return DiagnosticComControlClass object.

        Returns:
            DiagnosticComControlClass instance
        """
        # TODO: Add validation
        return self._obj
