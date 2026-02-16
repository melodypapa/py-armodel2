"""DiagnosticReadMemoryByAddressClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticReadMemoryByAddressClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadMemoryByAddressClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadMemoryByAddressClass."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadMemoryByAddressClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadMemoryByAddressClass":
        """Create DiagnosticReadMemoryByAddressClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadMemoryByAddressClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadMemoryByAddressClass since parent returns ARObject
        return cast("DiagnosticReadMemoryByAddressClass", obj)


class DiagnosticReadMemoryByAddressClassBuilder:
    """Builder for DiagnosticReadMemoryByAddressClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadMemoryByAddressClass = DiagnosticReadMemoryByAddressClass()

    def build(self) -> DiagnosticReadMemoryByAddressClass:
        """Build and return DiagnosticReadMemoryByAddressClass object.

        Returns:
            DiagnosticReadMemoryByAddressClass instance
        """
        # TODO: Add validation
        return self._obj
