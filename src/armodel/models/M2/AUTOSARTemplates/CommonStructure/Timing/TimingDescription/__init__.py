"""TimingDescription module."""
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event_chain import (
    TimingDescriptionEventChain,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)

__all__ = [
    "TimingDescription",
    "TimingDescriptionEvent",
    "TimingDescriptionEventChain",
]
