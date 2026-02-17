"""DiagnosticServiceTable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
    DiagnosticConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class DiagnosticServiceTable(DiagnosticCommonElement):
    """AUTOSAR DiagnosticServiceTable."""

    diagnostics: list[DiagnosticConnection]
    ecu_instance: Optional[EcuInstance]
    protocol_kind: Optional[NameToken]
    service_instances: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceTable."""
        super().__init__()
        self.diagnostics: list[DiagnosticConnection] = []
        self.ecu_instance: Optional[EcuInstance] = None
        self.protocol_kind: Optional[NameToken] = None
        self.service_instances: list[Any] = []


class DiagnosticServiceTableBuilder:
    """Builder for DiagnosticServiceTable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceTable = DiagnosticServiceTable()

    def build(self) -> DiagnosticServiceTable:
        """Build and return DiagnosticServiceTable object.

        Returns:
            DiagnosticServiceTable instance
        """
        # TODO: Add validation
        return self._obj
