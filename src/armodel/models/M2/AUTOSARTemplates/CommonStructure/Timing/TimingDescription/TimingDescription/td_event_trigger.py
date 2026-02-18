"""TDEventTrigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 58)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventTriggerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TDEventTrigger(TDEventVfbPort):
    """AUTOSAR TDEventTrigger."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    td_event_trigger: Optional[TDEventTriggerTypeEnum]
    trigger: Optional[Trigger]
    def __init__(self) -> None:
        """Initialize TDEventTrigger."""
        super().__init__()
        self.td_event_trigger: Optional[TDEventTriggerTypeEnum] = None
        self.trigger: Optional[Trigger] = None


class TDEventTriggerBuilder:
    """Builder for TDEventTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventTrigger = TDEventTrigger()

    def build(self) -> TDEventTrigger:
        """Build and return TDEventTrigger object.

        Returns:
            TDEventTrigger instance
        """
        # TODO: Add validation
        return self._obj
