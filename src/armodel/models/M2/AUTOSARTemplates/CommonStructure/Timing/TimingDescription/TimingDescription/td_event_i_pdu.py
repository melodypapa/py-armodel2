"""TDEventIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventIPdu(TDEventCom):
    """AUTOSAR TDEventIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_pdu", None, False, False, IPdu),  # iPdu
        ("physical_channel", None, False, False, PhysicalChannel),  # physicalChannel
        ("td_event_type", None, False, False, TDEventIPduTypeEnum),  # tdEventType
    ]

    def __init__(self) -> None:
        """Initialize TDEventIPdu."""
        super().__init__()
        self.i_pdu: Optional[IPdu] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type: Optional[TDEventIPduTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventIPdu":
        """Create TDEventIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventIPdu since parent returns ARObject
        return cast("TDEventIPdu", obj)


class TDEventIPduBuilder:
    """Builder for TDEventIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventIPdu = TDEventIPdu()

    def build(self) -> TDEventIPdu:
        """Build and return TDEventIPdu object.

        Returns:
            TDEventIPdu instance
        """
        # TODO: Add validation
        return self._obj
