"""DiagnosticRequestFileTransferNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticRequestFileTransferNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticRequestFileTransferNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransferNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestFileTransferNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestFileTransferNeeds":
        """Create DiagnosticRequestFileTransferNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestFileTransferNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestFileTransferNeeds since parent returns ARObject
        return cast("DiagnosticRequestFileTransferNeeds", obj)


class DiagnosticRequestFileTransferNeedsBuilder:
    """Builder for DiagnosticRequestFileTransferNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransferNeeds = DiagnosticRequestFileTransferNeeds()

    def build(self) -> DiagnosticRequestFileTransferNeeds:
        """Build and return DiagnosticRequestFileTransferNeeds object.

        Returns:
            DiagnosticRequestFileTransferNeeds instance
        """
        # TODO: Add validation
        return self._obj
