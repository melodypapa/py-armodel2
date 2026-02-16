"""DiagnosticFimAliasEventMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticFimAliasEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticFimAliasEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("actual_event", None, False, False, DiagnosticEvent),  # actualEvent
        ("alias_event_event", None, False, False, any (DiagnosticFimAlias)),  # aliasEventEvent
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventMapping."""
        super().__init__()
        self.actual_event: Optional[DiagnosticEvent] = None
        self.alias_event_event: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFimAliasEventMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventMapping":
        """Create DiagnosticFimAliasEventMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFimAliasEventMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFimAliasEventMapping since parent returns ARObject
        return cast("DiagnosticFimAliasEventMapping", obj)


class DiagnosticFimAliasEventMappingBuilder:
    """Builder for DiagnosticFimAliasEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventMapping = DiagnosticFimAliasEventMapping()

    def build(self) -> DiagnosticFimAliasEventMapping:
        """Build and return DiagnosticFimAliasEventMapping object.

        Returns:
            DiagnosticFimAliasEventMapping instance
        """
        # TODO: Add validation
        return self._obj
