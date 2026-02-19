"""ExternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 545)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class ExternalTriggerOccurredEvent(RTEEvent):
    """AUTOSAR ExternalTriggerOccurredEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ExternalTriggerOccurredEvent."""
        super().__init__()
        self.trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExternalTriggerOccurredEvent":
        """Deserialize XML element to ExternalTriggerOccurredEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExternalTriggerOccurredEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExternalTriggerOccurredEvent, cls).deserialize(element)

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.trigger_ref = trigger_ref_value

        return obj



class ExternalTriggerOccurredEventBuilder:
    """Builder for ExternalTriggerOccurredEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggerOccurredEvent = ExternalTriggerOccurredEvent()

    def build(self) -> ExternalTriggerOccurredEvent:
        """Build and return ExternalTriggerOccurredEvent object.

        Returns:
            ExternalTriggerOccurredEvent instance
        """
        # TODO: Add validation
        return self._obj
