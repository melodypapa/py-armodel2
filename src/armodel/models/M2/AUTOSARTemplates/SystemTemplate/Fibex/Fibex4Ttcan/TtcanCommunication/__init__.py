"""TtcanCommunication module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication.ttcan_absolutely_scheduled_timing import (
        TtcanAbsolutelyScheduledTiming,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication.ttcan_trigger_type import (
    TtcanTriggerType,
)

__all__ = [
    "TtcanAbsolutelyScheduledTiming",
    "TtcanTriggerType",
]
