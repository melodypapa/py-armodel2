"""UnresolvedReferenceRestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)


class UnresolvedReferenceRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR UnresolvedReferenceRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize UnresolvedReferenceRestrictionWithSeverity."""
        super().__init__()


class UnresolvedReferenceRestrictionWithSeverityBuilder:
    """Builder for UnresolvedReferenceRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnresolvedReferenceRestrictionWithSeverity = UnresolvedReferenceRestrictionWithSeverity()

    def build(self) -> UnresolvedReferenceRestrictionWithSeverity:
        """Build and return UnresolvedReferenceRestrictionWithSeverity object.

        Returns:
            UnresolvedReferenceRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
