"""DiagnosticProofOfOwnership AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)


class DiagnosticProofOfOwnership(DiagnosticAuthentication):
    """AUTOSAR DiagnosticProofOfOwnership."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticProofOfOwnership."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticProofOfOwnership to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticProofOfOwnership":
        """Create DiagnosticProofOfOwnership from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticProofOfOwnership instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticProofOfOwnership since parent returns ARObject
        return cast("DiagnosticProofOfOwnership", obj)


class DiagnosticProofOfOwnershipBuilder:
    """Builder for DiagnosticProofOfOwnership."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticProofOfOwnership = DiagnosticProofOfOwnership()

    def build(self) -> DiagnosticProofOfOwnership:
        """Build and return DiagnosticProofOfOwnership object.

        Returns:
            DiagnosticProofOfOwnership instance
        """
        # TODO: Add validation
        return self._obj
