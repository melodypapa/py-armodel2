"""EcucEnumerationLiteralDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucEnumerationLiteralDef(Identifiable):
    """AUTOSAR EcucEnumerationLiteralDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc_cond", None, False, False, any (EcucCondition)),  # ecucCond
        ("origin", None, True, False, None),  # origin
    ]

    def __init__(self) -> None:
        """Initialize EcucEnumerationLiteralDef."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.origin: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucEnumerationLiteralDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationLiteralDef":
        """Create EcucEnumerationLiteralDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucEnumerationLiteralDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucEnumerationLiteralDef since parent returns ARObject
        return cast("EcucEnumerationLiteralDef", obj)


class EcucEnumerationLiteralDefBuilder:
    """Builder for EcucEnumerationLiteralDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucEnumerationLiteralDef = EcucEnumerationLiteralDef()

    def build(self) -> EcucEnumerationLiteralDef:
        """Build and return EcucEnumerationLiteralDef object.

        Returns:
            EcucEnumerationLiteralDef instance
        """
        # TODO: Add validation
        return self._obj
