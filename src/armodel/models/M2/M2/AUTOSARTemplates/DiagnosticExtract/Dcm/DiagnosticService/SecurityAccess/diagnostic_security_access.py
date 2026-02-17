"""DiagnosticSecurityAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 96)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SecurityAccess.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)


class DiagnosticSecurityAccess(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSecurityAccess."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "request_seed_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # requestSeedId
        "security_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # securityAccess
        "security_delay": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # securityDelay
        "security_level": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticSecurityLevel,
        ),  # securityLevel
    }

    def __init__(self) -> None:
        """Initialize DiagnosticSecurityAccess."""
        super().__init__()
        self.request_seed_id: Optional[PositiveInteger] = None
        self.security_access: Optional[Any] = None
        self.security_delay: Optional[TimeValue] = None
        self.security_level: Optional[DiagnosticSecurityLevel] = None


class DiagnosticSecurityAccessBuilder:
    """Builder for DiagnosticSecurityAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityAccess = DiagnosticSecurityAccess()

    def build(self) -> DiagnosticSecurityAccess:
        """Build and return DiagnosticSecurityAccess object.

        Returns:
            DiagnosticSecurityAccess instance
        """
        # TODO: Add validation
        return self._obj
