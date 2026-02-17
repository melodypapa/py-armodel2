"""DiagnosticServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommonService.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticServiceInstance(DiagnosticCommonElement):
    """AUTOSAR DiagnosticServiceInstance."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DiagnosticServiceInstance."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
        self.service_class: Optional[DiagnosticServiceClass] = None


class DiagnosticServiceInstanceBuilder:
    """Builder for DiagnosticServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceInstance = DiagnosticServiceInstance()

    def build(self) -> DiagnosticServiceInstance:
        """Build and return DiagnosticServiceInstance object.

        Returns:
            DiagnosticServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
