"""UnlimitedIntegerValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 242)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UnlimitedIntegerValueVariationPoint(ARObject):
    """AUTOSAR UnlimitedIntegerValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UnlimitedIntegerValueVariationPoint."""
        super().__init__()


class UnlimitedIntegerValueVariationPointBuilder:
    """Builder for UnlimitedIntegerValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnlimitedIntegerValueVariationPoint = UnlimitedIntegerValueVariationPoint()

    def build(self) -> UnlimitedIntegerValueVariationPoint:
        """Build and return UnlimitedIntegerValueVariationPoint object.

        Returns:
            UnlimitedIntegerValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
