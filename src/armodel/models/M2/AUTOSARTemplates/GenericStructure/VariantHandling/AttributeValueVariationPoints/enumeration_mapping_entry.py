"""EnumerationMappingEntry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class EnumerationMappingEntry(ARObject):
    """AUTOSAR EnumerationMappingEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enumerator: NameToken
    numerical_value: PositiveInteger
    def __init__(self) -> None:
        """Initialize EnumerationMappingEntry."""
        super().__init__()
        self.enumerator: NameToken = None
        self.numerical_value: PositiveInteger = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EnumerationMappingEntry":
        """Deserialize XML element to EnumerationMappingEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EnumerationMappingEntry object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse enumerator
        child = ARObject._find_child_element(element, "ENUMERATOR")
        if child is not None:
            enumerator_value = child.text
            obj.enumerator = enumerator_value

        # Parse numerical_value
        child = ARObject._find_child_element(element, "NUMERICAL-VALUE")
        if child is not None:
            numerical_value_value = child.text
            obj.numerical_value = numerical_value_value

        return obj



class EnumerationMappingEntryBuilder:
    """Builder for EnumerationMappingEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EnumerationMappingEntry = EnumerationMappingEntry()

    def build(self) -> EnumerationMappingEntry:
        """Build and return EnumerationMappingEntry object.

        Returns:
            EnumerationMappingEntry instance
        """
        # TODO: Add validation
        return self._obj
