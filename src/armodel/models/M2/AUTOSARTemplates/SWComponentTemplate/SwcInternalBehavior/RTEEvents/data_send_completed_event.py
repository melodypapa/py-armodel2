"""DataSendCompletedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 542)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class DataSendCompletedEvent(RTEEvent):
    """AUTOSAR DataSendCompletedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_source: Optional[VariableAccess]
    def __init__(self) -> None:
        """Initialize DataSendCompletedEvent."""
        super().__init__()
        self.event_source: Optional[VariableAccess] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataSendCompletedEvent":
        """Deserialize XML element to DataSendCompletedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataSendCompletedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataSendCompletedEvent, cls).deserialize(element)

        # Parse event_source
        child = ARObject._find_child_element(element, "EVENT-SOURCE")
        if child is not None:
            event_source_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.event_source = event_source_value

        return obj



class DataSendCompletedEventBuilder:
    """Builder for DataSendCompletedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataSendCompletedEvent = DataSendCompletedEvent()

    def build(self) -> DataSendCompletedEvent:
        """Build and return DataSendCompletedEvent object.

        Returns:
            DataSendCompletedEvent instance
        """
        # TODO: Add validation
        return self._obj
