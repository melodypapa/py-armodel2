"""DiagnosticEcuResetClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticEcuResetClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("respond_to", None, False, False, DiagnosticResponseToEcuResetEnum),  # respondTo
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEcuResetClass."""
        super().__init__()
        self.respond_to: Optional[DiagnosticResponseToEcuResetEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEcuResetClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuResetClass":
        """Create DiagnosticEcuResetClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEcuResetClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEcuResetClass since parent returns ARObject
        return cast("DiagnosticEcuResetClass", obj)


class DiagnosticEcuResetClassBuilder:
    """Builder for DiagnosticEcuResetClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuResetClass = DiagnosticEcuResetClass()

    def build(self) -> DiagnosticEcuResetClass:
        """Build and return DiagnosticEcuResetClass object.

        Returns:
            DiagnosticEcuResetClass instance
        """
        # TODO: Add validation
        return self._obj
