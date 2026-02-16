"""TDEventFrClusterCycleStart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_cluster import (
    FlexrayCluster,
)


class TDEventFrClusterCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventFrClusterCycleStart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("fr_cluster", None, False, False, FlexrayCluster),  # frCluster
    ]

    def __init__(self) -> None:
        """Initialize TDEventFrClusterCycleStart."""
        super().__init__()
        self.fr_cluster: Optional[FlexrayCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventFrClusterCycleStart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrClusterCycleStart":
        """Create TDEventFrClusterCycleStart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventFrClusterCycleStart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventFrClusterCycleStart since parent returns ARObject
        return cast("TDEventFrClusterCycleStart", obj)


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
