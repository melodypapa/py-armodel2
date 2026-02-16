"""DiagnosticConnection AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("functional_requests", None, False, True, TpConnectionIdent),  # functionalRequests
        ("periodic_response_uudts", None, False, True, PduTriggering),  # periodicResponseUudts
        ("physical_request", None, False, False, TpConnectionIdent),  # physicalRequest
        ("response", None, False, False, TpConnectionIdent),  # response
        ("response_on", None, False, False, TpConnectionIdent),  # responseOn
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticConnection."""
        super().__init__()
        self.functional_requests: list[TpConnectionIdent] = []
        self.periodic_response_uudts: list[PduTriggering] = []
        self.physical_request: Optional[TpConnectionIdent] = None
        self.response: Optional[TpConnectionIdent] = None
        self.response_on: Optional[TpConnectionIdent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticConnection":
        """Create DiagnosticConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticConnection since parent returns ARObject
        return cast("DiagnosticConnection", obj)


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
