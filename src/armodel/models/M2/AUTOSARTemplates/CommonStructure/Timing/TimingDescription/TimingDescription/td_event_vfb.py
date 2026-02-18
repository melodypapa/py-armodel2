"""TDEventVfb AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from abc import ABC, abstractmethod


class TDEventVfb(TimingDescriptionEvent, ABC):
    """AUTOSAR TDEventVfb."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    component: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventVfb."""
        super().__init__()
        self.component: Optional[Any] = None


class TDEventVfbBuilder:
    """Builder for TDEventVfb."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfb = TDEventVfb()

    def build(self) -> TDEventVfb:
        """Build and return TDEventVfb object.

        Returns:
            TDEventVfb instance
        """
        # TODO: Add validation
        return self._obj
