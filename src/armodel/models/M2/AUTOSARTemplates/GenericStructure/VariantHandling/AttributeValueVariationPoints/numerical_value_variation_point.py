"""NumericalValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 302)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class NumericalValueVariationPoint(ARObject):
    """AUTOSAR NumericalValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize NumericalValueVariationPoint."""
        super().__init__()


class NumericalValueVariationPointBuilder:
    """Builder for NumericalValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalValueVariationPoint = NumericalValueVariationPoint()

    def build(self) -> NumericalValueVariationPoint:
        """Build and return NumericalValueVariationPoint object.

        Returns:
            NumericalValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
