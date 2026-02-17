"""DiagnosticEventToStorageConditionGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 248)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToStorageConditionGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToStorageConditionGroupMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
        "storage": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticStorage),
        ),  # storage
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventToStorageConditionGroupMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.storage: Optional[Any] = None


class DiagnosticEventToStorageConditionGroupMappingBuilder:
    """Builder for DiagnosticEventToStorageConditionGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToStorageConditionGroupMapping = DiagnosticEventToStorageConditionGroupMapping()

    def build(self) -> DiagnosticEventToStorageConditionGroupMapping:
        """Build and return DiagnosticEventToStorageConditionGroupMapping object.

        Returns:
            DiagnosticEventToStorageConditionGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
