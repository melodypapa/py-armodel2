"""TDEventIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventIPduTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class TDEventIPdu(TDEventCom):
    """AUTOSAR TDEventIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu: Optional[IPdu]
    physical_channel: Optional[PhysicalChannel]
    td_event_type: Optional[TDEventIPduTypeEnum]
    def __init__(self) -> None:
        """Initialize TDEventIPdu."""
        super().__init__()
        self.i_pdu: Optional[IPdu] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type: Optional[TDEventIPduTypeEnum] = None


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
