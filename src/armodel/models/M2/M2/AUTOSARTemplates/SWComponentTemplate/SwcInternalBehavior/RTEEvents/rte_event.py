"""RTEEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "disabled_mode_instance_refs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeDeclaration,
        ),  # disabledModeInstanceRefs
        "start_on_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RunnableEntity,
        ),  # startOnEvent
    }

    def __init__(self) -> None:
        """Initialize RTEEvent."""
        super().__init__()
        self.disabled_mode_instance_refs: list[ModeDeclaration] = []
        self.start_on_event: Optional[RunnableEntity] = None


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
