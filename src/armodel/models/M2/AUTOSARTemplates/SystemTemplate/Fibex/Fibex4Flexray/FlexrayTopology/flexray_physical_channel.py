"""FlexrayPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class FlexrayPhysicalChannel(PhysicalChannel):
    """AUTOSAR FlexrayPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "channel_name": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlexrayChannelName,
        ),  # channelName
    }

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
