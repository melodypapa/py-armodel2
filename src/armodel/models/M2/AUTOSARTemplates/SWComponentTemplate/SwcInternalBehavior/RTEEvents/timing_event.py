"""TimingEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TimingEvent(RTEEvent):
    """AUTOSAR TimingEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("offset", None, True, False, None),  # offset
        ("period", None, True, False, None),  # period
    ]

    def __init__(self) -> None:
        """Initialize TimingEvent."""
        super().__init__()
        self.offset: Optional[TimeValue] = None
        self.period: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimingEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingEvent":
        """Create TimingEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimingEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimingEvent since parent returns ARObject
        return cast("TimingEvent", obj)


class TimingEventBuilder:
    """Builder for TimingEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingEvent = TimingEvent()

    def build(self) -> TimingEvent:
        """Build and return TimingEvent object.

        Returns:
            TimingEvent instance
        """
        # TODO: Add validation
        return self._obj
