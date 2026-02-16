"""DiagnosticAuthenticationClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticAuthenticationClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticAuthenticationClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthenticationClass."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthenticationClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthenticationClass":
        """Create DiagnosticAuthenticationClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthenticationClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthenticationClass since parent returns ARObject
        return cast("DiagnosticAuthenticationClass", obj)


class DiagnosticAuthenticationClassBuilder:
    """Builder for DiagnosticAuthenticationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthenticationClass = DiagnosticAuthenticationClass()

    def build(self) -> DiagnosticAuthenticationClass:
        """Build and return DiagnosticAuthenticationClass object.

        Returns:
            DiagnosticAuthenticationClass instance
        """
        # TODO: Add validation
        return self._obj
