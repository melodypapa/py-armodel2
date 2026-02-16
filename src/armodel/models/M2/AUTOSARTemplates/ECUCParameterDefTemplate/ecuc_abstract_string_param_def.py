"""EcucAbstractStringParamDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RegularExpression,
    VerbatimString,
)


class EcucAbstractStringParamDef(ARObject):
    """AUTOSAR EcucAbstractStringParamDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_value", None, True, False, None),  # defaultValue
        ("max_length", None, True, False, None),  # maxLength
        ("min_length", None, True, False, None),  # minLength
        ("regular", None, True, False, None),  # regular
    ]

    def __init__(self) -> None:
        """Initialize EcucAbstractStringParamDef."""
        super().__init__()
        self.default_value: Optional[VerbatimString] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min_length: Optional[PositiveInteger] = None
        self.regular: Optional[RegularExpression] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAbstractStringParamDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractStringParamDef":
        """Create EcucAbstractStringParamDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAbstractStringParamDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAbstractStringParamDef since parent returns ARObject
        return cast("EcucAbstractStringParamDef", obj)


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
