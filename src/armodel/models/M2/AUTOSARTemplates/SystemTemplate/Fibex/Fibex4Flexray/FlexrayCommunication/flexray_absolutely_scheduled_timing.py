"""FlexrayAbsolutelyScheduledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR FlexrayAbsolutelyScheduledTiming."""

    communication_cycle_cycle: Optional[CommunicationCycle]
    slot_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize FlexrayAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.slot_id: Optional[PositiveInteger] = None


class FlexrayAbsolutelyScheduledTimingBuilder:
    """Builder for FlexrayAbsolutelyScheduledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayAbsolutelyScheduledTiming = FlexrayAbsolutelyScheduledTiming()

    def build(self) -> FlexrayAbsolutelyScheduledTiming:
        """Build and return FlexrayAbsolutelyScheduledTiming object.

        Returns:
            FlexrayAbsolutelyScheduledTiming instance
        """
        # TODO: Add validation
        return self._obj
