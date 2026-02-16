"""DiagnosticConnection AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "functional_requests": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TpConnectionIdent,
        ),  # functionalRequests
        "periodic_response_uudts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PduTriggering,
        ),  # periodicResponseUudts
        "physical_request": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpConnectionIdent,
        ),  # physicalRequest
        "response": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpConnectionIdent,
        ),  # response
        "response_on": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpConnectionIdent,
        ),  # responseOn
    }

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
