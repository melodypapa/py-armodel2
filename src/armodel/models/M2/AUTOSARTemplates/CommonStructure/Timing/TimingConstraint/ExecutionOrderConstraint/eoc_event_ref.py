"""EOCEventRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 120)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)


class EOCEventRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCEventRef."""

    def __init__(self) -> None:
        """Initialize EOCEventRef."""
        super().__init__()
        self.bsw_module: Optional[BswImplementation] = None
        self.component: Optional[Any] = None
        self.event: Optional[AbstractEvent] = None
        self.successors: list[Any] = []


class EOCEventRefBuilder:
    """Builder for EOCEventRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCEventRef = EOCEventRef()

    def build(self) -> EOCEventRef:
        """Build and return EOCEventRef object.

        Returns:
            EOCEventRef instance
        """
        # TODO: Add validation
        return self._obj
