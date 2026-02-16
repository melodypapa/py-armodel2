"""DiagnosticEnableConditionNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticEnableConditionNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEnableConditionNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("initial_status", None, False, False, EventAcceptanceStatusEnum),  # initialStatus
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionNeeds."""
        super().__init__()
        self.initial_status: Optional[EventAcceptanceStatusEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnableConditionNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableConditionNeeds":
        """Create DiagnosticEnableConditionNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnableConditionNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnableConditionNeeds since parent returns ARObject
        return cast("DiagnosticEnableConditionNeeds", obj)


class DiagnosticEnableConditionNeedsBuilder:
    """Builder for DiagnosticEnableConditionNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionNeeds = DiagnosticEnableConditionNeeds()

    def build(self) -> DiagnosticEnableConditionNeeds:
        """Build and return DiagnosticEnableConditionNeeds object.

        Returns:
            DiagnosticEnableConditionNeeds instance
        """
        # TODO: Add validation
        return self._obj
