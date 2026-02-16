"""DiagnosticRoutineSubfunction AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)


class DiagnosticRoutineSubfunction(Identifiable):
    """AUTOSAR DiagnosticRoutineSubfunction."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("access", None, False, False, DiagnosticAccessPermission),  # access
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineSubfunction."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRoutineSubfunction to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineSubfunction":
        """Create DiagnosticRoutineSubfunction from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRoutineSubfunction instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRoutineSubfunction since parent returns ARObject
        return cast("DiagnosticRoutineSubfunction", obj)


class DiagnosticRoutineSubfunctionBuilder:
    """Builder for DiagnosticRoutineSubfunction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineSubfunction = DiagnosticRoutineSubfunction()

    def build(self) -> DiagnosticRoutineSubfunction:
        """Build and return DiagnosticRoutineSubfunction object.

        Returns:
            DiagnosticRoutineSubfunction instance
        """
        # TODO: Add validation
        return self._obj
