"""TimingClockSyncAccuracy AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)


class TimingClockSyncAccuracy(Identifiable):
    """AUTOSAR TimingClockSyncAccuracy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "accuracy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultidimensionalTime,
        ),  # accuracy
        "lower": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingClock,
        ),  # lower
        "upper": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingClock,
        ),  # upper
    }

    def __init__(self) -> None:
        """Initialize TimingClockSyncAccuracy."""
        super().__init__()
        self.accuracy: Optional[MultidimensionalTime] = None
        self.lower: Optional[TimingClock] = None
        self.upper: Optional[TimingClock] = None


class TimingClockSyncAccuracyBuilder:
    """Builder for TimingClockSyncAccuracy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingClockSyncAccuracy = TimingClockSyncAccuracy()

    def build(self) -> TimingClockSyncAccuracy:
        """Build and return TimingClockSyncAccuracy object.

        Returns:
            TimingClockSyncAccuracy instance
        """
        # TODO: Add validation
        return self._obj
