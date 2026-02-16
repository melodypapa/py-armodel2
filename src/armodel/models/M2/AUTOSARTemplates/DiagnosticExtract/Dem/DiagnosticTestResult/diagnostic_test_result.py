"""DiagnosticTestResult AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_identifier import (
    DiagnosticTestIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_result import (
    DiagnosticTestResult,
)


class DiagnosticTestResult(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestResult."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("monitored", None, False, False, any (Diagnostic)),  # monitored
        ("test_identifier", None, False, False, DiagnosticTestIdentifier),  # testIdentifier
        ("update_kind", None, False, False, DiagnosticTestResult),  # updateKind
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTestResult."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.monitored: Optional[Any] = None
        self.test_identifier: Optional[DiagnosticTestIdentifier] = None
        self.update_kind: Optional[DiagnosticTestResult] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTestResult to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestResult":
        """Create DiagnosticTestResult from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTestResult instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTestResult since parent returns ARObject
        return cast("DiagnosticTestResult", obj)


class DiagnosticTestResultBuilder:
    """Builder for DiagnosticTestResult."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestResult = DiagnosticTestResult()

    def build(self) -> DiagnosticTestResult:
        """Build and return DiagnosticTestResult object.

        Returns:
            DiagnosticTestResult instance
        """
        # TODO: Add validation
        return self._obj
