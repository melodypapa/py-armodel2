"""DiagnosticEventToTroubleCodeUdsMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticEventToTroubleCodeUdsMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToTroubleCodeUdsMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("trouble_code_uds", None, False, False, DiagnosticTroubleCode),  # troubleCodeUds
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventToTroubleCodeUdsMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.trouble_code_uds: Optional[DiagnosticTroubleCode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventToTroubleCodeUdsMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToTroubleCodeUdsMapping":
        """Create DiagnosticEventToTroubleCodeUdsMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventToTroubleCodeUdsMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventToTroubleCodeUdsMapping since parent returns ARObject
        return cast("DiagnosticEventToTroubleCodeUdsMapping", obj)


class DiagnosticEventToTroubleCodeUdsMappingBuilder:
    """Builder for DiagnosticEventToTroubleCodeUdsMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToTroubleCodeUdsMapping = DiagnosticEventToTroubleCodeUdsMapping()

    def build(self) -> DiagnosticEventToTroubleCodeUdsMapping:
        """Build and return DiagnosticEventToTroubleCodeUdsMapping object.

        Returns:
            DiagnosticEventToTroubleCodeUdsMapping instance
        """
        # TODO: Add validation
        return self._obj
