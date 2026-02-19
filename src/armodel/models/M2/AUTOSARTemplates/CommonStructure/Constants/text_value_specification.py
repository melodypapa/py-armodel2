"""TextValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 435)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2074)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class TextValueSpecification(ValueSpecification):
    """AUTOSAR TextValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[VerbatimString]
    def __init__(self) -> None:
        """Initialize TextValueSpecification."""
        super().__init__()
        self.value: Optional[VerbatimString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextValueSpecification":
        """Deserialize XML element to TextValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextValueSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class TextValueSpecificationBuilder:
    """Builder for TextValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextValueSpecification = TextValueSpecification()

    def build(self) -> TextValueSpecification:
        """Build and return TextValueSpecification object.

        Returns:
            TextValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
