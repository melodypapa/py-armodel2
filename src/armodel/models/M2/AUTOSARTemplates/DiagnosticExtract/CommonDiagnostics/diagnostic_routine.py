"""DiagnosticRoutine AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_stop_routine import (
    DiagnosticStopRoutine,
)


class DiagnosticRoutine(DiagnosticCommonElement):
    """AUTOSAR DiagnosticRoutine."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("id", None, True, False, None),  # id
        ("request_result", None, False, False, any (DiagnosticRequest)),  # requestResult
        ("routine_info", None, True, False, None),  # routineInfo
        ("start", None, False, False, DiagnosticStartRoutine),  # start
        ("stop", None, False, False, DiagnosticStopRoutine),  # stop
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRoutine."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_result: Optional[Any] = None
        self.routine_info: Optional[PositiveInteger] = None
        self.start: Optional[DiagnosticStartRoutine] = None
        self.stop: Optional[DiagnosticStopRoutine] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRoutine to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutine":
        """Create DiagnosticRoutine from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRoutine instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRoutine since parent returns ARObject
        return cast("DiagnosticRoutine", obj)


class DiagnosticRoutineBuilder:
    """Builder for DiagnosticRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutine = DiagnosticRoutine()

    def build(self) -> DiagnosticRoutine:
        """Build and return DiagnosticRoutine object.

        Returns:
            DiagnosticRoutine instance
        """
        # TODO: Add validation
        return self._obj
