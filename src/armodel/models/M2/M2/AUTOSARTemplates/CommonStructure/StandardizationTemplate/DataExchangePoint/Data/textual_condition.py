"""TextualCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class TextualCondition(AbstractCondition):
    """AUTOSAR TextualCondition."""

    def __init__(self) -> None:
        """Initialize TextualCondition."""
        super().__init__()
        self.text: String = None


class TextualConditionBuilder:
    """Builder for TextualCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextualCondition = TextualCondition()

    def build(self) -> TextualCondition:
        """Build and return TextualCondition object.

        Returns:
            TextualCondition instance
        """
        # TODO: Add validation
        return self._obj
