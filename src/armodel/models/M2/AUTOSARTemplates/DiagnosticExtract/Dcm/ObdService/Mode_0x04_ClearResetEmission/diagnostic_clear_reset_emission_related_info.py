"""DiagnosticClearResetEmissionRelatedInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x04_ClearResetEmission.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearResetEmissionRelatedInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_reset: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticClearResetEmissionRelatedInfo."""
        super().__init__()
        self.clear_reset: Optional[Any] = None


class DiagnosticClearResetEmissionRelatedInfoBuilder:
    """Builder for DiagnosticClearResetEmissionRelatedInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearResetEmissionRelatedInfo = DiagnosticClearResetEmissionRelatedInfo()

    def build(self) -> DiagnosticClearResetEmissionRelatedInfo:
        """Build and return DiagnosticClearResetEmissionRelatedInfo object.

        Returns:
            DiagnosticClearResetEmissionRelatedInfo instance
        """
        # TODO: Add validation
        return self._obj
