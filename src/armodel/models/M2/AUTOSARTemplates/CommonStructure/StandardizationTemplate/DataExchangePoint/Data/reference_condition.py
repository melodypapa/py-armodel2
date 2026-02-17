"""ReferenceCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.reference_tailoring import (
    ReferenceTailoring,
)


class ReferenceCondition(AttributeCondition):
    """AUTOSAR ReferenceCondition."""

    reference: ReferenceTailoring
    def __init__(self) -> None:
        """Initialize ReferenceCondition."""
        super().__init__()
        self.reference: ReferenceTailoring = None


class ReferenceConditionBuilder:
    """Builder for ReferenceCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceCondition = ReferenceCondition()

    def build(self) -> ReferenceCondition:
        """Build and return ReferenceCondition object.

        Returns:
            ReferenceCondition instance
        """
        # TODO: Add validation
        return self._obj
