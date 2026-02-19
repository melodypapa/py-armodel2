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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class TextualCondition(AbstractCondition):
    """AUTOSAR TextualCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    text: String
    def __init__(self) -> None:
        """Initialize TextualCondition."""
        super().__init__()
        self.text: String = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextualCondition":
        """Deserialize XML element to TextualCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextualCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse text
        child = ARObject._find_child_element(element, "TEXT")
        if child is not None:
            text_value = child.text
            obj.text = text_value

        return obj



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
