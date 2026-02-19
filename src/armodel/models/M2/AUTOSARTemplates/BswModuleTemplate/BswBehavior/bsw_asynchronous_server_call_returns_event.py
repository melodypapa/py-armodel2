"""BswAsynchronousServerCallReturnsEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 98)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswAsynchronousServerCallReturnsEvent(BswScheduleEvent):
    """AUTOSAR BswAsynchronousServerCallReturnsEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source: Optional[Any]
    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallReturnsEvent."""
        super().__init__()
        self.event_source: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswAsynchronousServerCallReturnsEvent":
        """Deserialize XML element to BswAsynchronousServerCallReturnsEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswAsynchronousServerCallReturnsEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event_source
        child = ARObject._find_child_element(element, "EVENT-SOURCE")
        if child is not None:
            event_source_value = child.text
            obj.event_source = event_source_value

        return obj



class BswAsynchronousServerCallReturnsEventBuilder:
    """Builder for BswAsynchronousServerCallReturnsEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallReturnsEvent = BswAsynchronousServerCallReturnsEvent()

    def build(self) -> BswAsynchronousServerCallReturnsEvent:
        """Build and return BswAsynchronousServerCallReturnsEvent object.

        Returns:
            BswAsynchronousServerCallReturnsEvent instance
        """
        # TODO: Add validation
        return self._obj
