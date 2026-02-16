"""CompuConstNumericContent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class CompuConstNumericContent(CompuConstContent):
    """AUTOSAR CompuConstNumericContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("v", None, True, False, None),  # v
    ]

    def __init__(self) -> None:
        """Initialize CompuConstNumericContent."""
        super().__init__()
        self.v: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuConstNumericContent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuConstNumericContent":
        """Create CompuConstNumericContent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuConstNumericContent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuConstNumericContent since parent returns ARObject
        return cast("CompuConstNumericContent", obj)


class CompuConstNumericContentBuilder:
    """Builder for CompuConstNumericContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstNumericContent = CompuConstNumericContent()

    def build(self) -> CompuConstNumericContent:
        """Build and return CompuConstNumericContent object.

        Returns:
            CompuConstNumericContent instance
        """
        # TODO: Add validation
        return self._obj
