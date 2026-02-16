"""RTEEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class RTEEvent(AbstractEvent):
    """AUTOSAR RTEEvent."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("disabled_mode_instance_refs", None, False, True, ModeDeclaration),  # disabledModeInstanceRefs
        ("start_on_event", None, False, False, RunnableEntity),  # startOnEvent
    ]

    def __init__(self) -> None:
        """Initialize RTEEvent."""
        super().__init__()
        self.disabled_mode_instance_refs: list[ModeDeclaration] = []
        self.start_on_event: Optional[RunnableEntity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RTEEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RTEEvent":
        """Create RTEEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RTEEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RTEEvent since parent returns ARObject
        return cast("RTEEvent", obj)


class RTEEventBuilder:
    """Builder for RTEEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RTEEvent = RTEEvent()

    def build(self) -> RTEEvent:
        """Build and return RTEEvent object.

        Returns:
            RTEEvent instance
        """
        # TODO: Add validation
        return self._obj
