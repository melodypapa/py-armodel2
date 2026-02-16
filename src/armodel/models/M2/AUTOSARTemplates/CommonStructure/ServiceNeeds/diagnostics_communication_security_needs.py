"""DiagnosticsCommunicationSecurityNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticsCommunicationSecurityNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticsCommunicationSecurityNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticsCommunicationSecurityNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticsCommunicationSecurityNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticsCommunicationSecurityNeeds":
        """Create DiagnosticsCommunicationSecurityNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticsCommunicationSecurityNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticsCommunicationSecurityNeeds since parent returns ARObject
        return cast("DiagnosticsCommunicationSecurityNeeds", obj)


class DiagnosticsCommunicationSecurityNeedsBuilder:
    """Builder for DiagnosticsCommunicationSecurityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticsCommunicationSecurityNeeds = DiagnosticsCommunicationSecurityNeeds()

    def build(self) -> DiagnosticsCommunicationSecurityNeeds:
        """Build and return DiagnosticsCommunicationSecurityNeeds object.

        Returns:
            DiagnosticsCommunicationSecurityNeeds instance
        """
        # TODO: Add validation
        return self._obj
