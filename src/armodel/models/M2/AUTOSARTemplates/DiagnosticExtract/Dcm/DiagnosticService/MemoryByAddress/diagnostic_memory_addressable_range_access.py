"""DiagnosticMemoryAddressableRangeAccess AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticMemoryAddressableRangeAccess."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("memory_ranges", None, False, True, any (DiagnosticMemory)),  # memoryRanges
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryAddressableRangeAccess."""
        super().__init__()
        self.memory_ranges: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMemoryAddressableRangeAccess to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryAddressableRangeAccess":
        """Create DiagnosticMemoryAddressableRangeAccess from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMemoryAddressableRangeAccess instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMemoryAddressableRangeAccess since parent returns ARObject
        return cast("DiagnosticMemoryAddressableRangeAccess", obj)


class DiagnosticMemoryAddressableRangeAccessBuilder:
    """Builder for DiagnosticMemoryAddressableRangeAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryAddressableRangeAccess = DiagnosticMemoryAddressableRangeAccess()

    def build(self) -> DiagnosticMemoryAddressableRangeAccess:
        """Build and return DiagnosticMemoryAddressableRangeAccess object.

        Returns:
            DiagnosticMemoryAddressableRangeAccess instance
        """
        # TODO: Add validation
        return self._obj
