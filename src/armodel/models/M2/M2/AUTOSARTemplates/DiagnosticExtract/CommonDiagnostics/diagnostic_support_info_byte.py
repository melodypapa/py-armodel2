"""DiagnosticSupportInfoByte AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticSupportInfoByte(ARObject):
    """AUTOSAR DiagnosticSupportInfoByte."""

    def __init__(self) -> None:
        """Initialize DiagnosticSupportInfoByte."""
        super().__init__()
        self.position: Optional[PositiveInteger] = None
        self.size: Optional[PositiveInteger] = None


class DiagnosticSupportInfoByteBuilder:
    """Builder for DiagnosticSupportInfoByte."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSupportInfoByte = DiagnosticSupportInfoByte()

    def build(self) -> DiagnosticSupportInfoByte:
        """Build and return DiagnosticSupportInfoByte object.

        Returns:
            DiagnosticSupportInfoByte instance
        """
        # TODO: Add validation
        return self._obj
