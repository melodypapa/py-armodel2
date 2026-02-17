"""FlexrayCommunication module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_frame import (
        FlexrayFrame,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_frame_triggering import (
        FlexrayFrameTriggering,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_absolutely_scheduled_timing import (
        FlexrayAbsolutelyScheduledTiming,
    )

__all__ = [
    "FlexrayAbsolutelyScheduledTiming",
    "FlexrayFrame",
    "FlexrayFrameTriggering",
]
