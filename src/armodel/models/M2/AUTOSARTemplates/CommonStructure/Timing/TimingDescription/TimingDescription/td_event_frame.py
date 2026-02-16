"""TDEventFrame AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Frame,
        ),  # frame
        "physical_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PhysicalChannel,
        ),  # physicalChannel
        "td_event_type_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TDEventFrameTypeEnum,
        ),  # tdEventTypeEnum
    }

    def __init__(self) -> None:
        """Initialize TDEventFrame."""
        super().__init__()
        self.frame: Optional[Frame] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type_enum: Optional[TDEventFrameTypeEnum] = None


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
