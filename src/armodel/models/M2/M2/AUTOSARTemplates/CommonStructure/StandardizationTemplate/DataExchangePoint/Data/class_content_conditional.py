"""ClassContentConditional AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.sdg_tailoring import (
    SdgTailoring,
)


class ClassContentConditional(Identifiable):
    """AUTOSAR ClassContentConditional."""

    def __init__(self) -> None:
        """Initialize ClassContentConditional."""
        super().__init__()
        self.attributes: list[AttributeTailoring] = []
        self.condition: Optional[AbstractCondition] = None
        self.constraints: list[ConstraintTailoring] = []
        self.sdg_tailorings: list[SdgTailoring] = []


class ClassContentConditionalBuilder:
    """Builder for ClassContentConditional."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassContentConditional = ClassContentConditional()

    def build(self) -> ClassContentConditional:
        """Build and return ClassContentConditional object.

        Returns:
            ClassContentConditional instance
        """
        # TODO: Add validation
        return self._obj
