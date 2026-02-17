"""DiagnosticEventToEnableConditionGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 247)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToEnableConditionGroupMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
        "enable_condition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # enableCondition
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventToEnableConditionGroupMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.enable_condition: Optional[Any] = None


class DiagnosticEventToEnableConditionGroupMappingBuilder:
    """Builder for DiagnosticEventToEnableConditionGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToEnableConditionGroupMapping = DiagnosticEventToEnableConditionGroupMapping()

    def build(self) -> DiagnosticEventToEnableConditionGroupMapping:
        """Build and return DiagnosticEventToEnableConditionGroupMapping object.

        Returns:
            DiagnosticEventToEnableConditionGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
