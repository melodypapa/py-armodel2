"""ExternalTriggerOccurredEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class ExternalTriggerOccurredEvent(RTEEvent):
    """AUTOSAR ExternalTriggerOccurredEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("trigger", None, False, False, Trigger),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize ExternalTriggerOccurredEvent."""
        super().__init__()
        self.trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExternalTriggerOccurredEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExternalTriggerOccurredEvent":
        """Create ExternalTriggerOccurredEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExternalTriggerOccurredEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExternalTriggerOccurredEvent since parent returns ARObject
        return cast("ExternalTriggerOccurredEvent", obj)


class ExternalTriggerOccurredEventBuilder:
    """Builder for ExternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggerOccurredEvent = ExternalTriggerOccurredEvent()

    def build(self) -> ExternalTriggerOccurredEvent:
        """Build and return ExternalTriggerOccurredEvent object.

        Returns:
            ExternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
