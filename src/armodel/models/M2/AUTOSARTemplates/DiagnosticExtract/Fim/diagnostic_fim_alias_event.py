"""DiagnosticFimAliasEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
    DiagnosticAbstractAliasEvent,
)


class DiagnosticFimAliasEvent(DiagnosticAbstractAliasEvent):
    """AUTOSAR DiagnosticFimAliasEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEvent."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFimAliasEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEvent":
        """Create DiagnosticFimAliasEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFimAliasEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFimAliasEvent since parent returns ARObject
        return cast("DiagnosticFimAliasEvent", obj)


class DiagnosticFimAliasEventBuilder:
    """Builder for DiagnosticFimAliasEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEvent = DiagnosticFimAliasEvent()

    def build(self) -> DiagnosticFimAliasEvent:
        """Build and return DiagnosticFimAliasEvent object.

        Returns:
            DiagnosticFimAliasEvent instance
        """
        # TODO: Add validation
        return self._obj
