"""BswTimingEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswTimingEvent(BswScheduleEvent):
    """AUTOSAR BswTimingEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    period: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize BswTimingEvent."""
        super().__init__()
        self.period: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswTimingEvent":
        """Deserialize XML element to BswTimingEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswTimingEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswTimingEvent, cls).deserialize(element)

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        return obj



class BswTimingEventBuilder:
    """Builder for BswTimingEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTimingEvent = BswTimingEvent()

    def build(self) -> BswTimingEvent:
        """Build and return BswTimingEvent object.

        Returns:
            BswTimingEvent instance
        """
        # TODO: Add validation
        return self._obj
