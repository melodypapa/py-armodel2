"""EcucEnumerationParamDef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_enumeration_literal_def import (
    EcucEnumerationLiteralDef,
)


class EcucEnumerationParamDef(EcucParameterDef):
    """AUTOSAR EcucEnumerationParamDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # defaultValue
        "literals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucEnumerationLiteralDef,
        ),  # literals
    }

    def __init__(self) -> None:
        """Initialize EcucEnumerationParamDef."""
        super().__init__()
        self.default_value: Optional[Identifier] = None
        self.literals: list[EcucEnumerationLiteralDef] = []


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
