"""DiagnosticProtocol AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostics": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticConnection,
        ),  # diagnostics
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "protocol_kind": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # protocolKind
        "send_resp_pend": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sendRespPend
        "service_table": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticServiceTable,
        ),  # serviceTable
    }

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
