"""TDEventTTCanCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_cluster import (
    TtcanCluster,
)


class TDEventTTCanCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventTTCanCycleStart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tt_can_cluster: Optional[TtcanCluster]
    def __init__(self) -> None:
        """Initialize TDEventTTCanCycleStart."""
        super().__init__()
        self.tt_can_cluster: Optional[TtcanCluster] = None


class TDEventTTCanCycleStartBuilder:
    """Builder for TDEventTTCanCycleStart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventTTCanCycleStart = TDEventTTCanCycleStart()

    def build(self) -> TDEventTTCanCycleStart:
        """Build and return TDEventTTCanCycleStart object.

        Returns:
            TDEventTTCanCycleStart instance
        """
        # TODO: Add validation
        return self._obj
