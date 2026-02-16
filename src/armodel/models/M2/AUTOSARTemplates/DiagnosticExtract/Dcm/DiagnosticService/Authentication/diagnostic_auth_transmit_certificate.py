"""DiagnosticAuthTransmitCertificate AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)


class DiagnosticAuthTransmitCertificate(DiagnosticAuthentication):
    """AUTOSAR DiagnosticAuthTransmitCertificate."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("certificates", None, False, True, any (DiagnosticAuthTransmit)),  # certificates
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificate."""
        super().__init__()
        self.certificates: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthTransmitCertificate to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificate":
        """Create DiagnosticAuthTransmitCertificate from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthTransmitCertificate instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthTransmitCertificate since parent returns ARObject
        return cast("DiagnosticAuthTransmitCertificate", obj)


class DiagnosticAuthTransmitCertificateBuilder:
    """Builder for DiagnosticAuthTransmitCertificate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificate = DiagnosticAuthTransmitCertificate()

    def build(self) -> DiagnosticAuthTransmitCertificate:
        """Build and return DiagnosticAuthTransmitCertificate object.

        Returns:
            DiagnosticAuthTransmitCertificate instance
        """
        # TODO: Add validation
        return self._obj
