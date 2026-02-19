"""BswScheduleEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class BswScheduleEvent(BswEvent, ABC):
    """AUTOSAR BswScheduleEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize BswScheduleEvent."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswScheduleEvent":
        """Deserialize XML element to BswScheduleEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswScheduleEvent object
        """
        # Delegate to parent class to handle inherited attributes
        return super(BswScheduleEvent, cls).deserialize(element)



class BswScheduleEventBuilder:
    """Builder for BswScheduleEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswScheduleEvent = BswScheduleEvent()

    def build(self) -> BswScheduleEvent:
        """Build and return BswScheduleEvent object.

        Returns:
            BswScheduleEvent instance
        """
        # TODO: Add validation
        return self._obj
