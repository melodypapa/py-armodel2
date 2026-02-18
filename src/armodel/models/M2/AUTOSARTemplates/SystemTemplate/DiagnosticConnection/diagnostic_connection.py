"""DiagnosticConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 60)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 632)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)


class DiagnosticConnection(ARElement):
    """AUTOSAR DiagnosticConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    functional_requests: list[TpConnectionIdent]
    periodic_response_uudts: list[PduTriggering]
    physical_request: Optional[TpConnectionIdent]
    response: Optional[TpConnectionIdent]
    response_on: Optional[TpConnectionIdent]
    def __init__(self) -> None:
        """Initialize DiagnosticConnection."""
        super().__init__()
        self.functional_requests: list[TpConnectionIdent] = []
        self.periodic_response_uudts: list[PduTriggering] = []
        self.physical_request: Optional[TpConnectionIdent] = None
        self.response: Optional[TpConnectionIdent] = None
        self.response_on: Optional[TpConnectionIdent] = None


class DiagnosticConnectionBuilder:
    """Builder for DiagnosticConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticConnection = DiagnosticConnection()

    def build(self) -> DiagnosticConnection:
        """Build and return DiagnosticConnection object.

        Returns:
            DiagnosticConnection instance
        """
        # TODO: Add validation
        return self._obj
