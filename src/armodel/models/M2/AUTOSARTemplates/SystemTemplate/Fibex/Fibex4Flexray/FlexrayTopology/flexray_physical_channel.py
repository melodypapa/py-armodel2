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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayChannelName,
)


class FlexrayPhysicalChannel(PhysicalChannel):
    """AUTOSAR FlexrayPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    channel_name: Optional[FlexrayChannelName]
    def __init__(self) -> None:
        """Initialize FlexrayPhysicalChannel."""
        super().__init__()
        self.channel_name: Optional[FlexrayChannelName] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayPhysicalChannel":
        """Deserialize XML element to FlexrayPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayPhysicalChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse channel_name
        child = ARObject._find_child_element(element, "CHANNEL-NAME")
        if child is not None:
            channel_name_value = child.text
            obj.channel_name = channel_name_value

        return obj



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
