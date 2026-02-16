"""BswExternalTriggerOccurredEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    """AUTOSAR BswExternalTriggerOccurredEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("trigger", None, False, False, Trigger),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize BswExternalTriggerOccurredEvent."""
        super().__init__()
        self.trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswExternalTriggerOccurredEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswExternalTriggerOccurredEvent":
        """Create BswExternalTriggerOccurredEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswExternalTriggerOccurredEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswExternalTriggerOccurredEvent since parent returns ARObject
        return cast("BswExternalTriggerOccurredEvent", obj)


class BswExternalTriggerOccurredEventBuilder:
    """Builder for BswExternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswExternalTriggerOccurredEvent = BswExternalTriggerOccurredEvent()

    def build(self) -> BswExternalTriggerOccurredEvent:
        """Build and return BswExternalTriggerOccurredEvent object.

        Returns:
            BswExternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
