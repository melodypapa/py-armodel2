"""BswInternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """AUTOSAR BswInternalTriggerOccurredEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source_point_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswInternalTriggerOccurredEvent."""
        super().__init__()
        self.event_source_point_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalTriggerOccurredEvent":
        """Deserialize XML element to BswInternalTriggerOccurredEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInternalTriggerOccurredEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event_source_point_ref
        child = ARObject._find_child_element(element, "EVENT-SOURCE-POINT")
        if child is not None:
            event_source_point_ref_value = ARObject._deserialize_by_tag(child, "BswInternalTriggeringPoint")
            obj.event_source_point_ref = event_source_point_ref_value

        return obj



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
