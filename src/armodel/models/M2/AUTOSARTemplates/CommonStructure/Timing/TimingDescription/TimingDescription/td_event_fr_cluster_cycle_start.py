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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_cluster import (
    FlexrayCluster,
)


class TDEventFrClusterCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventFrClusterCycleStart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fr_cluster: Optional[FlexrayCluster]
    def __init__(self) -> None:
        """Initialize TDEventFrClusterCycleStart."""
        super().__init__()
        self.fr_cluster: Optional[FlexrayCluster] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrClusterCycleStart":
        """Deserialize XML element to TDEventFrClusterCycleStart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventFrClusterCycleStart object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse fr_cluster
        child = ARObject._find_child_element(element, "FR-CLUSTER")
        if child is not None:
            fr_cluster_value = ARObject._deserialize_by_tag(child, "FlexrayCluster")
            obj.fr_cluster = fr_cluster_value

        return obj



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
