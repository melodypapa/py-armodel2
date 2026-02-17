"""FlexrayFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_absolutely_scheduled_timing import (
    FlexrayAbsolutelyScheduledTiming,
)


class FlexrayFrameTriggering(FrameTriggering):
    """AUTOSAR FlexrayFrameTriggering."""

    absolutelies: list[FlexrayAbsolutelyScheduledTiming]
    allow_dynamic: Optional[Boolean]
    message_id: Optional[PositiveInteger]
    payload_preamble: Optional[Any]
    def __init__(self) -> None:
        """Initialize FlexrayFrameTriggering."""
        super().__init__()
        self.absolutelies: list[FlexrayAbsolutelyScheduledTiming] = []
        self.allow_dynamic: Optional[Boolean] = None
        self.message_id: Optional[PositiveInteger] = None
        self.payload_preamble: Optional[Any] = None


class FlexrayFrameTriggeringBuilder:
    """Builder for FlexrayFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFrameTriggering = FlexrayFrameTriggering()

    def build(self) -> FlexrayFrameTriggering:
        """Build and return FlexrayFrameTriggering object.

        Returns:
            FlexrayFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
