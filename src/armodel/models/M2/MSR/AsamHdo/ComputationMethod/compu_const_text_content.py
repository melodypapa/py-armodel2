"""CompuConstTextContent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class CompuConstTextContent(CompuConstContent):
    """AUTOSAR CompuConstTextContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("vt", None, True, False, None),  # vt
    ]

    def __init__(self) -> None:
        """Initialize CompuConstTextContent."""
        super().__init__()
        self.vt: Optional[VerbatimString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuConstTextContent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuConstTextContent":
        """Create CompuConstTextContent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuConstTextContent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuConstTextContent since parent returns ARObject
        return cast("CompuConstTextContent", obj)


class CompuConstTextContentBuilder:
    """Builder for CompuConstTextContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstTextContent = CompuConstTextContent()

    def build(self) -> CompuConstTextContent:
        """Build and return CompuConstTextContent object.

        Returns:
            CompuConstTextContent instance
        """
        # TODO: Add validation
        return self._obj
