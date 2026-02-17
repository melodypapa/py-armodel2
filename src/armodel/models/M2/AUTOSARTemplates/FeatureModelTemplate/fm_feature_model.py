"""FMFeatureModel AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 21)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureModel(ARElement):
    """AUTOSAR FMFeatureModel."""

    def __init__(self) -> None:
        """Initialize FMFeatureModel."""
        super().__init__()
        self.features: list[FMFeature] = []
        self.root: Optional[FMFeature] = None


class FMFeatureModelBuilder:
    """Builder for FMFeatureModel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureModel = FMFeatureModel()

    def build(self) -> FMFeatureModel:
        """Build and return FMFeatureModel object.

        Returns:
            FMFeatureModel instance
        """
        # TODO: Add validation
        return self._obj
