"""DiagnosticParameterElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticParameterElement(Identifiable):
    """AUTOSAR DiagnosticParameterElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("array_size", None, True, False, None),  # arraySize
        ("sub_elements", None, False, True, DiagnosticParameter),  # subElements
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticParameterElement."""
        super().__init__()
        self.array_size: Optional[PositiveInteger] = None
        self.sub_elements: list[DiagnosticParameter] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticParameterElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterElement":
        """Create DiagnosticParameterElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticParameterElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticParameterElement since parent returns ARObject
        return cast("DiagnosticParameterElement", obj)


class DiagnosticParameterElementBuilder:
    """Builder for DiagnosticParameterElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterElement = DiagnosticParameterElement()

    def build(self) -> DiagnosticParameterElement:
        """Build and return DiagnosticParameterElement object.

        Returns:
            DiagnosticParameterElement instance
        """
        # TODO: Add validation
        return self._obj
