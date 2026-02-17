"""FMFeatureSelectionSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_model import (
    FMFeatureModel,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_selection import (
    FMFeatureSelection,
)


class FMFeatureSelectionSet(ARElement):
    """AUTOSAR FMFeatureSelectionSet."""

    feature_models: list[FMFeatureModel]
    includes: list[FMFeatureSelectionSet]
    selections: list[FMFeatureSelection]
    def __init__(self) -> None:
        """Initialize FMFeatureSelectionSet."""
        super().__init__()
        self.feature_models: list[FMFeatureModel] = []
        self.includes: list[FMFeatureSelectionSet] = []
        self.selections: list[FMFeatureSelection] = []


class FMFeatureSelectionSetBuilder:
    """Builder for FMFeatureSelectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelectionSet = FMFeatureSelectionSet()

    def build(self) -> FMFeatureSelectionSet:
        """Build and return FMFeatureSelectionSet object.

        Returns:
            FMFeatureSelectionSet instance
        """
        # TODO: Add validation
        return self._obj
