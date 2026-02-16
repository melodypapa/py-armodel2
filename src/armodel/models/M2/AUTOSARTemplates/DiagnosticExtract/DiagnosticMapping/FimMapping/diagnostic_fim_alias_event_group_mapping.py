"""DiagnosticFimAliasEventGroupMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_event_group import (
    DiagnosticFimEventGroup,
)


class DiagnosticFimAliasEventGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticFimAliasEventGroupMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("actual_event", None, False, False, DiagnosticFimEventGroup),  # actualEvent
        ("alias_event", None, False, False, any (DiagnosticFimAlias)),  # aliasEvent
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroupMapping."""
        super().__init__()
        self.actual_event: Optional[DiagnosticFimEventGroup] = None
        self.alias_event: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFimAliasEventGroupMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventGroupMapping":
        """Create DiagnosticFimAliasEventGroupMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFimAliasEventGroupMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFimAliasEventGroupMapping since parent returns ARObject
        return cast("DiagnosticFimAliasEventGroupMapping", obj)


class DiagnosticFimAliasEventGroupMappingBuilder:
    """Builder for DiagnosticFimAliasEventGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventGroupMapping = DiagnosticFimAliasEventGroupMapping()

    def build(self) -> DiagnosticFimAliasEventGroupMapping:
        """Build and return DiagnosticFimAliasEventGroupMapping object.

        Returns:
            DiagnosticFimAliasEventGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
