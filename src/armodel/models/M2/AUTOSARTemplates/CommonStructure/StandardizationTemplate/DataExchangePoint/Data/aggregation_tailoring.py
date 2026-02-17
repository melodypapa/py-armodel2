"""AggregationTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)


class AggregationTailoring(AttributeTailoring):
    """AUTOSAR AggregationTailoring."""

    type_tailorings: list[ClassTailoring]
    def __init__(self) -> None:
        """Initialize AggregationTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []


class AggregationTailoringBuilder:
    """Builder for AggregationTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AggregationTailoring = AggregationTailoring()

    def build(self) -> AggregationTailoring:
        """Build and return AggregationTailoring object.

        Returns:
            AggregationTailoring instance
        """
        # TODO: Add validation
        return self._obj
