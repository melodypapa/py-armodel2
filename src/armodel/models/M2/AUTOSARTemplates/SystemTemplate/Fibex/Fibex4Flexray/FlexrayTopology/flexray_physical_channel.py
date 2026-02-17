"""FlexrayPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayChannelName,
)


class FlexrayPhysicalChannel(PhysicalChannel):
    """AUTOSAR FlexrayPhysicalChannel."""

    channel_name: Optional[FlexrayChannelName]
    def __init__(self) -> None:
        """Initialize FlexrayPhysicalChannel."""
        super().__init__()
        self.channel_name: Optional[FlexrayChannelName] = None


class FlexrayPhysicalChannelBuilder:
    """Builder for FlexrayPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayPhysicalChannel = FlexrayPhysicalChannel()

    def build(self) -> FlexrayPhysicalChannel:
        """Build and return FlexrayPhysicalChannel object.

        Returns:
            FlexrayPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
