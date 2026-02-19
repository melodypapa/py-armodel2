"""ModeSwitchedAckEvent AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_switch_point import (
    ModeSwitchPoint,
)


class ModeSwitchedAckEvent(RTEEvent):
    """AUTOSAR ModeSwitchedAckEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source: Optional[ModeSwitchPoint]
    def __init__(self) -> None:
        """Initialize ModeSwitchedAckEvent."""
        super().__init__()
        self.event_source: Optional[ModeSwitchPoint] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchedAckEvent":
        """Deserialize XML element to ModeSwitchedAckEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchedAckEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event_source
        child = ARObject._find_child_element(element, "EVENT-SOURCE")
        if child is not None:
            event_source_value = ARObject._deserialize_by_tag(child, "ModeSwitchPoint")
            obj.event_source = event_source_value

        return obj



class ModeSwitchedAckEventBuilder:
    """Builder for ModeSwitchedAckEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchedAckEvent = ModeSwitchedAckEvent()

    def build(self) -> ModeSwitchedAckEvent:
        """Build and return ModeSwitchedAckEvent object.

        Returns:
            ModeSwitchedAckEvent instance
        """
        # TODO: Add validation
        return self._obj
