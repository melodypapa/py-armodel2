"""DiagnosticAuthenticationConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)


class DiagnosticAuthenticationConfiguration(DiagnosticAuthentication):
    """AUTOSAR DiagnosticAuthenticationConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthenticationConfiguration."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthenticationConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthenticationConfiguration":
        """Create DiagnosticAuthenticationConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthenticationConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthenticationConfiguration since parent returns ARObject
        return cast("DiagnosticAuthenticationConfiguration", obj)


class DiagnosticAuthenticationConfigurationBuilder:
    """Builder for DiagnosticAuthenticationConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthenticationConfiguration = DiagnosticAuthenticationConfiguration()

    def build(self) -> DiagnosticAuthenticationConfiguration:
        """Build and return DiagnosticAuthenticationConfiguration object.

        Returns:
            DiagnosticAuthenticationConfiguration instance
        """
        # TODO: Add validation
        return self._obj
