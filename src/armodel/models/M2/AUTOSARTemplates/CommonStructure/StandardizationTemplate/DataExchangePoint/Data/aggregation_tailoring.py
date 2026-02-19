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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)


class AggregationTailoring(AttributeTailoring):
    """AUTOSAR AggregationTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_tailorings: list[ClassTailoring]
    def __init__(self) -> None:
        """Initialize AggregationTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AggregationTailoring":
        """Deserialize XML element to AggregationTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AggregationTailoring object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse type_tailorings (list)
        obj.type_tailorings = []
        for child in ARObject._find_all_child_elements(element, "TYPE-TAILORINGS"):
            type_tailorings_value = ARObject._deserialize_by_tag(child, "ClassTailoring")
            obj.type_tailorings.append(type_tailorings_value)

        return obj



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
