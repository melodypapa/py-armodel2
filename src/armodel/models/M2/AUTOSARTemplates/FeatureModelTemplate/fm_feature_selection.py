"""FMFeatureSelection AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_value import (
    FMAttributeValue,
)


class FMFeatureSelection(Identifiable):
    """AUTOSAR FMFeatureSelection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute_values: list[FMAttributeValue]
    def __init__(self) -> None:
        """Initialize FMFeatureSelection."""
        super().__init__()
        self.attribute_values: list[FMAttributeValue] = []


class FMFeatureSelectionBuilder:
    """Builder for FMFeatureSelection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelection = FMFeatureSelection()

    def build(self) -> FMFeatureSelection:
        """Build and return FMFeatureSelection object.

        Returns:
            FMFeatureSelection instance
        """
        # TODO: Add validation
        return self._obj
