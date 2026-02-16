"""Tbody AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class Tbody(ARObject):
    """AUTOSAR Tbody."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("valign", None, False, False, ValignEnum),  # valign
    ]

    def __init__(self) -> None:
        """Initialize Tbody."""
        super().__init__()
        self.valign: Optional[ValignEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Tbody to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tbody":
        """Create Tbody from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Tbody instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Tbody since parent returns ARObject
        return cast("Tbody", obj)


class TbodyBuilder:
    """Builder for Tbody."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tbody = Tbody()

    def build(self) -> Tbody:
        """Build and return Tbody object.

        Returns:
            Tbody instance
        """
        # TODO: Add validation
        return self._obj
