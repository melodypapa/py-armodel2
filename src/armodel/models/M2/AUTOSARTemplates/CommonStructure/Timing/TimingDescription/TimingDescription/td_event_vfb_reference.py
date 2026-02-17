"""TDEventVfbReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)


class TDEventVfbReference(TDEventVfb):
    """AUTOSAR TDEventVfbReference."""

    referenced_td_event_vfb: Optional[TDEventVfb]
    def __init__(self) -> None:
        """Initialize TDEventVfbReference."""
        super().__init__()
        self.referenced_td_event_vfb: Optional[TDEventVfb] = None


class TDEventVfbReferenceBuilder:
    """Builder for TDEventVfbReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbReference = TDEventVfbReference()

    def build(self) -> TDEventVfbReference:
        """Build and return TDEventVfbReference object.

        Returns:
            TDEventVfbReference instance
        """
        # TODO: Add validation
        return self._obj
