"""SwcModeSwitchEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class SwcModeSwitchEvent(RTEEvent):
    """AUTOSAR SwcModeSwitchEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "activation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeActivationKind,
        ),  # activation
    }

    def __init__(self) -> None:
        """Initialize SwcModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None


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
