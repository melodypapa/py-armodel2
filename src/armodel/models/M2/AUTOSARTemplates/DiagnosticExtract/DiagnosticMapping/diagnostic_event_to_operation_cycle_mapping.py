"""DiagnosticEventToOperationCycleMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToOperationCycleMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToOperationCycleMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("operation_cycle", None, False, False, any (DiagnosticOperation)),  # operationCycle
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventToOperationCycleMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.operation_cycle: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventToOperationCycleMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToOperationCycleMapping":
        """Create DiagnosticEventToOperationCycleMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventToOperationCycleMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventToOperationCycleMapping since parent returns ARObject
        return cast("DiagnosticEventToOperationCycleMapping", obj)


class DiagnosticEventToOperationCycleMappingBuilder:
    """Builder for DiagnosticEventToOperationCycleMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToOperationCycleMapping = DiagnosticEventToOperationCycleMapping()

    def build(self) -> DiagnosticEventToOperationCycleMapping:
        """Build and return DiagnosticEventToOperationCycleMapping object.

        Returns:
            DiagnosticEventToOperationCycleMapping instance
        """
        # TODO: Add validation
        return self._obj
