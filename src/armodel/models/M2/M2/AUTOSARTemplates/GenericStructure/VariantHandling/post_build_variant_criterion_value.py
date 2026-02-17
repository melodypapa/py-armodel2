"""PostBuildVariantCriterionValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 77)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 258)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)


class PostBuildVariantCriterionValue(ARObject):
    """AUTOSAR PostBuildVariantCriterionValue."""

    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterionValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.value: Integer = None
        self.variant_criterion: Any = None


class PostBuildVariantCriterionValueBuilder:
    """Builder for PostBuildVariantCriterionValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterionValue = PostBuildVariantCriterionValue()

    def build(self) -> PostBuildVariantCriterionValue:
        """Build and return PostBuildVariantCriterionValue object.

        Returns:
            PostBuildVariantCriterionValue instance
        """
        # TODO: Add validation
        return self._obj
