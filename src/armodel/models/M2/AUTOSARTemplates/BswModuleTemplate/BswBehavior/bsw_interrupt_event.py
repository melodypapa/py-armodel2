"""BswInterruptEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)


class BswInterruptEvent(BswEvent):
    """AUTOSAR BswInterruptEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize BswInterruptEvent."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswInterruptEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInterruptEvent":
        """Create BswInterruptEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswInterruptEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswInterruptEvent since parent returns ARObject
        return cast("BswInterruptEvent", obj)


class BswInterruptEventBuilder:
    """Builder for BswInterruptEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInterruptEvent = BswInterruptEvent()

    def build(self) -> BswInterruptEvent:
        """Build and return BswInterruptEvent object.

        Returns:
            BswInterruptEvent instance
        """
        # TODO: Add validation
        return self._obj
