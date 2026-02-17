"""EcuTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 30)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_value_collection import (
    EcucValueCollection,
)


class EcuTiming(TimingExtension):
    """AUTOSAR EcuTiming."""

    def __init__(self) -> None:
        """Initialize EcuTiming."""
        super().__init__()
        self.ecu: Optional[EcucValueCollection] = None


class EcuTimingBuilder:
    """Builder for EcuTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuTiming = EcuTiming()

    def build(self) -> EcuTiming:
        """Build and return EcuTiming object.

        Returns:
            EcuTiming instance
        """
        # TODO: Add validation
        return self._obj
