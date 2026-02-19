"""AbstractValueRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 103)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    PositiveInteger,
    RegularExpression,
)
from abc import ABC, abstractmethod


class AbstractValueRestriction(ARObject, ABC):
    """AUTOSAR AbstractValueRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    max: Optional[Limit]
    max_length: Optional[PositiveInteger]
    min: Optional[Limit]
    min_length: Optional[PositiveInteger]
    pattern: Optional[RegularExpression]
    def __init__(self) -> None:
        """Initialize AbstractValueRestriction."""
        super().__init__()
        self.max: Optional[Limit] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min: Optional[Limit] = None
        self.min_length: Optional[PositiveInteger] = None
        self.pattern: Optional[RegularExpression] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractValueRestriction":
        """Deserialize XML element to AbstractValueRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractValueRestriction object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.max = max_value

        # Parse max_length
        child = ARObject._find_child_element(element, "MAX-LENGTH")
        if child is not None:
            max_length_value = child.text
            obj.max_length = max_length_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.min = min_value

        # Parse min_length
        child = ARObject._find_child_element(element, "MIN-LENGTH")
        if child is not None:
            min_length_value = child.text
            obj.min_length = min_length_value

        # Parse pattern
        child = ARObject._find_child_element(element, "PATTERN")
        if child is not None:
            pattern_value = child.text
            obj.pattern = pattern_value

        return obj



class AbstractValueRestrictionBuilder:
    """Builder for AbstractValueRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractValueRestriction = AbstractValueRestriction()

    def build(self) -> AbstractValueRestriction:
        """Build and return AbstractValueRestriction object.

        Returns:
            AbstractValueRestriction instance
        """
        # TODO: Add validation
        return self._obj
