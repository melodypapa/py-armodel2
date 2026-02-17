"""VariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1010)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2078)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 80)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 226)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 39)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class VariationPoint(ARObject):
    """AUTOSAR VariationPoint."""

    def __init__(self) -> None:
        """Initialize VariationPoint."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.sw_syscond: Optional[ConditionByFormula] = None


class VariationPointBuilder:
    """Builder for VariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationPoint = VariationPoint()

    def build(self) -> VariationPoint:
        """Build and return VariationPoint object.

        Returns:
            VariationPoint instance
        """
        # TODO: Add validation
        return self._obj
