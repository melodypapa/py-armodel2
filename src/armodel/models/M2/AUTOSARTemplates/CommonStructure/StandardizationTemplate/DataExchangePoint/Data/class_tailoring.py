"""ClassTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_content_conditional import (
    ClassContentConditional,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)


class ClassTailoring(ARObject):
    """AUTOSAR ClassTailoring."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize ClassTailoring."""
        super().__init__()
        self.class_contents: list[ClassContentConditional] = []
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None


class ClassTailoringBuilder:
    """Builder for ClassTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassTailoring = ClassTailoring()

    def build(self) -> ClassTailoring:
        """Build and return ClassTailoring object.

        Returns:
            ClassTailoring instance
        """
        # TODO: Add validation
        return self._obj
