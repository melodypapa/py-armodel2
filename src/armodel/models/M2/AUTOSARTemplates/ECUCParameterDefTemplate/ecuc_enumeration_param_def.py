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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucEnumerationParamDef, cls).deserialize(element)

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.default_value = default_value_value

        # Parse literals (list from container "LITERALS")
        obj.literals = []
        container = ARObject._find_child_element(element, "LITERALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.literals.append(child_value)

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
