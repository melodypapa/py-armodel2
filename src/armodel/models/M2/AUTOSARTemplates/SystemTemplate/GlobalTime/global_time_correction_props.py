"""GlobalTimeCorrectionProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 862)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class GlobalTimeCorrectionProps(ARObject):
    """AUTOSAR GlobalTimeCorrectionProps."""

    offset_correction: Optional[TimeValue]
    rate_correction: Optional[TimeValue]
    rate_corrections: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize GlobalTimeCorrectionProps."""
        super().__init__()
        self.offset_correction: Optional[TimeValue] = None
        self.rate_correction: Optional[TimeValue] = None
        self.rate_corrections: Optional[PositiveInteger] = None


class GlobalTimeCorrectionPropsBuilder:
    """Builder for GlobalTimeCorrectionProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCorrectionProps = GlobalTimeCorrectionProps()

    def build(self) -> GlobalTimeCorrectionProps:
        """Build and return GlobalTimeCorrectionProps object.

        Returns:
            GlobalTimeCorrectionProps instance
        """
        # TODO: Add validation
        return self._obj
