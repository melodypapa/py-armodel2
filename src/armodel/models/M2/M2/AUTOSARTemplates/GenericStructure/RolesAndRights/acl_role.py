"""AclRole AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UriString,
)


class AclRole(ARElement):
    """AUTOSAR AclRole."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ldap_url": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ldapUrl
    }

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
