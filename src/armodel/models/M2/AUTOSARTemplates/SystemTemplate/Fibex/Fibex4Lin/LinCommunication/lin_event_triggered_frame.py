"""LinEventTriggeredFrame AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinEventTriggeredFrame(LinFrame):
    """AUTOSAR LinEventTriggeredFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "collision_schedule": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LinScheduleTable,
        ),  # collisionSchedule
        "lin_unconditional_frames": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LinUnconditionalFrame,
        ),  # linUnconditionalFrames
    }

    def __init__(self) -> None:
        """Initialize LinEventTriggeredFrame."""
        super().__init__()
        self.collision_schedule: Optional[LinScheduleTable] = None
        self.lin_unconditional_frames: list[LinUnconditionalFrame] = []


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
