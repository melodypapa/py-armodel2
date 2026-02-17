"""TDHeaderIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TDHeaderIdRange(ARObject):
    """AUTOSAR TDHeaderIdRange."""

    max_header_id: Optional[Integer]
    min_header_id: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TDHeaderIdRange."""
        super().__init__()
        self.max_header_id: Optional[Integer] = None
        self.min_header_id: Optional[Integer] = None


class TDHeaderIdRangeBuilder:
    """Builder for TDHeaderIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDHeaderIdRange = TDHeaderIdRange()

    def build(self) -> TDHeaderIdRange:
        """Build and return TDHeaderIdRange object.

        Returns:
            TDHeaderIdRange instance
        """
        # TODO: Add validation
        return self._obj
