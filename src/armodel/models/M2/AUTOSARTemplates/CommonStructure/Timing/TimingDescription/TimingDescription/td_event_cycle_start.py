"""TDEventCycleStart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from abc import ABC, abstractmethod


class TDEventCycleStart(TDEventCom, ABC):
    """AUTOSAR TDEventCycleStart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    cycle_repetition: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TDEventCycleStart."""
        super().__init__()
        self.cycle_repetition: Optional[Integer] = None


class TDEventCycleStartBuilder:
    """Builder for TDEventCycleStart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventCycleStart = TDEventCycleStart()

    def build(self) -> TDEventCycleStart:
        """Build and return TDEventCycleStart object.

        Returns:
            TDEventCycleStart instance
        """
        # TODO: Add validation
        return self._obj
