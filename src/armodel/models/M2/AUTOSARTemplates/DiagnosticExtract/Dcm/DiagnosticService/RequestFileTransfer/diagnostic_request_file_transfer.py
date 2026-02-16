"""DiagnosticRequestFileTransfer AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestFileTransfer(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestFileTransfer."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request_file", None, False, False, any (DiagnosticRequestFile)),  # requestFile
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransfer."""
        super().__init__()
        self.request_file: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestFileTransfer to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestFileTransfer":
        """Create DiagnosticRequestFileTransfer from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestFileTransfer instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestFileTransfer since parent returns ARObject
        return cast("DiagnosticRequestFileTransfer", obj)


class DiagnosticRequestFileTransferBuilder:
    """Builder for DiagnosticRequestFileTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransfer = DiagnosticRequestFileTransfer()

    def build(self) -> DiagnosticRequestFileTransfer:
        """Build and return DiagnosticRequestFileTransfer object.

        Returns:
            DiagnosticRequestFileTransfer instance
        """
        # TODO: Add validation
        return self._obj
