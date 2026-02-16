"""DiagnosticAuthentication AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticAuthentication(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticAuthentication."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentication", None, False, False, any (Diagnostic)),  # authentication
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthentication."""
        super().__init__()
        self.authentication: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthentication to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthentication":
        """Create DiagnosticAuthentication from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthentication instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthentication since parent returns ARObject
        return cast("DiagnosticAuthentication", obj)


class DiagnosticAuthenticationBuilder:
    """Builder for DiagnosticAuthentication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthentication = DiagnosticAuthentication()

    def build(self) -> DiagnosticAuthentication:
        """Build and return DiagnosticAuthentication object.

        Returns:
            DiagnosticAuthentication instance
        """
        # TODO: Add validation
        return self._obj
