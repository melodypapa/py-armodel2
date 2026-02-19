"""EcucEnumerationParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 66)
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
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_enumeration_literal_def import (
    EcucEnumerationLiteralDef,
)


class EcucEnumerationParamDef(EcucParameterDef):
    """AUTOSAR EcucEnumerationParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[Identifier]
    literals: list[EcucEnumerationLiteralDef]
    def __init__(self) -> None:
        """Initialize EcucEnumerationParamDef."""
        super().__init__()
        self.default_value: Optional[Identifier] = None
        self.literals: list[EcucEnumerationLiteralDef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationParamDef":
        """Deserialize XML element to EcucEnumerationParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucEnumerationParamDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = child.text
            obj.default_value = default_value_value

        # Parse literals (list)
        obj.literals = []
        for child in ARObject._find_all_child_elements(element, "LITERALS"):
            literals_value = ARObject._deserialize_by_tag(child, "EcucEnumerationLiteralDef")
            obj.literals.append(literals_value)

        return obj



class EcucEnumerationParamDefBuilder:
    """Builder for EcucEnumerationParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucEnumerationParamDef = EcucEnumerationParamDef()

    def build(self) -> EcucEnumerationParamDef:
        """Build and return EcucEnumerationParamDef object.

        Returns:
            EcucEnumerationParamDef instance
        """
        # TODO: Add validation
        return self._obj
