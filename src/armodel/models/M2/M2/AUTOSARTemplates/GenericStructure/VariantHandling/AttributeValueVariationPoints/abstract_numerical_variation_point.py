"""AbstractNumericalVariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 969)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 240)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AbstractNumericalVariationPoint(ARObject):
    """AUTOSAR AbstractNumericalVariationPoint."""

    def __init__(self) -> None:
        """Initialize AbstractNumericalVariationPoint."""
        super().__init__()


class AbstractNumericalVariationPointBuilder:
    """Builder for AbstractNumericalVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractNumericalVariationPoint = AbstractNumericalVariationPoint()

    def build(self) -> AbstractNumericalVariationPoint:
        """Build and return AbstractNumericalVariationPoint object.

        Returns:
            AbstractNumericalVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
