"""DiagnosticRoutineControl AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine import (
    DiagnosticRoutine,
)


class DiagnosticRoutineControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRoutineControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("routine", None, False, False, DiagnosticRoutine),  # routine
        ("routine_control", None, False, False, DiagnosticRoutine),  # routineControl
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineControl."""
        super().__init__()
        self.routine: Optional[DiagnosticRoutine] = None
        self.routine_control: Optional[DiagnosticRoutine] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRoutineControl to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineControl":
        """Create DiagnosticRoutineControl from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRoutineControl instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRoutineControl since parent returns ARObject
        return cast("DiagnosticRoutineControl", obj)


class DiagnosticRoutineControlBuilder:
    """Builder for DiagnosticRoutineControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineControl = DiagnosticRoutineControl()

    def build(self) -> DiagnosticRoutineControl:
        """Build and return DiagnosticRoutineControl object.

        Returns:
            DiagnosticRoutineControl instance
        """
        # TODO: Add validation
        return self._obj
