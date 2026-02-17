"""ConcreteClassTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import (
    DataFormatElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class ConcreteClassTailoring(DataFormatElementScope):
    """AUTOSAR ConcreteClassTailoring."""

    validation_root: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ConcreteClassTailoring."""
        super().__init__()
        self.validation_root: Optional[Boolean] = None


class ConcreteClassTailoringBuilder:
    """Builder for ConcreteClassTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConcreteClassTailoring = ConcreteClassTailoring()

    def build(self) -> ConcreteClassTailoring:
        """Build and return ConcreteClassTailoring object.

        Returns:
            ConcreteClassTailoring instance
        """
        # TODO: Add validation
        return self._obj
