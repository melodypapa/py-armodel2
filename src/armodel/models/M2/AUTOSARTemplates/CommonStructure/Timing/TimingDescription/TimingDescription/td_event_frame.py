"""TDEventFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventFrameTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventFrame(TDEventCom):
    """AUTOSAR TDEventFrame."""

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
