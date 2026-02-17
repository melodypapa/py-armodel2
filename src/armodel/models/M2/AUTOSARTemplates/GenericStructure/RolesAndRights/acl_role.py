"""AclRole AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UriString,
)


class AclRole(ARElement):
    """AUTOSAR AclRole."""

    ldap_url: Optional[UriString]
    def __init__(self) -> None:
        """Initialize AclRole."""
        super().__init__()
        self.ldap_url: Optional[UriString] = None


class AclRoleBuilder:
    """Builder for AclRole."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AclRole = AclRole()

    def build(self) -> AclRole:
        """Build and return AclRole object.

        Returns:
            AclRole instance
        """
        # TODO: Add validation
        return self._obj
