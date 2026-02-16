"""DiagnosticEventToDebounceAlgorithmMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToDebounceAlgorithmMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("debounce", None, False, False, any (DiagnosticDebounce)),  # debounce
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventToDebounceAlgorithmMapping."""
        super().__init__()
        self.debounce: Optional[Any] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventToDebounceAlgorithmMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToDebounceAlgorithmMapping":
        """Create DiagnosticEventToDebounceAlgorithmMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventToDebounceAlgorithmMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventToDebounceAlgorithmMapping since parent returns ARObject
        return cast("DiagnosticEventToDebounceAlgorithmMapping", obj)


class DiagnosticEventToDebounceAlgorithmMappingBuilder:
    """Builder for DiagnosticEventToDebounceAlgorithmMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToDebounceAlgorithmMapping = DiagnosticEventToDebounceAlgorithmMapping()

    def build(self) -> DiagnosticEventToDebounceAlgorithmMapping:
        """Build and return DiagnosticEventToDebounceAlgorithmMapping object.

        Returns:
            DiagnosticEventToDebounceAlgorithmMapping instance
        """
        # TODO: Add validation
        return self._obj
