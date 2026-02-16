"""DiagnosticRequestUploadClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestUploadClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestUploadClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestUploadClass."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestUploadClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestUploadClass":
        """Create DiagnosticRequestUploadClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestUploadClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestUploadClass since parent returns ARObject
        return cast("DiagnosticRequestUploadClass", obj)


class DiagnosticRequestUploadClassBuilder:
    """Builder for DiagnosticRequestUploadClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestUploadClass = DiagnosticRequestUploadClass()

    def build(self) -> DiagnosticRequestUploadClass:
        """Build and return DiagnosticRequestUploadClass object.

        Returns:
            DiagnosticRequestUploadClass instance
        """
        # TODO: Add validation
        return self._obj
