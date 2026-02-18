"""DiagnosticProtocol AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 58)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
    DiagnosticConnection,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)


class DiagnosticProtocol(DiagnosticCommonElement):
    """AUTOSAR DiagnosticProtocol."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostics: list[DiagnosticConnection]
    priority: Optional[PositiveInteger]
    protocol_kind: Optional[NameToken]
    send_resp_pend: Optional[Boolean]
    service_table: Optional[DiagnosticServiceTable]
    def __init__(self) -> None:
        """Initialize DiagnosticProtocol."""
        super().__init__()
        self.diagnostics: list[DiagnosticConnection] = []
        self.priority: Optional[PositiveInteger] = None
        self.protocol_kind: Optional[NameToken] = None
        self.send_resp_pend: Optional[Boolean] = None
        self.service_table: Optional[DiagnosticServiceTable] = None


class DiagnosticProtocolBuilder:
    """Builder for DiagnosticProtocol."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticProtocol = DiagnosticProtocol()

    def build(self) -> DiagnosticProtocol:
        """Build and return DiagnosticProtocol object.

        Returns:
            DiagnosticProtocol instance
        """
        # TODO: Add validation
        return self._obj
