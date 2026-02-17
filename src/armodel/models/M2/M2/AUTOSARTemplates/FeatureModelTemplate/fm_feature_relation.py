"""FMFeatureRelation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
        FMFeature,
    )



class FMFeatureRelation(Identifiable):
    """AUTOSAR FMFeatureRelation."""

    def __init__(self) -> None:
        """Initialize FMFeatureRelation."""
        super().__init__()
        self.features: list[FMFeature] = []
        self.restriction: Optional[Any] = None


class FMFeatureRelationBuilder:
    """Builder for FMFeatureRelation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRelation = FMFeatureRelation()

    def build(self) -> FMFeatureRelation:
        """Build and return FMFeatureRelation object.

        Returns:
            FMFeatureRelation instance
        """
        # TODO: Add validation
        return self._obj
