"""FMAttributeDef AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)


class FMAttributeDef(Identifiable):
    """AUTOSAR FMAttributeDef."""

    def __init__(self) -> None:
        """Initialize FMAttributeDef."""
        super().__init__()
        self.default_value: Optional[Numerical] = None
        self.max: Optional[Limit] = None
        self.min: Optional[Limit] = None


class FMAttributeDefBuilder:
    """Builder for FMAttributeDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMAttributeDef = FMAttributeDef()

    def build(self) -> FMAttributeDef:
        """Build and return FMAttributeDef object.

        Returns:
            FMAttributeDef instance
        """
        # TODO: Add validation
        return self._obj
