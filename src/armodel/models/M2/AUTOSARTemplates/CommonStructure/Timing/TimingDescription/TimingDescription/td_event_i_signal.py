"""TDEventISignal AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventISignal(TDEventCom):
    """AUTOSAR TDEventISignal."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_signal", None, False, False, ISignal),  # iSignal
        ("physical_channel", None, False, False, PhysicalChannel),  # physicalChannel
        ("td_event_type_enum", None, False, False, TDEventISignalTypeEnum),  # tdEventTypeEnum
    ]

    def __init__(self) -> None:
        """Initialize TDEventISignal."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type_enum: Optional[TDEventISignalTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventISignal to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventISignal":
        """Create TDEventISignal from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventISignal instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventISignal since parent returns ARObject
        return cast("TDEventISignal", obj)


class TDEventISignalBuilder:
    """Builder for TDEventISignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventISignal = TDEventISignal()

    def build(self) -> TDEventISignal:
        """Build and return TDEventISignal object.

        Returns:
            TDEventISignal instance
        """
        # TODO: Add validation
        return self._obj
