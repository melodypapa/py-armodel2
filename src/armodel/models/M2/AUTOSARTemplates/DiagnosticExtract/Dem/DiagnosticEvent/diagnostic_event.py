"""DiagnosticEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import (
    DiagnosticClearEventAllowedBehaviorEnum,
    DiagnosticEventClearAllowedEnum,
    DiagnosticEventKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticEvent(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEvent."""

    associated: Optional[PositiveInteger]
    clear_event: Optional[DiagnosticClearEventAllowedBehaviorEnum]
    confirmation: Optional[PositiveInteger]
    connecteds: list[Any]
    event_clear: Optional[DiagnosticEventClearAllowedEnum]
    event_kind: Optional[DiagnosticEventKindEnum]
    prestorage: Optional[Boolean]
    prestored: Optional[Boolean]
    recoverable_in: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticEvent."""
        super().__init__()
        self.associated: Optional[PositiveInteger] = None
        self.clear_event: Optional[DiagnosticClearEventAllowedBehaviorEnum] = None
        self.confirmation: Optional[PositiveInteger] = None
        self.connecteds: list[Any] = []
        self.event_clear: Optional[DiagnosticEventClearAllowedEnum] = None
        self.event_kind: Optional[DiagnosticEventKindEnum] = None
        self.prestorage: Optional[Boolean] = None
        self.prestored: Optional[Boolean] = None
        self.recoverable_in: Optional[Boolean] = None


class DiagnosticEventBuilder:
    """Builder for DiagnosticEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEvent = DiagnosticEvent()

    def build(self) -> DiagnosticEvent:
        """Build and return DiagnosticEvent object.

        Returns:
            DiagnosticEvent instance
        """
        # TODO: Add validation
        return self._obj
