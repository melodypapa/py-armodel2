"""DiagnosticInhibitSourceEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 260)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_FimMapping.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_event_group import (
    DiagnosticFimEventGroup,
)


class DiagnosticInhibitSourceEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticInhibitSourceEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
        "event_group_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticFimEventGroup,
        ),  # eventGroupGroup
        "inhibition_source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticFunction),
        ),  # inhibitionSource
    }

    def __init__(self) -> None:
        """Initialize DiagnosticInhibitSourceEventMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.event_group_group: Optional[DiagnosticFimEventGroup] = None
        self.inhibition_source: Optional[Any] = None


class DiagnosticInhibitSourceEventMappingBuilder:
    """Builder for DiagnosticInhibitSourceEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticInhibitSourceEventMapping = DiagnosticInhibitSourceEventMapping()

    def build(self) -> DiagnosticInhibitSourceEventMapping:
        """Build and return DiagnosticInhibitSourceEventMapping object.

        Returns:
            DiagnosticInhibitSourceEventMapping instance
        """
        # TODO: Add validation
        return self._obj
