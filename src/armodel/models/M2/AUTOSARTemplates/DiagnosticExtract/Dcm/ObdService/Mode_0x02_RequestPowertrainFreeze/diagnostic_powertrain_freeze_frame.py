"""DiagnosticPowertrainFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x02_RequestPowertrainFreeze.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticPowertrainFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticPowertrainFreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pids: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticPowertrainFreezeFrame."""
        super().__init__()
        self.pids: list[DiagnosticParameter] = []


class DiagnosticPowertrainFreezeFrameBuilder:
    """Builder for DiagnosticPowertrainFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticPowertrainFreezeFrame = DiagnosticPowertrainFreezeFrame()

    def build(self) -> DiagnosticPowertrainFreezeFrame:
        """Build and return DiagnosticPowertrainFreezeFrame object.

        Returns:
            DiagnosticPowertrainFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
