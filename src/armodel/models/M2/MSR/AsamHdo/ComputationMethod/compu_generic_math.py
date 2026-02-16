"""CompuGenericMath AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
)


class CompuGenericMath(ARObject):
    """AUTOSAR CompuGenericMath."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("level", None, True, False, None),  # level
    ]

    def __init__(self) -> None:
        """Initialize CompuGenericMath."""
        super().__init__()
        self.level: Optional[PrimitiveIdentifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuGenericMath to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuGenericMath":
        """Create CompuGenericMath from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuGenericMath instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuGenericMath since parent returns ARObject
        return cast("CompuGenericMath", obj)


class CompuGenericMathBuilder:
    """Builder for CompuGenericMath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuGenericMath = CompuGenericMath()

    def build(self) -> CompuGenericMath:
        """Build and return CompuGenericMath object.

        Returns:
            CompuGenericMath instance
        """
        # TODO: Add validation
        return self._obj
