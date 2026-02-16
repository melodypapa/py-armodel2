"""BswModeSwitchedAckEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeSwitchedAckEvent(BswScheduleEvent):
    """AUTOSAR BswModeSwitchedAckEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_group", None, False, False, ModeDeclarationGroup),  # modeGroup
    ]

    def __init__(self) -> None:
        """Initialize BswModeSwitchedAckEvent."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModeSwitchedAckEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSwitchedAckEvent":
        """Create BswModeSwitchedAckEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModeSwitchedAckEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModeSwitchedAckEvent since parent returns ARObject
        return cast("BswModeSwitchedAckEvent", obj)


class BswModeSwitchedAckEventBuilder:
    """Builder for BswModeSwitchedAckEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchedAckEvent = BswModeSwitchedAckEvent()

    def build(self) -> BswModeSwitchedAckEvent:
        """Build and return BswModeSwitchedAckEvent object.

        Returns:
            BswModeSwitchedAckEvent instance
        """
        # TODO: Add validation
        return self._obj
