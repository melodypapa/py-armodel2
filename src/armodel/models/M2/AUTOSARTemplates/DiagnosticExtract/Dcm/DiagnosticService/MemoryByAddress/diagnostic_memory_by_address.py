"""DiagnosticMemoryByAddress AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticMemoryByAddress(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticMemoryByAddress."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryByAddress."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMemoryByAddress to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryByAddress":
        """Create DiagnosticMemoryByAddress from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMemoryByAddress instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMemoryByAddress since parent returns ARObject
        return cast("DiagnosticMemoryByAddress", obj)


class DiagnosticMemoryByAddressBuilder:
    """Builder for DiagnosticMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryByAddress = DiagnosticMemoryByAddress()

    def build(self) -> DiagnosticMemoryByAddress:
        """Build and return DiagnosticMemoryByAddress object.

        Returns:
            DiagnosticMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
