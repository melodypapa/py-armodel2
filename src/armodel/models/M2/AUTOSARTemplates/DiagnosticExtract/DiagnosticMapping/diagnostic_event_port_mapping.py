"""DiagnosticEventPortMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEventPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_service", None, False, False, any (BswService)),  # bswService
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("swc_flat_service", None, False, False, any (SwcService)),  # swcFlatService
        ("swc_service", None, False, False, any (SwcService)),  # swcService
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventPortMapping."""
        super().__init__()
        self.bsw_service: Optional[Any] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventPortMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventPortMapping":
        """Create DiagnosticEventPortMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventPortMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventPortMapping since parent returns ARObject
        return cast("DiagnosticEventPortMapping", obj)


class DiagnosticEventPortMappingBuilder:
    """Builder for DiagnosticEventPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventPortMapping = DiagnosticEventPortMapping()

    def build(self) -> DiagnosticEventPortMapping:
        """Build and return DiagnosticEventPortMapping object.

        Returns:
            DiagnosticEventPortMapping instance
        """
        # TODO: Add validation
        return self._obj
