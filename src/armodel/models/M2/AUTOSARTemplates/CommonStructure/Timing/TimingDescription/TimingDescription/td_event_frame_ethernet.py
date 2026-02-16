"""TDEventFrameEthernet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
    StaticSocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_frame_ethernet import (
    TDEventFrameEthernet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_header_id_range import (
    TDHeaderIdRange,
)


class TDEventFrameEthernet(TDEventCom):
    """AUTOSAR TDEventFrameEthernet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("static_socket", None, False, False, StaticSocketConnection),  # staticSocket
        ("td_event_type", None, False, False, TDEventFrameEthernet),  # tdEventType
        ("td_header_id_filters", None, False, True, TDHeaderIdRange),  # tdHeaderIdFilters
        ("td_pdu_triggerings", None, False, True, PduTriggering),  # tdPduTriggerings
    ]

    def __init__(self) -> None:
        """Initialize TDEventFrameEthernet."""
        super().__init__()
        self.static_socket: Optional[StaticSocketConnection] = None
        self.td_event_type: Optional[TDEventFrameEthernet] = None
        self.td_header_id_filters: list[TDHeaderIdRange] = []
        self.td_pdu_triggerings: list[PduTriggering] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventFrameEthernet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrameEthernet":
        """Create TDEventFrameEthernet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventFrameEthernet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventFrameEthernet since parent returns ARObject
        return cast("TDEventFrameEthernet", obj)


class TDEventFrameEthernetBuilder:
    """Builder for TDEventFrameEthernet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventFrameEthernet = TDEventFrameEthernet()

    def build(self) -> TDEventFrameEthernet:
        """Build and return TDEventFrameEthernet object.

        Returns:
            TDEventFrameEthernet instance
        """
        # TODO: Add validation
        return self._obj
