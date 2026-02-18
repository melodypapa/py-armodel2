"""FMFeatureMap AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map_element import (
        FMFeatureMapElement,
    )



class FMFeatureMap(ARElement):
    """AUTOSAR FMFeatureMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mappings: list[FMFeatureMapElement]
    def __init__(self) -> None:
        """Initialize FMFeatureMap."""
        super().__init__()
        self.mappings: list[FMFeatureMapElement] = []


class FMFeatureMapBuilder:
    """Builder for FMFeatureMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMap = FMFeatureMap()

    def build(self) -> FMFeatureMap:
        """Build and return FMFeatureMap object.

        Returns:
            FMFeatureMap instance
        """
        # TODO: Add validation
        return self._obj
