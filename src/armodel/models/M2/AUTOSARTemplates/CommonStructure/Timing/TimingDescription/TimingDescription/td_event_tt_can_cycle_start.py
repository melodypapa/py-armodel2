"""TDEventTTCanCycleStart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_cycle_start import (
    TDEventCycleStart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanTopology.ttcan_cluster import (
    TtcanCluster,
)


class TDEventTTCanCycleStart(TDEventCycleStart):
    """AUTOSAR TDEventTTCanCycleStart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tt_can_cluster", None, False, False, TtcanCluster),  # ttCanCluster
    ]

    def __init__(self) -> None:
        """Initialize TDEventTTCanCycleStart."""
        super().__init__()
        self.tt_can_cluster: Optional[TtcanCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventTTCanCycleStart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventTTCanCycleStart":
        """Create TDEventTTCanCycleStart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventTTCanCycleStart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventTTCanCycleStart since parent returns ARObject
        return cast("TDEventTTCanCycleStart", obj)


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
