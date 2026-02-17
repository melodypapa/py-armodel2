"""FMFeatureMapElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map import (
        FMFeatureMap,
    )



class FMFeatureMapElement(Identifiable):
    """AUTOSAR FMFeatureMapElement."""

    def __init__(self) -> None:
        """Initialize FMFeatureMapElement."""
        super().__init__()
        self.assertions: list[FMFeatureMap] = []
        self.conditions: list[FMFeatureMap] = []
        self.post_build_variants: list[Any] = []
        self.sw_value_sets: list[SwSystemconstantValueSet] = []


class FMFeatureMapElementBuilder:
    """Builder for FMFeatureMapElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapElement = FMFeatureMapElement()

    def build(self) -> FMFeatureMapElement:
        """Build and return FMFeatureMapElement object.

        Returns:
            FMFeatureMapElement instance
        """
        # TODO: Add validation
        return self._obj
