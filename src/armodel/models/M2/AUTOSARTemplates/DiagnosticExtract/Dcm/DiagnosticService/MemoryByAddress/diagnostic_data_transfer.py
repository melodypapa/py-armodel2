"""DiagnosticDataTransfer AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_data_transfer import (
    DiagnosticDataTransfer,
)


class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticDataTransfer."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_transfer", None, False, False, DiagnosticDataTransfer),  # dataTransfer
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticDataTransfer."""
        super().__init__()
        self.data_transfer: Optional[DiagnosticDataTransfer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticDataTransfer to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataTransfer":
        """Create DiagnosticDataTransfer from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticDataTransfer instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticDataTransfer since parent returns ARObject
        return cast("DiagnosticDataTransfer", obj)


class DiagnosticDataTransferBuilder:
    """Builder for DiagnosticDataTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataTransfer = DiagnosticDataTransfer()

    def build(self) -> DiagnosticDataTransfer:
        """Build and return DiagnosticDataTransfer object.

        Returns:
            DiagnosticDataTransfer instance
        """
        # TODO: Add validation
        return self._obj
