"""DiagnosticEventToSecurityEventMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToSecurityEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToSecurityEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("security_event_context", None, False, False, any (SecurityEventContext)),  # securityEventContext
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventToSecurityEventMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.security_event_context: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventToSecurityEventMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToSecurityEventMapping":
        """Create DiagnosticEventToSecurityEventMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventToSecurityEventMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventToSecurityEventMapping since parent returns ARObject
        return cast("DiagnosticEventToSecurityEventMapping", obj)


class DiagnosticEventToSecurityEventMappingBuilder:
    """Builder for DiagnosticEventToSecurityEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToSecurityEventMapping = DiagnosticEventToSecurityEventMapping()

    def build(self) -> DiagnosticEventToSecurityEventMapping:
        """Build and return DiagnosticEventToSecurityEventMapping object.

        Returns:
            DiagnosticEventToSecurityEventMapping instance
        """
        # TODO: Add validation
        return self._obj
