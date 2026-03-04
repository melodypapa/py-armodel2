"""DiagnosticAuthRoleProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticAuthRoleProxy(ARObject):
    """AUTOSAR DiagnosticAuthRoleProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-AUTH-ROLE-PROXY"


    authentication_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "AUTHENTICATION-REFS": lambda obj, elem: [obj.authentication_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticAuthRoleProxy."""
        super().__init__()
        self.authentication_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthRoleProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthRoleProxy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication_refs (list to container "AUTHENTICATION-REFS")
        if self.authentication_refs:
            wrapper = ET.Element("AUTHENTICATION-REFS")
            for item in self.authentication_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticAuthRole")
                if serialized is not None:
                    child_elem = ET.Element("AUTHENTICATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthRoleProxy":
        """Deserialize XML element to DiagnosticAuthRoleProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthRoleProxy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthRoleProxy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTHENTICATION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.authentication_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticAuthRoleProxyBuilder(BuilderBase):
    """Builder for DiagnosticAuthRoleProxy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticAuthRoleProxy = DiagnosticAuthRoleProxy()


    def with_authentications(self, items: list[DiagnosticAuthRole]) -> "DiagnosticAuthRoleProxyBuilder":
        """Set authentications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.authentications = list(items) if items else []
        return self


    def add_authentication(self, item: DiagnosticAuthRole) -> "DiagnosticAuthRoleProxyBuilder":
        """Add a single item to authentications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.authentications.append(item)
        return self

    def clear_authentications(self) -> "DiagnosticAuthRoleProxyBuilder":
        """Clear all items from authentications list.

        Returns:
            self for method chaining
        """
        self._obj.authentications = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "authentication",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticAuthRoleProxy:
        """Build and return the DiagnosticAuthRoleProxy instance with validation."""
        self._validate_instance()
        return self._obj