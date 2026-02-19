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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAccessPermission, cls).deserialize(element)

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = ARObject._deserialize_by_tag(child, "DiagnosticAuthRole")
            obj.authentication = authentication_value

        # Parse diagnostic_sessions (list from container "DIAGNOSTIC-SESSIONS")
        obj.diagnostic_sessions = []
        container = ARObject._find_child_element(element, "DIAGNOSTIC-SESSIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.diagnostic_sessions.append(child_value)

        # Parse environmental
        child = ARObject._find_child_element(element, "ENVIRONMENTAL")
        if child is not None:
            environmental_value = child.text
            obj.environmental = environmental_value

        # Parse security_levels (list from container "SECURITY-LEVELS")
        obj.security_levels = []
        container = ARObject._find_child_element(element, "SECURITY-LEVELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.security_levels.append(child_value)

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
