"""DiagnosticWriteMemoryByAddress AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticWriteMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticWriteMemoryByAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("write_class", None, False, False, any (DiagnosticWriteMemory)),  # writeClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticWriteMemoryByAddress."""
        super().__init__()
        self.write_class: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticWriteMemoryByAddress to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticWriteMemoryByAddress":
        """Create DiagnosticWriteMemoryByAddress from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticWriteMemoryByAddress instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticWriteMemoryByAddress since parent returns ARObject
        return cast("DiagnosticWriteMemoryByAddress", obj)


class DiagnosticWriteMemoryByAddressBuilder:
    """Builder for DiagnosticWriteMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteMemoryByAddress = DiagnosticWriteMemoryByAddress()

    def build(self) -> DiagnosticWriteMemoryByAddress:
        """Build and return DiagnosticWriteMemoryByAddress object.

        Returns:
            DiagnosticWriteMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
