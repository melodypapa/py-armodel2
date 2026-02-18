"""FMFeature AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 24)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_restriction import (
    FMFeatureRestriction,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_relation import (
        FMFeatureRelation,
    )



class FMFeature(ARElement):
    """AUTOSAR FMFeature."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute_defs: list[FMAttributeDef]
    decomposition_decompositions: list[FMFeature]
    maximum: Optional[BindingTimeEnum]
    minimum: Optional[BindingTimeEnum]
    relations: list[FMFeatureRelation]
    restrictions: list[FMFeatureRestriction]
    def __init__(self) -> None:
        """Initialize FMFeature."""
        super().__init__()
        self.attribute_defs: list[FMAttributeDef] = []
        self.decomposition_decompositions: list[FMFeature] = []
        self.maximum: Optional[BindingTimeEnum] = None
        self.minimum: Optional[BindingTimeEnum] = None
        self.relations: list[FMFeatureRelation] = []
        self.restrictions: list[FMFeatureRestriction] = []


class FMFeatureBuilder:
    """Builder for FMFeature."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeature = FMFeature()

    def build(self) -> FMFeature:
        """Build and return FMFeature object.

        Returns:
            FMFeature instance
        """
        # TODO: Add validation
        return self._obj
