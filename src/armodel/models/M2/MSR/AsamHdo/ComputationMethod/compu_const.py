"""CompuConst AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)


class CompuConst(ARObject):
    """AUTOSAR CompuConst."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_const_content", None, False, False, CompuConstContent),  # compuConstContent
    ]

    def __init__(self) -> None:
        """Initialize CompuConst."""
        super().__init__()
        self.compu_const_content: Optional[CompuConstContent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuConst to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuConst":
        """Create CompuConst from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuConst instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuConst since parent returns ARObject
        return cast("CompuConst", obj)


class CompuConstBuilder:
    """Builder for CompuConst."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConst = CompuConst()

    def build(self) -> CompuConst:
        """Build and return CompuConst object.

        Returns:
            CompuConst instance
        """
        # TODO: Add validation
        return self._obj
