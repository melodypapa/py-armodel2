"""TimingClockSyncAccuracy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accuracy", None, False, False, MultidimensionalTime),  # accuracy
        ("lower", None, False, False, TimingClock),  # lower
        ("upper", None, False, False, TimingClock),  # upper
    ]

    def __init__(self) -> None:
        """Initialize TimingClockSyncAccuracy."""
        super().__init__()
        self.accuracy: Optional[MultidimensionalTime] = None
        self.lower: Optional[TimingClock] = None
        self.upper: Optional[TimingClock] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingClockSyncAccuracy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingClockSyncAccuracy":
        """Create TimingClockSyncAccuracy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingClockSyncAccuracy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingClockSyncAccuracy since parent returns ARObject
        return cast("TimingClockSyncAccuracy", obj)


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
