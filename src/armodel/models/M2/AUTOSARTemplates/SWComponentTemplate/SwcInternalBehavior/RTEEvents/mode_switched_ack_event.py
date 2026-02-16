"""ModeSwitchedAckEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_switch_point import (
    ModeSwitchPoint,
)


class ModeSwitchedAckEvent(RTEEvent):
    """AUTOSAR ModeSwitchedAckEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_source", None, False, False, ModeSwitchPoint),  # eventSource
    ]

    def __init__(self) -> None:
        """Initialize ModeSwitchedAckEvent."""
        super().__init__()
        self.event_source: Optional[ModeSwitchPoint] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeSwitchedAckEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchedAckEvent":
        """Create ModeSwitchedAckEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeSwitchedAckEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeSwitchedAckEvent since parent returns ARObject
        return cast("ModeSwitchedAckEvent", obj)


class ModeSwitchedAckEventBuilder:
    """Builder for ModeSwitchedAckEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchedAckEvent = ModeSwitchedAckEvent()

    def build(self) -> ModeSwitchedAckEvent:
        """Build and return ModeSwitchedAckEvent object.

        Returns:
            ModeSwitchedAckEvent instance
        """
        # TODO: Add validation
        return self._obj
