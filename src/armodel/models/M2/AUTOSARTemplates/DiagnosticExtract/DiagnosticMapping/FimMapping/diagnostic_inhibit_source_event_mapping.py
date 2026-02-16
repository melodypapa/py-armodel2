"""DiagnosticInhibitSourceEventMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_event_group import (
    DiagnosticFimEventGroup,
)


class DiagnosticInhibitSourceEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticInhibitSourceEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("event_group_group", None, False, False, DiagnosticFimEventGroup),  # eventGroupGroup
        ("inhibition_source", None, False, False, any (DiagnosticFunction)),  # inhibitionSource
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticInhibitSourceEventMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.event_group_group: Optional[DiagnosticFimEventGroup] = None
        self.inhibition_source: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticInhibitSourceEventMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticInhibitSourceEventMapping":
        """Create DiagnosticInhibitSourceEventMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticInhibitSourceEventMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticInhibitSourceEventMapping since parent returns ARObject
        return cast("DiagnosticInhibitSourceEventMapping", obj)


class DiagnosticInhibitSourceEventMappingBuilder:
    """Builder for DiagnosticInhibitSourceEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticInhibitSourceEventMapping = DiagnosticInhibitSourceEventMapping()

    def build(self) -> DiagnosticInhibitSourceEventMapping:
        """Build and return DiagnosticInhibitSourceEventMapping object.

        Returns:
            DiagnosticInhibitSourceEventMapping instance
        """
        # TODO: Add validation
        return self._obj
