"""DiagnosticFimEventGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticFimEventGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFimEventGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("events", None, False, True, DiagnosticEvent),  # events
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFimEventGroup."""
        super().__init__()
        self.events: list[DiagnosticEvent] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFimEventGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimEventGroup":
        """Create DiagnosticFimEventGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFimEventGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFimEventGroup since parent returns ARObject
        return cast("DiagnosticFimEventGroup", obj)


class DiagnosticFimEventGroupBuilder:
    """Builder for DiagnosticFimEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimEventGroup = DiagnosticFimEventGroup()

    def build(self) -> DiagnosticFimEventGroup:
        """Build and return DiagnosticFimEventGroup object.

        Returns:
            DiagnosticFimEventGroup instance
        """
        # TODO: Add validation
        return self._obj
