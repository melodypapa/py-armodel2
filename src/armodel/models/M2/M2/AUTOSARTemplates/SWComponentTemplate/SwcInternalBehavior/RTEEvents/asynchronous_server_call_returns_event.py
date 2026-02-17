"""AsynchronousServerCallReturnsEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class AsynchronousServerCallReturnsEvent(RTEEvent):
    """AUTOSAR AsynchronousServerCallReturnsEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # eventSource
    }

    def __init__(self) -> None:
        """Initialize AsynchronousServerCallReturnsEvent."""
        super().__init__()
        self.event_source: Optional[Any] = None


class AsynchronousServerCallReturnsEventBuilder:
    """Builder for AsynchronousServerCallReturnsEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallReturnsEvent = AsynchronousServerCallReturnsEvent()

    def build(self) -> AsynchronousServerCallReturnsEvent:
        """Build and return AsynchronousServerCallReturnsEvent object.

        Returns:
            AsynchronousServerCallReturnsEvent instance
        """
        # TODO: Add validation
        return self._obj
