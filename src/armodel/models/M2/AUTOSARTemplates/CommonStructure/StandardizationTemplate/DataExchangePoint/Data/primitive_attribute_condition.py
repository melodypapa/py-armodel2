"""PrimitiveAttributeCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class PrimitiveAttributeCondition(AttributeCondition):
    """AUTOSAR PrimitiveAttributeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute: Any
    def __init__(self) -> None:
        """Initialize PrimitiveAttributeCondition."""
        super().__init__()
        self.attribute: Any = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrimitiveAttributeCondition":
        """Deserialize XML element to PrimitiveAttributeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PrimitiveAttributeCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse attribute
        child = ARObject._find_child_element(element, "ATTRIBUTE")
        if child is not None:
            attribute_value = child.text
            obj.attribute = attribute_value

        return obj



class PrimitiveAttributeConditionBuilder:
    """Builder for PrimitiveAttributeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrimitiveAttributeCondition = PrimitiveAttributeCondition()

    def build(self) -> PrimitiveAttributeCondition:
        """Build and return PrimitiveAttributeCondition object.

        Returns:
            PrimitiveAttributeCondition instance
        """
        # TODO: Add validation
        return self._obj
