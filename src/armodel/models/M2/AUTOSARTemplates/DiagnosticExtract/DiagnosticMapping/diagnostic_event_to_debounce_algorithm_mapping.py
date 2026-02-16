"""DiagnosticEventToDebounceAlgorithmMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToDebounceAlgorithmMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "debounce": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticDebounce),
        ),  # debounce
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventToDebounceAlgorithmMapping."""
        super().__init__()
        self.debounce: Optional[Any] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None


class DiagnosticEventToDebounceAlgorithmMappingBuilder:
    """Builder for DiagnosticEventToDebounceAlgorithmMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToDebounceAlgorithmMapping = DiagnosticEventToDebounceAlgorithmMapping()

    def build(self) -> DiagnosticEventToDebounceAlgorithmMapping:
        """Build and return DiagnosticEventToDebounceAlgorithmMapping object.

        Returns:
            DiagnosticEventToDebounceAlgorithmMapping instance
        """
        # TODO: Add validation
        return self._obj
