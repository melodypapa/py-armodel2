"""BswModeSwitchEvent AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswModeSwitchEvent(BswScheduleEvent):
    """AUTOSAR BswModeSwitchEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize BswModeSwitchEvent."""
        super().__init__()


class BswModeSwitchEventBuilder:
    """Builder for BswModeSwitchEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchEvent = BswModeSwitchEvent()

    def build(self) -> BswModeSwitchEvent:
        """Build and return BswModeSwitchEvent object.

        Returns:
            BswModeSwitchEvent instance
        """
        # TODO: Add validation
        return self._obj
