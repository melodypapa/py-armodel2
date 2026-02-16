"""DiagnosticParameterIdent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.ident_caption import (
    IdentCaption,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterIdent(IdentCaption):
    """AUTOSAR DiagnosticParameterIdent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sub_elements", None, False, True, DiagnosticParameter),  # subElements
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdent."""
        super().__init__()
        self.sub_elements: list[DiagnosticParameter] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticParameterIdent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterIdent":
        """Create DiagnosticParameterIdent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticParameterIdent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticParameterIdent since parent returns ARObject
        return cast("DiagnosticParameterIdent", obj)


class DiagnosticParameterIdentBuilder:
    """Builder for DiagnosticParameterIdent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterIdent = DiagnosticParameterIdent()

    def build(self) -> DiagnosticParameterIdent:
        """Build and return DiagnosticParameterIdent object.

        Returns:
            DiagnosticParameterIdent instance
        """
        # TODO: Add validation
        return self._obj
