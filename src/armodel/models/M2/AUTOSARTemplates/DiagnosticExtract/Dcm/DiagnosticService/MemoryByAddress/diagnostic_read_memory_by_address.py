"""DiagnosticReadMemoryByAddress AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticReadMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticReadMemoryByAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("read_class", None, False, False, any (DiagnosticReadMemory)),  # readClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadMemoryByAddress."""
        super().__init__()
        self.read_class: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadMemoryByAddress to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadMemoryByAddress":
        """Create DiagnosticReadMemoryByAddress from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadMemoryByAddress instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadMemoryByAddress since parent returns ARObject
        return cast("DiagnosticReadMemoryByAddress", obj)


class DiagnosticReadMemoryByAddressBuilder:
    """Builder for DiagnosticReadMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadMemoryByAddress = DiagnosticReadMemoryByAddress()

    def build(self) -> DiagnosticReadMemoryByAddress:
        """Build and return DiagnosticReadMemoryByAddress object.

        Returns:
            DiagnosticReadMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
