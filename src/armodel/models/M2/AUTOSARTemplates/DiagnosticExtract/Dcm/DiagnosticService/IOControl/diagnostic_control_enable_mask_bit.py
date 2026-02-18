"""DiagnosticControlEnableMaskBit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticControlEnableMaskBit(ARObject):
    """AUTOSAR DiagnosticControlEnableMaskBit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bit_number: Optional[PositiveInteger]
    controlled_datas: list[DiagnosticDataElement]
    def __init__(self) -> None:
        """Initialize DiagnosticControlEnableMaskBit."""
        super().__init__()
        self.bit_number: Optional[PositiveInteger] = None
        self.controlled_datas: list[DiagnosticDataElement] = []


class DiagnosticControlEnableMaskBitBuilder:
    """Builder for DiagnosticControlEnableMaskBit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlEnableMaskBit = DiagnosticControlEnableMaskBit()

    def build(self) -> DiagnosticControlEnableMaskBit:
        """Build and return DiagnosticControlEnableMaskBit object.

        Returns:
            DiagnosticControlEnableMaskBit instance
        """
        # TODO: Add validation
        return self._obj
