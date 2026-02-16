"""Sd AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    VerbatimStringPlain,
)


class Sd(ARObject):
    """AUTOSAR Sd."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("gid", None, True, False, None),  # gid
        ("value", None, True, False, None),  # value
        ("xml_space", None, False, False, None),  # xmlSpace
    ]

    def __init__(self) -> None:
        """Initialize Sd."""
        super().__init__()
        self.gid: NameToken = None
        self.value: VerbatimStringPlain = None
        self.xml_space: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Sd to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sd":
        """Create Sd from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Sd instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Sd since parent returns ARObject
        return cast("Sd", obj)


class SdBuilder:
    """Builder for Sd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sd = Sd()

    def build(self) -> Sd:
        """Build and return Sd object.

        Returns:
            Sd instance
        """
        # TODO: Add validation
        return self._obj
