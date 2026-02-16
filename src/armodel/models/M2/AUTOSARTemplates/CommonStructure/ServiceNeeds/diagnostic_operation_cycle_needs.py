"""DiagnosticOperationCycleNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticOperationCycleNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation_cycle", None, False, False, any (OperationCycleType)),  # operationCycle
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycleNeeds."""
        super().__init__()
        self.operation_cycle: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticOperationCycleNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCycleNeeds":
        """Create DiagnosticOperationCycleNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticOperationCycleNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticOperationCycleNeeds since parent returns ARObject
        return cast("DiagnosticOperationCycleNeeds", obj)


class DiagnosticOperationCycleNeedsBuilder:
    """Builder for DiagnosticOperationCycleNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCycleNeeds = DiagnosticOperationCycleNeeds()

    def build(self) -> DiagnosticOperationCycleNeeds:
        """Build and return DiagnosticOperationCycleNeeds object.

        Returns:
            DiagnosticOperationCycleNeeds instance
        """
        # TODO: Add validation
        return self._obj
