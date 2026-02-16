"""DiagnosticStorageConditionNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticStorageConditionNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticStorageConditionNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("initial_status", None, False, False, StorageConditionStatusEnum),  # initialStatus
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionNeeds."""
        super().__init__()
        self.initial_status: Optional[StorageConditionStatusEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticStorageConditionNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionNeeds":
        """Create DiagnosticStorageConditionNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticStorageConditionNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticStorageConditionNeeds since parent returns ARObject
        return cast("DiagnosticStorageConditionNeeds", obj)


class DiagnosticStorageConditionNeedsBuilder:
    """Builder for DiagnosticStorageConditionNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionNeeds = DiagnosticStorageConditionNeeds()

    def build(self) -> DiagnosticStorageConditionNeeds:
        """Build and return DiagnosticStorageConditionNeeds object.

        Returns:
            DiagnosticStorageConditionNeeds instance
        """
        # TODO: Add validation
        return self._obj
