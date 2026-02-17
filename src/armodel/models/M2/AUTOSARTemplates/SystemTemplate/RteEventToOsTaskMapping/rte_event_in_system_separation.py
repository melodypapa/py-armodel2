"""RteEventInSystemSeparation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 214)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInSystemSeparation(Identifiable):
    """AUTOSAR RteEventInSystemSeparation."""

    def __init__(self) -> None:
        """Initialize RteEventInSystemSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []


class RteEventInSystemSeparationBuilder:
    """Builder for RteEventInSystemSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInSystemSeparation = RteEventInSystemSeparation()

    def build(self) -> RteEventInSystemSeparation:
        """Build and return RteEventInSystemSeparation object.

        Returns:
            RteEventInSystemSeparation instance
        """
        # TODO: Add validation
        return self._obj
