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
    def serialize(self) -> ET.Element:
        """Serialize AclRole to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclRole, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ldap_url
        if self.ldap_url is not None:
            serialized = ARObject._serialize_item(self.ldap_url, "UriString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LDAP-URL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclRole":
        """Deserialize XML element to AclRole object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclRole object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclRole, cls).deserialize(element)

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
