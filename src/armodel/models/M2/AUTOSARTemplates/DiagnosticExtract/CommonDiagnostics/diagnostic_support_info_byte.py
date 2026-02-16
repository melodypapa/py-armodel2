"""DiagnosticSupportInfoByte AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticSupportInfoByte(ARObject):
    """AUTOSAR DiagnosticSupportInfoByte."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("position", None, True, False, None),  # position
        ("size", None, True, False, None),  # size
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSupportInfoByte."""
        super().__init__()
        self.position: Optional[PositiveInteger] = None
        self.size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSupportInfoByte to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSupportInfoByte":
        """Create DiagnosticSupportInfoByte from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSupportInfoByte instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSupportInfoByte since parent returns ARObject
        return cast("DiagnosticSupportInfoByte", obj)


class DiagnosticSupportInfoByteBuilder:
    """Builder for DiagnosticSupportInfoByte."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSupportInfoByte = DiagnosticSupportInfoByte()

    def build(self) -> DiagnosticSupportInfoByte:
        """Build and return DiagnosticSupportInfoByte object.

        Returns:
            DiagnosticSupportInfoByte instance
        """
        # TODO: Add validation
        return self._obj
