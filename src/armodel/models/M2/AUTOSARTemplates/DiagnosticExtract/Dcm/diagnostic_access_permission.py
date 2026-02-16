"""DiagnosticAccessPermission AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)


class DiagnosticAccessPermission(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAccessPermission."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentication", None, False, False, DiagnosticAuthRole),  # authentication
        ("diagnostic_sessions", None, False, True, DiagnosticSession),  # diagnosticSessions
        ("environmental", None, False, False, any (Diagnostic)),  # environmental
        ("security_levels", None, False, True, DiagnosticSecurityLevel),  # securityLevels
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAccessPermission."""
        super().__init__()
        self.authentication: Optional[DiagnosticAuthRole] = None
        self.diagnostic_sessions: list[DiagnosticSession] = []
        self.environmental: Optional[Any] = None
        self.security_levels: list[DiagnosticSecurityLevel] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAccessPermission to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAccessPermission":
        """Create DiagnosticAccessPermission from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAccessPermission instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAccessPermission since parent returns ARObject
        return cast("DiagnosticAccessPermission", obj)


class DiagnosticAccessPermissionBuilder:
    """Builder for DiagnosticAccessPermission."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAccessPermission = DiagnosticAccessPermission()

    def build(self) -> DiagnosticAccessPermission:
        """Build and return DiagnosticAccessPermission object.

        Returns:
            DiagnosticAccessPermission instance
        """
        # TODO: Add validation
        return self._obj
