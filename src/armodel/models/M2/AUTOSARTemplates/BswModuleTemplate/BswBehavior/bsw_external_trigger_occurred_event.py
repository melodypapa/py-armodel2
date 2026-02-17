"""BswExternalTriggerOccurredEvent AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    """AUTOSAR BswExternalTriggerOccurredEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize BswExternalTriggerOccurredEvent."""
        super().__init__()


class BswExternalTriggerOccurredEventBuilder:
    """Builder for BswExternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswExternalTriggerOccurredEvent = BswExternalTriggerOccurredEvent()

    def build(self) -> BswExternalTriggerOccurredEvent:
        """Build and return BswExternalTriggerOccurredEvent object.

        Returns:
            BswExternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
