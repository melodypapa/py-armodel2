"""InvertCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class InvertCondition(AbstractCondition):
    """AUTOSAR InvertCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    condition: AbstractCondition
    def __init__(self) -> None:
        """Initialize InvertCondition."""
        super().__init__()
        self.condition: AbstractCondition = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InvertCondition":
        """Deserialize XML element to InvertCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InvertCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InvertCondition, cls).deserialize(element)

        # Parse condition
        child = ARObject._find_child_element(element, "CONDITION")
        if child is not None:
            condition_value = ARObject._deserialize_by_tag(child, "AbstractCondition")
            obj.condition = condition_value

        return obj



class InvertConditionBuilder:
    """Builder for InvertCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InvertCondition = InvertCondition()

    def build(self) -> InvertCondition:
        """Build and return InvertCondition object.

        Returns:
            InvertCondition instance
        """
        # TODO: Add validation
        return self._obj
