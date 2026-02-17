"""SdgAggregationWithVariation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgAggregationWithVariation(SdgElementWithGid):
    """AUTOSAR SdgAggregationWithVariation."""

    def __init__(self) -> None:
        """Initialize SdgAggregationWithVariation."""
        super().__init__()
        self.sub_sdg: Optional[SdgClass] = None


class SdgAggregationWithVariationBuilder:
    """Builder for SdgAggregationWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAggregationWithVariation = SdgAggregationWithVariation()

    def build(self) -> SdgAggregationWithVariation:
        """Build and return SdgAggregationWithVariation object.

        Returns:
            SdgAggregationWithVariation instance
        """
        # TODO: Add validation
        return self._obj
