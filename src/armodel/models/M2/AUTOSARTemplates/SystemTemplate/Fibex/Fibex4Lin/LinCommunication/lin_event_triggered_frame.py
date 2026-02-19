"""LinEventTriggeredFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 430)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinEventTriggeredFrame(LinFrame):
    """AUTOSAR LinEventTriggeredFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    collision_schedule: Optional[LinScheduleTable]
    lin_unconditional_frames: list[LinUnconditionalFrame]
    def __init__(self) -> None:
        """Initialize LinEventTriggeredFrame."""
        super().__init__()
        self.collision_schedule: Optional[LinScheduleTable] = None
        self.lin_unconditional_frames: list[LinUnconditionalFrame] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinEventTriggeredFrame":
        """Deserialize XML element to LinEventTriggeredFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinEventTriggeredFrame object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse collision_schedule
        child = ARObject._find_child_element(element, "COLLISION-SCHEDULE")
        if child is not None:
            collision_schedule_value = ARObject._deserialize_by_tag(child, "LinScheduleTable")
            obj.collision_schedule = collision_schedule_value

        # Parse lin_unconditional_frames (list)
        obj.lin_unconditional_frames = []
        for child in ARObject._find_all_child_elements(element, "LIN-UNCONDITIONAL-FRAMES"):
            lin_unconditional_frames_value = ARObject._deserialize_by_tag(child, "LinUnconditionalFrame")
            obj.lin_unconditional_frames.append(lin_unconditional_frames_value)

        return obj



class LinEventTriggeredFrameBuilder:
    """Builder for LinEventTriggeredFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinEventTriggeredFrame = LinEventTriggeredFrame()

    def build(self) -> LinEventTriggeredFrame:
        """Build and return LinEventTriggeredFrame object.

        Returns:
            LinEventTriggeredFrame instance
        """
        # TODO: Add validation
        return self._obj
