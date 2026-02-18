"""PrimitiveAttributeTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import (
    DefaultValueApplicationStrategyEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.value_restriction_with_severity import (
    ValueRestrictionWithSeverity,
)


class PrimitiveAttributeTailoring(AttributeTailoring):
    """AUTOSAR PrimitiveAttributeTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[DefaultValueApplicationStrategyEnum]
    sub_attributes: list[Any]
    value_restriction_with_severity: Optional[ValueRestrictionWithSeverity]
    def __init__(self) -> None:
        """Initialize PrimitiveAttributeTailoring."""
        super().__init__()
        self.default_value: Optional[DefaultValueApplicationStrategyEnum] = None
        self.sub_attributes: list[Any] = []
        self.value_restriction_with_severity: Optional[ValueRestrictionWithSeverity] = None


class PrimitiveAttributeTailoringBuilder:
    """Builder for PrimitiveAttributeTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrimitiveAttributeTailoring = PrimitiveAttributeTailoring()

    def build(self) -> PrimitiveAttributeTailoring:
        """Build and return PrimitiveAttributeTailoring object.

        Returns:
            PrimitiveAttributeTailoring instance
        """
        # TODO: Add validation
        return self._obj
