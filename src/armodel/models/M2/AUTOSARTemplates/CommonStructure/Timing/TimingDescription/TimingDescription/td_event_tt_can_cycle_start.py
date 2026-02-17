"""TDEventTTCanCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_cluster import (
    TtcanCluster,
)


class TDEventTTCanCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventTTCanCycleStart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tt_can_cluster": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TtcanCluster,
        ),  # ttCanCluster
    }

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
