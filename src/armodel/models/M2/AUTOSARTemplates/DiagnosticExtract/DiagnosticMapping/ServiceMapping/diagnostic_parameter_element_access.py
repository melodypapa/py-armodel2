"""DiagnosticParameterElementAccess AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterElementAccess(ARObject):
    """AUTOSAR DiagnosticParameterElementAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_elements", None, False, True, DiagnosticParameter),  # contextElements
        ("target_element", None, False, False, DiagnosticParameter),  # targetElement
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticParameterElementAccess."""
        super().__init__()
        self.context_elements: list[DiagnosticParameter] = []
        self.target_element: Optional[DiagnosticParameter] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticParameterElementAccess to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterElementAccess":
        """Create DiagnosticParameterElementAccess from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticParameterElementAccess instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticParameterElementAccess since parent returns ARObject
        return cast("DiagnosticParameterElementAccess", obj)


class DiagnosticParameterElementAccessBuilder:
    """Builder for DiagnosticParameterElementAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterElementAccess = DiagnosticParameterElementAccess()

    def build(self) -> DiagnosticParameterElementAccess:
        """Build and return DiagnosticParameterElementAccess object.

        Returns:
            DiagnosticParameterElementAccess instance
        """
        # TODO: Add validation
        return self._obj
