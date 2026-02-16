"""DiagnosticVerifyCertificateUnidirectional AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)


class DiagnosticVerifyCertificateUnidirectional(DiagnosticAuthentication):
    """AUTOSAR DiagnosticVerifyCertificateUnidirectional."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticVerifyCertificateUnidirectional."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticVerifyCertificateUnidirectional to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticVerifyCertificateUnidirectional":
        """Create DiagnosticVerifyCertificateUnidirectional from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticVerifyCertificateUnidirectional instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticVerifyCertificateUnidirectional since parent returns ARObject
        return cast("DiagnosticVerifyCertificateUnidirectional", obj)


class DiagnosticVerifyCertificateUnidirectionalBuilder:
    """Builder for DiagnosticVerifyCertificateUnidirectional."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticVerifyCertificateUnidirectional = DiagnosticVerifyCertificateUnidirectional()

    def build(self) -> DiagnosticVerifyCertificateUnidirectional:
        """Build and return DiagnosticVerifyCertificateUnidirectional object.

        Returns:
            DiagnosticVerifyCertificateUnidirectional instance
        """
        # TODO: Add validation
        return self._obj
