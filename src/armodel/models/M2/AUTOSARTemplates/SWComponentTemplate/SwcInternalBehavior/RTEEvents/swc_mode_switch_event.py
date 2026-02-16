"""SwcModeSwitchEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class SwcModeSwitchEvent(RTEEvent):
    """AUTOSAR SwcModeSwitchEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("activation", None, False, False, ModeActivationKind),  # activation
    ]

    def __init__(self) -> None:
        """Initialize SwcModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcModeSwitchEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcModeSwitchEvent":
        """Create SwcModeSwitchEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcModeSwitchEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcModeSwitchEvent since parent returns ARObject
        return cast("SwcModeSwitchEvent", obj)


class SwcModeSwitchEventBuilder:
    """Builder for SwcModeSwitchEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcModeSwitchEvent = SwcModeSwitchEvent()

    def build(self) -> SwcModeSwitchEvent:
        """Build and return SwcModeSwitchEvent object.

        Returns:
            SwcModeSwitchEvent instance
        """
        # TODO: Add validation
        return self._obj
