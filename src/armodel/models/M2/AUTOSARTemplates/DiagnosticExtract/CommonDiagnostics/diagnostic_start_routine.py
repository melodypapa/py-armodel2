"""DiagnosticStartRoutine AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import (
    DiagnosticRoutineSubfunction,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticStartRoutine(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticStartRoutine."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("requests", None, False, True, DiagnosticParameter),  # requests
        ("responses", None, False, True, DiagnosticParameter),  # responses
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticStartRoutine."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticStartRoutine to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStartRoutine":
        """Create DiagnosticStartRoutine from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticStartRoutine instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticStartRoutine since parent returns ARObject
        return cast("DiagnosticStartRoutine", obj)


class DiagnosticStartRoutineBuilder:
    """Builder for DiagnosticStartRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStartRoutine = DiagnosticStartRoutine()

    def build(self) -> DiagnosticStartRoutine:
        """Build and return DiagnosticStartRoutine object.

        Returns:
            DiagnosticStartRoutine instance
        """
        # TODO: Add validation
        return self._obj
