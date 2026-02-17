"""PostBuildVariantCriterion AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 304)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 614)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 232)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)


class PostBuildVariantCriterion(ARElement):
    """AUTOSAR PostBuildVariantCriterion."""

    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterion."""
        super().__init__()
        self.compu_method: CompuMethod = None


class PostBuildVariantCriterionBuilder:
    """Builder for PostBuildVariantCriterion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterion = PostBuildVariantCriterion()

    def build(self) -> PostBuildVariantCriterion:
        """Build and return PostBuildVariantCriterion object.

        Returns:
            PostBuildVariantCriterion instance
        """
        # TODO: Add validation
        return self._obj
