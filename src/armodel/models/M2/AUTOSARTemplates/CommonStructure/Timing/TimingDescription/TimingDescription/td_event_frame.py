"""TDEventFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventFrame(TDEventCom):
    """AUTOSAR TDEventFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("frame", None, False, False, Frame),  # frame
        ("physical_channel", None, False, False, PhysicalChannel),  # physicalChannel
        ("td_event_type_enum", None, False, False, TDEventFrameTypeEnum),  # tdEventTypeEnum
    ]

    def __init__(self) -> None:
        """Initialize TDEventFrame."""
        super().__init__()
        self.frame: Optional[Frame] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type_enum: Optional[TDEventFrameTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrame":
        """Create TDEventFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventFrame since parent returns ARObject
        return cast("TDEventFrame", obj)


class TDEventFrameBuilder:
    """Builder for TDEventFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventFrame = TDEventFrame()

    def build(self) -> TDEventFrame:
        """Build and return TDEventFrame object.

        Returns:
            TDEventFrame instance
        """
        # TODO: Add validation
        return self._obj
