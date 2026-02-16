"""ModeSwitchEventTriggeredActivity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.swc_mode_switch_event import (
    SwcModeSwitchEvent,
)


class ModeSwitchEventTriggeredActivity(ARObject):
    """AUTOSAR ModeSwitchEventTriggeredActivity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("role", None, True, False, None),  # role
        ("swc_mode_switch_event", None, False, False, SwcModeSwitchEvent),  # swcModeSwitchEvent
    ]

    def __init__(self) -> None:
        """Initialize ModeSwitchEventTriggeredActivity."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.swc_mode_switch_event: Optional[SwcModeSwitchEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeSwitchEventTriggeredActivity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchEventTriggeredActivity":
        """Create ModeSwitchEventTriggeredActivity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeSwitchEventTriggeredActivity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeSwitchEventTriggeredActivity since parent returns ARObject
        return cast("ModeSwitchEventTriggeredActivity", obj)


class ModeSwitchEventTriggeredActivityBuilder:
    """Builder for ModeSwitchEventTriggeredActivity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchEventTriggeredActivity = ModeSwitchEventTriggeredActivity()

    def build(self) -> ModeSwitchEventTriggeredActivity:
        """Build and return ModeSwitchEventTriggeredActivity object.

        Returns:
            ModeSwitchEventTriggeredActivity instance
        """
        # TODO: Add validation
        return self._obj
