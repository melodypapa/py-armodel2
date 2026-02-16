"""InternalTriggerOccurredEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.internal_triggering_point import (
    InternalTriggeringPoint,
)


class InternalTriggerOccurredEvent(RTEEvent):
    """AUTOSAR InternalTriggerOccurredEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_source", None, False, False, InternalTriggeringPoint),  # eventSource
    ]

    def __init__(self) -> None:
        """Initialize InternalTriggerOccurredEvent."""
        super().__init__()
        self.event_source: Optional[InternalTriggeringPoint] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InternalTriggerOccurredEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalTriggerOccurredEvent":
        """Create InternalTriggerOccurredEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InternalTriggerOccurredEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InternalTriggerOccurredEvent since parent returns ARObject
        return cast("InternalTriggerOccurredEvent", obj)


class InternalTriggerOccurredEventBuilder:
    """Builder for InternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalTriggerOccurredEvent = InternalTriggerOccurredEvent()

    def build(self) -> InternalTriggerOccurredEvent:
        """Build and return InternalTriggerOccurredEvent object.

        Returns:
            InternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
