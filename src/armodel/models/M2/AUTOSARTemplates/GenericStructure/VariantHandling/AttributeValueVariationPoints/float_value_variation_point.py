"""FloatValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 240)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FloatValueVariationPoint(ARObject):
    """AUTOSAR FloatValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize FloatValueVariationPoint."""
        super().__init__()


class FloatValueVariationPointBuilder:
    """Builder for FloatValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FloatValueVariationPoint = FloatValueVariationPoint()

    def build(self) -> FloatValueVariationPoint:
        """Build and return FloatValueVariationPoint object.

        Returns:
            FloatValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
