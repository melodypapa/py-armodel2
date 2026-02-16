"""DiagnosticAuthRoleProxy AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)


class DiagnosticAuthRoleProxy(ARObject):
    """AUTOSAR DiagnosticAuthRoleProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "authentications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticAuthRole,
        ),  # authentications
    }

    def __init__(self) -> None:
        """Initialize DiagnosticAuthRoleProxy."""
        super().__init__()
        self.authentications: list[DiagnosticAuthRole] = []


class DiagnosticAuthRoleProxyBuilder:
    """Builder for DiagnosticAuthRoleProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthRoleProxy = DiagnosticAuthRoleProxy()

    def build(self) -> DiagnosticAuthRoleProxy:
        """Build and return DiagnosticAuthRoleProxy object.

        Returns:
            DiagnosticAuthRoleProxy instance
        """
        # TODO: Add validation
        return self._obj
