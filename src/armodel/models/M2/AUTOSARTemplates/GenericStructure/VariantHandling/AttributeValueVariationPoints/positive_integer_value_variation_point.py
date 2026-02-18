"""PositiveIntegerValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class PositiveIntegerValueVariationPoint(ARObject):
    """AUTOSAR PositiveIntegerValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize PositiveIntegerValueVariationPoint."""
        super().__init__()


class PositiveIntegerValueVariationPointBuilder:
    """Builder for PositiveIntegerValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PositiveIntegerValueVariationPoint = PositiveIntegerValueVariationPoint()

    def build(self) -> PositiveIntegerValueVariationPoint:
        """Build and return PositiveIntegerValueVariationPoint object.

        Returns:
            PositiveIntegerValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
