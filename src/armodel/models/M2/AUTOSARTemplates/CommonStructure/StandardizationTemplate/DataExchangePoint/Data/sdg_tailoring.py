"""SdgTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgTailoring(RestrictionWithSeverity):
    """AUTOSAR SdgTailoring."""

    def __init__(self) -> None:
        """Initialize SdgTailoring."""
        super().__init__()
        self.sdg_class: Optional[SdgClass] = None


class SdgTailoringBuilder:
    """Builder for SdgTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgTailoring = SdgTailoring()

    def build(self) -> SdgTailoring:
        """Build and return SdgTailoring object.

        Returns:
            SdgTailoring instance
        """
        # TODO: Add validation
        return self._obj
