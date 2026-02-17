"""AggregationCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.aggregation_tailoring import (
    AggregationTailoring,
)


class AggregationCondition(AttributeCondition):
    """AUTOSAR AggregationCondition."""

    aggregation: AggregationTailoring
    def __init__(self) -> None:
        """Initialize AggregationCondition."""
        super().__init__()
        self.aggregation: AggregationTailoring = None


class AggregationConditionBuilder:
    """Builder for AggregationCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AggregationCondition = AggregationCondition()

    def build(self) -> AggregationCondition:
        """Build and return AggregationCondition object.

        Returns:
            AggregationCondition instance
        """
        # TODO: Add validation
        return self._obj
