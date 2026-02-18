"""BswCompositionTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)


class BswCompositionTiming(TimingExtension):
    """AUTOSAR BswCompositionTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implementations: list[BswImplementation]
    def __init__(self) -> None:
        """Initialize BswCompositionTiming."""
        super().__init__()
        self.implementations: list[BswImplementation] = []


class BswCompositionTimingBuilder:
    """Builder for BswCompositionTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswCompositionTiming = BswCompositionTiming()

    def build(self) -> BswCompositionTiming:
        """Build and return BswCompositionTiming object.

        Returns:
            BswCompositionTiming instance
        """
        # TODO: Add validation
        return self._obj
