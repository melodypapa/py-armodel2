"""DiagnosticCustomServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CustomServiceInstance.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticCustomServiceInstance(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticCustomServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticCustomServiceInstance."""
        super().__init__()
        self.custom_service: Optional[Any] = None


class DiagnosticCustomServiceInstanceBuilder:
    """Builder for DiagnosticCustomServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCustomServiceInstance = DiagnosticCustomServiceInstance()

    def build(self) -> DiagnosticCustomServiceInstance:
        """Build and return DiagnosticCustomServiceInstance object.

        Returns:
            DiagnosticCustomServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
