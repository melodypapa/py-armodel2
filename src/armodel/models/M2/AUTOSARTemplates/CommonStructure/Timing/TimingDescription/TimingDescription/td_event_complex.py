"""TDEventComplex AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TDEventComplex(TimingDescriptionEvent):
    """AUTOSAR TDEventComplex."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize TDEventComplex."""
        super().__init__()


class TDEventComplexBuilder:
    """Builder for TDEventComplex."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventComplex = TDEventComplex()

    def build(self) -> TDEventComplex:
        """Build and return TDEventComplex object.

        Returns:
            TDEventComplex instance
        """
        # TODO: Add validation
        return self._obj
