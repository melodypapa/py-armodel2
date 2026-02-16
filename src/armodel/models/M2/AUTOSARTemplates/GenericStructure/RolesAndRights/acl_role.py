"""AclRole AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UriString,
)


class AclRole(ARElement):
    """AUTOSAR AclRole."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ldap_url", None, True, False, None),  # ldapUrl
    ]

    def __init__(self) -> None:
        """Initialize AclRole."""
        super().__init__()
        self.ldap_url: Optional[UriString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AclRole to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclRole":
        """Create AclRole from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AclRole instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AclRole since parent returns ARObject
        return cast("AclRole", obj)


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
