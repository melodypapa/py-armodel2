"""DiagnosticEventToTroubleCodeJ1939Mapping AUTOSAR element."""

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


class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToTroubleCodeJ1939Mapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("trouble_code", None, False, False, DiagnosticTroubleCode),  # troubleCode
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventToTroubleCodeJ1939Mapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.trouble_code: Optional[DiagnosticTroubleCode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventToTroubleCodeJ1939Mapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """Create DiagnosticEventToTroubleCodeJ1939Mapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventToTroubleCodeJ1939Mapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventToTroubleCodeJ1939Mapping since parent returns ARObject
        return cast("DiagnosticEventToTroubleCodeJ1939Mapping", obj)


class DiagnosticEventToTroubleCodeJ1939MappingBuilder:
    """Builder for DiagnosticEventToTroubleCodeJ1939Mapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToTroubleCodeJ1939Mapping = DiagnosticEventToTroubleCodeJ1939Mapping()

    def build(self) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        """Build and return DiagnosticEventToTroubleCodeJ1939Mapping object.

        Returns:
            DiagnosticEventToTroubleCodeJ1939Mapping instance
        """
        # TODO: Add validation
        return self._obj
