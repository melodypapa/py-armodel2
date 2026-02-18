"""DiagnosticTroubleCodeJ1939 AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)


class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeJ1939."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dtc_props_props: Optional[DiagnosticTroubleCode]
    fmi: Optional[PositiveInteger]
    kind: Optional[DiagnosticTroubleCode]
    node: Optional[DiagnosticJ1939Node]
    spn: Optional[DiagnosticJ1939Spn]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeJ1939."""
        super().__init__()
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.fmi: Optional[PositiveInteger] = None
        self.kind: Optional[DiagnosticTroubleCode] = None
        self.node: Optional[DiagnosticJ1939Node] = None
        self.spn: Optional[DiagnosticJ1939Spn] = None


class DiagnosticTroubleCodeJ1939Builder:
    """Builder for DiagnosticTroubleCodeJ1939."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeJ1939 = DiagnosticTroubleCodeJ1939()

    def build(self) -> DiagnosticTroubleCodeJ1939:
        """Build and return DiagnosticTroubleCodeJ1939 object.

        Returns:
            DiagnosticTroubleCodeJ1939 instance
        """
        # TODO: Add validation
        return self._obj
