"""PostBuildVariantCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 614)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 232)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class PostBuildVariantCondition(ARObject):
    """AUTOSAR PostBuildVariantCondition."""

    def __init__(self) -> None:
        """Initialize PostBuildVariantCondition."""
        super().__init__()
        self.matching: Any = None
        self.value: Integer = None


class PostBuildVariantConditionBuilder:
    """Builder for PostBuildVariantCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCondition = PostBuildVariantCondition()

    def build(self) -> PostBuildVariantCondition:
        """Build and return PostBuildVariantCondition object.

        Returns:
            PostBuildVariantCondition instance
        """
        # TODO: Add validation
        return self._obj
