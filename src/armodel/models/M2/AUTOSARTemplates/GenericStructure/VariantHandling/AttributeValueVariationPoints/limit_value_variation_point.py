"""LimitValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    IntervalTypeEnum,
)


class LimitValueVariationPoint(ARObject):
    """AUTOSAR LimitValueVariationPoint."""

    interval_type_enum: Optional[IntervalTypeEnum]
    def __init__(self) -> None:
        """Initialize LimitValueVariationPoint."""
        super().__init__()
        self.interval_type_enum: Optional[IntervalTypeEnum] = None


class LimitValueVariationPointBuilder:
    """Builder for LimitValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LimitValueVariationPoint = LimitValueVariationPoint()

    def build(self) -> LimitValueVariationPoint:
        """Build and return LimitValueVariationPoint object.

        Returns:
            LimitValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
