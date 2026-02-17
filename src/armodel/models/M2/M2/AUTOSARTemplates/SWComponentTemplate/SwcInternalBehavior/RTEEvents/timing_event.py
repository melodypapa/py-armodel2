"""TimingEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 532)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 254)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TimingEvent(RTEEvent):
    """AUTOSAR TimingEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offset
        "period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # period
    }

    def __init__(self) -> None:
        """Initialize TimingEvent."""
        super().__init__()
        self.offset: Optional[TimeValue] = None
        self.period: Optional[TimeValue] = None


class TimingEventBuilder:
    """Builder for TimingEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingEvent = TimingEvent()

    def build(self) -> TimingEvent:
        """Build and return TimingEvent object.

        Returns:
            TimingEvent instance
        """
        # TODO: Add validation
        return self._obj
