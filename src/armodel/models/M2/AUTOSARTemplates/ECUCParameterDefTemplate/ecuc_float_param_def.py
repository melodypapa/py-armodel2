"""EcucFloatParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 61)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    Limit,
)


class EcucFloatParamDef(EcucParameterDef):
    """AUTOSAR EcucFloatParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[Float]
    max: Optional[Limit]
    min: Optional[Limit]
    def __init__(self) -> None:
        """Initialize EcucFloatParamDef."""
        super().__init__()
        self.default_value: Optional[Float] = None
        self.max: Optional[Limit] = None
        self.min: Optional[Limit] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucFloatParamDef":
        """Deserialize XML element to EcucFloatParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucFloatParamDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = child.text
            obj.default_value = default_value_value

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = child.text
            obj.max = max_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = child.text
            obj.min = min_value

        return obj



class EcucFloatParamDefBuilder:
    """Builder for EcucFloatParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucFloatParamDef = EcucFloatParamDef()

    def build(self) -> EcucFloatParamDef:
        """Build and return EcucFloatParamDef object.

        Returns:
            EcucFloatParamDef instance
        """
        # TODO: Add validation
        return self._obj
