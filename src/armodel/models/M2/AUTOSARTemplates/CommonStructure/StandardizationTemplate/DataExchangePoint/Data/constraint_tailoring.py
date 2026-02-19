"""ConstraintTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 117)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class ConstraintTailoring(RestrictionWithSeverity):
    """AUTOSAR ConstraintTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    constraint: Optional[TraceableText]
    def __init__(self) -> None:
        """Initialize ConstraintTailoring."""
        super().__init__()
        self.constraint: Optional[TraceableText] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstraintTailoring":
        """Deserialize XML element to ConstraintTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConstraintTailoring object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse constraint
        child = ARObject._find_child_element(element, "CONSTRAINT")
        if child is not None:
            constraint_value = ARObject._deserialize_by_tag(child, "TraceableText")
            obj.constraint = constraint_value

        return obj



class ConstraintTailoringBuilder:
    """Builder for ConstraintTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstraintTailoring = ConstraintTailoring()

    def build(self) -> ConstraintTailoring:
        """Build and return ConstraintTailoring object.

        Returns:
            ConstraintTailoring instance
        """
        # TODO: Add validation
        return self._obj
