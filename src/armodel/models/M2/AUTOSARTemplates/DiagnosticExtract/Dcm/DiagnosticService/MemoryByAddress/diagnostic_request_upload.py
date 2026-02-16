"""DiagnosticRequestUpload AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticRequestUpload."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request_upload", None, False, False, any (DiagnosticRequest)),  # requestUpload
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestUpload."""
        super().__init__()
        self.request_upload: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestUpload to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestUpload":
        """Create DiagnosticRequestUpload from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestUpload instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestUpload since parent returns ARObject
        return cast("DiagnosticRequestUpload", obj)


class DiagnosticRequestUploadBuilder:
    """Builder for DiagnosticRequestUpload."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestUpload = DiagnosticRequestUpload()

    def build(self) -> DiagnosticRequestUpload:
        """Build and return DiagnosticRequestUpload object.

        Returns:
            DiagnosticRequestUpload instance
        """
        # TODO: Add validation
        return self._obj
