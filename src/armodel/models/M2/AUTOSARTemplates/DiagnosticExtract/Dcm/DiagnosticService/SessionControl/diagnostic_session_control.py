"""DiagnosticSessionControl AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)


class DiagnosticSessionControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSessionControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_session_session", None, False, False, DiagnosticSession),  # diagnosticSessionSession
        ("session_control", None, False, False, DiagnosticSession),  # sessionControl
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSessionControl."""
        super().__init__()
        self.diagnostic_session_session: Optional[DiagnosticSession] = None
        self.session_control: Optional[DiagnosticSession] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSessionControl to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSessionControl":
        """Create DiagnosticSessionControl from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSessionControl instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSessionControl since parent returns ARObject
        return cast("DiagnosticSessionControl", obj)


class DiagnosticSessionControlBuilder:
    """Builder for DiagnosticSessionControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControl = DiagnosticSessionControl()

    def build(self) -> DiagnosticSessionControl:
        """Build and return DiagnosticSessionControl object.

        Returns:
            DiagnosticSessionControl instance
        """
        # TODO: Add validation
        return self._obj
