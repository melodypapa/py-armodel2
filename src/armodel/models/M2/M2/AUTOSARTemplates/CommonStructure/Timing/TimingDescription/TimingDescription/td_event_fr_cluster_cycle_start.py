"""TDEventFrClusterCycleStart AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_cluster import (
    FlexrayCluster,
)


class TDEventFrClusterCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventFrClusterCycleStart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "fr_cluster": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlexrayCluster,
        ),  # frCluster
    }

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
