"""DiagnosticSession AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import (
    DiagnosticJumpToBootLoaderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class DiagnosticSession(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSession."""

    id: Optional[PositiveInteger]
    jump_to_boot: Optional[DiagnosticJumpToBootLoaderEnum]
    p2_server_max: Optional[TimeValue]
    p2_star_server: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize DiagnosticSession."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.jump_to_boot: Optional[DiagnosticJumpToBootLoaderEnum] = None
        self.p2_server_max: Optional[TimeValue] = None
        self.p2_star_server: Optional[TimeValue] = None


class DiagnosticSessionBuilder:
    """Builder for DiagnosticSession."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSession = DiagnosticSession()

    def build(self) -> DiagnosticSession:
        """Build and return DiagnosticSession object.

        Returns:
            DiagnosticSession instance
        """
        # TODO: Add validation
        return self._obj
