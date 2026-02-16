"""DiagnosticControlNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticControlNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticControlNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticControlNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticControlNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlNeeds":
        """Create DiagnosticControlNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticControlNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticControlNeeds since parent returns ARObject
        return cast("DiagnosticControlNeeds", obj)


class DiagnosticControlNeedsBuilder:
    """Builder for DiagnosticControlNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlNeeds = DiagnosticControlNeeds()

    def build(self) -> DiagnosticControlNeeds:
        """Build and return DiagnosticControlNeeds object.

        Returns:
            DiagnosticControlNeeds instance
        """
        # TODO: Add validation
        return self._obj
