"""AclRole AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UriString,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AclRole(ARElement):
    """AUTOSAR AclRole."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ACL-ROLE"


    ldap_url: Optional[UriString]
    _DESERIALIZE_DISPATCH = {
        "LDAP-URL": lambda obj, elem: setattr(obj, "ldap_url", SerializationHelper.deserialize_by_tag(elem, "UriString")),
    }


    def __init__(self) -> None:
        """Initialize AclRole."""
        super().__init__()
        self.ldap_url: Optional[UriString] = None

    def serialize(self) -> ET.Element:
        """Serialize AclRole to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclRole, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ldap_url
        if self.ldap_url is not None:
            serialized = SerializationHelper.serialize_item(self.ldap_url, "UriString")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LDAP-URL":
                setattr(obj, "ldap_url", SerializationHelper.deserialize_by_tag(child, "UriString"))

        return obj



class AclRoleBuilder(ARElementBuilder):
    """Builder for AclRole with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AclRole = AclRole()


    def with_ldap_url(self, value: Optional[UriString]) -> "AclRoleBuilder":
        """Set ldap_url attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ldap_url' is required and cannot be None")
        self._obj.ldap_url = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ldapUrl",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AclRole:
        """Build and return the AclRole instance with validation."""
        self._validate_instance()
        return self._obj