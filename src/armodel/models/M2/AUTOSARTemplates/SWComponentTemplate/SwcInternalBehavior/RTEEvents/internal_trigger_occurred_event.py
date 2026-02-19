"""InternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 546)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.internal_triggering_point import (
    InternalTriggeringPoint,
)


class InternalTriggerOccurredEvent(RTEEvent):
    """AUTOSAR InternalTriggerOccurredEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize InternalTriggerOccurredEvent."""
        super().__init__()
        self.event_source_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalTriggerOccurredEvent":
        """Deserialize XML element to InternalTriggerOccurredEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalTriggerOccurredEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InternalTriggerOccurredEvent, cls).deserialize(element)

        # Parse event_source_ref
        child = ARObject._find_child_element(element, "EVENT-SOURCE")
        if child is not None:
            event_source_ref_value = ARObject._deserialize_by_tag(child, "InternalTriggeringPoint")
            obj.event_source_ref = event_source_ref_value

        return obj



class InternalTriggerOccurredEventBuilder:
    """Builder for InternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalTriggerOccurredEvent = InternalTriggerOccurredEvent()

    def build(self) -> InternalTriggerOccurredEvent:
        """Build and return InternalTriggerOccurredEvent object.

        Returns:
            InternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
