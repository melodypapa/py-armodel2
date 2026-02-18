"""DiagnosticTroubleCodeGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 177)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dtcs: list[DiagnosticTroubleCode]
    group_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeGroup."""
        super().__init__()
        self.dtcs: list[DiagnosticTroubleCode] = []
        self.group_number: Optional[PositiveInteger] = None


class DiagnosticTroubleCodeGroupBuilder:
    """Builder for DiagnosticTroubleCodeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeGroup = DiagnosticTroubleCodeGroup()

    def build(self) -> DiagnosticTroubleCodeGroup:
        """Build and return DiagnosticTroubleCodeGroup object.

        Returns:
            DiagnosticTroubleCodeGroup instance
        """
        # TODO: Add validation
        return self._obj
