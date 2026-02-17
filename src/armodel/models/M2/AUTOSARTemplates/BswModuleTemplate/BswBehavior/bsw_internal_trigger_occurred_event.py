"""BswInternalTriggerOccurredEvent AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """AUTOSAR BswInternalTriggerOccurredEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize BswInternalTriggerOccurredEvent."""
        super().__init__()


class BswInternalTriggerOccurredEventBuilder:
    """Builder for BswInternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInternalTriggerOccurredEvent = BswInternalTriggerOccurredEvent()

    def build(self) -> BswInternalTriggerOccurredEvent:
        """Build and return BswInternalTriggerOccurredEvent object.

        Returns:
            BswInternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
