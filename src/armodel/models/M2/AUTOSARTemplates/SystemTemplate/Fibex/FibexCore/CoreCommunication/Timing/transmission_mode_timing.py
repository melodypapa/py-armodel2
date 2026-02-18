"""TransmissionModeTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 393)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.cyclic_timing import (
    CyclicTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.event_controlled_timing import (
    EventControlledTiming,
)


class TransmissionModeTiming(ARObject):
    """AUTOSAR TransmissionModeTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cyclic_timing: Optional[CyclicTiming]
    event_controlled_timing_timing: Optional[EventControlledTiming]
    def __init__(self) -> None:
        """Initialize TransmissionModeTiming."""
        super().__init__()
        self.cyclic_timing: Optional[CyclicTiming] = None
        self.event_controlled_timing_timing: Optional[EventControlledTiming] = None


class TransmissionModeTimingBuilder:
    """Builder for TransmissionModeTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeTiming = TransmissionModeTiming()

    def build(self) -> TransmissionModeTiming:
        """Build and return TransmissionModeTiming object.

        Returns:
            TransmissionModeTiming instance
        """
        # TODO: Add validation
        return self._obj
