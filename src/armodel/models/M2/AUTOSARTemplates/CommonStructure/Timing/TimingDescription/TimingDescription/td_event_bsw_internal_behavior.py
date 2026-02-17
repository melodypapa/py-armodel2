"""TDEventBswInternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)


class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """AUTOSAR TDEventBswInternalBehavior."""

    bsw_module_entity_entity: Optional[BswModuleEntity]
    td_event_bsw_behavior_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventBswInternalBehavior."""
        super().__init__()
        self.bsw_module_entity_entity: Optional[BswModuleEntity] = None
        self.td_event_bsw_behavior_type: Optional[Any] = None


class TDEventBswInternalBehaviorBuilder:
    """Builder for TDEventBswInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswInternalBehavior = TDEventBswInternalBehavior()

    def build(self) -> TDEventBswInternalBehavior:
        """Build and return TDEventBswInternalBehavior object.

        Returns:
            TDEventBswInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
