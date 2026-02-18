"""ReferenceTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.unresolved_reference_restriction_with_severity import (
    UnresolvedReferenceRestrictionWithSeverity,
)


class ReferenceTailoring(AttributeTailoring):
    """AUTOSAR ReferenceTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_tailorings: list[ClassTailoring]
    unresolved_restriction_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ReferenceTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []
        self.unresolved_restriction_ref: Optional[ARRef] = None


class ReferenceTailoringBuilder:
    """Builder for ReferenceTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceTailoring = ReferenceTailoring()

    def build(self) -> ReferenceTailoring:
        """Build and return ReferenceTailoring object.

        Returns:
            ReferenceTailoring instance
        """
        # TODO: Add validation
        return self._obj
