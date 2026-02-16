"""EcucEnumerationParamDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_value", None, True, False, None),  # defaultValue
        ("literals", None, False, True, EcucEnumerationLiteralDef),  # literals
    ]

    def __init__(self) -> None:
        """Initialize EcucEnumerationParamDef."""
        super().__init__()
        self.default_value: Optional[Identifier] = None
        self.literals: list[EcucEnumerationLiteralDef] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucEnumerationParamDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationParamDef":
        """Create EcucEnumerationParamDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucEnumerationParamDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucEnumerationParamDef since parent returns ARObject
        return cast("EcucEnumerationParamDef", obj)


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
