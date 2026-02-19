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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventTTCanCycleStart":
        """Deserialize XML element to TDEventTTCanCycleStart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventTTCanCycleStart object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tt_can_cluster
        child = ARObject._find_child_element(element, "TT-CAN-CLUSTER")
        if child is not None:
            tt_can_cluster_value = ARObject._deserialize_by_tag(child, "TtcanCluster")
            obj.tt_can_cluster = tt_can_cluster_value

        return obj



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
