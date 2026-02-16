"""DiagnosticAbstractAliasEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)


class DiagnosticAbstractAliasEvent(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAbstractAliasEvent."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAbstractAliasEvent."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAbstractAliasEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAbstractAliasEvent":
        """Create DiagnosticAbstractAliasEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAbstractAliasEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAbstractAliasEvent since parent returns ARObject
        return cast("DiagnosticAbstractAliasEvent", obj)


class DiagnosticAbstractAliasEventBuilder:
    """Builder for DiagnosticAbstractAliasEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAbstractAliasEvent = DiagnosticAbstractAliasEvent()

    def build(self) -> DiagnosticAbstractAliasEvent:
        """Build and return DiagnosticAbstractAliasEvent object.

        Returns:
            DiagnosticAbstractAliasEvent instance
        """
        # TODO: Add validation
        return self._obj
