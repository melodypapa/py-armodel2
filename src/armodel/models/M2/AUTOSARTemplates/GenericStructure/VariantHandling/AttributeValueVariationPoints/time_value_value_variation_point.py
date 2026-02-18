"""TimeValueValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 242)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TimeValueValueVariationPoint(ARObject):
    """AUTOSAR TimeValueValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize TimeValueValueVariationPoint."""
        super().__init__()


class TimeValueValueVariationPointBuilder:
    """Builder for TimeValueValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeValueValueVariationPoint = TimeValueValueVariationPoint()

    def build(self) -> TimeValueValueVariationPoint:
        """Build and return TimeValueValueVariationPoint object.

        Returns:
            TimeValueValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
