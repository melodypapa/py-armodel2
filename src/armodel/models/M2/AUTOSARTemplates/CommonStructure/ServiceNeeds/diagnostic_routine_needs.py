"""DiagnosticRoutineNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticRoutineNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diag_routine", None, False, False, DiagnosticRoutineTypeEnum),  # diagRoutine
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineNeeds."""
        super().__init__()
        self.diag_routine: Optional[DiagnosticRoutineTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRoutineNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineNeeds":
        """Create DiagnosticRoutineNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRoutineNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRoutineNeeds since parent returns ARObject
        return cast("DiagnosticRoutineNeeds", obj)


class DiagnosticRoutineNeedsBuilder:
    """Builder for DiagnosticRoutineNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineNeeds = DiagnosticRoutineNeeds()

    def build(self) -> DiagnosticRoutineNeeds:
        """Build and return DiagnosticRoutineNeeds object.

        Returns:
            DiagnosticRoutineNeeds instance
        """
        # TODO: Add validation
        return self._obj
