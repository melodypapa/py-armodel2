"""DiagnosticResponseOnEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_event_window import (
    DiagnosticEventWindow,
)


class DiagnosticResponseOnEvent(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticResponseOnEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_windows": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticEventWindow,
        ),  # eventWindows
        "response_on": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticResponseOn),
        ),  # responseOn
    }

    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEvent."""
        super().__init__()
        self.event_windows: list[DiagnosticEventWindow] = []
        self.response_on: Optional[Any] = None


class DiagnosticResponseOnEventBuilder:
    """Builder for DiagnosticResponseOnEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticResponseOnEvent = DiagnosticResponseOnEvent()

    def build(self) -> DiagnosticResponseOnEvent:
        """Build and return DiagnosticResponseOnEvent object.

        Returns:
            DiagnosticResponseOnEvent instance
        """
        # TODO: Add validation
        return self._obj
