"""CompuConstFormulaContent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class CompuConstFormulaContent(CompuConstContent):
    """AUTOSAR CompuConstFormulaContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("vf", None, True, False, None),  # vf
    ]

    def __init__(self) -> None:
        """Initialize CompuConstFormulaContent."""
        super().__init__()
        self.vf: Numerical = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuConstFormulaContent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuConstFormulaContent":
        """Create CompuConstFormulaContent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuConstFormulaContent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuConstFormulaContent since parent returns ARObject
        return cast("CompuConstFormulaContent", obj)


class CompuConstFormulaContentBuilder:
    """Builder for CompuConstFormulaContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstFormulaContent = CompuConstFormulaContent()

    def build(self) -> CompuConstFormulaContent:
        """Build and return CompuConstFormulaContent object.

        Returns:
            CompuConstFormulaContent instance
        """
        # TODO: Add validation
        return self._obj
