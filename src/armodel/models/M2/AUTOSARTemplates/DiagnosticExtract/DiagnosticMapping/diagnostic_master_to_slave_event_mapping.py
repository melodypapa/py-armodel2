"""DiagnosticMasterToSlaveEventMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticMasterToSlaveEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticMasterToSlaveEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "master_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # masterEvent
        "slave_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # slaveEvent
    }

    def __init__(self) -> None:
        """Initialize DiagnosticMasterToSlaveEventMapping."""
        super().__init__()
        self.master_event: Optional[DiagnosticEvent] = None
        self.slave_event: Optional[DiagnosticEvent] = None


class DiagnosticMasterToSlaveEventMappingBuilder:
    """Builder for DiagnosticMasterToSlaveEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMasterToSlaveEventMapping = DiagnosticMasterToSlaveEventMapping()

    def build(self) -> DiagnosticMasterToSlaveEventMapping:
        """Build and return DiagnosticMasterToSlaveEventMapping object.

        Returns:
            DiagnosticMasterToSlaveEventMapping instance
        """
        # TODO: Add validation
        return self._obj
