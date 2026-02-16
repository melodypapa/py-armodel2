"""DiagnosticMemoryDestinationPrimary AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)


class DiagnosticMemoryDestinationPrimary(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationPrimary."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type_of_dtc", None, False, False, DiagnosticTypeOfDtcSupportedEnum),  # typeOfDtc
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationPrimary."""
        super().__init__()
        self.type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMemoryDestinationPrimary to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestinationPrimary":
        """Create DiagnosticMemoryDestinationPrimary from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMemoryDestinationPrimary instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMemoryDestinationPrimary since parent returns ARObject
        return cast("DiagnosticMemoryDestinationPrimary", obj)


class DiagnosticMemoryDestinationPrimaryBuilder:
    """Builder for DiagnosticMemoryDestinationPrimary."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestinationPrimary = DiagnosticMemoryDestinationPrimary()

    def build(self) -> DiagnosticMemoryDestinationPrimary:
        """Build and return DiagnosticMemoryDestinationPrimary object.

        Returns:
            DiagnosticMemoryDestinationPrimary instance
        """
        # TODO: Add validation
        return self._obj
