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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UriString,
)


class AclRole(ARElement):
    """AUTOSAR AclRole."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ldap_url: Optional[UriString]
    def __init__(self) -> None:
        """Initialize AclRole."""
        super().__init__()
        self.ldap_url: Optional[UriString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclRole":
        """Deserialize XML element to AclRole object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclRole object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ldap_url
        child = ARObject._find_child_element(element, "LDAP-URL")
        if child is not None:
            ldap_url_value = child.text
            obj.ldap_url = ldap_url_value

        return obj



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
