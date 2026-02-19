"""DiagnosticAccessPermission AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[DiagnosticAuthRole]
    diagnostic_sessions: list[DiagnosticSession]
    environmental: Optional[Any]
    security_levels: list[DiagnosticSecurityLevel]
    def __init__(self) -> None:
        """Initialize DiagnosticAccessPermission."""
        super().__init__()
        self.authentication: Optional[DiagnosticAuthRole] = None
        self.diagnostic_sessions: list[DiagnosticSession] = []
        self.environmental: Optional[Any] = None
        self.security_levels: list[DiagnosticSecurityLevel] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAccessPermission":
        """Deserialize XML element to DiagnosticAccessPermission object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAccessPermission object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = ARObject._deserialize_by_tag(child, "DiagnosticAuthRole")
            obj.authentication = authentication_value

        # Parse diagnostic_sessions (list)
        obj.diagnostic_sessions = []
        for child in ARObject._find_all_child_elements(element, "DIAGNOSTIC-SESSIONS"):
            diagnostic_sessions_value = ARObject._deserialize_by_tag(child, "DiagnosticSession")
            obj.diagnostic_sessions.append(diagnostic_sessions_value)

        # Parse environmental
        child = ARObject._find_child_element(element, "ENVIRONMENTAL")
        if child is not None:
            environmental_value = child.text
            obj.environmental = environmental_value

        # Parse security_levels (list)
        obj.security_levels = []
        for child in ARObject._find_all_child_elements(element, "SECURITY-LEVELS"):
            security_levels_value = ARObject._deserialize_by_tag(child, "DiagnosticSecurityLevel")
            obj.security_levels.append(security_levels_value)

        return obj



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
