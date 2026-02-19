"""EcucAbstractStringParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 63)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RegularExpression,
    VerbatimString,
)
from abc import ABC, abstractmethod


class EcucAbstractStringParamDef(ARObject, ABC):
    """AUTOSAR EcucAbstractStringParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    default_value: Optional[VerbatimString]
    max_length: Optional[PositiveInteger]
    min_length: Optional[PositiveInteger]
    regular: Optional[RegularExpression]
    def __init__(self) -> None:
        """Initialize EcucAbstractStringParamDef."""
        super().__init__()
        self.default_value: Optional[VerbatimString] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min_length: Optional[PositiveInteger] = None
        self.regular: Optional[RegularExpression] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractStringParamDef":
        """Deserialize XML element to EcucAbstractStringParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractStringParamDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = ARObject._deserialize_by_tag(child, "VerbatimString")
            obj.default_value = default_value_value

        # Parse max_length
        child = ARObject._find_child_element(element, "MAX-LENGTH")
        if child is not None:
            max_length_value = child.text
            obj.max_length = max_length_value

        # Parse min_length
        child = ARObject._find_child_element(element, "MIN-LENGTH")
        if child is not None:
            min_length_value = child.text
            obj.min_length = min_length_value

        # Parse regular
        child = ARObject._find_child_element(element, "REGULAR")
        if child is not None:
            regular_value = child.text
            obj.regular = regular_value

        return obj



class EcucAbstractStringParamDefBuilder:
    """Builder for EcucAbstractStringParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractStringParamDef = EcucAbstractStringParamDef()

    def build(self) -> EcucAbstractStringParamDef:
        """Build and return EcucAbstractStringParamDef object.

        Returns:
            EcucAbstractStringParamDef instance
        """
        # TODO: Add validation
        return self._obj
