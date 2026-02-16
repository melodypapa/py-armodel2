"""DiagnosticEventToSecurityEventMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToSecurityEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToSecurityEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
        "security_event_context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SecurityEventContext),
        ),  # securityEventContext
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventToSecurityEventMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.security_event_context: Optional[Any] = None


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
