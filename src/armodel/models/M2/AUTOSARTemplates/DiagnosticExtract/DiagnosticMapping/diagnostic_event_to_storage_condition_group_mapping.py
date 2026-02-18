"""DiagnosticEventToStorageConditionGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 248)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToStorageConditionGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToStorageConditionGroupMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    storage: Optional[Any]
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
