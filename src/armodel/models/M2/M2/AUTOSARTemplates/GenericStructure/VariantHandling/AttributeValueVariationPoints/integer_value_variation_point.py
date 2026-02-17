"""IntegerValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class IntegerValueVariationPoint(ARObject):
    """AUTOSAR IntegerValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize IntegerValueVariationPoint."""
        super().__init__()


class IntegerValueVariationPointBuilder:
    """Builder for IntegerValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IntegerValueVariationPoint = IntegerValueVariationPoint()

    def build(self) -> IntegerValueVariationPoint:
        """Build and return IntegerValueVariationPoint object.

        Returns:
            IntegerValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
