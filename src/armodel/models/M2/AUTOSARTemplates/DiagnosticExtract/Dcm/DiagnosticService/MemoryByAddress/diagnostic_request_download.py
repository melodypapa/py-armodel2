"""DiagnosticRequestDownload AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticRequestDownload(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticRequestDownload."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request", None, False, False, any (DiagnosticRequest)),  # request
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestDownload."""
        super().__init__()
        self.request: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestDownload to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestDownload":
        """Create DiagnosticRequestDownload from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestDownload instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestDownload since parent returns ARObject
        return cast("DiagnosticRequestDownload", obj)


class DiagnosticRequestDownloadBuilder:
    """Builder for DiagnosticRequestDownload."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestDownload = DiagnosticRequestDownload()

    def build(self) -> DiagnosticRequestDownload:
        """Build and return DiagnosticRequestDownload object.

        Returns:
            DiagnosticRequestDownload instance
        """
        # TODO: Add validation
        return self._obj
