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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinEventTriggeredFrame(LinFrame):
    """AUTOSAR LinEventTriggeredFrame."""

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
