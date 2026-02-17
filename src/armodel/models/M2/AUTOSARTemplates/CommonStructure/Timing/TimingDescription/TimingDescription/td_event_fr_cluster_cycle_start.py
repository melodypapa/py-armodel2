"""TDEventFrClusterCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_cluster import (
    FlexrayCluster,
)


class TDEventFrClusterCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventFrClusterCycleStart."""

    def __init__(self) -> None:
        """Initialize TDEventFrClusterCycleStart."""
        super().__init__()
        self.fr_cluster: Optional[FlexrayCluster] = None


class TDEventFrClusterCycleStartBuilder:
    """Builder for TDEventFrClusterCycleStart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventFrClusterCycleStart = TDEventFrClusterCycleStart()

    def build(self) -> TDEventFrClusterCycleStart:
        """Build and return TDEventFrClusterCycleStart object.

        Returns:
            TDEventFrClusterCycleStart instance
        """
        # TODO: Add validation
        return self._obj
