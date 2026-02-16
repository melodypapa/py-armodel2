"""DiagnosticEnvBswModeElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_mode_element import (
    DiagnosticEnvModeElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class DiagnosticEnvBswModeElement(DiagnosticEnvModeElement):
    """AUTOSAR DiagnosticEnvBswModeElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode", None, False, False, ModeDeclaration),  # mode
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnvBswModeElement."""
        super().__init__()
        self.mode: Optional[ModeDeclaration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnvBswModeElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvBswModeElement":
        """Create DiagnosticEnvBswModeElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnvBswModeElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnvBswModeElement since parent returns ARObject
        return cast("DiagnosticEnvBswModeElement", obj)


class DiagnosticEnvBswModeElementBuilder:
    """Builder for DiagnosticEnvBswModeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvBswModeElement = DiagnosticEnvBswModeElement()

    def build(self) -> DiagnosticEnvBswModeElement:
        """Build and return DiagnosticEnvBswModeElement object.

        Returns:
            DiagnosticEnvBswModeElement instance
        """
        # TODO: Add validation
        return self._obj
