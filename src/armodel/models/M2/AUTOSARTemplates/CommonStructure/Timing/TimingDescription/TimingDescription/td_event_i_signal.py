"""TDEventISignal AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "i_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignal,
        ),  # iSignal
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
            element_class=TDEventISignalTypeEnum,
        ),  # tdEventTypeEnum
    }

    def __init__(self) -> None:
        """Initialize TDEventISignal."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type_enum: Optional[TDEventISignalTypeEnum] = None


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
