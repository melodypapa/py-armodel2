"""VfbTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 24)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class VfbTiming(TimingExtension):
    """AUTOSAR VfbTiming."""

    def __init__(self) -> None:
        """Initialize VfbTiming."""
        super().__init__()
        self.component: Optional[SwComponentType] = None


class VfbTimingBuilder:
    """Builder for VfbTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VfbTiming = VfbTiming()

    def build(self) -> VfbTiming:
        """Build and return VfbTiming object.

        Returns:
            VfbTiming instance
        """
        # TODO: Add validation
        return self._obj
