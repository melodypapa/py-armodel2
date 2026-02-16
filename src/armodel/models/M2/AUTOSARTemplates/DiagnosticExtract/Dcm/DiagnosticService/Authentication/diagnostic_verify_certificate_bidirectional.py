"""DiagnosticVerifyCertificateBidirectional AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)


class DiagnosticVerifyCertificateBidirectional(DiagnosticAuthentication):
    """AUTOSAR DiagnosticVerifyCertificateBidirectional."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticVerifyCertificateBidirectional."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticVerifyCertificateBidirectional to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticVerifyCertificateBidirectional":
        """Create DiagnosticVerifyCertificateBidirectional from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticVerifyCertificateBidirectional instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticVerifyCertificateBidirectional since parent returns ARObject
        return cast("DiagnosticVerifyCertificateBidirectional", obj)


class DiagnosticVerifyCertificateBidirectionalBuilder:
    """Builder for DiagnosticVerifyCertificateBidirectional."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticVerifyCertificateBidirectional = DiagnosticVerifyCertificateBidirectional()

    def build(self) -> DiagnosticVerifyCertificateBidirectional:
        """Build and return DiagnosticVerifyCertificateBidirectional object.

        Returns:
            DiagnosticVerifyCertificateBidirectional instance
        """
        # TODO: Add validation
        return self._obj
