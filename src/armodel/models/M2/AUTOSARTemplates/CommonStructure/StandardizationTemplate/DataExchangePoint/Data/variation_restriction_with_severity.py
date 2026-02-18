"""VariationRestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)


class VariationRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR VariationRestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize VariationRestrictionWithSeverity."""
        super().__init__()


class VariationRestrictionWithSeverityBuilder:
    """Builder for VariationRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationRestrictionWithSeverity = VariationRestrictionWithSeverity()

    def build(self) -> VariationRestrictionWithSeverity:
        """Build and return VariationRestrictionWithSeverity object.

        Returns:
            VariationRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
