"""DiagnosticReadDTCInformationClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDTCInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticReadDTCInformationClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDTCInformationClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticReadDTCInformationClass."""
        super().__init__()


class DiagnosticReadDTCInformationClassBuilder:
    """Builder for DiagnosticReadDTCInformationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDTCInformationClass = DiagnosticReadDTCInformationClass()

    def build(self) -> DiagnosticReadDTCInformationClass:
        """Build and return DiagnosticReadDTCInformationClass object.

        Returns:
            DiagnosticReadDTCInformationClass instance
        """
        # TODO: Add validation
        return self._obj
