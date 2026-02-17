"""PredefinedVariant AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 77)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class PredefinedVariant(ARElement):
    """AUTOSAR PredefinedVariant."""

    included_variants: list[PredefinedVariant]
    post_build_variants: list[Any]
    sws: list[SwSystemconstantValueSet]
    def __init__(self) -> None:
        """Initialize PredefinedVariant."""
        super().__init__()
        self.included_variants: list[PredefinedVariant] = []
        self.post_build_variants: list[Any] = []
        self.sws: list[SwSystemconstantValueSet] = []


class PredefinedVariantBuilder:
    """Builder for PredefinedVariant."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PredefinedVariant = PredefinedVariant()

    def build(self) -> PredefinedVariant:
        """Build and return PredefinedVariant object.

        Returns:
            PredefinedVariant instance
        """
        # TODO: Add validation
        return self._obj
