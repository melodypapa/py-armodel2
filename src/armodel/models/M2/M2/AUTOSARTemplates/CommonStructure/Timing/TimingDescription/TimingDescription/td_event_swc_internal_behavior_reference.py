"""TDEventSwcInternalBehaviorReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
    TDEventSwc,
)


class TDEventSwcInternalBehaviorReference(TDEventSwc):
    """AUTOSAR TDEventSwcInternalBehaviorReference."""

    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehaviorReference."""
        super().__init__()
        self.referenced_td_event_swc: Optional[TDEventSwc] = None


class TDEventSwcInternalBehaviorReferenceBuilder:
    """Builder for TDEventSwcInternalBehaviorReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwcInternalBehaviorReference = TDEventSwcInternalBehaviorReference()

    def build(self) -> TDEventSwcInternalBehaviorReference:
        """Build and return TDEventSwcInternalBehaviorReference object.

        Returns:
            TDEventSwcInternalBehaviorReference instance
        """
        # TODO: Add validation
        return self._obj
