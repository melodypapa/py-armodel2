"""TimingDescriptionEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("clock_reference", None, False, False, TimingClock),  # clockReference
        ("occurrence", None, False, False, any (TDEventOccurrence)),  # occurrence
    ]

    def __init__(self) -> None:
        """Initialize TimingDescriptionEvent."""
        super().__init__()
        self.clock_reference: Optional[TimingClock] = None
        self.occurrence: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingDescriptionEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingDescriptionEvent":
        """Create TimingDescriptionEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingDescriptionEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingDescriptionEvent since parent returns ARObject
        return cast("TimingDescriptionEvent", obj)


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
