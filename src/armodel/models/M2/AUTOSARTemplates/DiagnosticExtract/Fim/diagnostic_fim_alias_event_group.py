"""DiagnosticFimAliasEventGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
    DiagnosticAbstractAliasEvent,
)


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """AUTOSAR DiagnosticFimAliasEventGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("grouped_aliases", None, False, True, any (DiagnosticFimAlias)),  # groupedAliases
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroup."""
        super().__init__()
        self.grouped_aliases: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFimAliasEventGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventGroup":
        """Create DiagnosticFimAliasEventGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFimAliasEventGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFimAliasEventGroup since parent returns ARObject
        return cast("DiagnosticFimAliasEventGroup", obj)


class DiagnosticFimAliasEventGroupBuilder:
    """Builder for DiagnosticFimAliasEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventGroup = DiagnosticFimAliasEventGroup()

    def build(self) -> DiagnosticFimAliasEventGroup:
        """Build and return DiagnosticFimAliasEventGroup object.

        Returns:
            DiagnosticFimAliasEventGroup instance
        """
        # TODO: Add validation
        return self._obj
