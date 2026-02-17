"""DiagnosticInfoType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticInfoType(DiagnosticCommonElement):
    """AUTOSAR DiagnosticInfoType."""

    def __init__(self) -> None:
        """Initialize DiagnosticInfoType."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None


class DiagnosticInfoTypeBuilder:
    """Builder for DiagnosticInfoType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticInfoType = DiagnosticInfoType()

    def build(self) -> DiagnosticInfoType:
        """Build and return DiagnosticInfoType object.

        Returns:
            DiagnosticInfoType instance
        """
        # TODO: Add validation
        return self._obj
