"""MultiplicityRestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)


class MultiplicityRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR MultiplicityRestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize MultiplicityRestrictionWithSeverity."""
        super().__init__()


class MultiplicityRestrictionWithSeverityBuilder:
    """Builder for MultiplicityRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplicityRestrictionWithSeverity = MultiplicityRestrictionWithSeverity()

    def build(self) -> MultiplicityRestrictionWithSeverity:
        """Build and return MultiplicityRestrictionWithSeverity object.

        Returns:
            MultiplicityRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
