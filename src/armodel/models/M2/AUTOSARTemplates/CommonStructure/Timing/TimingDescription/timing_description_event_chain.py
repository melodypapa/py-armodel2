"""TimingDescriptionEventChain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TimingDescriptionEventChain(TimingDescription):
    """AUTOSAR TimingDescriptionEventChain."""

    is_pipelining: Optional[Boolean]
    response: Optional[TimingDescriptionEvent]
    segments: list[TimingDescriptionEvent]
    stimulus: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEventChain."""
        super().__init__()
        self.is_pipelining: Optional[Boolean] = None
        self.response: Optional[TimingDescriptionEvent] = None
        self.segments: list[TimingDescriptionEvent] = []
        self.stimulus: Optional[TimingDescriptionEvent] = None


class TimingDescriptionEventChainBuilder:
    """Builder for TimingDescriptionEventChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEventChain = TimingDescriptionEventChain()

    def build(self) -> TimingDescriptionEventChain:
        """Build and return TimingDescriptionEventChain object.

        Returns:
            TimingDescriptionEventChain instance
        """
        # TODO: Add validation
        return self._obj
