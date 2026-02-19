"""TextTableValuePair AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class TextTableValuePair(ARObject):
    """AUTOSAR TextTableValuePair."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_value: Optional[Numerical]
    second_value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize TextTableValuePair."""
        super().__init__()
        self.first_value: Optional[Numerical] = None
        self.second_value: Optional[Numerical] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableValuePair":
        """Deserialize XML element to TextTableValuePair object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextTableValuePair object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_value
        child = ARObject._find_child_element(element, "FIRST-VALUE")
        if child is not None:
            first_value_value = child.text
            obj.first_value = first_value_value

        # Parse second_value
        child = ARObject._find_child_element(element, "SECOND-VALUE")
        if child is not None:
            second_value_value = child.text
            obj.second_value = second_value_value

        return obj



class TextTableValuePairBuilder:
    """Builder for TextTableValuePair."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextTableValuePair = TextTableValuePair()

    def build(self) -> TextTableValuePair:
        """Build and return TextTableValuePair object.

        Returns:
            TextTableValuePair instance
        """
        # TODO: Add validation
        return self._obj
