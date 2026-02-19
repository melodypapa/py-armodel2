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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    frame: Optional[Frame]
    physical_channel: Optional[PhysicalChannel]
    td_event_type_enum: Optional[TDEventFrameTypeEnum]
    def __init__(self) -> None:
        """Initialize TDEventFrame."""
        super().__init__()
        self.frame: Optional[Frame] = None
        self.physical_channel: Optional[PhysicalChannel] = None
        self.td_event_type_enum: Optional[TDEventFrameTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrame":
        """Deserialize XML element to TDEventFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventFrame, cls).deserialize(element)

        # Parse frame
        child = ARObject._find_child_element(element, "FRAME")
        if child is not None:
            frame_value = ARObject._deserialize_by_tag(child, "Frame")
            obj.frame = frame_value

        # Parse physical_channel
        child = ARObject._find_child_element(element, "PHYSICAL-CHANNEL")
        if child is not None:
            physical_channel_value = ARObject._deserialize_by_tag(child, "PhysicalChannel")
            obj.physical_channel = physical_channel_value

        # Parse td_event_type_enum
        child = ARObject._find_child_element(element, "TD-EVENT-TYPE-ENUM")
        if child is not None:
            td_event_type_enum_value = TDEventFrameTypeEnum.deserialize(child)
            obj.td_event_type_enum = td_event_type_enum_value

        return obj



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
