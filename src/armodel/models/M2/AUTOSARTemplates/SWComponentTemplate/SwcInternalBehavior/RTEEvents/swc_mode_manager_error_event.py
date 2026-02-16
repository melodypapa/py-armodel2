"""SwcModeManagerErrorEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class SwcModeManagerErrorEvent(RTEEvent):
    """AUTOSAR SwcModeManagerErrorEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_group", None, False, False, ModeDeclarationGroup),  # modeGroup
    ]

    def __init__(self) -> None:
        """Initialize SwcModeManagerErrorEvent."""
        super().__init__()
        self.mode_group: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcModeManagerErrorEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcModeManagerErrorEvent":
        """Create SwcModeManagerErrorEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcModeManagerErrorEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcModeManagerErrorEvent since parent returns ARObject
        return cast("SwcModeManagerErrorEvent", obj)


class SwcModeManagerErrorEventBuilder:
    """Builder for SwcModeManagerErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcModeManagerErrorEvent = SwcModeManagerErrorEvent()

    def build(self) -> SwcModeManagerErrorEvent:
        """Build and return SwcModeManagerErrorEvent object.

        Returns:
            SwcModeManagerErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
