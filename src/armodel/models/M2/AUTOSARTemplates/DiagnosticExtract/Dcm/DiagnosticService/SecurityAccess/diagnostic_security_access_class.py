"""DiagnosticSecurityAccessClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SecurityAccess.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticSecurityAccessClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticSecurityAccessClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticSecurityAccessClass."""
        super().__init__()


class DiagnosticSecurityAccessClassBuilder:
    """Builder for DiagnosticSecurityAccessClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityAccessClass = DiagnosticSecurityAccessClass()

    def build(self) -> DiagnosticSecurityAccessClass:
        """Build and return DiagnosticSecurityAccessClass object.

        Returns:
            DiagnosticSecurityAccessClass instance
        """
        # TODO: Add validation
        return self._obj
