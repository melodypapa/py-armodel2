"""DiagnosticEventToTroubleCodeJ1939Mapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToTroubleCodeJ1939Mapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
        "trouble_code": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTroubleCode,
        ),  # troubleCode
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventToTroubleCodeJ1939Mapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.trouble_code: Optional[DiagnosticTroubleCode] = None


class DiagnosticEventToTroubleCodeJ1939MappingBuilder:
    """Builder for DiagnosticEventToTroubleCodeJ1939Mapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToTroubleCodeJ1939Mapping = DiagnosticEventToTroubleCodeJ1939Mapping()

    def build(self) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        """Build and return DiagnosticEventToTroubleCodeJ1939Mapping object.

        Returns:
            DiagnosticEventToTroubleCodeJ1939Mapping instance
        """
        # TODO: Add validation
        return self._obj
