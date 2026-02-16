"""TimingDescriptionEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)


class TimingDescriptionEvent(TimingDescription):
    """AUTOSAR TimingDescriptionEvent."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "clock_reference": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingClock,
        ),  # clockReference
        "occurrence": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (TDEventOccurrence),
        ),  # occurrence
    }

    def __init__(self) -> None:
        """Initialize TimingDescriptionEvent."""
        super().__init__()
        self.clock_reference: Optional[TimingClock] = None
        self.occurrence: Optional[Any] = None


class TimingDescriptionEventBuilder:
    """Builder for TimingDescriptionEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEvent = TimingDescriptionEvent()

    def build(self) -> TimingDescriptionEvent:
        """Build and return TimingDescriptionEvent object.

        Returns:
            TimingDescriptionEvent instance
        """
        # TODO: Add validation
        return self._obj
