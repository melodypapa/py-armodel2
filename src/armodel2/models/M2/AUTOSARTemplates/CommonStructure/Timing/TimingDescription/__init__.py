"""TimingDescription module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event_chain import (
        TimingDescriptionEventChain,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
        TimingDescription,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
        TimingDescriptionEvent,
    )

__all__ = [
    "TimingDescription",
    "TimingDescriptionEvent",
    "TimingDescriptionEventChain",
]
