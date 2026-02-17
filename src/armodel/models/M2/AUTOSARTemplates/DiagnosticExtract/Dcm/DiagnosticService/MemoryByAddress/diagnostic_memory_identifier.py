"""DiagnosticMemoryIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)


class DiagnosticMemoryIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMemoryIdentifier."""

    access: Optional[DiagnosticAccessPermission]
    id: Optional[PositiveInteger]
    memory_high: Optional[String]
    memory_low: Optional[String]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryIdentifier."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
        self.id: Optional[PositiveInteger] = None
        self.memory_high: Optional[String] = None
        self.memory_low: Optional[String] = None


class DiagnosticMemoryIdentifierBuilder:
    """Builder for DiagnosticMemoryIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryIdentifier = DiagnosticMemoryIdentifier()

    def build(self) -> DiagnosticMemoryIdentifier:
        """Build and return DiagnosticMemoryIdentifier object.

        Returns:
            DiagnosticMemoryIdentifier instance
        """
        # TODO: Add validation
        return self._obj
