"""TDEventBsw AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 251)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
    BswModuleDescription,
)


class TDEventBsw(TimingDescriptionEvent):
    """AUTOSAR TDEventBsw."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize TDEventBsw."""
        super().__init__()
        self.bsw_module_description: Optional[BswModuleDescription] = None


class TDEventBswBuilder:
    """Builder for TDEventBsw."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBsw = TDEventBsw()

    def build(self) -> TDEventBsw:
        """Build and return TDEventBsw object.

        Returns:
            TDEventBsw instance
        """
        # TODO: Add validation
        return self._obj
