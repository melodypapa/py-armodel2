"""DiagnosticSwMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)


class DiagnosticSwMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSwMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSwMapping."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSwMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSwMapping":
        """Create DiagnosticSwMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSwMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSwMapping since parent returns ARObject
        return cast("DiagnosticSwMapping", obj)


class DiagnosticSwMappingBuilder:
    """Builder for DiagnosticSwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSwMapping = DiagnosticSwMapping()

    def build(self) -> DiagnosticSwMapping:
        """Build and return DiagnosticSwMapping object.

        Returns:
            DiagnosticSwMapping instance
        """
        # TODO: Add validation
        return self._obj
