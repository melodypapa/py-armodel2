"""EventTriggeringConstraint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class EventTriggeringConstraint(TimingConstraint):
    """AUTOSAR EventTriggeringConstraint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event", None, False, False, TimingDescriptionEvent),  # event
    ]

    def __init__(self) -> None:
        """Initialize EventTriggeringConstraint."""
        super().__init__()
        self.event: Optional[TimingDescriptionEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EventTriggeringConstraint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventTriggeringConstraint":
        """Create EventTriggeringConstraint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EventTriggeringConstraint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EventTriggeringConstraint since parent returns ARObject
        return cast("EventTriggeringConstraint", obj)


class EventTriggeringConstraintBuilder:
    """Builder for EventTriggeringConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventTriggeringConstraint = EventTriggeringConstraint()

    def build(self) -> EventTriggeringConstraint:
        """Build and return EventTriggeringConstraint object.

        Returns:
            EventTriggeringConstraint instance
        """
        # TODO: Add validation
        return self._obj
