"""DiagnosticWriteDataByIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticWriteDataByIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticWriteDataByIdentifierClass."""

    def __init__(self) -> None:
        """Initialize DiagnosticWriteDataByIdentifierClass."""
        super().__init__()


class DiagnosticWriteDataByIdentifierClassBuilder:
    """Builder for DiagnosticWriteDataByIdentifierClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteDataByIdentifierClass = DiagnosticWriteDataByIdentifierClass()

    def build(self) -> DiagnosticWriteDataByIdentifierClass:
        """Build and return DiagnosticWriteDataByIdentifierClass object.

        Returns:
            DiagnosticWriteDataByIdentifierClass instance
        """
        # TODO: Add validation
        return self._obj
