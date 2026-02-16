"""SwBitRepresentation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class SwBitRepresentation(ARObject):
    """AUTOSAR SwBitRepresentation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bit_position", None, True, False, None),  # bitPosition
        ("number_of_bits", None, True, False, None),  # numberOfBits
    ]

    def __init__(self) -> None:
        """Initialize SwBitRepresentation."""
        super().__init__()
        self.bit_position: Optional[Integer] = None
        self.number_of_bits: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwBitRepresentation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwBitRepresentation":
        """Create SwBitRepresentation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwBitRepresentation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwBitRepresentation since parent returns ARObject
        return cast("SwBitRepresentation", obj)


class SwBitRepresentationBuilder:
    """Builder for SwBitRepresentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwBitRepresentation = SwBitRepresentation()

    def build(self) -> SwBitRepresentation:
        """Build and return SwBitRepresentation object.

        Returns:
            SwBitRepresentation instance
        """
        # TODO: Add validation
        return self._obj
